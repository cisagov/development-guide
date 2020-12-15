# Coordinating Skeleton Updates #

When Lineage runs to push out skeleton updates to its descendent
repositories, this often results in generating tens of PRs to review. To
minimize this kraken-like behavior and reduce the burden on team of so many
PR reviews, we try to coordinate updates to the skeletons in batches.

## Checking the Lineage GitHub Action ##

First, check the status of the [lineage GitHub Action]. If it's about to run,
you'll see that the last-run time was about `1 hour ago`.

If you want multiple PRs to be released in one Lineage run to minimize
the Kraken of PRs to approve, wait until the next run completes and then start
the merge process.

## Merging ##

The part that takes the longest is waiting for the checks to complete as you
update each PR from the newly-updated `develop` branch before merging.

Wait until a the [lineage GitHub Action] has completed, and do the process:

1. Merge a PR
2. Go to the next PR, `update from ##words here##`
3. Wait for tests to complete and merge the PR
4. Repeat for the next batched PR

## Schedule ##

Add note here about calendar events and create them?

<!-- Links for use throughout the checklist -->
[lineage GitHub Action]: https://github.com/cisagov/action-lineage/actions?query=workflow%3Alineage_scan
