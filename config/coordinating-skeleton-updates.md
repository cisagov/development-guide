# Coordinating Skeleton Updates #

When Lineage runs to push out skeleton updates to its descendent
repositories, this often results in generating tens of PRs to review. To
minimize this Kraken-like behavior and reduce the burden on team of so many
PR reviews, we try to coordinate updates to the skeletons in batches.

<!-- Links for use throughout the document -->
[Lineage GitHub Action]: https://github.com/cisagov/action-lineage/actions?query=workflow%3Alineage_scan

## Checking the Lineage GitHub Action ##

First, check the status of the [Lineage GitHub Action].
If it's about to run, you'll see the latest entry has a run time of roughly
`1 hour ago`.

If you want multiple PRs to be released in one Lineage run, so as to minimize
the Kraken of PRs to approve, wait until the next run completes and then start
the merge process.

You'll also want to start from the top of the skeleton hierarchy and
merge from `skeleton-generic` first, then once Lineage has run, do the same
into the next level of skeletons, and so on until you just have a boatload
of PRs to review.

## Merging ##

The part that takes the longest is waiting for the checks to complete as you
update each PR from its newly-updated `develop` branch before merging.

Wait until the [Lineage GitHub Action] has completed, then:

1. Merge one PR into the skeleton repository
1. Go to the next PR and click `Merge branch 'develop' into <this-branch>` -
  you can also rebase from the command-line if you prefer
1. Wait for tests to complete and merge this PR
1. Repeat the preceding steps for the next batched PR until all PRs are merged
1. Wait for Lineage to run and then review and merge the resulting PRs

## Schedule ##

Generally, we schedule the batching and coordinate to review and merge
efficiently. To do so, create a team calendar invite a la `Unleash the Kraken`
and start adding links to PRs that belong in that batch.
