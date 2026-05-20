# AI-Assisted Development #

This guide describes how to use AI-assisted development tools - such as
Cursor, Claude Code, GitHub Copilot, and OpenAI Codex - responsibly within
our projects. The goal is to capture the productivity benefits of these
tools while maintaining the security, quality, and review standards
expected of code produced in a regulated environment.

Treat AI-assisted tools as *assistants*, not as autonomous decision-makers.
Every suggestion, completion, or generated change is the responsibility of
the human contributor who commits it.

## Scope ##

This guidance applies to any tool that suggests, generates, or transforms
source code, configuration, documentation, tests, or commit messages based
on a language model. It complements - and does not replace - the existing
[CONTRIBUTING](CONTRIBUTING.md), [Style Guide](style-guide.md), and
[Project Setup](project_setup/README.md) guidance.

## Responsible use ##

- Use AI tools to accelerate well-understood work, not to bypass
  understanding. You should be able to explain, defend, and maintain any
  code you commit, regardless of how it was produced.
- Prefer official, organization-approved tooling and configurations. Do
  not enable AI features in tools that have not been reviewed for use on
  your project.
- Review and understand each tool's data-handling policy before sending
  it any project content. Default to assuming prompts and context are
  transmitted off-device.
- Disable AI features when working in repositories or directories that
  contain content not approved for transmission to a third party.

## Protecting sensitive information ##

AI tools typically read open files, recently edited files, and selected
context from the workspace. Assume that anything within the tool's
context window may leave your machine.

- Never include secrets, credentials, tokens, private keys, or signed
  URLs in prompts, comments, or generated code.
- Do not paste production data, personally identifiable information
  (PII), or controlled unclassified information (CUI) into a prompt.
- Keep `.env` files, credential files, and other sensitive artifacts out
  of the workspace, or ensure they are excluded from the tool's indexing
  and context.
- Be cautious when sharing proprietary or internal-only code with hosted
  models. When in doubt, ask before sending it off-device.
- If a secret is exposed in a prompt or generated output, treat it as
  compromised and rotate it immediately.

## Human review requirements ##

AI-generated code is *untrusted input* until a human has reviewed it.

- Every AI-assisted change must be read, understood, and explicitly
  accepted by the contributor before it is committed.
- AI-assisted pull requests follow the same review process as any other
  contribution. They are not exempt from code owner review, CI checks,
  or the quality assurance expectations described in
  [CONTRIBUTING](CONTRIBUTING.md).
- Reviewers should not approve changes that the author cannot explain.
- Authorship and accountability remain with the human contributor. The
  tool is not a co-author for review purposes.

## Testing and validation ##

- Run the project's existing test suite against any AI-generated change
  before opening a pull request.
- Add or update tests to cover new behavior. Do not rely on the model's
  assertion that code is correct.
- Validate that referenced APIs, functions, modules, flags, and
  configuration keys actually exist and behave as described. Models can
  fabricate plausible-looking identifiers that do not exist.
- Confirm that example commands, URLs, and file paths in generated
  documentation are real and correct.

## Security review expectations ##

Apply the same security scrutiny to AI-generated code as to any other
contribution, with particular attention to common failure modes.

- Validate and sanitize all external input handled by generated code.
- Check authentication, authorization, and session-handling logic
  carefully. Models frequently produce code that "looks right" but omits
  important checks.
- Watch for insecure defaults: disabled certificate verification,
  permissive CORS, overly broad IAM policies, world-readable files,
  hard-coded credentials, or weak cryptographic primitives.
- Confirm that error handling does not leak stack traces, secrets, or
  internal implementation details.
- Run the project's static analysis, dependency scanning, and CodeQL
  checks before merging.

## Licensing and provenance ##

- Do not accept large verbatim blocks of code from a model without
  understanding their origin. Generated output may resemble code from
  training data under licenses incompatible with this project's
  [public domain dedication](LICENSE).
- If a suggestion appears to be copied from an identifiable upstream
  source, locate the original and follow its license terms, including
  attribution where required.
- Prefer small, idiomatic suggestions that you can write or rewrite
  yourself over large generated blocks of uncertain origin.

