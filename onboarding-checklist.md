# Onboarding Checklist

## Instructions

When someone new joins the team:

1. A team member adds the new team member to the `cisagov` organization in GitHub. This constitutes 'formal approval` by leadership
1. Create a new issue in the [somewhere??]() called "Onboard [NewPerson]".
  * Use of a private repo helps satisfy AC-2, that we have officially added a person to our team before further onboarding.
2. View the raw source of this file.
3. Copy the text after the line to the issue, replacing "NewPerson" with the new person's name and  "Buddy" with the onboarding buddy's name.
3. Remove any block of tasks that doesn't apply to the new team member's role
4. Submit the issue.
5. Assign the new person and the new person's Onboarding Buddy to the issue.
6. Put the issue into _Doing_.

---

To get NewPerson productively contributing to the team, Buddy should help NewPerson complete a prescribed set of tasks that will bring them up to speed.

## Directions

**NewPerson and Buddy:** Try to go through your checklists in order.

**Buddy:** If you can’t complete any of the items on your checklist personally, _you are responsible for ensuring that someone with the correct access completes that item_.

## New Person checklist

### Getting to know VM Fusion

- [ ] Take judicious notes on what about your onboarding process is confusing or frustrating.
    - Please share this information with your buddy (or the team) so we can make things better.
    - If you notice a problem (especially with things like documentation), you are more than welcome to fix it!
    - You can also file issues and pull requests on the [template onboarding checklist]
