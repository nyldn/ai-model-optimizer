# Contributing

Model Optimizer Lite is one self-contained skill. Edit
`skills/model-optimizer-lite/SKILL.md` directly. Keep ChatGPT, Codex, and Claude
guidance in that file so an installed copy does not need repository references,
scripts, generated files, or a provider CLI.

Use `skills/model-optimizer-lite/agents/openai.yaml` only for ChatGPT and Codex
display metadata. Keep it consistent with the skill name and description.

Before submitting a change, run:

```sh
python3 scripts/validate.py
git diff --check
```

Also read the skill as a new user would. Confirm that it respects explicit model
choices, does not assume model availability, and distinguishes ChatGPT controls
from Codex CLI commands.

Adding executable helpers, reference files, installers, plugins, generated
copies, or marketplaces is a product-scope change. Discuss that need before
reintroducing it.

Read [docs/DELIVERY.md](docs/DELIVERY.md) before changing installation, client
support, packaging, or release behavior.
