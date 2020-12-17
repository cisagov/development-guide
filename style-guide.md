# Style Guide #

Here lie the heretofore-unwritten rules and styles we use when writing
documentation, issues, pull requests, and other forms of written expression.

## References ##

- [Plain Language guide](https://www.plainlanguage.gov/guidelines/)
- [GitHub list of supported languages](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)

## Repositories ##

- Set a minimum of two codeowners for all repositories.
- Set all repositories containing code public.
- Use repository names to describe its purpose specifically and descriptively.
  - Avoid references to pop culture or other secondary implications.

## Lists ##

### List punctuation ###

Periods or no periods?

- Use periods at the end of bullets that are full sentences.
- Omit periods at the end of partial sentences.
- Match the rest of the bulleted or numbered list as much as possible.

## Code blocks ##

When formatting code blocks, use the formatting that best highlights the
syntax in the code block.

We generally use code blocks for scripts, command-line usage, and when showing
file contents like configuration files.

### Scripts ###

- Use `shell` formatting for shell scripts
  - `shell` is also aliased as `sh`, `bash`, `zsh`, and others
- Use language-specific formatting, such as `python`, for blocks with scripts
written in specific languages
  - Reference the [GitHub list of supported languages](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)

### Command-line ###

- `console` is most effective at highlighting a command _and_ its resulting
output, like this:

    ```console
    $ the_first_command
    the output
    more output
    $ the_second_command
    yet more output
    ```

- `shell` should be used for result-less commands, _especially_ if
there is any shell-fu like pipes, file redirects, shell variables, etc. to
apply syntax highlighting so the reader is more aware of the magic happening

### File contents ###

- Extension-specific formatting, such as `hcl` for Terraform, should be used
