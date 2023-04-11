# development-guide #

[![GitHub Build Status](https://github.com/cisagov/development-guide/workflows/build/badge.svg)](https://github.com/cisagov/development-guide/actions)

A set of guidelines and best practices for an awesome engineering team.
Heavily "inspired" by the
[18F Development Guide](https://github.com/18f/development-guide).

- [Open Source Policy](/open-source-policy)
<!-- - [Development Ethos](/ethos)-->
- [Project Setup](/project_setup)
- [Development Environments](/dev_envs)
  - [CISA-provided Mac Setup](/dev_envs/mac-env-setup.md)
- Language Guides
  - HCL
  - JavaScript
  - [Python](/languages/python)

## Git, GitHub, and you ##

- [FISMA-Ready GitHub account setup](https://github.com/fisma-ready/github)
- [How to Write a Git Commit Message](https://chris.beams.io/posts/git-commit/#seven-rules)

## Tools and services we use ##

- [AWS](https://aws.amazon.com) - Our main cloud provider
- [CodeQL](https://codeql.github.com) - Code analysis engine developed by GitHub
  to automate security checks and help prevent critical vulnerabilities.
  Replaces [LGTM](https://lgtm.com).
- [Coveralls](https://coveralls.io/github/cisagov) - Test coverage tracking
- [Dependabot](https://docs.github.com/en/code-security/dependabot) -
  Monitor vulnerabilities in dependencies and keep dependencies
  up-to-date
- [GitHub Actions](https://github.com/features/actions) -
  Continuous integration and delivery
- [PyPi](https://pypi.org/search/?q=cisagov) - Python package publication
- [Snyk](https://app.snyk.io/org/cisagov) - Dependency vulnerability management
  and remediation

## Installation ##

This guide has several supporting Python scripts.  The simplest way to install these
scripts and their dependencies is to use `pip`.  In the root of this project execute:

`pip install -r requirements.txt`

Please see the
[Creating the Python virtual environment](CONTRIBUTING.md#creating-the-python-virtual-environment)
section of the [CONTRIBUTING](CONTRIBUTING.md) document for
information about setting up these scripts in a Python virtual environment.

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.
