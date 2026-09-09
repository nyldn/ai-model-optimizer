#!/usr/bin/env python3
"""Validate the repository's self-contained skill."""

from pathlib import Path
import re
import subprocess


ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "model-optimizer-lite"
SKILL = SKILL_DIR / "SKILL.md"
OPENAI = SKILL_DIR / "agents" / "openai.yaml"


def main():
    expected = {
        Path("SKILL.md"),
        Path("agents/openai.yaml"),
    }
    actual = {
        path.relative_to(SKILL_DIR)
        for path in SKILL_DIR.rglob("*")
        if path.is_file()
    }
    assert actual == expected, f"unexpected installed files: {sorted(map(str, actual ^ expected))}"

    text = SKILL.read_text(encoding="utf-8")
    assert text.startswith("---\n"), "SKILL.md must start with YAML frontmatter"
    match = re.match(r"---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "SKILL.md frontmatter is incomplete"
    frontmatter = match.group(1)
    assert re.search(r"^name: model-optimizer-lite$", frontmatter, re.MULTILINE)
    assert re.search(r"^description: .+", frontmatter, re.MULTILINE)
    assert re.search(r'^  version: "5\.0\.0-dev"$', frontmatter, re.MULTILINE)
    assert re.search(
        r'^  source: "https://github\.com/nyldn/model-optimizer-lite"$',
        frontmatter,
        re.MULTILINE,
    )
    assert len(text.splitlines()) <= 140, "SKILL.md should remain compact"
    assert "references/" not in text and "scripts/" not in text

    metadata = OPENAI.read_text(encoding="utf-8")
    for required in (
        'display_name: "Model Optimizer Lite"',
        'short_description: "Choose the right model and reasoning effort"',
        "$model-optimizer-lite",
    ):
        assert required in metadata, f"openai.yaml missing {required}"

    listed = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    ).stdout
    candidates = [value.decode() for value in listed.split(b"\0") if value]
    blocked_paths = (
        re.compile(r"(^|/)research/"),
        re.compile(r"(^|/)Docs/"),
        re.compile(r"(^|/)\.claude/"),
        re.compile(r"\.(png|jpe?g|webp|gif|mov|mp4)$", re.IGNORECASE),
    )
    blocked_names = {"transcript.md", "example-claude.md", "internal-notes.md", "FABLE5_HANDOFF.md"}
    for relative in candidates:
        name = Path(relative).name
        secret_env = name.startswith(".env") and name != ".env.example"
        blocked = secret_env or name in blocked_names or any(pattern.search(relative) for pattern in blocked_paths)
        assert not blocked, f"blocked file present: {relative}"

    print("OK: self-contained skill validated")


if __name__ == "__main__":
    main()
