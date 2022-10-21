# Branch Protection #

We require branch protection to be enabled on all cisagov repositories after
creation and initial population.

## Setting up a rule to protect the `develop` branch ##

To enable branch protection, you must have permission to access the Settings
menu.

In `Settings`, go to the `Branches` entry and create a rule with the following:

- Branch name pattern: `develop`
  - Note: Our primary branches are named `develop`, as a rule.
  - Verify that adding this name pattern then shows that it
`Applies to 1 branch: develop`.

- Protect matching branches
  - [X] Require pull request reviews before merging
    - Required approving reviews: `2`
    - [ ] Dismiss stale pull request approvals when new commits are pushed
    - [X] Require review from Code Owners
    - [X] Restrict who can dismiss pull request reviews
  - [X] Require status checks to pass before merging
    - [X] Require branches to be up to date before merging
      - There may be a list of status checks under this option. We require
      passing status checks to merge, so all status checks should generally be
      checked as required.
      - Please note that the list of status checks will not fully populate in a
      new repository until the first pull request (PR) has been created.
  - [X] Require conversation resolution before merging
  - [ ] Require signed commits
  - [ ] Require linear history
  - [X] Do not allow bypassing the above settings
  - [X] Restrict who can push to matching branches
    - Note: this allows by default "People, teams or apps with push access", so
you likely don't have to make any changes *under* this entry

- Rules applied to everyone including administrators
  - [ ] Allow force pushes
  - [ ] Allow deletions