## Small, auditable changes ##

- Prefer many small, reviewable AI-assisted changes over a single large
  generation that is difficult to audit.
- Generate one logical change at a time and review it before moving on.
  Stacking unreviewed generations compounds risk and makes regressions
  harder to isolate.
- Keep commits scoped and atomic so that a faulty suggestion can be
  reverted cleanly.

## Transparency and documentation ##

- When AI assistance materially shaped a non-trivial change, note it in
  the pull request description so reviewers can calibrate their
  attention. A short sentence is sufficient; detailed prompt logs are
  not required.
- Do not attribute AI tools as commit authors or co-authors. The human
  contributor is the author of record.
- Do not paste raw model output into commit messages, issues, or pull
  requests without editing it for accuracy and tone.

## Known risks to watch for ##

- **Hallucinated APIs and dependencies.** Models may invent functions,
  packages, command-line flags, or configuration options that do not
  exist. Verify against authoritative documentation.
- **Outdated patterns.** Generated code may reflect deprecated APIs,
  superseded best practices, or end-of-life library versions. Confirm
  against current upstream documentation.
- **Insecure implementations.** Cryptography, authentication, input
  parsing, and shell-command construction are common sources of subtly
  insecure generated code.
- **Supply-chain risk.** Verify that any new dependency suggested by a
  model exists, is actively maintained, and is appropriate for the
  project. Watch for typosquatting and look-alike package names.
- **Confident incorrectness.** Models present wrong answers with the
  same confidence as correct ones. Skepticism is the default posture.

## Recommended practices ##

- Keep the model's context narrow. Open only the files you intend to
  work on.
- Read every diff before accepting it. Do not bulk-accept changes
  across multiple files without inspection.
- Ask the tool to explain unfamiliar code it produced, then verify the
  explanation against documentation.
- Use AI assistance for boilerplate, refactoring, test scaffolding, and
  documentation drafts where verification is straightforward.
- Avoid using AI assistance as the primary author of security-sensitive
  code, cryptographic logic, or infrastructure-as-code that grants
  privileges.
- When a generated change touches more than a handful of files, stop and
  reconsider whether it can be broken into smaller commits.

## Pre-commit and local linting ##

This repository, and most `cisagov` projects, enforce style and quality
through [pre-commit](https://pre-commit.com/) hooks that run the same
checks as CI. AI-assisted changes frequently introduce small formatting,
whitespace, line-length, or import-ordering issues that these hooks will
catch. Running them locally before pushing keeps pull requests clean and
shortens the review cycle.

If you have not already configured the environment, follow the
[Setting up pre-commit](CONTRIBUTING.md#setting-up-pre-commit) section of
the [CONTRIBUTING](CONTRIBUTING.md) document. The short version, once
`pyenv`, `pyenv-virtualenv`, and the project virtual environment are in
place, is:

```console
pip install --requirement requirements-dev.txt
pre-commit install
```

Before opening a pull request that includes AI-assisted changes:

- Run the hooks against the full repository to catch issues outside the
  files you edited:

    ```console
    pre-commit run --all-files
    ```

- Re-stage any files that the hooks auto-fixed (for example, trailing
  whitespace, end-of-file fixes, or import sorting) and commit the
  result.
- Resolve remaining failures locally rather than relying on CI to
  surface them. Common categories include:
  - Markdown lint findings from `markdownlint` (see
    [`.mdl_config.yaml`](.mdl_config.yaml)), such as line length,
    heading style, and list style.
  - Python findings from `flake8` and `isort` (see
    [`.flake8`](.flake8) and [`.isort.cfg`](.isort.cfg)).
  - YAML findings from `yamllint` (see [`.yamllint`](.yamllint)).
  - Ansible findings from `ansible-lint` (see
    [`.ansible-lint`](.ansible-lint)) where applicable.
- If a hook fails on a file you did not knowingly change, inspect it.
  Editor- or tool-driven reformatting is a frequent side effect of
  AI-assisted workflows and should not be merged unintentionally.

Treat a clean local `pre-commit run --all-files` as a prerequisite for
opening a pull request, not as an optional convenience.
