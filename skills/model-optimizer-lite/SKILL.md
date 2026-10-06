---
name: model-optimizer-lite
description: Recommends whether to keep or switch an AI model and reasoning effort in ChatGPT, Codex, or Claude. Use for model-choice, escalation, or cross-model review decisions. Ordinary coding, research, or review requests do not activate this skill.
metadata:
  version: "5.0.0"
  source: "https://github.com/nyldn/model-optimizer-lite"
---

# Model Optimizer Lite

Help the user make one model decision. Give advice only. Do not change model
settings, start another AI session, run a provider CLI, or dispatch work unless
the user separately asks for that action.

## Start with the actual client

Identify whether the conversation is in ChatGPT Chat or Work, Codex, or Claude.
Codex may run inside the ChatGPT desktop app, a terminal, an IDE, or the cloud.
Do not treat those clients as interchangeable.

- Preserve any model or reasoning effort the user explicitly selected.
- Prefer the current capable model when it already has useful task context.
- Use only model names and controls exposed by the current client and account.
- If the current model is not visible, call it unknown. Do not infer it from the
  application name, generated prose, configuration files, or a requested model.
  In Claude Code, `/status` or a configured status line can show the selection.
  Recheck after a host fallback; the requested model may differ from the runtime.
- Do not require Codex CLI for ChatGPT desktop use. Use the app's visible model
  and reasoning controls when they are available.
  No user terminal does not imply that the app lacks code execution or tools.

Ask a short question only when the available models or current selection would
materially change the recommendation.

## Choose the smallest suitable tier

Catalog guidance checked on 2026-10-05. These are starting points for a new
choice; they do not override an explicit selection or useful existing context.

| Client | Model and ID | Suitable work |
| --- | --- | --- |
| ChatGPT Work / Codex | GPT-6 Luna, `gpt-6-luna` | Routine edits, extraction, focused coding, repeatable tasks |
| ChatGPT Work / Codex | GPT-6.1 Sol, `gpt-6.1-sol` | Everyday implementation, complex coding, writing, analysis |
| ChatGPT Work / Codex | GPT-6 Astra, `gpt-6-astra` | Hard debugging, major architecture, demanding work across tools |
| Claude | Haiku 4.5, `claude-haiku-4-5-20251001` | Simple edits, extraction, fast routine work |
| Claude | Sonnet 5.5, `claude-sonnet-5-5` | Everyday coding and analysis with a speed priority |
| Claude | Opus 5.5, `claude-opus-5-5` | Complex coding, review, long-running knowledge work |
| Claude | Fable 5.1, `claude-fable-5-1` | Hard reasoning and long tasks where Opus at higher effort falls short |

Use the current selector or an already-exposed account catalog to confirm access.
API IDs identify versions; an API listing does not prove app availability.
GPT-6.1 Sol, GPT-6 Sol, and GPT-6 Luna are Work/Codex choices, not Chat choices.
For ChatGPT Chat, recommend only its visible models and controls. Older GPT-6
Sol and GPT-5.6 Sol/Terra/Luna can remain suitable when available; Terra is not
a separate tier in the current GPT-6 lineup. Claude aliases can resolve to older
versions depending on the provider, gateway, or client version.
Claude Code needs v2.1.284+ for Sonnet 5.5, v2.1.280+ for Opus 5.5, and
v2.1.257+ for Fable 5.1; a client upgrade does not establish account access.

If availability or lifecycle matters, check current official documentation when
browsing is available. Otherwise disclose that this dated guidance may be stale.
Use [OpenAI client models](https://learn.chatgpt.com/docs/models),
[OpenAI API models](https://developers.openai.com/api/docs/models),
[Claude models](https://platform.claude.com/docs/en/models/overview), and
[Claude Code controls](https://code.claude.com/docs/en/model-config).
Avoid retired choices. GPT-5.4, GPT-5.4-mini, and GPT-5.3-Codex-Spark have retired
from Codex with ChatGPT sign-in; GPT-5.5 retires there on 2026-10-14. These client
retirements do not establish API retirement. Explain an unavailable explicit
choice and offer a replacement conditionally, without silently changing it.

## Choose a supported effort

Preserve explicit effort; otherwise start with the selected client's default.
Raise it for deeper planning, analysis, or verification. Labels and defaults
vary by model and client; do not transfer effort settings across providers.
OpenAI Light corresponds to CLI `low`, and Extra High to `xhigh`. Max is deeper
single-task reasoning; Ultra uses subagents and requires supported controls,
divisible work, and authorized scope. GPT-6 Luna supports Max, not Ultra.
In Claude Code, Opus 5.5 and Sonnet 5.5 default to `medium`, Fable 5.1 to `high`.
Haiku 4.5 has no effort control. Use only levels the active client exposes;
an unsupported effort request alone does not establish a need for a larger model.
Claude API defaults can differ from Claude Code. Reserve the highest effort for
a specific hard problem instead of making it a standing default.
Claude Code's Ultracode is a workflow toggle, separate from effort in v2.1.284+.
Do not enable it merely to raise effort or treat it as OpenAI Ultra.

## Decide whether to switch

Stay with the current model when it can finish the task, already holds useful
context, or the likely gain does not justify a handoff.

Consider a switch when one of these is true:

- the task has become materially harder than the current tier suits;
- progress is blocked after the model has inspected the relevant evidence;
- the work needs a capability or tool the current client lacks;
- the user wants an independent review with a distinct question.

Do not switch merely because a stronger model exists. First check whether the
real problem is missing context, unclear acceptance criteria, unavailable tools,
or a failing environment.

## Use the native control

- In ChatGPT, invoke the skill with `@model-optimizer-lite` and use the model and
  reasoning controls shown near the composer.
- In Codex, invoke it with `$model-optimizer-lite`. Use the visible app control
  or `/model` in Codex CLI. Mention CLI flags only when the user is working in a
  terminal and asks for a command.
- In Claude Code, invoke it with `/model-optimizer-lite` and use `/model` or the
  client's selector; use `/effort` for supported effort changes. Other Claude
  clients may expose different controls.
  For a one-task change, prefer the picker's session-only action. Claude Code
  uses `s` in `/model`, and v2.1.257+ in `/effort`; Enter saves a default. Put the
  skill invocation at the start of the message for a direct run.

If the client cannot change models in the current conversation, explain the
manual action: open the selector, start a new conversation with the chosen
model, or keep the current model.

## Return a compact recommendation

State:

1. `Stay` or `Switch`.
2. The model tier or exact visible model, plus reasoning effort when relevant.
3. One task-specific reason.
4. The native action needed, if any.
5. Any uncertainty about availability or the model that is currently running.

When a switch or review is worthwhile, include a short handoff with the goal,
current state, evidence already gathered, constraints, checks already run, and
the one question the next model should answer. Keep one owner responsible for
integrating the result.

Never claim that a recommendation proves quality, lowers subscription cost, or
confirms that a named model executed the work. Treat another model's output as
evidence to verify, not authority.
