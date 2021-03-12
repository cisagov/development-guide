# Style Guide #

Here lie the heretofore-unwritten rules and styles we use when writing
documentation, issues, pull requests, and other forms of written expression.

## References ##

- [Plain Language guide](https://www.plainlanguage.gov/guidelines/)
- [GitHub list of supported languages](https://github.com/github/linguist/blob/master/lib/linguist/languages.yml)

## Capitalization ##

Follow standard capitalization for written work such as comments,
documentation, reports, and emails, namely that

> words are lowercase unless there is specific guidance to capitalize them.
> For example, capitalize the first word of a sentence, unless the sentence
> begins with the name of a person whose name starts with a lowercase letter.

Reference: [APA's capitalization guidelines](https://apastyle.apa.org/style-grammar-guidelines/capitalization)

When an object being referenced has a nonstandard capitalization, defer to its
capitalization. For example, GitHub has a capital letter mid-word.

Use uppercase for abbreviations, including technical protocols such as HTTPS
and SSL.

Please note that this guidance is specifically for *written work such as
documentation* and that code capitalization has its own standards that vary by
language.

## Repositories ##

**All repositories should be public.**

Whether creating new repositories or transferring existing repositories,
remember that we work in the open by default. For a discussion of the
rare cases in which we might use private repositories, read our
[open source policy](https://github.com/cisagov/development-guide/tree/develop/open-source-policy).

### Repository naming ###

Use a repository's name to describe its purpose. Names should be:

1. Descriptive
1. Readable
1. Consistent
1. Contextual
1. Future-friendly
1. Extensible
1. Reusable

Avoid references to pop culture or other implicit references. GitLab has a
good guide on using [inclusive language in documentation](https://docs.gitlab.com/ee/development/documentation/styleguide/#inclusive-language).

Specifically, when naming a repository:

- Use lower case
- Use dashes
  - For readability, where spaces would otherwise separate words
  - Avoid underscores, which require extra keystrokes

### Repository settings ###

Specify code owners in each repository's `.github/codeowners` file to make
sure that changes and pull requests are reviewed by people familiar with
the codebase. This way, we'll catch more problems before they get into the
protected branch.

- Set a minimum of two code owners for all repositories.
  - Add or edit each repository's `.github/codeowners` file.
- Set up [branch protection](project_setup/branch-protection.md).

## Titles and subjects ##

Use [title case](https://apastyle.apa.org/style-grammar-guidelines/capitalization/title-case)
for the main title of a document.

## Headers and headings ##

Use [sentence case](https://apastyle.apa.org/style-grammar-guidelines/capitalization/sentence-case)
for headings within a document that are not the inital document title.

When referencing an object or another document, use the capitalization of the
referenced item, such as "GitHub" or "the Style Guide".

Use both opening and closing octothorpes (`#`) to indicate the Markdown header
level. Our Markdown linting enforces this as well.

For example:

- `### Use variables to configure pipelines ###`
- `## Using the Style Guide ##`

## Lists ##

Use bulleted lists unless order matters, in which case use numbered lists.

Always capitalize the first word of list items, unless they’re parameters or
commands that are in backticks, or a similar situation.

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
