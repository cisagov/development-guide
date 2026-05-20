# AI Agent Configuration Guide #

This document is structured by topic; under each, we include "Standards",
"Defaults", and "Suggestions".

**Standards** are practices that have a strong consensus across CISA; they
should generally be followed.

**Defaults** are safe selections that tend to be used by a large number of our
projects; you may find yourself with a better or more tailored solution,
however.

**Suggestions** contain examples that have worked well on a project or two;
they're not widely used enough to be defaults, but are worth considering.

This guide covers configuration artifacts that shape how AI-assisted
development tools (Cursor, Claude Code, GitHub Copilot, OpenAI Codex,
and similar systems) behave inside a repository. For broader guidance
on responsible use of these tools, see the
[AI-Assisted Development guide](../ai-assisted-development.md).

## Scope ##

Two categories of configuration are in scope:

- **Rules.** Persistent, repository-scoped instructions that constrain
  or steer agent behavior across a session. See [Rules](rules.md).
- **Skills.** Reusable, task-scoped capability packages that an agent
  can load on demand. See [Skills](skills.md).

Both are checked into the repository, reviewed like code, and treated
as part of the project's engineering surface.

## Why this matters ##

AI agents act on whatever context they receive. Rules and Skills are
the primary mechanisms a project has for making that context
predictable, reviewable, and aligned with the project's security and
quality expectations. Treating them as configuration artifacts - rather
than as ephemeral chat instructions - is what makes their behavior
auditable.

## Standards ##

- Rules and Skills are committed to the repository, reviewed in pull
  requests, and subject to the same expectations as any other code
  change. See the [AI-Assisted Development guide](../ai-assisted-development.md)
  and [CONTRIBUTING](../CONTRIBUTING.md).
- Rules and Skills must not contain secrets, credentials, tokens,
  internal hostnames, or non-public data. Assume their contents will
  be transmitted to the agent's backing model.
- Rules and Skills are advisory to the model and are not a security
  boundary. They do not replace code review, CI checks, or the
  project's existing access controls.
- Every Rule and Skill has a clear purpose, a named owner (via
  `CODEOWNERS`), and is removed when no longer used.

## Defaults ##

- Keep Rules short and specific. Prefer several small, focused Rules
  over one large general one.
- Keep Skills narrowly scoped to a single capability or workflow.
- Document, in the file itself, what the Rule or Skill is for and when
  it should apply.
- Store Rules and Skills in the conventional locations expected by the
  tool in use (for example, `.cursor/rules/` for Cursor, `AGENTS.md`
  for tools that read it, `.claude/skills/` for Claude Code). Avoid
  scattering equivalent guidance across multiple ad-hoc files.

## Suggestions ##

- When multiple tools are in use on the same project, prefer a single
  source of truth (typically `AGENTS.md`) and reference it from
  tool-specific files rather than duplicating content.
- Review Rules and Skills periodically. Stale guidance is worse than
  no guidance, because it teaches the agent to do the wrong thing
  confidently.

## Contents ##

- [Rules](rules.md) - persistent, repository-scoped agent instructions.
- [Skills](skills.md) - reusable, task-scoped agent capabilities.
