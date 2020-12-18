# Managing cross-organization labels in existing repositories #

This is a step-by-step guide/script for managing organization-wide GitHub
issue labels across all repositories.

## Prerequisites ##

- User has access to the GitHub organization's repositories
- User can generate a GitHub [personal access token](https://github.com/settings/tokens)

## Initial Setup ##

1. Clone the repository locally

    ```console
    git clone https://github.com/alta3/github-label-management.git
    cd github-label-management
    ```

1. Activate/create the virtual environment and install the requirements

    ```console
    pyenv virtualenv 3.8.3 github-label-management
    pyenv local github-label-management
    python3 -m pip install --upgrade pip setuptools wheel
    python3 -m pip install --requirement requirements.txt
    ```

1. Create a local configuration file by running `touch config`
1. Open `config` in your favorite editor and start from this template

    ```sh
    export GITHUB_USER_TOKEN="<YOUR_TOKEN_HERE>"
    export LABELS_TOKEN=${GITHUB_USER_TOKEN}
    export LABELS_USERNAME="<YOUR_USERNAME>"
    export LABELS_ORGNAME="cisagov"
    ```

1. Create a GitHub [personal access token](https://github.com/settings/tokens)
    - Give it a descriptive name like "label management"
    - **Only** select the `repo` scope
    - Copy the generated token into `GITHUB_USER_TOKEN`
1. Save your changes and run `source config`

## Label management operations ##

There are several operations you'll probably want to do, now that you've
set up the environment and have the script ready.

### Re-initializing the environment ###

When you return to the directory in a new shell, remember to:

```console
pyenv activate github-label-management
source config
```

### List all organization repositories ###

```console
python3 list-all-repos.py
```

This will yield a list of all repositories you have access to in the specified
GitHub organization. If you have not specified a token, this will yield a list
of all public repositories.

### Back up all current repository labels ###

This will generate a `.toml` file for each repository in a directory of your
choosing. Each `.toml` file will contain the details of the repository's
labels, including names, colors, and descriptions.

Please note these output files are the same format as the `default-labels.toml`
file, so you can use one as a template if you have a repository set up with
the labels you want organization-wide.

```sh
# Make the directory if it doesn't already exist
# The -p option specifies to create intermediate directories as required
mkdir -p repo-labels-backup

# Use the output of list-all-repos.py to fetch each repository's labels
python3 list-all-repos.py | xargs -I {} labels fetch --owner "$LABELS_ORGNAME" --repo {} --filename repo-labels-backup/{}-labels.toml
```

### Apply default labels across the organization ###

View and edit `default-labels.toml` to specify the default labels and their
attributes such as name, color, and description. This is the same format as
the output `.toml` files from the ["back up" step](#Back-up-all-current-repository-labels),
so if you have an example repository, you can copy straight from that
repository's file.

Please note that the `labels ... sync` operation is **destructive** and will
reduce the set of labels in each repository to _only_ those specified.

The label history of each issue and PR will show the removal of the previous
labels in case you need to restore some.

Once you've set up your `default-labels.toml` file, create a list of all the
repositories in a file so you can edit the list to remove any repositories you
do not want to alter labels for.

```sh
python3 list-all-repos.py > repolist.txt
```

Make any edits to the list to exclude repositories that are special or that
you don't want to sync the labels for whatever reason, and then apply the
labels to the remaining list of repositories.

```sh
cat repolist.txt | xargs -I {} labels --verbose sync --owner "$LABELS_ORGNAME" --repo {} --filename default-labels.toml
```

#### ⚠️ Dangerous operation: Apply labels in one step ####

The following is **not recommended**, but to apply the `sync` without an
interstitial `repolist.txt` file (and live dangerously), you can instead run
the `sync` in one step.

```sh
python3 list-all-repos.py | xargs -I {} labels sync --owner "$LABELS_ORGNAME" --repo {} --filename default-labels.toml
```
