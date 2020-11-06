# Onboarding Checklist #

## Instructions ##

When someone new joins the team:

1. A team member adds the new team member to the `cisagov` organization in
GitHub.
1. Create a new issue called "Onboard _Name_".
1. View the raw source of this file.
1. Copy the text after the line below to the issue.
1. Remove any block of tasks that doesn't apply to the new team member's role.
1. Submit the issue.
1. Assign the new person and their onboarding buddy to the issue.
1. Move the issue into _In Progress_.

---

## Directions ##

**Onboardee and buddy:** Try to go through your checklists in order.

**Buddy:** If you can’t complete any of the items on your checklist
personally, _you are responsible for ensuring that someone with the
correct access completes that item._

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

Pre-requisites:

- [ ] Complete [PALMS Cybersecurity Training](https://etms.hq.dhs.gov),
including Mandatory Cyber Security and Privacy Training, including accepting
the Rules of Behavior, which is required before we can give you access to any
systems, like Trio.
- [ ] Go through the [FISMA-Ready Github guide](https://github.com/fisma-ready/github)
to set up your GitHub account to be added to CISA.

### Microsoft Teams chat ###

Once you're set up on Microsoft Teams, we recommend you join the following:

- [ ] [CISA](https://teams.microsoft.com/l/team/19%3aa40fd338ea7a45de994a7c7ce9671fd4%40thread.skype/conversations?groupId=8c6c0b00-7244-46e1-bef9-76ce2a1906f5&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)
- [ ] [CSD All Staff](https://teams.microsoft.com/l/team/19%3a65f1c4b58edf4246995ae3fa732767ee%40thread.skype/conversations?groupId=6dfc3f23-3a49-44ce-ad37-6c7a9d8fb0aa&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)
- [ ] [Vulnerability Management](https://teams.microsoft.com/l/team/19%3a2161749c8eb94adeb31480e298f3b532%40thread.skype/conversations?groupId=61e939a6-2165-4085-a26e-decae97d1471&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)

### Getting to know the VM Fusion Dev Team ###

- [ ] Bookmark the [dev team project board] to track issues and work across
multiple Github repositories.
- [ ] Bookmark [VM JIRA] to work with the rest of VM Fusion.
- [ ] In addition to your CISA email address `first.last@cisa.dhs.gov`, you'll
also get an account on Trio, which is a Google Workspace account used for
cross-team and cross-agency collaboration and is generally
`first.last@trio.dhs.gov`. Trio may take a few days to get set up.
  - Once you're set up on Trio, visit
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
- [ ] Add the [NCATS Google Drive folder] to your Google Drive. If you create
or move a doc there, it'll get the right access permissions for team members
to be able to view and edit it.

## Role-specific items ##

### Dev Team ###

Useful links:

- [ ] [NCATS Data Dictionary](https://github.com/cisagov/ncats-data-dictionary)
repo for information about what's stored in the MongoDB database
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
- [ ] Identify a straightforward, well-defined issue that involves
their skills domain, schedule a meeting with the owner for an introduction (if
it's not you), and set up pairing sessions several times a week to start.
- [ ] Identify a straightforward, well-defined first story, ideally something
they could conceivably complete in their first two/three weeks using their
existing skills. Discuss the context with them, then make them the assignee.
- [ ] Discuss suggestions for how the onboarding experience could have been
improved and open as PRs on the [template onboarding checklist].

## Required items for all team members ##

- [ ] Invite them to relevant recurring meetings.
- [ ] Invite them to relevant [Github cisagov teams](https://github.com/orgs/cisagov/teams/).

## Platform- and compliance-specific required items ##

- [ ] Help them review and understand the responsibilities of becoming a
VM Fusion team member.
- Grant them access to the following:
  - [ ] [CISA AWS Accounts](https://docs.google.com/spreadsheets/d/1It0FIlG7ZxTwrRV-zVYUAMw18L6ZstQiAYT7vGYf5VE/edit#gid=2069139012)
  and provide one-time credentials.
  - Note: AWS user names should be identical across accounts so that
  permissions can be correctly managed by Terraform.

<!-- Links for use throughout the checklist -->
[template onboarding checklist]: https://github.com/cisagov/development-guide/blob/master/onboarding-checklist.md
[NCATS Google Drive folder]: https://drive.google.com/drive/folders/0APw76nbCAmzuUk9PVA
[VM JIRA]: https://jira.ncats.cyber.dhs.gov/secure/Dashboard.jspa

<!-- dev team -->
[dev team project board]: https://app.zenhub.com/workspaces/vm-bizops-dev-5e596691c12d3435405dfaf3/board
[dev team Google Groups]: https://groups.google.com/a/trio.dhs.gov/forum/#!myforums