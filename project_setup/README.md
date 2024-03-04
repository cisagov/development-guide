# Project Setup #

We recommend you follow the directions below and use a skeleton for
all new repositories.

The [`gh-skeleton`][gh-skeleton] GitHub CLI
(`gh`) extension provides the ability to easily start new projects
from the existing library of skeleton repositories.

For repositories created from skeletons, run `setup-env` and
`pre-commit install` to [set up your environment](#set-up-your-environment-and-pre-commit),
enable linting and other tools to prevent new commits from immediately
running into linting failures.

Once you've set up a repository, make sure to enable
branch protection - [see our branch protection guide for details](branch-protection.md).

## Contents ##

- [Adding a skeleton configuration to an existing repository](#adding-a-skeleton-configuration-to-an-existing-repository)
- [Using the gh-skeleton `gh` extension to start a new repository](#using-the-gh-skeleton-gh-extension-to-start-a-new-repository)
  - [Selecting a skeleton](#selecting-a-skeleton)
  - [Cloning a selected skeleton](#cloning-a-selected-skeleton)
- [Create and publish the GitHub repository](#create-and-publish-the-github-repository)
- [Disabling squash merging](#disabling-squash-merging)
- [Set up your environment and pre-commit](#set-up-your-environment-and-pre-commit)
- [Create an initial pull request](#create-an-initial-pull-request)
- [Setting up branch protection](#setting-up-branch-protection)
- [Setting up type-specific configuration settings](#setting-up-type-specific-configuration-settings)
  - [Setting up Coveralls for Python projects](#setting-up-coveralls-for-python-projects)
  - [Ansible requirement file generation tool](#ansible-requirement-file-generation-tool)
  - [Terraform IAM credentials to GitHub secrets](#terraform-iam-credentials-to-github-secrets)
  - [Managing SSM parameters from files](#managing-ssm-parameters-from-files)

## Adding a skeleton configuration to an existing repository ##

To skeletonize an existing repository, please see the guide to
[skeletonize an existing repository](skeletonize-existing-repository.md).

## Using the gh-skeleton `gh` extension to start a new repository ##

We recommend that you start your project from one of the
[skeleton projects](https://github.com/search?q=org%3Acisagov+topic%3Askeleton)
in this organization.  The [`gh-skeleton`][gh-skeleton]
`gh` extension provides the ability to easily start new projects from the existing
library of skeleton repositories.

### Selecting a skeleton ###

First, identify a suitable skeleton project to use as the starting point
for your new repository. For a list of available skeletons, see the
[Skeleton List](skeleton-list.md) or use the following command:

```console
$ gh skeleton list

Available skeletons in cisagov:

skeleton-ansible-role       A skeleton project for quickly getting a new cisagov Ansible role started.
skeleton-ansible-role-with-test-user    A skeleton project for quickly getting a new cisagov Ansible role started when that role requires an AWS test user.
skeleton-aws-lambda-python  A skeleton project for quickly getting a new Python-based AWS Lambda project started.
skeleton-docker             A skeleton project for quickly getting a new cisagov Docker container started.
skeleton-generic            A generic skeleton project for quickly getting a new cisagov project started.
skeleton-packer             A skeleton project for quickly getting a new cisagov packer project started.
skeleton-python-library     A skeleton project for quickly getting a new cisagov Python library started.
skeleton-tf-module          A skeleton project for quickly getting a new cisagov Terraform module started.
```

### Cloning a selected skeleton ###

Next, use the [`gh-skeleton`][gh-skeleton]
`gh` extension to clone, rename, and prepare the contents of your new repository
for publication.  The tool will print out each command it is issuing
and its result.

```console
$ gh skeleton clone [options] <parent-repo-name> <new-repo-name>
# Expected output:
# Cloning into 'new-repo-name'
```

For example, to create a project based on `skeleton-ansible-role` named
`ansible-role-quantum-rng` in your local `~/projects` directory:

```console
$ gh skeleton clone --change-dir ~/projects skeleton-ansible-role ansible-role-quantum-rng
# Expected output:
# Cloning into 'repo-name'
```

This command results in:

```console
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
💬 Clone an existing remote repository to the new name locally.
➤  git clone git@github.com:cisagov/skeleton-ansible-role.git ansible-role-quantum-rng
Cloning into 'ansible-role-quantum-rng'...
✅ success
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
💬 Disable pushing to the upstream (parent) repository.
➤  git remote set-url --push skeleton-ansible-role no_push
✅ success
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
💬 Add a new remote origin for the this repository.
➤  git remote add origin git@github.com:cisagov/ansible-role-quantum-rng.git
✅ success
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
💬 Search and replace repository name in source files.
➤  find . \( ! -regex '.*/\.git/.*' \) -type f -print0 | xargs -0 sed -i "" "s/skeleton-ansible-role/ansible-role-quantum-rng/g"
✅ success
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
💬 Stage modified files.
➤  git add --verbose .
add 'CONTRIBUTING.md'
add 'README.md'
add 'molecule/default/playbook.yml'
✅ success
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
💬 Commit staged files to the new repository.
➤  git commit --message "Rename repository references after clone."
[develop 565e041] Rename repository references after clone.
 3 files changed, 10 insertions(+), 10 deletions(-)
✅ success
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――

The repository "skeleton-ansible-role" has been cloned and renamed to "ansible-role-quantum-rng".
Use the following commands to push the new repository to github:
    cd ~/projects/ansible-role-quantum-rng
    git push --set-upstream origin develop
```

## Create and publish the GitHub repository ##

Once the `gh-skeleton` `gh` extension has run, the next step is to publish to a GitHub
remote repository.

To publish your new repository on GitHub, the remote must already exist.
[Create a new repository](https://github.com/organizations/cisagov/repositories/new)
on GitHub with the same name as your new local repository.  If you do not
have permission, ask an administrator to create it for you.

Add the repository name and description, set the repository to public, and
skip the rest of the options.

Next, publish your new repository to GitHub:

```bash
git push --set-upstream origin develop
```

## Disabling squash merging ##

Click on the settings tab for your new repository and, in the
"Pull Request" section, make sure that "Allow squash merging" is
*unchecked*.

## Set up your environment and pre-commit ##

Follow the instructions in [CONTRIBUTING.md on setting up pre-commit](../CONTRIBUTING.md#setting-up-pre-commit)
to run `setup-env` and enable the `pre-commit` hooks. If you have already set
up the prerequisites, this involves:

```sh
# In the root directory of the repository
./setup-env
```

## Create an initial pull request ##

You probably want to add code, documentation, and other items to your
repository to customize it from the skeleton and make changes.

Create a new branch called `first-commits` and publish it:

```bash
git checkout -b first-commits
git push origin first-commits --set-upstream
```

Edit the existing files and add your own as needed, then commit your changes,
push them, and create a pull request (PR) via GitHub or the command-line for
your teammates to review.

GitHub only populates its list of status checks once a PR
has been created so checks can run against changes. Status checks are
extremely useful for quality control and automated testing,
so we require these checks to pass before merging. This first PR will ensure
your new repository is ready to go and give your teammates a chance to review
your code before merging it.

If a status check doesn't apply to your new repository, leave it enabled
anyway - it won't hurt anything.

## Setting up branch protection ##

Once you've made your initial pull request, enable [branch protection](branch-protection.md)
to enforce the `codeowners` approval requirements for pull requests.

## Setting up type-specific configuration settings ##

### Setting up Coveralls for Python projects ###

The README for your new Python project will be prepared with a Coveralls badge.
To make the badge work properly, you'll need to add a repository secret.

1. Visit [Coveralls](https://coveralls.io/) and go to `Add Repos`.
1. Select your new repository and enable it. This will take you to a
page with `Python set up for Coveralls`. The code block will have an entry for
`repo_token: <token>`.
1. Copy the `repo_token` value.
1. On GitHub, visit your new repository's `Settings -> Secrets` page.
    - Note: If you don't have access to `Settings`, please contact an
    administrator to do this step for you.
1. Add a `New repository secret` and name it `COVERALLS_REPO_TOKEN` with the
value from Coveralls.

### Ansible requirement file generation tool ###

We have a [plethora](https://www.youtube.com/watch?v=zWld721Wk-Q) of
[ansible-roles in our organization](https://github.com/search?q=org%3Acisagov+topic%3Aansible-role+NOT+skeleton+archived%3Afalse).
To facilitate the creation of a `requirements.yml` file used in an Ansible
project, we have created the [`ansible-roles`](scripts/ansible-roles) tool
located in the [`scripts`](scripts) directory.  The tool will output `yml`
for all the current (non-archived) Ansible role repositories.  A common
usage of the tool is:

```bash
./ansible-roles > myproject/src/requirements.yml
```

This file will now contain definitions for all the Ansible roles.  Edit
the file, and remove any role that will not be required for your project.

### Terraform IAM credentials to GitHub secrets ###

When GitHub Actions workflows require credentials to run we provide them via
[secrets](https://help.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets).
This usually involves extracting the secrets from the Terraform state
json output.  Then some pointing, clicking, cutting and pasting on the
repository's settings.

To simplify this task use the [`terraform-to-secrets`](scripts/terraform-to-secrets)
tool located in the [`scripts`](scripts) directory.  The tool will create secrets
using your
[personal access token (PAT)](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).
Note: Your PAT needs to have the "repo" scope set.

Execute the tool from your GitHub project's terraform directory:

```bash
terraform-to-secrets 9f4ae878de917c7cf191b9861d3c1cf9224939f7
```

```console
2020-02-22 15:50:36,059 INFO Using GitHub repository name: cisagov/ansible-role-dev-ssh-access
2020-02-22 15:50:36,060 INFO Searching Terraform state for IAM credentials.
2020-02-22 15:50:40,643 INFO Found credentials for user: test-ansible-role-dev-ssh-access
2020-02-22 15:50:40,643 INFO Creating GitHub API session using personal access token.
2020-02-22 15:50:40,644 INFO Requesting public key for repository cisagov/ansible-role-dev-ssh-access
2020-02-22 15:50:40,832 INFO Setting secrets for user: test-ansible-role-dev-ssh-access
2020-02-22 15:50:40,832 INFO Creating secret AWS_ACCESS_KEY_ID
2020-02-22 15:50:41,027 INFO Creating secret AWS_SECRET_ACCESS_KEY
2020-02-22 15:50:41,036 INFO Success!
```

### Managing SSM parameters from files ###

Use the [`ssm-param`](scripts/ssm-param) tool to copy files into
[SSM parameters](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-store-about-examples.html)
in multiple regions simultaneously:

```console
ssm-param cp *.pem /demo/
```

```console
2019-08-27 16:45:58,651 INFO Found credentials in shared credentials file: ~/.aws/credentials
2019-08-27 16:45:58,744 INFO Putting parameter '/demo/dh4096.pem' in region 'us-east-1'
2019-08-27 16:45:58,981 INFO Putting parameter '/demo/dh4096.pem' in region 'us-east-2'
2019-08-27 16:45:59,327 INFO Putting parameter '/demo/dh4096.pem' in region 'us-west-1'
2019-08-27 16:45:59,887 INFO Putting parameter '/demo/dh4096.pem' in region 'us-west-2'
2019-08-27 16:46:00,363 INFO Putting parameter '/demo/private.pem' in region 'us-east-1'
2019-08-27 16:46:00,480 INFO Putting parameter '/demo/private.pem' in region 'us-east-2'
2019-08-27 16:46:00,640 INFO Putting parameter '/demo/private.pem' in region 'us-west-1'
2019-08-27 16:46:01,008 INFO Putting parameter '/demo/private.pem' in region 'us-west-2'
2019-08-27 16:46:01,414 INFO Putting parameter '/demo/public.pem' in region 'us-east-1'
2019-08-27 16:46:01,553 INFO Putting parameter '/demo/public.pem' in region 'us-east-2'
2019-08-27 16:46:01,718 INFO Putting parameter '/demo/public.pem' in region 'us-west-1'
2019-08-27 16:46:02,070 INFO Putting parameter '/demo/public.pem' in region 'us-west-2'
```

It can also delete parameters from multiple regions:

```console
ssm-param rm /demo/dh4096.pem /demo/private.pem /demo/public.pem
```

```console
2019-08-27 16:47:59,384 INFO Found credentials in shared credentials file: ~/.aws/credentials
2019-08-27 16:47:59,478 INFO Deleting parameter '/demo/dh4096.pem' in region 'us-east-1'
2019-08-27 16:47:59,715 INFO Deleting parameter '/demo/dh4096.pem' in region 'us-east-2'
2019-08-27 16:48:00,003 INFO Deleting parameter '/demo/dh4096.pem' in region 'us-west-1'
2019-08-27 16:48:00,523 INFO Deleting parameter '/demo/dh4096.pem' in region 'us-west-2'
2019-08-27 16:48:01,065 INFO Deleting parameter '/demo/private.pem' in region 'us-east-1'
2019-08-27 16:48:01,202 INFO Deleting parameter '/demo/private.pem' in region 'us-east-2'
2019-08-27 16:48:01,355 INFO Deleting parameter '/demo/private.pem' in region 'us-west-1'
2019-08-27 16:48:01,728 INFO Deleting parameter '/demo/private.pem' in region 'us-west-2'
2019-08-27 16:48:02,138 INFO Deleting parameter '/demo/public.pem' in region 'us-east-1'
2019-08-27 16:48:02,269 INFO Deleting parameter '/demo/public.pem' in region 'us-east-2'
2019-08-27 16:48:02,417 INFO Deleting parameter '/demo/public.pem' in region 'us-west-1'
2019-08-27 16:48:02,795 INFO Deleting parameter '/demo/public.pem' in region 'us-west-2'
```

[gh-skeleton]: https://github.com/cisagov/gh-skeleton
