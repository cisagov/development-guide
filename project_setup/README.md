# Project Setup #

We recommend you use a skeleton for all new repositories following the
directions below.

For repositories from skeletons, run `pre-commit install` to run linting
and other tools before committing a faux pas to the repository which
will immediately cause linting failures.

Once you've set up a repository, make sure to enable
[branch protection](branch-protection.md).

## Skeleton Tool 💀🛠 ##

It is recommended that you start your project from one of the
[skeleton projects](https://github.com/search?q=org%3Acisagov+topic%3Askeleton)
that exist in this organization.  The [`skeleton`](scripts/skeleton)
helper tool included in the [`scripts`](scripts) directory can quickly setup
a new local repository.  Once you've cloned and configured the repository
to your local machine, it can be published to a repository created on GitHub.

First, identify a suitable skeleton project to use as the starting point
for your new repository.

```bash
./skeleton list
```

```text
Available skeletons in cisagov:

skeleton-docker
        A skeleton project for quickly getting a new cisagov Docker container started.

skeleton-ansible-role
        A skeleton project for quickly getting a new cisagov Ansible role started.

skeleton-generic
        A generic skeleton project for quickly getting a new cisagov project started.

skeleton-python-library
        A skeleton project for quickly getting a new cisagov Python library started.

```

Next, use the `skeleton` tool to clone, rename, and prepare the contents of
your new repository for publication.  The tool will print out each command it
is issuing and its result.

```console
./skeleton clone [options] <parent-repo-name> <new-repo-name>
```

For example, to create a project based on `skeleton-ansible-role` named
`ansible-role-quantum-rng` in your `~/projects` directory:

```bash
./skeleton clone --change-dir ~/projects skeleton-ansible-role ansible-role-quantum-rng
```

```text
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

Once the `skeleton` tool is complete, inspect the new repository for accuracy.

To publish your new repository on GitHub, the remote must already exist.
[Create a new repository](https://github.com/organizations/cisagov/repositories/new)
on GitHub with the same name as your new local repository.  If you do not
have permission, ask an administrator to create it for you.

If everything looks good, publish your new repository to GitHub:

```bash
git push --set-upstream origin develop
```

## Ansible Requirement File Generation Tool 🧻🛠 ##

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

## Terraform IAM Credentials to GitHub Secrets 🔑‍👉🤫 ##

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

## Managing SSM Parameters from Files 🗂👉☁️ ##

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
