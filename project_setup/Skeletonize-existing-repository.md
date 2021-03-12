# Skeletonize an Existing Repository #

Skeletonizing a repository standardizes our development setup and environment,
and it enables our [Lineage](https://github.com/cisagov/action-lineage/)
Github Action to keep the repository updated and standardized.

## About skeletons ##

Skeleton projects contain [licensing information](LICENSE), as
well as [pre-commit hooks](https://pre-commit.com) and
[GitHub Actions](https://github.com/features/actions) configurations
appropriate for the major languages that we use. This lets us standardize
[cisagov](https://github.com/cisagov) GitHub projects to a
[list of cisagov skeleton projects](https://github.com/search?q=org%3Acisagov+skeleton&type=Repositories).

## General overview ##

The general outline of how to add a skeleton to a repository is:

1. Add the skeleton as a remote to the non-skeletonized repository
2. Pull with `--allow-unrelated-histories`
3. Fix all the inevitable conflicts (this takes the longest)
4. Run `pre-commit install`
5. Fix problems that may arise from `pre-commit` being added
6. Commit to a branch and submit a PR

## Adding a skeleton as remote ##

### Choose a skeleton ###

First, decide which of the available skeletons fits your existing repository.
As an example, we'll be using [`skeleton-python-library`](https://github.com/cisagov/skeleton-python-library)
in this document.

```console
cd <target_repository>
git remote add skeleton-parent git@github.com:cisagov/skeleton-python-library.git

# You can verify the remote has been added by
git remote --verbose

# Create a new branch for this work
git checkout -b skeletonize

# Pull skeleton's history
git pull skeleton-parent develop --allow-unrelated-histories
```

## Fix merge conflicts ##

This merge process will almost certainly fail, resulting in merge conflicts.
The next step is to fix those conflicts and add the files once the fixes are
in place.

```console
# Determine which files need fixes
git status

# After fixing the merge conflicts in a file,  add it
git add <filename>

...
# When all conflicts have been fixed and added, commit to complete the merge
git commit
```

## Fix GitHub Actions ##

**Note:** Remainder of doc still in-progress

- Run `pre-commit install` to set up pre-commit hooks
- `pre-commit run --all-files` - runs against all files to check the
pre-commit hooks
- isort and `.isort.cfg` - will have to deconflict packages (remove the
known-first and known-third and let it populate them) and manually add the
package name as known-first-party
- If the repository needs coverage checks and integration with
[Coveralls](https://coveralls.io/github/cisagov):
  - Modify the `.coveragerc` to point to the src package
  - Add appropriate secrets so they're available to the Actions
workflow, e.g. `secrets.COVERALLS_REPO_TOKEN` for the repo badge
    - Once the commit/repo is up, add a token from
  [Coveralls](https://coveralls.io/github/cisagov) to the repository's secrets
- Run pytest manually
