---
name: model-optimizer-lite
description: Choose whether to keep or switch the current AI model and reasoning effort in ChatGPT, Codex, or Claude. Use when the user asks which model, effort, or AI should handle a task, whether the current model is enough, or whether another model should review it.
metadata:
  version: "5.0.0-dev"
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
- Do not require Codex CLI for ChatGPT desktop use. Use the app's visible model
  and reasoning controls when they are available.

Ask a short question only when the available models or current selection would
materially change the recommendation.

## Choose the smallest suitable tier

| Work | Starting tier |
| --- | --- |
| Repetitive edits, formatting, or simple extraction | Fastest available model |
| Ordinary implementation, writing, or analysis | Balanced everyday model |
| Ambiguous research, detailed review, or difficult coding | Strong reasoning model |
| Hard debugging, major architecture, or sustained work across tools | Highest-capability model |

When the current OpenAI client offers these model families, Luna is the fast
tier, Terra is the everyday tier, Sol is the stronger reasoning tier, and Astra
is the highest-capability tier. When Claude offers Sonnet, Opus, and Fable, use
them in the same broad order. Availability varies by account, client, and
rollout, so describe an unavailable recommendation as conditional.

Start with the client's default reasoning effort. Raise it only when the task
needs deeper planning, analysis, or verification. Use the highest effort for a
specific hard problem, not as a standing default. An effort mode that delegates
work is appropriate only when the task can be split safely and the user has
authorized that scope.

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
  client's selector. Other Claude clients may expose different controls.

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
