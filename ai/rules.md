# Rules for AI Agents #

Rules are persistent, repository-scoped instructions that shape how an
AI-assisted development tool behaves while working in a project. They
are typically loaded automatically when the tool opens the workspace
and apply across a session.

Common forms include `AGENTS.md` at the repository root (read by many
agent tools), `.cursor/rules/*.mdc` for Cursor, and similar
tool-specific files. The exact filename varies, but the engineering
expectations below do not.

For broader context on responsible use of AI tools, see the
[AI-Assisted Development guide](../ai-assisted-development.md). For an
overview of how Rules relate to Skills, see this directory's
[README](README.md).

## When to use a Rule ##

Use a Rule when the guidance is:

- Repository-wide or scoped to a clear subdirectory.
- Long-lived. The behavior should persist across sessions and
  contributors.
- Concise enough to read in a single sitting. Rules are read by both
  humans and models; both benefit from brevity.

Do *not* use a Rule for:

- One-off task instructions. Put those in the prompt.
- Anything secret or non-public. Rules live in the repository and are
  sent to the model.
- Project policy that requires legal review. Keep policy in the
  documents that already govern it and reference them from the Rule.

## Standards ##

- Rules are checked in, reviewed in pull requests, and owned via
  `CODEOWNERS`.
- Rules must not contain secrets, credentials, tokens, customer data,
  internal hostnames, or any non-public information.
- Rules are advisory to the model. They do not substitute for code
  review, CI checks, branch protection, or the project's existing
  access controls.
- Every Rule states, near the top, what it is for and when it
  applies.

## Defaults ##

- Prefer a single `AGENTS.md` at the repository root as the primary
  source of truth when the project uses more than one AI tool.
- For tool-specific Rules, use the conventional location expected by
  the tool (for example, `.cursor/rules/` for Cursor) rather than
  inventing a new one.
- Keep individual Rule files short - generally under a page of
  rendered Markdown. Split by topic when they grow.
- Use plain, declarative language. Avoid hedging, marketing tone, or
  open-ended aspirations.
- Link out to existing documentation (such as the
  [Style Guide](../style-guide.md) or [CONTRIBUTING](../CONTRIBUTING.md))
  rather than restating it.

## Suggestions ##

- Organize larger rule sets by topic: one file for code style, one for
  testing expectations, one for security guardrails, and so on.
- Include a short "When this applies" section at the top of each Rule
  so the model and reviewers can quickly decide whether it is
  relevant.
- Periodically re-read each Rule and remove anything that no longer
  reflects current practice. Stale Rules quietly degrade output
  quality.

## What to put in a Rule ##

Useful content includes:

- Pointers to the project's style, testing, and contribution guides.
- Repository-specific conventions that are not obvious from the code
  (for example, "tests live next to the module they test, not in a
  top-level `tests/` directory").
- Guardrails against known failure modes (for example, "do not modify
  generated files under `vendor/`").
- Explicit out-of-scope statements (for example, "do not add new
  third-party dependencies without an issue and review").

Avoid:

- Long prose explanations of *why* a convention exists. Link to the
  authoritative document instead.
- Conflicting guidance between Rules. Resolve conflicts in the source
  files, not by hoping the model picks the right one.
- Instructions that depend on information the model cannot verify
  (for example, "always check the latest internal wiki page").

## Review expectations ##

- Treat Rule changes like code changes. Require review, and prefer
  small, focused pull requests.
- When a Rule changes behavior in a way reviewers should know about,
  call it out in the pull request description.
- If a Rule is added to work around a recurring AI failure mode,
  document the failure briefly so future maintainers understand why
  the Rule exists.

## Limitations ##

Rules are not a security control. A model may ignore, misinterpret,
or be argued out of a Rule. They reduce variance and make agent
behavior more predictable, but the human contributor remains
responsible for every change that is committed.
