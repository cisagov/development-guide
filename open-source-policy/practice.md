# Practicing our open source policy #

We have an "open-by-default" development policy. This document is meant to
give specific team guidance on putting our [open source policy](policy.md)
into practice.

- CISA releases software into the [international public domain](#public-domain).
- Contribute back to outside open source projects whenever possible.
- We [develop our software in the open](#working-in-public), while also
  [protecting sensitive information](#protecting-sensitive-information).
- There are [narrow, documented exceptions](policy.md#exceptions) where we may
  delay or withhold source code.

CISA team members should work with the strong presumption that all of their
code will be public, both during and after development.

Before deciding to delay or withhold the release of source code, consult with
the team and be prepared to publicly document this exception.

## Public domain ##

[By law](http://www.law.cornell.edu/uscode/text/17/105), works of the United
States government are not copyrightable in the US, and so are public domain.
But by default, US government works **are** copyrightable internationally, and
so CISA intentionally waives this copyright abroad using
[Creative Commons Zero (CC0) 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

There are potentially other cases where copyright is involved: where
contractors produce the work, or where work was otherwise originally performed
outside the capacity of a US government employee.

To the extent CISA has the rights to do so, CISA will normalize the copyright
status of its work product under CC0.

## Contributing back to outside projects ##

CISA staff are encouraged to seek existing, open source solutions -- whether
government or non-government -- before writing custom tools. When existing
libraries need to be modified or improved, CISA staff should make the
modifications with eventual upstream contribution in mind.

In practice, this generally involves forking the relevant repository to the
CISA organization within GitHub (`cisagov`), creating a new branch with the
modifications, and sending a pull request to upstream from the CISA fork.
Unlike our own projects, there is no need for internal code review in this
scenario (though it doesn't hurt).

In terms of licensing: as works of the government, employee contributions are
public domain in the United States, regardless of the outside project's
contribution agreement. This does not change the overall license status of the
outside project.

As [the Free Software Foundation says](https://www.gnu.org/licenses/gpl-faq.html#GPLUSGovAdd)
about government-contributed improvements to GPL software:

> Yes. If the improvements are written by US government employees in the
course of their employment, then the improvements are in the public domain.
However, the improved version, as a whole, is still covered by the GNU GPL.
There is no problem in this situation.

See also: [The Department of Defense's FAQ question about this](http://dodcio.defense.gov/Open-Source-Software-FAQ/#Q:_Can_government_employees_contribute_code_to_open_source_software_projects.3F).

### Contributor License Agreements (CLAs) ###

Some external projects have CLAs. You cannot sign these yourself, in your
official capacity.

1. See if there is an organizational CLA available
1. Send the agreement to DHS's Office of General Counsel (OGC) for review
    - Email
      [github@cisa.dhs.gov](mailto:github@cisa.dhs.gov)
      to determine the best contact
1. Collect names/emails/GitHub usernames (whatever is needed) for folks you
think will be contributing
    - Err on the side of adding too many than too few - this is much easier
1. Get it signed
1. Add to list below
1. Contribute

CISA currently has the following CLAs signed:

- None 😒

## How to license CISA repos ##

When creating a repo, we highly recommend that you start from one of our
maintained skeleton projects.  This will quickly get you setup with the
correct LICENSE and CONTRIBUTING documents as well as some spiffy tooling to
keep your project healthy.  See our [project setup](/project_setup) document
for the best way to do this.

## Accepting contributions from the public ##

Any CISA project can (and should!) accept open source contributions from the
public.

Projects can **encourage public contributions** by:

- Creating open issues where public help would be especially welcome
- Labeling those issues with `help wanted` so people can scan issues quickly
and [services](http://www.codeforamerica.org/geeks/civicissues) can aggregate
volunteer opportunities
- Asking for contributions, in the README and in other public writing about the
  project
- Providing solid documentation for any project setup process
- Being super nice when communicating with volunteers

As [described above](#public-domain), CISA projects are dedicated to the
international public domain wherever possible. In this situation, contributors
must agree to release their contributions into the international public
domain. Projects can inform contributors of this agreement by copying the
[`CONTRIBUTING.md`](CONTRIBUTING.md) file from this repo into new project
repos, and copying the
["Public domain" section of this repo's README](README.md#public-domain)
into the new project's README.

When an CISA project has a non-standard license status (e.g. it's a fork of a
previously licensed project, or is a module/plugin for a GPL project), then
that project needs to figure out an appropriate contributing agreement.

## Working in public ##

CISA believes in
[working in public](https://18f.gsa.gov/2014/07/31/working-in-public-from-day-1/)
It creates a healthier working environment, a more collaborative process, and
just better software.

All CISA team members are expected to make new source code
repositories public from the time of creation. This means we often
publish drafts in our repos that may change substantially. If you're
interested in learning more about the contents of a repo, email
[github@cisa.dhs.gov](mailto:github@cisa.dhs.gov)
and we'll direct you to the right person or team.

## Protecting sensitive information ##

As part of responsibly working in the open, CISA team members are expected to
protect information that needs to be protected. We already receive training
and guidance about information we can’t publish for [ethical](https://www.oge.gov/web/oge.nsf/Topics),
[legal](https://handbook.18f.gov/intro-to-18f-infrastructure/), and [security](https://insite.gsa.gov/portal/content/627226)
reasons — this section is a reminder about sensitive information (formally
called “[controlled unclassified information](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171.pdf)”)
to carefully protect when working with our open source projects. Sensitive
information can include code, configuration, content, or documentation. (We
have [approved options for sharing sensitive information](https://handbook.18f.gov/sensitive-information/).)

If CISA team members aren't sure whether they should make something public,
they should ask a person on our CISA Infrastructure team for advice *first*.

If CISA team members inadvertently come into the possession of classified
information (Secret, Top Secret, etc.), they should immediately report the
incident and follow the established information spill procedures.

Sensitive information we need to protect includes, but is not limited to:

- Information an attacker could plausibly use to help them compromise any
system (including a prototype/development system). Examples:
  - **Secret keys:** Passwords, passcodes, access codes, access tokens, API
  keys, TLS keys, SSH keys, OAuth secrets, or any other “secret keys” that
  protect access to something.
  - **Undisclosed vulnerabilities:** If we know of a security problem or
  potential security problem with our code that isn’t already publicly-known
  (such as a vulnerability that can’t be found with a publicly-available open
  source scanning tool run on the public-facing system), we shouldn’t write
  publicly about it until we fix it.
- Nonpublic information in general about vulnerabilities, including
attribution/source information (such as how and when we learned about a
vulnerability, if the disclosure to us was not public).
- We may wish to withhold some non-CISA IP addresses. If something looks like
an IP address, ask CISA Infrastructure before publishing that info.
- Personally Identifiable Information (PII). Here’s [OMB's definition and GSA's policy](http://www.gsa.gov/portal/content/104256).
18F also has [guidance for systems involving PII](https://pages.18f.gov/before-you-ship/security/pii/).
- Some kinds of procurement and acquisition information, which may include
non-public cost or pricing data, contract information, trade secrets, indirect
costs, and direct labor rates. If you’re an CISA team member working with this
kind of data, ask our acquisition specialists for help determining whether it
can be public.
- Emergency procedures, such as evacuation plans.

There are more categories of controlled unclassified information to protect;
those are just the kinds that we work with most often. Here’s the
[complete list of CUI categories](https://www.archives.gov/cui/registry/category-list).

## Private repositories ##

If the CISA Infrastructure team determines that a repository should not be
public, as described in the [open source policy](policy.md#exceptions), the
reasoning should be documented and a link to that reasoning provided in the
repository's `README` to preserve that knowledge and so the decision can be
revisited in the future if circumstances change.  If the underlying reasons
for making the repository private are not themselves sensitive, this
explanation can be placed directly in the `README`.

## Managing CISA resources ##

CISA intends to produce great software for the American people. That means not
just rushing through projects to get them working as fast as possible, but
managing [technical debt](https://en.wikipedia.org/wiki/Technical_debt) with
an eye towards usability and reusability.

If a refactoring or feature makes the tool easier for CISA to use in its work,
and the teammate doing it is otherwise meeting their duties, then that's time
well spent for CISA and the taxpayer.

Open source projects can - and hopefully do! - get use and uptake from outside
CISA. It's also okay for individual teammates to create projects they intend
to use both at CISA and in their personal capacity.

Teammates do not need permission to start new open source projects in the CISA
GitHub organization. However, generally speaking, these projects should have
some work applicability.

When creating new open source projects:

- If you're creating a repo because it's primarily for your CISA work, and the
work you perform in it is primarily to benefit CISA, start the repo's life in
the CISA organization. It's okay if you also think it'll be helpful in
personal work.
- If you're creating a repo that isn't primarily for CISA work, but you think
will likely see use at CISA, start it in your personal account. If you don't
have strong feelings or concerns about ownership, consider releasing the
project under CC0 to save yourself even having to ever think about it.

As people open issues and request features (no matter whether the repo is in
your account or CISA's), continue to exercise professional judgment about how
to spend CISA time.

If you think something will benefit CISA and is worth the time, then that's
valuable CISA work. If it won't benefit CISA but makes the library better for
other uses, that may best be done with personal time.

## Archiving a repository ##

When a repository is no longer useful, it should be [archived](https://help.github.com/articles/archiving-repositories/).
This may be because the work has been incorporated into another repository,
the project is unmaintained and out-of-date, or some other reason. In order to
preserve repository metadata like pull request discussions and issues, the
repository should not be deleted or made private.
