# Model Optimizer Lite

Model Optimizer Lite helps ChatGPT, Codex, or Claude answer one practical
question: should you keep the current model for this task, or switch?

It is a self-contained skill. There is no model router, background process,
plugin, provider connection, or automatic model switching. The skill gives a
recommendation and tells you which native control to use.

## Install in the ChatGPT desktop app or Codex

Open Codex in the ChatGPT desktop app, Codex CLI, or the Codex IDE extension and
ask the built-in installer:

```text
$skill-installer install the skill from https://github.com/nyldn/model-optimizer-lite/tree/main/skills/model-optimizer-lite
```

Start a new conversation after installation. In ChatGPT, type `@` and choose
Model Optimizer Lite. In Codex, invoke it with `$model-optimizer-lite`.

```text
@model-optimizer-lite Should I keep this model for a difficult debugging task?
```

```text
$model-optimizer-lite Should I keep this model for a difficult debugging task?
```

The ChatGPT desktop app can display standalone skills from local projects in its
Skills sidebar. ChatGPT and Codex may also select the skill automatically when
you ask which model or reasoning effort to use.

Installation makes the skill available to supported local clients. It does not
publish the skill to ChatGPT's public plugin directory or make it available in
web-only and mobile ChatGPT clients.

[Read OpenAI's skill instructions](https://learn.chatgpt.com/docs/build-skills).

## Update or remove an older installation

The built-in installer does not overwrite an existing folder. Update each scope
where you still want the skill:

- For ChatGPT desktop and Codex user scope, move any existing copy from
  `~/.codex/skills/model-optimizer-lite` or the v4 location
  `~/.agents/skills/model-optimizer-lite` to a backup outside `skills`. Then run
  the installation prompt above.
- For a Codex project copy, move `.agents/skills/model-optimizer-lite` to a
  backup, then copy the complete `skills/model-optimizer-lite` directory from a
  fresh checkout into the same `.agents/skills` directory.
- For Claude Code, move the existing user or project copy from its
  `.claude/skills` directory to a backup, then copy the complete skill directory
  from a fresh checkout into that same scope.

Start a new conversation in each updated client. Open the installed `SKILL.md`
and confirm that `metadata.version` is `5.0.0-dev`, then invoke the skill before
removing the backup. Updating one scope does not update the others.

Version 4 also offered a plugin. If Model Optimizer Lite appears under Plugins,
uninstall or disable that copy through the app's plugin manager. Keep only the
standalone skill so the selector does not show duplicates. Do not delete plugin
caches or unrelated skills by hand.

If v4 was installed with `install.sh claude-md`, it may also have added an
always-on block to the project's `CLAUDE.md`. Remove only the complete block from
the line `<!-- model-optimizer-lite:start -->` through the line
`<!-- model-optimizer-lite:end -->`, including those two marker lines. Preserve
all surrounding instructions. If either marker is missing, stop and inspect the
file instead of deleting a guessed range.

To remove the standalone skill, move each installed folder outside its containing
`skills` directory. Remove the marked `CLAUDE.md` block as described above when
present. This keeps recoverable copies while removing the skill from discovery.

## Install in Claude Code

Copy the `skills/model-optimizer-lite` directory into a Claude Code user or
project skills directory. All instructions are in `SKILL.md`.
`agents/openai.yaml` adds optional display metadata for OpenAI clients and is not
a runtime dependency.

Invoke the installed skill with `/model-optimizer-lite` in Claude Code. Other
Claude clients may use their own skill import flow.

## What it does

- Keeps an explicitly selected model or reasoning effort.
- Favors the current capable model when switching would discard useful context.
- Suggests a faster model for routine work and a stronger model for hard work.
- Distinguishes ChatGPT controls from Codex CLI commands.
- Produces a compact handoff when a switch or independent review is worthwhile.

The recommendation uses the models and controls visible in the current client.
It does not unlock models, prove account access, or promise cost savings.

## Repository layout

```text
skills/model-optimizer-lite/
├── SKILL.md
└── agents/
    └── openai.yaml
```

The installed skill has no scripts or referenced instruction files. Maintainers
can run `python3 scripts/validate.py` and `git diff --check` before submitting a
change. See [CONTRIBUTING.md](CONTRIBUTING.md) for the small maintenance contract.
The [delivery contract](docs/DELIVERY.md) records the supported clients and
release boundary.

MIT licensed.
