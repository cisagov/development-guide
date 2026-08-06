# Coding Agents #

A *coding agent* is a system that uses a language model to plan and
take actions against a software project on a developer's behalf -
reading files, running commands, editing source, running tests,
opening pull requests, and so on - rather than only producing text in
a chat window. Examples include in-editor coding agents (Cursor,
Claude Code, GitHub Copilot agent modes, OpenAI Codex agent modes)
and longer-running background or "cloud" coding agents that operate
against a repository or build environment without a developer
present.

This document covers building and operating coding agents within
projects that follow this development guide. It assumes the agent's
output is code, configuration, tests, or related repository
artifacts, and that those outputs flow through the project's normal
review and CI controls.

Agents built for other purposes - business process automation, data
pipelines, customer-facing assistants, and so on - are out of scope
for this document. See [Non-Coding Agents](non-coding-agents.md) for
guidance that applies to those.

Coding agents combine the considerations covered in [Rules](rules.md),
[Skills](skills.md), and [MCP](mcp.md), and add new ones because they
*act*. For broader context on responsible use of AI tools generally,
see the [AI-Assisted Development guide](../ai-assisted-development.md).

## When to use a coding agent ##

Use a coding agent when:

- The task is well-scoped, reproducible, and benefits from automation
  more than from one-shot assistance.
- The actions the agent will take are bounded and reviewable - for
  example, "open a draft pull request that updates dependency
  versions" rather than "improve the codebase".
- The output of the agent will pass through the same review and CI
  gates as any other change before it has effect.

Do *not* use a coding agent when:

- The task requires judgment the agent cannot reliably exercise -
  notably anything that grants privileges, handles secrets, touches
  production systems, or makes security-relevant trade-offs.
- The actions the agent would take cannot be reverted easily.
- The agent's effective permissions exceed what the human running it
  would be granted for the same task.

## Standards ##

- Agents act under a clearly identified principal. The human who
  starts the agent is accountable for everything it does in that
  session. Service accounts used by autonomous agents are owned,
  documented, and scoped to the minimum permissions required.
- Agents do not bypass code review, branch protection, CI checks, or
  any other control that applies to human contributors. Agent-
  produced changes land through normal pull requests.
- Agents must not be granted secrets, credentials, or production
  access beyond what their narrowly defined task requires. Long-
  lived broad credentials are not appropriate for agent use.
- Destructive, irreversible, or privilege-changing actions are gated
  on explicit human confirmation. "Auto-approve everything" modes
  are not used against project repositories or shared environments.
- Agent configuration - prompts, Rules, Skills, MCP servers, allowed
  tools, model selection - is checked in, reviewed in pull requests,
  and owned via `CODEOWNERS` when it affects the project.

## Defaults ##

- Start with the smallest agent that can do the job. Prefer an
  in-editor assistant with human-in-the-loop approval over an
  autonomous background agent unless the task clearly warrants the
  latter.
- Scope agents to a single repository or a single task type. Avoid
  agents whose role description is "do whatever the user asks across
  any system".
- Run agents in an isolated working environment (an ephemeral
  container, a dedicated workspace, or a sandboxed worktree) when
  they execute commands. Do not point agents at a developer's main
  shell with broad credentials available.
- Default to requiring human approval before the agent:
  - Executes shell commands.
  - Writes to files outside a well-defined working area.
  - Calls external services that have side effects.
  - Pushes branches, opens pull requests, or interacts with the
    issue tracker.
- Log what the agent did - prompts, tool calls, commands executed,
  files changed - in a form that a reviewer can inspect after the
  fact.
- Pin the agent's model, tool list, and MCP server set to known
  versions. Treat changes to any of these as configuration changes
  subject to review.

## Suggestions ##

- For repetitive, well-understood maintenance work (dependency
  bumps, lint fix-ups, documentation regeneration), a narrowly
  scoped agent with a clear success criterion can be a good fit.
