# Skeleton Repositories #

We maintain a number of [`cisagov` skeleton projects](https://github.com/search?q=org%3Acisagov+topic%3Askeleton)
to make starting new repositories quicker and to simplify maintaining
configurations and dependencies across the organization.

The [`gh-skeleton`][gh-skeleton] project is
a GitHub CLI (`gh`) extension that provides the ability to easily start new projects
from an existing library of skeleton repositories.

- To skeletonize an existing repository, please see the guide to
[skeletonize an existing repository](skeletonize-existing-repository.md).
- To skeletonize a new repository, please see the guide to
[start a new repository from a skeleton](README.md#using-the-gh-skeleton-gh-extension-to-start-a-new-repository).

## List available skeletons with the command-line tool ##

After you've installed the [`gh` CLI][gh CLI] followed
by the [`gh-skeleton`][gh-skeleton] extension,
the tool will be available to you via the command line. To see a list of
available skeletons, use the following command:

```console
$ gh skeleton list
# Expected output:
# Listing of available skeleton repositories
```

## Available skeletons in cisagov ##

[`skeleton-generic`](https://github.com/cisagov/skeleton-generic):
A generic skeleton project for quickly getting a new cisagov project started.

[`skeleton-python-library`](https://github.com/cisagov/skeleton-python-library):
A skeleton project for quickly getting a new cisagov Python library started.

[`skeleton-docker`](https://github.com/cisagov/skeleton-docker):
A skeleton project for quickly getting a new cisagov Docker container started.

[`skeleton-tf-module`](https://github.com/cisagov/skeleton-tf-module):
A skeleton project for quickly getting a new cisagov Terraform module started.

[`skeleton-ansible-role`](https://github.com/cisagov/skeleton-ansible-role):
A skeleton project for quickly getting a new cisagov Ansible role started.

[`skeleton-ansible-role-with-test-user`](https://github.com/cisagov/skeleton-ansible-role-with-test-user):
A skeleton project for quickly getting a new cisagov Ansible role started when
that role requires an AWS test user.

[`skeleton-packer`](https://github.com/cisagov/skeleton-packer):
A skeleton project for quickly getting a new cisagov packer project started.

[`skeleton-aws-lambda-python`](https://github.com/cisagov/skeleton-aws-lambda-python):
A skeleton project for quickly getting a new cisagov Python AWS Lambda started.

Note: If you discover a new flavor of skeleton that doesn't yet exist, use
`skeleton-generic` to create it, or add an issue to this repository to get
assistance.

[gh-skeleton]: https://github.com/cisagov/gh-skeleton
[gh CLI]: https://github.com/cli/cli
