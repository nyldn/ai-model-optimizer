# Model Optimizer Lite development

Maintain `skills/model-optimizer-lite/SKILL.md` directly. The installed skill is
self-contained and has no scripts or referenced instruction files.

Keep ChatGPT, Codex, and Claude behavior distinct. Preserve explicit model
choices, report unavailable model identity as unknown, and do not require Codex
CLI for ChatGPT desktop use. The skill recommends an action but does not switch
models or dispatch inference.

Run `python3 scripts/validate.py` and `git diff --check` after changes. Keep user
edits and local agent state separate. Publishing and release changes require
separate authorization.

Read `docs/DELIVERY.md` before changing installation, supported clients,
packaging, or release behavior.
