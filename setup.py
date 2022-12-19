"""
This is the setup module for the example project.

Based on:

- https://packaging.python.org/distributing/
- https://github.com/pypa/sampleproject/blob/master/setup.py
- https://blog.ionelmc.ro/2014/05/25/python-packaging/#the-structure
"""

# Third-Party Libraries
from setuptools import setup


def readme():
    """Read in and return the contents of the project's README.md file."""
    with open("README.md", encoding="utf-8") as f:
        return f.read()


def package_vars(version_file):
    """Read in and return the variables defined by the version_file."""
    pkg_vars = {}
    with open(version_file) as f:
        exec(f.read(), pkg_vars)  # nosec
    return pkg_vars


setup(
    name="project_setup",
    # Versions should comply with PEP440
    version="1.0.0",
    description="Documentation for Github projects in the cisagov organization.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    # NCATS "homepage"
    url="https://www.us-cert.gov/resources/ncats",
    # The project's main homepage
    download_url="https://github.com/cisagov/skeleton-python-library",
    # Author details
    author="Cyber and Infrastructure Security Agency",
    author_email="ncats@hq.dhs.gov",
    license="License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        "Development Status :: 3 - Alpha",
        # Indicate who your project is intended for
        "Intended Audience :: Developers",
        # Pick your license as you wish (should match "license" above)
        "License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication",
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.6",
    # What does your project relate to?
    keywords="documentation",
    package_dir={"": "project_setup/scripts"},
    install_requires=[
        "boto3",
        "docopt",
        "keyring",
        "PyGithub",
        "PyNaCl",
        "pyyaml",
        "schema",
        "setuptools >= 24.2.0",
        "wheel",
    ],
    extras_require={
        "test": [
            "pre-commit",
            "coveralls",
            "coverage < 8.0",
            "pytest-cov",
            "pytest",
        ]
    },
    scripts=[
        "project_setup/scripts/ansible-roles",
        "project_setup/scripts/iam-to-travis",
        "project_setup/scripts/terraform-to-secrets",
        "project_setup/scripts/skeleton",
        "project_setup/scripts/ssm-param",
    ],
    entry_points={},
)
