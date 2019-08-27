# Project Setup #

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

## Terraform IAM Credentials to Travis Tool 🔑‍👉👷🏻 ##

When Travis-CI needs credentials to run we provide them in its `.travis.yml`
file in an encrypted format.  Extracting fresh IAM credentials from a
Terraform run,
[encrypting them properly](https://docs.travis-ci.com/user/environment-variables/#defining-encrypted-variables-in-travisyml)
, and then formatting them into well-formed `yml` that will make the linters
happy is no small task.

To simplify this task use the [`iam-to-travis`](scripts/iam-to-travis) tool
located in the [`scripts`](scripts) directory.  The tool will output `yml`
that can be pasted directly into a `.travis.yml` file.  The tool has
adjustable indentation and width with reasonable defaults.

Execute the tool from your GitHub project's terraform directory:

```bash
iam-to-travis
```

```yml
# AWS_ACCESS_KEY_ID
- secure: "UZVXTpslA2qID+51nIlVOPaDZNdIuTuEw7AMG7045zEAuxtmViHBKL5z6fpwUnmV\
  vqnjZksQGLuLnYFIX+E85ObwrFBjhnr0m5baARG3wdS3+KrQjruStetz8gpKeXLA+L81VfhxF\
  Z3pCTATN86FSEcVFSgA8hGGr1nKqpVKFqxnKCXnBeQCgqD0MrQ1bfj7AvhY1s97pf6kXBwQ7/\
  MoRhFgwcnituhhDpb6QZWFo6L6W/UUKL5sATA3H2tGSLtS8W8a0MMTKr6n8uSoiQwNO8+qGvm\
  Iu10tl+XPzHzYGdpmBZignA63HFOcodtDy3PJJzICrEmkGZ9zvp0kgtHi7hBLXSLf82D28lMt\
  r8QC+ZCnuaH+ar0SaSueDS7MkUVXl0DNIkqjQZP4/AwTuAomJ4i60cpPS3Xte8GO8dUqwkc+/\
  2mg1cqeUQAVaIMsFzs3U11LfC5CMzHNe9qe8jRt6aVylxpdXEpxLeD3kNG3mBEGxOAQD0YkYw\
  tp1paKJOt2CHEnTkDrs8hJ9bZzlwGrmu0vIfFoO0k1/rYbemNGZ+VCY1TWtxOdqxeJRLVYZBJ\
  J0cTlYf5N3//RUZS6QZ85dJ/7zKn4SRjalLMAD/zjAte5EsRag34KWG6LurRojKqpPUfzaxRu\
  IEYQ1+ATLZoEgMLYETiEWG6Il2QNv1c6uOM="

# AWS_SECRET_ACCESS_KEY
- secure: "PcuGEOpW7f448RSA6TB07EwI2IlcCoWkrjztO8zz34rKE2VYNTaNEseZizTg0B0p\
  s80jvlJRfkuQi+h0nYsLCANjsX+o1HooXnNBFsREzuKhYu1qB80Tcpl3DY/uYXF0yLbe0Qk0s\
  ZmDxK3Fe62bjLzlMTh2i5Aocf+e176zQ+VrJqHG4qSVrgRPXeRcKRrKFyOYA/HbmC7Wcno85d\
  nsj0s3U4sDxrn6rWaHetHFxEml5kD86XhJ4xKXhZfwCR+aVgvKEdiY4ft6wmfbogVhAqfa5NG\
  N4CrCs1ooKutB/95axlmuxEG73mnYdBaE2FphOvx+2lL8JOVjtUK5ENac1QumHngztAASTtVc\
  RXpEaRH5OGEgWkmqptN3fJAqZyfLu74zOr61/thJuh6fkAciXDoKt8e2CyCxAqbAB+6SKwxG3\
  +K6rEtms6c3dwtHrssoHOsozADxVeK/I2two1QzcVsw92hRfF9ecWyV+QUaJ6iZYEk2VqgsDi\
  NuBbVa2SQT9mO3A4fcn23fRjHy/ac/Cmz9q3hGKnMWl27CSRaPq7PR4sNPr9ebabRRrjAZ0I2\
  UaWaDqIOwz85EWTQ6Y/53dgr2Zgv8KpfzfdNWhKtKS4woJGYPoU1k17V2TGZhs2S85XfT2aB3\
  injrwJ5qqmcUljFdByuA08WyX4UkBCWtkJE="
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
