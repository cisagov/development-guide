# Non-Coding Agents #

A *non-coding agent* is an AI agent whose primary outputs are not
source code, configuration, or other repository artifacts. Examples
include agents that triage and respond to messages, summarize
documents, route tickets, drive a data pipeline, generate reports,
or act on a user's behalf against an internal API or SaaS product.

This document collects the engineering and security expectations
that apply when a CISA project builds or operates such an agent. It
complements - and does not replace - the project's domain-specific
requirements (privacy, accessibility, records management, sector-
specific regulation, customer-facing-product review, and so on).
Those domain requirements are *not* described here and must be
sourced from the appropriate authoritative documents and teams.

For coding agents (agents whose output flows through the project's
repository, review, and CI controls), see [Agents](agents.md). For
broader context on responsible use of AI tools, see the
[AI-Assisted Development guide](../ai-assisted-development.md). For
how agents relate to Rules, Skills, and MCP servers, see this
directory's [README](README.md).

## What this document covers ##

- General engineering and security expectations that apply to any
  agent built or operated within a CISA project.
- A construction checklist that should be filled in before an agent
  is enabled in any shared environment.
- A catalog of risks that apply to agents regardless of output
  channel.

## What this document does *not* cover ##

- Privacy, civil liberties, records management, accessibility, or
  any other compliance regime specific to the agent's domain.
- Approval workflows for customer-facing or public-facing systems.
- Content policy for agents that produce text consumed by external
  audiences.
- Procurement, vendor risk, and authority-to-operate (ATO)
  processes.

If any of the above apply, treat the engagement of the responsible
team as a prerequisite, not a follow-up.

## When to build a non-coding agent ##

Build a non-coding agent when:

- The task is well-scoped, recurring, and benefits from automation
  more than from one-shot assistance.
- The actions the agent will take are bounded, reviewable, and
  reversible, or are gated on human approval before taking effect.
- The agent's effective permissions can be kept at or below what
  the requesting user would be granted for the same task.
- The relevant domain teams have reviewed the use case.

Do *not* build a non-coding agent when:

- The task requires judgment the agent cannot reliably exercise -
  notably anything that grants privileges, handles secrets, makes
  benefits or eligibility determinations, or makes security-
  relevant trade-offs.
- The agent would take actions that cannot be reverted easily, with
  no human approval gate.
- The agent would handle data the project is not authorized to
  process through a language model or an external service.

## Standards ##

- Agents act under a clearly identified principal. The human who
  starts the agent, or the team that owns an autonomous agent's
  service account, is accountable for everything it does. Service
  accounts are owned, documented, and scoped to the minimum
  permissions required.
- Agents must not be granted secrets, credentials, or production
  access beyond what their narrowly defined task requires. Long-
  lived, broadly scoped credentials are not appropriate for agent
  use.
- Destructive, irreversible, or privilege-changing actions are
  gated on explicit human confirmation. "Auto-approve everything"
  modes are not used against shared systems or systems of record.
- Agent inputs and outputs are logged in a form that a reviewer can
  inspect after the fact, subject to the project's existing data-
  handling and retention rules.
- Agents do not bypass any control - access control, change
  management, approval workflow, records retention, or audit
  logging - that applies to human operators performing the same
  task.
- Agent configuration - prompts, Rules, Skills, MCP servers, tools,
  model selection, and any allow-lists or guardrails - is checked
  in, reviewed in pull requests, and owned via `CODEOWNERS`.

## Defaults ##

- Start with the smallest agent that can do the job. Prefer a
  human-in-the-loop design over an autonomous one unless the task
  clearly warrants the latter.
- Scope agents to a single task type and a single set of systems.
  Avoid agents whose role description is "do whatever the user
  asks across any system".
- Run agents in an isolated execution environment (an ephemeral
  container, a dedicated service, a sandboxed worker) with only
  the credentials and network reach the task requires.
- Default to requiring human approval before the agent:
  - Calls external services that have side effects.
  - Writes to systems of record.
  - Sends messages, tickets, or notifications to people outside
    the team operating the agent.
  - Accesses or transmits any data classified above public.
- Pin the agent's model, tool list, and MCP server set to known
  versions. Treat changes to any of these as configuration changes
  subject to review.
- Set explicit limits on runtime, request volume, token usage, and
  cost. Monitor against those limits.

## Suggestions ##

- For recurring back-office work (categorizing documents, drafting
  summaries, preparing reports), a narrowly scoped agent with a
  clear success criterion and a human approval step can be a good
  fit.
