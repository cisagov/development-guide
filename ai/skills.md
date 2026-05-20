# Skills for AI Agents #

Skills are reusable, task-scoped capability packages that an AI agent
can load on demand. A Skill typically bundles a short instruction file
(often `SKILL.md`) with optional supporting scripts, templates, or
reference material. The agent selects a Skill based on the user's
request and follows the instructions inside it for that task.

Skills differ from [Rules](rules.md) in scope and lifetime. Rules
apply broadly and persistently; Skills apply narrowly and only when
invoked.

For broader context on responsible use of AI tools, see the
[AI-Assisted Development guide](../ai-assisted-development.md).

## When to use a Skill ##

Use a Skill when the work is:

- A recurring, well-defined task (for example, "scaffold a new Python
  module following the project skeleton" or "draft a release note
  from a list of merged pull requests").
- Worth standardizing so that every contributor and agent performs it
  the same way.
- Specific enough that a focused instruction set produces meaningfully
  better results than a general-purpose prompt.

Do *not* use a Skill for:

- Project-wide conventions that should always apply. Those belong in
  a [Rule](rules.md).
- One-off tasks. Write them as a prompt instead.
- Anything that requires secrets, credentials, or non-public data at
  authoring time. Skills are checked into the repository.

## Standards ##

- Skills are checked in, reviewed in pull requests, and owned via
  `CODEOWNERS`.
- Skills must not contain secrets, credentials, tokens, customer
  data, internal hostnames, or any non-public information.
- Each Skill has a clear, narrow purpose stated at the top of its
  `SKILL.md` (or equivalent entry file).
- Any scripts or commands invoked by a Skill follow the same security
  and review expectations as any other code in the repository.

## Defaults ##

- Store Skills in the conventional location expected by the tool in
  use (for example, `.claude/skills/<skill-name>/` for Claude Code,
  or the location documented by whatever tool the project has
  standardized on).
- Give each Skill its own directory. Keep the entry file short and
  put supporting material in sibling files.
- Begin each Skill with a short description of:
  - What the Skill does.
  - When it should be used.
  - When it should *not* be used.
- Prefer Skills that produce small, reviewable changes. A Skill that
  rewrites large portions of the codebase in one step is hard to
  audit.

## Suggestions ##

- Keep `SKILL.md` focused on instructions for the agent. Put
  human-facing rationale in a sibling `README.md` if needed.
- When a Skill wraps a shell command or script, prefer invoking an
  existing, reviewed script in the repository over embedding new
  logic in the Skill file.
- Include a brief "Validation" section in the Skill describing how
  the contributor should verify the result (for example, "run
  `pre-commit run --all-files` and the project test suite").
- Version Skills with the repository. Avoid pinning Skills to
  external sources that can change without review.

## What to put in a Skill ##

Useful content includes:

- A precise description of the task the Skill performs.
- The inputs the agent should gather from the user before acting.
- The concrete steps to perform, in order.
- The files or directories the Skill is permitted to modify.
- Validation steps the contributor should run before committing.
- Explicit out-of-scope statements.

Avoid:

- Vague aspirational language ("write great code"). Be specific.
- Embedded credentials, tokens, or environment-specific URLs.
- Instructions that require the agent to make autonomous decisions
  about security-sensitive code without human review.

## Review expectations ##

- Treat new Skills and changes to existing Skills as code changes.
  Require review, and prefer small, focused pull requests.
- When a Skill invokes scripts, links to external resources, or
  modifies sensitive paths, call that out in the pull request
  description so reviewers can scrutinize the relevant surface.
- Remove Skills that are no longer used. Unmaintained Skills produce
  inconsistent, sometimes wrong, results.

## Limitations ##

A Skill influences what the agent attempts; it does not guarantee the
agent will follow the instructions correctly. Every change produced
by a Skill is still untrusted input until reviewed by a human, run
through the project's tests, and passed through the existing CI
checks. See the
[AI-Assisted Development guide](../ai-assisted-development.md) for the
full set of expectations that apply to AI-generated changes.
