# Onboarding Checklist #

## Instructions ##

When someone new joins the team:

1. Create a new issue called "Onboard *Name*" from this template.
1. Remove any block of tasks that doesn't apply to the new team member's role.
1. Assign the new person's onboarding buddy to this issue.
1. Remove this `Instructions` block.
1. Submit this issue.

---

## Directions ##

**Onboardee and buddy:** Try to go through your checklists in order.

**Buddy:** If you can’t complete any of the items on your checklist
personally, *you are responsible for ensuring that someone with the
correct access completes that item.*

## Onboardee checklist ##

### Getting to know VM Fusion ###

- [ ] Take notes on anything that is confusing or frustrating during your
onboarding process.
  - Please share this information with your buddy and the team so we can
  make things better.
  - If you notice a problem (especially with things like documentation), you
  are more than welcome to fix it!
  - You can also file issues and pull requests on the [template onboarding checklist].
- [ ] Meet with your onboarding buddy (they should reach out to you).
- [ ] Once you've finished the checklists below, make suggestions for steps
that would have improved your onboarding experience as pull requests on the
[template onboarding checklist] used to make this issue.

### Required items for all team members ###

Completing these items helps us fulfill security and compliance requirements.
If you get stuck, or if these requirements are confusing, ask for help from
your onboarding buddy.

#### GitHub ####