- Prefer designs in which the agent produces a draft artifact for a
  human to approve, edit, and act on, rather than designs in which
  the agent acts directly on systems of record.
- When the agent must call out to external systems, prefer an MCP
  server or other reviewed integration over ad-hoc credentials in
  the agent's environment. See [MCP](mcp.md).
- Periodically sample agent inputs, outputs, and logs even when
  nothing has obviously gone wrong. Drift in behavior is easier to
  catch early.
- Sunset agents that are no longer used. Idle agents with live
  credentials are a quiet liability.

## Constructing a non-coding agent ##

When designing a new non-coding agent for a project, document the
following before it is enabled in any shared environment:

- **Purpose.** One or two sentences describing what the agent is
  for and what it is *not* for.
- **Domain review.** Which domain teams (privacy, accessibility,
  records, legal, mission, security, etc.) have reviewed the use
  case, and the outcome of that review. If none apply, say so
  explicitly.
- **Trigger.** How the agent is started (a user action, a scheduled
  job, an incoming message, a webhook, etc.).
- **Principal and permissions.** Whose credentials the agent uses,
  what scopes those credentials carry, and where the credentials
  are stored.
- **Data handled.** The categories of data the agent reads, writes,
  or transmits, and the authority under which it does so.
- **Allowed actions.** The specific tools, endpoints, and systems
  the agent is permitted to act against.
- **Forbidden actions.** Explicit out-of-scope items, especially
  any destructive, privilege-changing, or externally visible
  operations.
- **Inputs.** What context the agent receives - which prompts,
  which Rules, which Skills, which MCP servers, which environment
  variables, which user-supplied content.
- **Outputs.** What the agent produces (a message, a record, a
  ticket, a file, a recommendation), who receives it, and how it
  is reviewed or approved before it has effect.
- **Failure behavior.** What the agent does on error, timeout,
  refusal, or contradiction. Default to stopping and reporting
  rather than retrying aggressively.
- **Limits.** Runtime, request volume, token usage, cost, and any
  rate limits the agent must respect.
- **Logging and retention.** What is logged, where it is stored,
  who can access it, and for how long.
- **Owner.** A named team or individual responsible for the
  agent's configuration and behavior.

Keep this description short and check it in alongside the agent's
configuration so reviewers can evaluate changes against the stated
design.

## Operating a non-coding agent ##

- Start an agent with the narrowest task description that still
  captures the work. Vague tasks produce vague, harder-to-review
  results.
- Watch the first runs of any new or materially changed agent
  configuration. Do not leave an agent unattended in a shared
  environment until its behavior is understood.
- Treat the agent's output as untrusted input. Review it - or have
  the receiving system enforce constraints - before it has effect.
- Stop the agent if it begins doing something unexpected, exceeds
  configured limits, or operates against data it should not be
  touching. Investigate before resuming.
- Rotate any credential the agent may have been exposed to if the
  agent's environment, configuration, or upstream services are
  compromised.

## Risks specific to agents ##

These apply regardless of the agent's output channel.

- **Privilege amplification.** An agent with broad credentials and
  the ability to call tools can do far more damage than a one-shot
  assistant. Keep credentials and tools tightly scoped.
- **Prompt injection.** Content the agent reads - messages,
  documents, tickets, MCP server responses, web pages, user input
  - can contain instructions intended to redirect the agent. Treat
  all such content as untrusted.
- **Tool misuse.** An agent may call a tool in a way the project
  did not anticipate. Constrain tool inputs where the tool itself
  supports it, and review the actions the agent actually performs.
- **Confident, irreversible action.** Agents will sometimes act
  decisively on incorrect conclusions. Reversibility and human
  approval gates are the primary defenses.
- **Data leakage.** Inputs, retrieved context, and tool outputs
  can leave the project's environment via the model provider, MCP
  servers, or logs. Verify the data path for each before enabling
  the agent.
- **Cost and resource exhaustion.** Long-running agents can
  consume significant compute, API quota, or vendor spend. Set
  explicit limits and monitor usage.
- **Drift.** Model updates, tool updates, and MCP server updates
  can change agent behavior without any change to the project's
  own configuration. Pin where possible and re-evaluate
  periodically.

## Limitations ##

The guidance above is engineering and security baseline guidance.
It does not, by itself, make an agent appropriate for any specific
domain, audience, or data classification. Domain-specific
requirements - privacy, accessibility, records management, sector
regulation, customer-facing-product review, and so on - apply on
top of this baseline and must be sourced from the appropriate
authoritative documents and teams. When in doubt, prefer the more
conservative option: smaller scope, narrower permissions, more
human approval, and smaller, more auditable steps.
