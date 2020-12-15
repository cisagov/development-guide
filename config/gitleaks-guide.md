# Using gitleaks to check for PII and credentials #

This process is based on [`caulking`](https://github.com/cloud-gov/caulking)
by 18F's cloud.gov.

Please note that our [gitleaks configuration file](gitleaks.toml) results in a
number of false positives for things like code referencing "user_name" etc.

Results should be reviewed by humans.

## Installation ##

This assumes you are on MacOS with HomeBrew installed.

- Install `gitleaks` via `brew install gitleaks`
- Add the pattern configuration file somewhere like `$HOME/.git-support/gitleaks.toml`

## Usage ##

To check the commit history of a locally checked-out repository once you've
finished installation, you can use the `--repo-path=<relative path>` option.

Useful flags:

- `--config=<file-path>` specifies the configuration file to use
- `--repo-path=<relative-path>` specifies a local repository folder to check
- `--verbose` gives you more details about each item found
- `--pretty` formats the output so it's more human-readable

```sh
gitleaks --config=$HOME/.git-support/gitleaks.toml --repo-path=<relative-repo-path> --verbose --pretty
```

Without the `--verbose` flag, you'll get output with totals but not details,
such as:

```console
WARN[2020-12-08T10:47:03-05:00] 7 leaks detected. 24 commits scanned in 325 milliseconds 936 microseconds
```

If you want to save the console output to file so you can review it at your
leisure, use the `>` syntax and specify a location and filename.

```sh
gitleaks --config=$HOME/.git-support/gitleaks.toml --repo-path=<relative-repo-path> --verbose --pretty > ~/gitleaks.txt
```

You can then open the file and review the results for credential inclusions
and false positives.
