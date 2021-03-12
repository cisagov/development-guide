# Coordinating Skeleton Updates #

When Lineage runs to push out skeleton updates to its descendent
repositories, this often results in generating tens of PRs to review. To
minimize this Kraken-like behavior and reduce the burden on team of so many
PR reviews, we try to coordinate updates to the skeletons in batches.

<!-- Links for use throughout the document -->
[lineage GitHub Action]: https://github.com/cisagov/action-lineage/actions?query=workflow%3Alineage_scan

## Checking the Lineage GitHub Action ##

First, check the status of the [lineage GitHub Action].
If it's about to run, you'll see the latest entry has a run time of roughly
`1 hour ago`.

If you want multiple PRs to be released in one Lineage run, so as to minimize
the Kraken of PRs to approve, wait until the next run completes and then start
the merge process.

## Merging ##

The part that takes the longest is waiting for the checks to complete as you
update each PR from its newly-updated `develop` branch before merging.

Wait until the [lineage GitHub Action] has completed, and do the process:

1. Merge a PR
2. Go to the next PR, `update from ##words here##`
3. Wait for tests to complete and merge the PR
4. Repeat for the next batched PR

## Schedule ##

Add note here about calendar events and create them?