- [ ] Figure out who your onboarding buddy is (they should reach out to you).
<!-- - [ ] Read [the team onboarding document](https://github.com/cloud-gov/product/blob/master/Onboarding.md) for more context. -->
<!-- - [ ] Bookmark the [pertinent links listed here](https://github.com/cloud-gov/product/blob/master/PertinentLinks.md). -->
<!-- - [ ] Read the [Delivery Process document](https://github.com/cloud-gov/product/blob/master/DeliveryProcess.md) to learn about how we work. -->
- [ ] Once you've finished the checklists below, make suggestions for steps that would have improved your onboarding experience as pull requests on [template onboarding checklist] used to make this issue.

### Required items for all team members

Completing these items helps us fulfill security and compliance requirements. If you get stuck, or if these requirements are confusing, ask for help from your onboarding buddy.

Pre-requisites:

- [ ] Complete [PALMS Cybersecurity Training](https://etms.hq.dhs.gov), including Mandatory Cyber Security and Privacy Training, including accepting the Rules of Behavior, which is required before we can give you access to any systems, like Trio.
- [ ] Go through the [FISMA-Ready Github guide](https://github.com/fisma-ready/github) to set up your Github account to be added to CISA

Learn our policies and procedures:

- [ ] []()

Read the following documents as well, which explain our practices in a formal written way. Reach out to your buddy or the team if anything is unexpected or confusing.

- [ ] []()

### Microsoft Teams chat

Once you're set up on Microsoft Teams, we recommend you join the following:

- [ ] [CISA](https://teams.microsoft.com/l/team/19%3aa40fd338ea7a45de994a7c7ce9671fd4%40thread.skype/conversations?groupId=8c6c0b00-7244-46e1-bef9-76ce2a1906f5&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)
- [ ] [CISA - VM- Fusion Branch](https://teams.microsoft.com/l/team/19%3a2d4e9f3e321f4ef9a09f4ed94a32105c%40thread.skype/conversations?groupId=2992771f-df53-4097-87dd-75898a5830db&tenantId=3ccde76c-946d-4a12-bb7a-fc9d0842354a)

### Getting to know the VM Fusion Dev Team

- [ ] Bookmark the [dev team project board] to track issues and work across multiple Github repositories
- [ ] Bookmark [VM JIRA] to work with the rest of VM Fusion.
- [ ] In addition to your CISA email address `first.last@cisa.dhs.gov`, you'll also get an account on Trio, which is a Google-based account used for cross-team and cross-agency collaboration and is generally `first.last@trio.dhs.gov`. Trio may take a few days to get set up.
    - Once you're set up on Trio, visit [chat.google.com](https://chat.google.com) and join applicable rooms.
- [ ] Make sure you have been added to several [dev team Google Groups] so you can participate in team-wide internal communication:
    - [ ] [ALL Trio users@beta.dhs.gov](https://groups.google.com/a/beta.dhs.gov/d/forum/all)
    - [ ] [CISA COOL](https://groups.google.com/a/trio.dhs.gov/forum/#!forum/cisa-cool-group)
    - [ ] [cisagov-github](https://groups.google.com/a/trio.dhs.gov/forum/#!forum/cisagov-github-group)
    - [ ] [NCATS@beta.dhs.gov](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats)
    - [ ] [NCATS AWS Support@beta.dhs.gov](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats-aws-support)
    - [ ] [NCATS Infrastructure Development@beta.dhs.gov](https://groups.google.com/a/beta.dhs.gov/d/forum/ncats-dev)
- [ ] Add the [NCATS Google Drive folder] to your Google Drive. If you create or move a doc there, it'll get the right access permissions for team members to be able to view and edit it.

## Role-specific items

### Dev Team

Useful links:

- [ ] [NCATS Data Dictionary](https://github.com/cisagov/ncats-data-dictionary) repo for information about what's stored in the MongoDB database 
- [ ] [CISA COOL AWS Accounts](https://docs.google.com/spreadsheets/d/1It0FIlG7ZxTwrRV-zVYUAMw18L6ZstQiAYT7vGYf5VE/edit#gid=2069139012) sheet for AWS accounts reference
- [ ] [Performance Plans](https://docs.google.com/spreadsheets/d/1UaGI8u70CXOGBtvJFQ85vCkPbqyDh5PVws0Xu893piw/edit?ts=5e558417&pli=1#gid=474573185) sheet, until performance plans are individualized again (sometime after June 2020)
- [ ] [COOL Wiki](https://github.com/cisagov/cool-system/wiki/)
- [ ] 

### Platform-Ops- and compliance-specific items

- [ ] Install `caulking` git leak prevention by following the [README](https://github.com/cloud-gov/caulking/blob/master/README.md)
- [ ] Verify `caulking` by running `make audit` and pasting a screenshot as a comment on this GitHub issue
- [ ] Review the System Security Plan (the latest version lives on [Google Drive](https://drive.google.com/drive/u/0/folders/0B6fPl5s12igNX3JwR2xFZVpmek0); look for "cloud.gov System Security Plan (SSP)" as a `.docx` file). Of particular note for onboarding: Section 9 (System Description) and Section 10 (System Environment)
- [ ] Join the `#cg-platform`, `#cg-platform-news`, and `#cg-support` channels on Slack.
- [ ] Bookmark the [GitHub Projects Board](https://github.com/orgs/cloud-gov/projects/2)
- [ ] Add the [Developer Docs Google Drive folder](https://drive.google.com/drive/folders/1-JuCl9WmxjOMPNCUI49srHHuEtkA4BoE) to your Google Drive - these docs serve as supplemental documentation to the [cloud.gov site Team Documentation section](https://cloud.gov/docs/ops/repos/)
- [ ] Learn about [setting up a local development environment](https://cloud.gov/docs/ops/setting-up-a-local-development-environment/), which contains setup instructions for GSA Macs for the rest of these software items
- Learn about [Cloud Foundry](https://www.cloudfoundry.org/)
  - [ ] Watch [Build Your Own Private Cloud Foundry](https://www.youtube.com/watch?v=v85r4Hy3jbs) to learn about running Cloud Foundry
  - [ ] Set up Cloud Foundry locally using [cfdev](https://github.com/cloudfoundry-incubator/cfdev) and push an app to it
  - [ ] Join [the Cloud Foundry Slack](http://slack.cloudfoundry.org/) in case you need to ask questions of upstream developers
- Learn about [BOSH](https://bosh.io/):
  - [ ] Watch [this video](https://www.youtube.com/watch?v=2jpN1mSPZ4Q)
  - [ ] Complete this [tutorial for BOSH](https://mariash.github.io/learn-bosh/)
  - [ ] For a bit of levity, read [this](http://events.linuxfoundation.org/sites/events/files/slides/seven-stages-of-bosh.pdf)
- [ ] Get to know how UAA is deployed/integrated
- Get familiar with [Terraform](https://www.terraform.io/)
  - [ ] Go through the [getting started guide](https://www.terraform.io/intro/getting-started/install.html)
  - [ ] Examine [our provisioning procedures](https://github.com/cloud-gov/cg-provision)
- Learn about [Concourse](https://concourse.ci/)
  - [ ] Try a [tutorial](https://github.com/starkandwayne/concourse-tutorial).
  - [ ] Check out our [staging](https://ci.fr-stage.cloud.gov/) and [production](https://ci.fr.cloud.gov) Concourse instances, and take a look at some of [our pipelines](https://github.com/search?q=org%3A18F+cg-deploy).
  - [ ] Join [the Concourse Discord](https://discordapp.com/invite/MeRxXKW) in case you need to ask questions of upstream developers.
- Learn about [Kubernetes](https://kubernetes.io/)
  - [ ] Go through the [official tutorial](https://kubernetes.io/docs/tutorials/kubernetes-basics/)
  - [ ] Read about [ETCD: The Brain of a Kubernetes Cluster](https://medium.com/better-programming/a-closer-look-at-etcd-the-brain-of-a-kubernetes-cluster-788c8ea759a5)
  - [ ] Read about [Raft: Understandable Distributed Consensus](http://thesecretlivesofdata.com/raft/)
  - [ ] Read the cloud.gov guide for [troubleshooting k8s](https://cloud.gov/docs/ops/runbook/troubleshooting-kubernetes/)
  - [ ] Watch [The illustrated Children's Guide to Kubernetes](https://youtu.be/4ht22ReBjno)
- Get familiar with our AWS setup
  - [ ] Read about [AWS onboarding](https://cloud.gov/docs/ops/aws-onboarding/)
  - [ ] Read about the [AWS CLI](https://aws.amazon.com/cli/)
- [ ] Review the [ongoing maintenance and support tasks](https://cloud.gov/docs/ops/maintenance-list/)
- [ ] Make sure that OpsGenie will alert you through at least one of these ways:
  - [ ] Install/configure the app on the phone, go to the app settings, and change the alert for Low-Urgency alerts to actually alert you (make noise, vibrate, etc).
  - [ ] Make sure that OpsGenie is set up to alert you via email, and make sure that when it sends you an alert, it gets into your inbox, not spam.  If it gets into spam, releasing the spam seems to make it so that future emails will not make it there.
- [ ] Join [the cloud.gov operations notifications Google Group](https://groups.google.com/a/gsa.gov/forum/?hl=en#!forum/cloud-gov-notifications), so you can see alert information if OpsGenie is unavailable

### Business unit-specific items

- [ ] Bookmark the [Github Project board](https://github.com/orgs/cloud-gov/projects/2)
- [ ] Join Slack channels especially `#cg-business` and `#cg-platform`.
- [ ] Ask Director or Deputy Director to add you to the [cloud-gov-inquiries](https://groups.google.com/a/gsa.gov/forum/#!forum/cloud-gov-inquiries), [cloud-gov-support](https://groups.google.com/a/gsa.gov/forum/#!forum/cloud-gov-support), [cloud-gov-notifications](https://groups.google.com/a/gsa.gov/forum/#!forum/cloud-gov-notifications), and [cloud-gov-emergency](https://groups.google.com/a/gsa.gov/forum/#!forum/cloud-gov-emergency) groups.
- [ ] Read [how the cloud-gov-emergency group works](https://docs.google.com/document/d/1O5UW1M-XX8YIZJV1OcF1EqGWjPnNUi7L0mZpJZ6d-cs/edit#), and set up push notifications for these emails from your work smartphone if appropriate for your role.
- [ ] [If not also Cloud Ops], ask Director or Deputy Director for view-only access to [admin UI](https://admin.fr.cloud.gov).
- [ ] Ask `#acquisition` for the Acquisition NDA so you can sign it, if you haven't already.
- [ ] [If not also Cloud Ops] If appropriate for your role, ask for access to billing info in commercial AWS account from Director or Deputy Director.
- [ ] Review the primary cloud.gov sites: [the dashboard](https://dashboard.cloud.gov/#/), [main landing page](https://cloud.gov/), and [documentation](https://cloud.gov/docs/).
- [ ] Bookmark link to [design folder](https://drive.google.com/drive/u/1/folders/0BwLqM4Nicmq-bUt0NjRjclFMUEU).
- [ ] Read and bookmark our [Google Doc on cloud.gov Analytics](https://docs.google.com/document/d/1gSbP2ak2a3QLpCZIF_KlbQ2QHE6RjDI-7ZnnrJZvMDE/edit)
- [ ] [Request access to 18F Google Analytics](https://handbook.18f.gov/google-analytics/), so you can view cloud.gov site analytics ([including for the dashboard](https://docs.google.com/document/d/1gSbP2ak2a3QLpCZIF_KlbQ2QHE6RjDI-7ZnnrJZvMDE/edit)).
- [ ] Also request access to [Google Tag Manager](https://tagmanager.google.com/) which we mostly use to manage event tracking in Google Analytics.
- [ ] Ask the Director or Deputy Director for an invite to a DigitalGov Search account for cg-site, so you can configure it and view analytics for the most common searches.
- [ ] Review the dashboard: current [prod](https://dashboard.fr.cloud.gov/#/), [staging](https://dashboard-staging.app.cloud.gov/#/), and [beta](https://dashboard-beta.cloud.gov/#/).

### If developing or working on cloud.gov site content

- [ ] Review the [dashboard contributing guide](https://github.com/cloud-gov/cg-dashboard/blob/master/CONTRIBUTING.md) and [`cg-style` standards](https://github.com/cloud-gov/cg-style/) which help frame what we're looking for in code review
- [ ] Set up the [landing/docs page](https://github.com/cloud-gov/cg-site), [dashboard](https://github.com/cloud-gov/cg-dashboard), and [`cg-style`](https://github.com/cloud-gov/cg-style) locally
- [ ] Set up `cg-style` to be [linked to the other sites locally](https://github.com/cloud-gov/cg-style#development-and-contributing-setup)
- [ ] For additional development environment setup, see [setting up a local development environment](https://cloud.gov/docs/ops/setting-up-a-local-development-environment/), which contains setup instructions for GSA Macs

### New Director (System Owner) items

- [ ] Ask `#tock` to list you as the project contact for cloud.gov lines.
- [ ] Ask previous Director to give you Owner access to Nessus Manager (this requires the current primary contact access to Nessus, and then the owner of the license key also needs to change to the new director so that the new director can reset license keys - lastly, the new director needs to be made the primary contact).
- [ ] Ask previous Director to give you Owner access in Zendesk.
- [ ] Ask previous Director to give you [AWS account ownership](https://cloud.gov/docs/ops/aws-onboarding/) for GovCloud.
- [ ] Ask System Owner or previous Director to give you cloud.gov calendar ownership.
- [ ] Ask System Owner or previous Director to give you owner permission on the Google Groups. This should include [our Google Groups for our AWS accounts](https://docs.google.com/document/d/110o1L7EOby3hvE5d-cDhg2LBLHymbZLnMPe9kuk4qp8/edit#).
- [ ] Ask System Owner or previous Director to let TTS Infrastructure know you are the new technical contact for cloud.gov.
- [ ] Ask Cloud Ops for read-write access to Admin UI.
- [ ] Review the [GSA Information Technology (IT) Security Policy](https://insite.gsa.gov/portal/content/520281) to understand our responsibilities as part of GSA.
- [ ] Review the [cloud.gov System Security Plan version 1.33](https://drive.google.com/drive/folders/0B6fPl5s12igNX3JwR2xFZVpmek0).

### Non team-specific items

_Note: These are items that do not fall into the boundary of work for a specific team. However, please consult your onboarding buddy to verify that your work relates to these items prior doing these two checklists._

### Compliance-specific items

- [ ] Join the `#cg-compliance` channel on Slack.
- [ ] Watch [Handling FISMA Faster and Better](https://www.youtube.com/watch?v=T1S52B1-NT4) for important context and background on the federal regulatory context in which cloud.gov operates.
- [ ] Do a cursory read of [Before You Ship](https://pages.18f.gov/before-you-ship/).

### Services-specific items

- [ ] Read about Cloud Foundry [services from a user perspective](http://docs.cloudfoundry.org/devguide/services/).
- [ ] Read about [implementing services](http://docs.cloudfoundry.org/services/).
- [ ] Take a look at [our existing brokers](https://github.com/cloud-gov?q=broker).
- [ ] Learn about [Concourse](https://concourse.ci/)
  - [ ] Try a [tutorial|https://github.com/starkandwayne/concourse-tutorial].
  - [ ] Check out our [staging](https://ci.fr-stage.cloud.gov/) and [production](https://ci.fr.cloud.gov) Concourse instances, and take a look at some of [our pipelines](https://github.com/search?q=org%3A18F+cg-deploy).
- [ ] Join [the Cloud Foundry Slack](http://slack.cloudfoundry.org/).

## Buddy checklist

- [ ] Introduce yourself to the new team member and give them some of your background so they know who you are.
- [ ] Identify a straightforward, well-groomed story in progress that involves their skills domain, schedule a meeting with the owner for an introduction (if it's not you), and setup pairing sessions several times in the first week on the project.
- [ ] Identify a straightforward, well-groomed first story, ideally something they could conceivably complete in their first two/three weeks using their existing skills. Discuss the context with them, then make them the assignee for the card.
- [ ] Discuss suggestions for how the onboarding experience could have been improved and open as PRs on [the onboarding template](https://github.com/cloud-gov/product/blob/master/OnboardingChecklist.md).
- [ ] Ask the Director or Deputy Director to add the person to [Zendesk](https://cloud-gov.zendesk.com), so they can see how we handle support and read technical discussions happening with outside groups.
- [ ] Invite them to the private Slack channel `#cg-supportstream`, used for Zendesk integration to post and discuss new support tickets.

## Required items for all team members

These items help us fulfill security and compliance requirements (including for FedRAMP).

- [ ] Make sure they're in [the list of people working on the project](https://docs.google.com/spreadsheets/d/1mW3tphZ98ExmMxLHPogSpTq8DzYr5Oh8_SHnOTvjRWM/edit#gid=0).
- [ ] Add their name, whether they're Cloud Ops (Platform), and the date they joined the team to the [training tracker](https://docs.google.com/spreadsheets/d/1hqU6cNeEB293OT0j3OvbdAFRkrf2zDOrPVxGfnr4sSw/edit#gid=0). Copy the formulas for the due dates from an existing row (grab the "corner" of the cells and pull down).
- [ ] As they complete training, fill out their completion dates in the [training tracker](https://docs.google.com/spreadsheets/d/1hqU6cNeEB293OT0j3OvbdAFRkrf2zDOrPVxGfnr4sSw/edit#gid=0).
- [ ] Add them to the @cloud-gov-team [in Slack’s Team Directory](https://get.slack.help/hc/en-us/articles/212906697-User-Groups#edit-a-user-group).
- [ ] Add them to the recurring cloud.gov meetings that are relevant for them in [the team calendar](https://calendar.google.com/calendar/embed?src=gsa.gov_0samf7guodi7o2jhdp0ec99aks@group.calendar.google.com&amp;ctz=America/Los_Angeles).
- [ ] Ask one of our cloud-gov team Github Maintainers to add them to the [@18F/cloud.gov team](https://github.com/orgs/18F/teams/cloud-gov) on GitHub.
- [ ] Invite the new person to `#cg-priv-all` and if applicable `#cg-priv-gov`

## Platform- and compliance-specific required items

- [ ] Help them review and understand the responsibilities of becoming a VM Fusion team member, as listed in our SSP. (*C: y*)
- [ ] Ask the System Owner to have them added to the [@18F/cloud-gov-ops](https://github.com/orgs/18F/teams/cloud-gov-ops) team on GitHub. -(For contractors: Confirm they have cleared GSA security review before doing this one!)- (*C: y*)
- [ ] If the new person is a contractor, ask the System Owner to have them added to the [@18F/cloud-gov-contractors](https://github.com/orgs/18F/teams/cloud-gov-contractors) team on GitHub. (*C: no, not applicable*)
- [ ] Add them to @cg-operators [in Slack’s User Groups](https://get.slack.help/hc/en-us/articles/212906697-User-Groups#edit-a-user-group). (*C: no*)
- Grant them access to the following:
  - [ ] [AWS Accounts](https://cloud.gov/docs/ops/aws-onboarding/) via the AWS web console (not Terraform) and provide one-time credentials. (*C: security auditor*)
  - [ ] AWS GovCloud (*C: security auditor* )
  - [ ] AWS East tied to GovCloud (*C: security auditor*)
  - [ ] AWS Admin Access (*C: consult with compliance lead*)
  - Note: AWS user names should be identical across accounts so that permissions can be correctly managed by terraform
  - [ ] Google Cloud Platform (GCP) Projects (by asking Derrick Rogers in GSA IT)
  - [ ] Nessus Manager GUI (*C: y*)
  - [ ] Opsgenie (*C: y*)
  - [ ] StatusPage (*C: y*)
- [ ] [Make them an admin](https://cloud.gov/docs/ops/managing-users/#managing-admins) of the platform. (*C: not yet, pending updates to cg-scripts for audit role*)
- [ ] Add them to the `cloud-gov-operators` organization in cloud.gov. (*C: not yet, pending creation of cloud-gov-auditors` role*)
- [ ] Take them through [AWS onboarding](https://cloud.gov/docs/ops/aws-onboarding/). (*C: y*)
- [ ] Add them to the set of [users in CloudCheckr](https://app.cloudcheckr.com/Users) and make them a member of [the cloud.gov group](https://app.cloudcheckr.com/Admin/UserGroupBuilder/fb111fab-ef5d-48d0-9472-cff691e1bd9c). (*C: y*)
- [ ] Ask `#infrastructure` to add them to [the cloudgov subteam in Docker Hub](https://hub.docker.com/u/18fgsa/dashboard/teams/?team=cloudgov). (*C: no*)
- [ ] Give them a walkthrough of cloud.gov from an architecture and repository perspective, focusing on SSP diagrams, external git repository and bosh.io dependencies, and our continuous delivery process with Concourse. (*C: y*)
- [ ] Add them to the [cloud.gov team on Cloud Foundry Community](https://github.com/orgs/cloudfoundry-community/teams/cloud-gov/members) (*C: y*)

<!-- Links for use throughout the checklist -->
[template onboarding checklist]: https://github.com/cisagov/development-guide/blob/master/onboarding-checklist.md
[NCATS Google Drive folder]: https://drive.google.com/drive/folders/0APw76nbCAmzuUk9PVA
[VM JIRA]: https://jira.ncats.cyber.dhs.gov/secure/Dashboard.jspa

<!-- dev team -->
[dev team project board]: https://app.zenhub.com/workspaces/vm-bizops-dev-5e596691c12d3435405dfaf3/board
[dev team Google Groups]: https://groups.google.com/a/trio.dhs.gov/forum/#!myforums