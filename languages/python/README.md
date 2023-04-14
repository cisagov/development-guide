# Python Development Guide #

This document is structured by topic; under each, we include “Standards”,
“Defaults”, and “Suggestions”.

**Standards** are practices that have a strong consensus across CISA; they
should generally be followed.

**Defaults** are safe selections that tend to be used by a large number of our
projects; you may find yourself with a better or more tailored solution,
however.

**Suggestions** contain examples that have worked well on a project or two;
they're not widely used enough to be defaults, but are worth considering.

## Versions ##

We've **standardized** on Python 3.x over 2.x.  All new projects should begin
their life in 3.x.  When starting a Python project, select the latest Python
release available in `pyenv` and incrementally update as new releases are issued.

`pyenv install --list`

## Style ##

Our **standard** tool for ensuring consistency across Python code bases is
[black](https://github.com/psf/black). Our
[Python skeleton project](https://github.com/cisagov/skeleton-python-library)
contains a set of **default** linters and syntax checkers.  See the
[`CONTRIBUTING`](https://github.com/cisagov/skeleton-python-library/blob/develop/CONTRIBUTING.md)
file of this project for the most up-to-date information.

## Correctness and security ##

Our **standard** code vulnerability scanners in cisagov are
[CodeQL](https://codeql.github.com/),
[Dependabot](https://docs.github.com/en/code-security/dependabot), and
[Snyk](https://snyk.io).  By **default** all repositories in the
organization are scanned by these tools.

## Libraries ##

The Python ecosystem is large and full of alternative solutions to similar
problems. Here we document a few common use cases and the libraries we
recommend when trying to solve them.

| Purpose | Library | Conviction |
| --- | --- | --- |
| API (GraphQL) | [Flask-GraphQL] | Suggestion |
| API (REST) | [Django Rest Framework] | Suggestion |
| Argument Parser | [docopt](http://docopt.org) | Standard |
| Data Analysis | [Pandas](https://pandas.pydata.org) | Standard |
| HTTP Client | [Requests](https://requests.readthedocs.io/) | Standard |
| Input Validation | [schema](https://github.com/keleshev/schema) | Standard |
| Mongo ORM | [mongoengine](http://mongoengine.org) | Suggestion |
| Task Queue | [Celery](http://www.celeryproject.org/) | Suggestion |
| Test Coverage | [Coveralls] | Standard |
| Test Runner | [py.test](https://docs.pytest.org/en/latest/) | Standard |
| Web framework | [Flask](https://palletsprojects.com/p/flask/) | Default |

## Type support ##

Python 3.5 and beyond have had partial support for static type hints. Static
typing can both make code authors' intent clearer and reduce the number of
bugs through static analysis. It's also notorious for slowing down the pace of
prototyping and requiring a great deal of boiler-plate.

Given this state, we believe it's reasonable to **default** to using type
annotations when they make your intent clearer (i.e. as a form of
documentation). The static analysis tool
[mypy](http://mypy.readthedocs.io/en/latest/) is one of our **default** linters.

[Coveralls]: http://github.com/coveralls-clients/coveralls-python
[Django Rest Framework]: http://www.django-rest-framework.org/
[Flask-GraphQL]: https://github.com/graphql-python/flask-graphql
