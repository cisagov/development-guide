# Project Setup

## Skeleton Tool

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

Next, use the `skeleton` tool to clone, rename, and prepare the contents of your
new repository for publication.  The tool will print out each command it is
issuing and its result.

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

## Ansible Requirement File Generation Tool

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