- [ ] If you don't already have a GitHub account,
[create a GitHub account with your government email address](https://github.com/join).
- [ ] If you already have a GitHub account, [add your government email address](https://docs.github.com/en/free-pro-team@latest/github/setting-up-and-managing-your-github-user-account/adding-an-email-address-to-your-github-account).
- [ ] Go through the [FISMA-Ready GitHub guide](https://github.com/fisma-ready/github)
to set up your GitHub account to be added to CISA.
- [ ] Once your GitHub account has been added to the `cisagov` organization,
make sure you're assigned to this issue.

#### Mandatory training ####

- [ ] Complete [PALMS Cybersecurity Training](https://etms.hq.dhs.gov),
including Mandatory Cyber Security and Privacy Training, and accepting
the Rules of Behavior, which is required before we can give you access to any
systems, like Trio.

### Microsoft Teams chat ###

Once you're set up on Microsoft Teams, we recommend you join the following:

- [ ] [CISA](https://teams.microsoft.com/l/team/19%3aa40fd338ea7a45de994a7c7ce9671fd4%40thread.skype/conversations?groupId=8c6c0b00-7244-46e1-bef9-76ce2a1906f5&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)
- [ ] [CSD All Staff](https://teams.microsoft.com/l/team/19%3a65f1c4b58edf4246995ae3fa732767ee%40thread.skype/conversations?groupId=6dfc3f23-3a49-44ce-ad37-6c7a9d8fb0aa&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)
- [ ] [Vulnerability Management](https://teams.microsoft.com/l/team/19%3a2161749c8eb94adeb31480e298f3b532%40thread.skype/conversations?groupId=61e939a6-2165-4085-a26e-decae97d1471&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)

### Getting to know the VM Fusion Dev Team ###

- [ ] Bookmark the [dev team project board] to track issues and work across
multiple GitHub repositories.
- [ ] Bookmark [VM JIRA] to work with the rest of VM Fusion.

### Trio Google Workspace ###

In addition to your CISA email address `first.last@cisa.dhs.gov`, you'll
also get an account on Trio, which is a Google Workspace account used for
cross-team and cross-agency collaboration and is generally
`first.last@trio.dhs.gov`. Trio may take a few days to get set up.

Once your Trio account is set up:

- [ ] Visit
  [chat.google.com](https://chat.google.com) and join applicable rooms.
- [ ] Make sure you have been added to several [dev team Google Groups] so you
can participate in team-wide internal communication:
  - [ ] [ALL Trio users](https://groups.google.com/a/beta.dhs.gov/d/forum/all)
  - [ ] [CISA COOL Administrators](https://groups.google.com/a/trio.dhs.gov/forum/#!forum/cisa-cool-group)
  - [ ] [cisa-cool-account-support](https://groups.google.com/a/trio.dhs.gov/d/forum/cisa-cool-account-support-group)
  - [ ] [cisa-cool-users](https://groups.google.com/a/trio.dhs.gov/d/forum/cisa-cool-users-group)
  - [ ] [cisagov-github](https://groups.google.com/a/trio.dhs.gov/forum/#!forum/cisagov-github-group)
  - [ ] [NCATS](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats)
  - [ ] [NCATS AWS Support](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats-aws-support)
  - [ ] [NCATS Infrastructure Development](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats-dev)
- [ ] In Google Drive, add the [NCATS Google Drive folder]. If you create
or move a doc there, it'll get the right access permissions for team members
to be able to view and edit it.
- [ ] In Google Calendar, add the [Dev Team - Events & OOO calendar](https://calendar.google.com/calendar/embed?src=beta.dhs.gov_pou7e62ob7h1qadu1m8n4o996g%40group.calendar.google.com&ctz=America%2FNew_York).

## Role-specific items ##

### Dev team ###

Useful links:

- [ ] [NCATS Data Dictionary](https://github.com/cisagov/ncats-data-dictionary)
repo for information about what's stored in the CyHy environment MongoDB databases
- [ ] [CISA COOL AWS Accounts](https://docs.google.com/spreadsheets/d/1It0FIlG7ZxTwrRV-zVYUAMw18L6ZstQiAYT7vGYf5VE/edit#gid=2069139012)
sheet for AWS accounts reference
- [ ] [Performance Plans](https://docs.google.com/spreadsheets/d/1UaGI8u70CXOGBtvJFQ85vCkPbqyDh5PVws0Xu893piw/edit?ts=5e558417&pli=1#gid=474573185)
sheet, which is similar to what you'll see in USAPerformance.
- [ ] [COOL Wiki](https://github.com/cisagov/cool-system/wiki/)
- [ ] [CyHy Wiki](https://github.com/cisagov/cyhy-system/wiki/)
- [ ] Set up your [environment on your CISA-provided Mac laptop](/dev_envs/mac-env-setup.md).

## Buddy checklist ##

- [ ] Introduce yourself to the new team member and talk about your
background so they know who you are.
- [ ] Identify a straightforward, well-defined first issue, ideally something
they could conceivably complete in their first two/three weeks using their
existing skills. Discuss the context with them, then make them the assignee.
- [ ] Discuss suggestions for how the onboarding experience could have been
improved and open as PRs on the [template onboarding checklist].

## Required items for all team members ##

- [ ] Invite them to relevant recurring meetings.
- [ ] Invite them to relevant [GitHub cisagov teams](https://github.com/orgs/cisagov/teams/).

## Required items for VM Fusion dev team members ##

- [ ] Add them as a member of the [Dev Team - Events & OOO calendar].
- [ ] Add them as a member of the [NCATS Infrastructure Development group](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats-dev).

<!-- Links for use throughout the checklist -->
[template onboarding checklist]: https://github.com/cisagov/development-guide/blob/master/onboarding-checklist.md
[NCATS Google Drive folder]: https://drive.google.com/drive/folders/0APw76nbCAmzuUk9PVA
[Dev Team - Events & OOO calendar]: https://calendar.google.com/calendar/embed?src=beta.dhs.gov_pou7e62ob7h1qadu1m8n4o996g%40group.calendar.google.com&ctz=America%2FNew_York
[VM JIRA]: https://jira.ceil.cyber.dhs.gov/secure/Dashboard.jspa

<!-- dev team -->
[dev team project board]: https://app.zenhub.com/workspaces/vm-bizops-dev-5e596691c12d3435405dfaf3/board
[dev team Google Groups]: https://groups.google.com/a/trio.dhs.gov/forum/#!myforums
