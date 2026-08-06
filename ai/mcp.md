# Model Context Protocol (MCP) Servers #

The Model Context Protocol (MCP) is an open protocol that lets AI
agents call out to external servers for tools, resources, and data.
An MCP server can expose anything from a local script to a hosted
API. Once configured, the agent can invoke it during a session in
much the same way it reads files or runs shell commands.

MCP servers expand what an agent can do. They also expand the
attack surface and the set of systems that may receive project
context. Treat MCP configuration as a security-relevant change.

For broader context on responsible use of AI tools, see the
[AI-Assisted Development guide](../ai-assisted-development.md). For
how MCP relates to Rules and Skills, see this directory's
[README](README.md).

## When to use an MCP server ##

Use an MCP server when:

- The capability is not reasonably available through the agent's
  built-in tools or a checked-in script.
- The integration is reusable across sessions and contributors.
- The server, its source, and its data-handling behavior are
  understood and acceptable for the project.

Do *not* use an MCP server when:

- A simple, reviewed script in the repository would do the same job.
- The server's source, maintainer, or data-handling policy is
  unknown.
- The server would receive secrets, credentials, customer data, or
  other non-public information that has not been approved for that
  destination.

## Standards ##

- MCP server configuration is checked in, reviewed in pull requests,
  and owned via `CODEOWNERS`. Configuration that only lives on an
  individual contributor's machine is not subject to project review
  and should not be relied on by the project.
- MCP servers must not receive secrets, credentials, tokens,
  customer data, internal hostnames, or any non-public information
  unless the destination has been explicitly approved for that data.
- Credentials required by an MCP server are supplied through the
  environment or an approved secrets mechanism. They are never
  committed to the repository.
- Each MCP server in use has a clear, narrow purpose recorded
  alongside its configuration, including who owns it and what data
  it may receive.
- Adding, removing, or materially changing an MCP server is called
  out in the pull request description so reviewers can scrutinize
  the change.

## Defaults ##

- Prefer first-party or well-known MCP servers over unfamiliar
  third-party ones. Pin to a specific version or commit rather than
  tracking a moving tag.
- Prefer servers that run locally and operate on the workspace over
  hosted servers that receive workspace contents over the network,
  when both options are viable.
- Grant each MCP server the narrowest set of capabilities it needs.
  Disable tools, scopes, or permissions that the project does not
  use.
- Keep the list of enabled MCP servers small. Every additional
  server is additional surface to review and maintain.
- Document, near the configuration, what each enabled server is for
  and when it should be used.

## Suggestions ##

- Periodically review the list of enabled MCP servers and remove any
  that are no longer used. Unused servers quietly accumulate risk.
- When evaluating a new MCP server, read its source (or the
  authoritative documentation if it is a hosted service), confirm
  its maintenance status, and note what it does with the inputs it
  receives.
- For MCP servers that take action against external systems (for
  example, creating issues, opening pull requests, or modifying
  cloud resources), prefer configurations that require human
  confirmation before each action.
- If a project uses several AI tools, keep MCP configuration in a
  single, conventional location per tool rather than duplicating it.
  Reference shared documentation about what each server is for.

## What to put in MCP configuration ##

Useful content includes:

- The server name and a short description of its purpose.
- The command, package, or endpoint used to reach the server, pinned
  to a specific version where possible.
- The minimum permissions or scopes the project actually needs.
- The owner or team responsible for keeping the configuration
  current.

Avoid:

- Secrets, tokens, or credentials in the configuration file. Use
  environment variables or an approved secrets mechanism.
- Server entries with no description, no owner, and no obvious
  current use.
- Broad, "everything enabled" configurations. Narrow scope is the
  default.

## Review expectations ##

- Adding a new MCP server is a security-relevant change. Reviewers
  should confirm the server's source, its data-handling behavior,
  and the scope of access being granted.
- Changes that broaden an existing server's scope (new tools, new
  permissions, new endpoints) receive the same scrutiny as adding a
  new server.
- Removing an MCP server is usually low-risk and should be
  preferred when the server is no longer in active use.

## Limitations ##

MCP configuration controls what the agent *can* reach. It does not
control what the agent *will* do with that reach in any given
session. Outputs from MCP servers are untrusted input: they may be
inaccurate, out of date, or shaped by an attacker who controls the
upstream system. Validate results before acting on them, and apply
the same review expectations to code or changes produced with the
help of an MCP server as to any other AI-assisted change. See the
[AI-Assisted Development guide](../ai-assisted-development.md) for
the full set of expectations.