- For longer-running or background agents, prefer designs that
  produce a draft pull request the team reviews, rather than
  designs that merge or deploy directly.
- When an agent is given access to an MCP server that can take
  action on external systems, prefer the smallest scope the server
  supports and require human confirmation per action.
- Periodically review agent logs and outputs even when nothing has
  obviously gone wrong. Drift in behavior is easier to catch early.
- Sunset agents that are no longer used. Idle agents with live
  credentials are a quiet liability.

## Constructing a coding agent ##

When designing a new coding agent for a project, document the
following before it is enabled in any shared environment:

- **Purpose.** One or two sentences describing what the agent is for
  and what it is *not* for.
- **Trigger.** How the agent is started (a developer command, a
  scheduled job, a webhook, a comment on an issue, etc.).
- **Principal and permissions.** Whose credentials the agent uses,
  what scopes those credentials carry, and where the credentials
  are stored.
- **Allowed actions.** The specific tools, commands, file paths, and
  external endpoints the agent is permitted to use.
- **Forbidden actions.** Explicit out-of-scope items, especially any
  destructive or privilege-changing operations.
- **Inputs.** What context the agent receives - which files, which
  Rules, which Skills, which MCP servers, which environment
  variables.
- **Outputs.** What the agent produces - typically a pull request,
  an issue comment, or a written artifact - and how that output is
  reviewed before it has effect.
- **Failure behavior.** What the agent does on error, timeout, or
  refusal. Default to stopping and reporting rather than retrying
  aggressively.
- **Owner.** A named team or individual responsible for the agent's
  configuration and behavior.

Keep this description short and check it in alongside the agent's
configuration so reviewers can evaluate changes against the stated
design.

## Operating a coding agent ##

- Start a coding agent with the narrowest task description that
  still captures the work. Vague tasks produce vague, harder-to-
  review results.
- Watch the first run of any new or materially changed agent
  configuration. Do not leave it unattended until its behavior is
  understood.
- Treat the agent's output as untrusted input. Read every diff. Run
  the project's tests and `pre-commit run --all-files`. Do not merge
  changes the human author cannot explain.
- Stop the agent if it begins doing something unexpected. Investigate
  before resuming.
- Rotate any credential that the agent may have been exposed to if
  the agent's environment or configuration is compromised.

## Risks specific to coding agents ##

- **Privilege amplification.** An agent with broad credentials and
  the ability to run shell commands can do far more damage than a
  one-shot assistant. Keep credentials and tools tightly scoped.
- **Prompt injection.** Content the agent reads - files, issues,
  pull request descriptions, MCP server responses, web pages - can
  contain instructions intended to redirect the agent. Treat all
  such content as untrusted.
- **Tool misuse.** An agent may call a tool in a way the project did
  not anticipate. Constrain tool inputs where the tool itself
  supports it, and review the actions the agent actually performs.
- **Confident, irreversible action.** Agents will sometimes act
  decisively on incorrect conclusions. Reversibility and human
  approval gates are the primary defenses.
- **Cost and resource exhaustion.** Long-running agents can consume
  significant compute, API quota, or CI minutes. Set explicit limits
  and monitor usage.
- **Drift.** Model updates, tool updates, and MCP server updates can
  change agent behavior without any change to the project's own
  configuration. Pin where possible and re-evaluate periodically.

## Limitations ##

The guidance above reduces the likelihood and impact of coding
agent mistakes; it does not eliminate them. Agents are not a
security boundary. They are a productivity tool whose outputs and
actions remain the responsibility of the humans who configure, run,
and review them. When in doubt, prefer the more conservative
option: smaller scope, narrower permissions, more human approval,
and smaller, more auditable changes. See the
[AI-Assisted Development guide](../ai-assisted-development.md) for
the full set of expectations that apply to AI-assisted work, and
[Non-Coding Agents](non-coding-agents.md) for agents whose outputs
are not repository artifacts.
