# Upstream research

## October 8 catalog refresh

The seven-source catalog check found no changes to OpenAI's client or API model
lineup. The current choices remain GPT-6 Luna, GPT-6.1 Sol, and GPT-6 Astra,
subject to account and client availability. The changelog includes newer client
fixes. GPT-5.5 retires from ChatGPT Chat, Work, and Codex on October 14; API access
is unaffected. Sources: [client models](https://learn.chatgpt.com/docs/models),
[API models](https://developers.openai.com/api/docs/models), and
[changelog](https://learn.chatgpt.com/docs/changelog).

Claude Haiku 5.5 launched October 7 with adaptive thinking and effort support.
It is the current Haiku tier for classification, extraction, and routing.
Its API has a 1M context window and higher rates for prompts over 100K tokens.
Keep Haiku 4.5 conditional without transferring Haiku 5.5's effort support to it.
Sources: [Haiku 5.5](https://platform.claude.com/docs/en/models/haiku-5-5/overview)
and [platform release notes](https://platform.claude.com/docs/en/release-notes/overview).

Claude Code v2.1.293 adds Haiku 5.5 and updates the Anthropic API `haiku` alias.
Its default effort is Medium, as with Opus 5.5 and Sonnet 5.5 in Claude Code.
The Claude API's Sonnet default is High, so provider defaults remain distinct.
Claude Code v2.1.292 adds Agent `effort`; use that parameter only when the host
exposes it and the model supports it. Older or restricted hosts still require
a handoff when mandatory child effort cannot be applied. Sources:
[model configuration](https://code.claude.com/docs/en/model-config),
[model overview](https://platform.claude.com/docs/en/models/overview), and
[Claude Code changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md).

The reviewed catalog baseline and skill guidance now both date to October 8.
This local refresh preserves the unreleased bounded-delegation behavior and
explicit selections; it does not install client updates or change account settings.

## October 5 research

Checked on October 5, 2026. These notes are maintainer material. The installed
skill contains its own guidance and does not depend on this file.

The review covered Anthropic's current model and skills documentation, the
Claude Code changelog through v2.1.289, and OpenAI's current ChatGPT/Codex skill
documentation and changelog through Codex CLI 0.160.1. Model availability still
depends on the account, client, provider, and controls exposed in the session.

| Finding | Decision for Model Optimizer Lite | Source |
| --- | --- | --- |
| Claude Code's model picker saves a default with Enter and uses `s` for this session only. The effort picker supports `s` from v2.1.257. | Recommend the session-only action for a single task; preserve explicit choices. | [Model configuration](https://code.claude.com/docs/en/model-config) |
| Sonnet 5.5 needs Claude Code v2.1.284+, Opus 5.5 v2.1.280+, and Fable 5.1 v2.1.257+. | State minimum client versions alongside catalog guidance without implying account access. | [Model configuration](https://code.claude.com/docs/en/model-config) |
| Ultracode became a separate workflow toggle at any supported effort in v2.1.284. | Distinguish it from effort and OpenAI Ultra. | [Claude Code changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) |
| Skill frontmatter can override model, effort, tool access, hooks, or execution context. | Reject these runtime settings in repository validation so the skill remains advisory. | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Claude Code v2.1.287 fixed context loss when switching between Opus 5.5 and Sonnet 5.5, and clarified that a leading skill invocation runs directly. | Put direct invocations first; continue considering context when recommending a switch. | [Claude Code changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md) |
| Codex caps its initial skill list at 2% of context, or 8,000 characters when context size is unknown. Descriptions can be shortened. | Lead with model-choice intent and exclude ordinary coding or research triggers. | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| OpenAI documents `.agents/skills` discovery, automatic edit detection, and separate entries for duplicate names. | Correct the old migration-only label for `.agents`; verify the actual installed location and invocation. | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code watches local skills, but a newly created top-level skills directory needs `/reload-skills`. Cowork and cloud sessions use account skills instead of local user files. | Document local reload behavior; keep supported delivery limited to the existing local clients. | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Codex CLI 0.160.0 stopped mixing unsupported bundled models into explicit provider catalogs and stopped reusing stale entries after refresh failure. | Continue treating the visible catalog as authoritative; disclose failed or unavailable discovery. | [ChatGPT & Codex changelog](https://learn.chatgpt.com/docs/changelog) |
| Sonnet 4.5 was deprecated on September 30, with API retirement scheduled for November 30. | Recommend current supported choices; keep API retirement separate from client availability. | [Claude Platform release notes](https://platform.claude.com/docs/en/release-notes/overview) |

## Evaluation opportunity

Claude Code added `claude plugin eval` in v2.1.269. Its native runner can compare
with-skill and without-skill results. Anthropic recommends measuring discovery
and response quality separately in fresh sessions. The restored
[behavior cases](../tests/behavior-cases.md) cover both.

The next useful check is a native evaluation of those cases in an isolated
maintainer workspace. Local v2.1.289 help confirms that the runner accepts
skills-directory targets, writes JSON and HTML reports, supports a cost ceiling,
and offers `--no-publish` to keep reports local. Use that flag to respect the
repository's publication boundary. Keep evaluation fixtures outside the
installed skill, and record the actual model and client version.

Sources: [Claude Code skills](https://code.claude.com/docs/en/skills),
[Claude Code changelog](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md),
and local `claude plugin eval --help` on v2.1.289.

The October 6 follow-up executed the native comparisons, calibrated the judge,
and repeated the affected cases after two guidance corrections. See the
[evaluation results](EVALUATION.md) for counts, evidence, and limitations.
Discovery in every supported client remains unverified.

## Catalog monitoring

The October 6 [catalog drift checker](CATALOG-CHECK.md) records a separate
maintainer snapshot of seven public sources. It flags model mentions and
documentation changes for review, including retirement, effort, client-version,
and skill-control guidance. The initial Claude Code changelog capture includes
v2.1.291. Snapshot capture does not change the installed skill's dated catalog
guidance or establish model availability.
