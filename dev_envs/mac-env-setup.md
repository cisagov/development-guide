# Setting up a Mac-based development environment #

## Initial account setup (as administrator) ##

For this section, log in as your administrator account.

### Account permissions ###

You’ll need to allow your standard user access to run `sudo` commands.
First, you’ll want to take note of your account name by viewing the folders
listed inside of the `/Users/` folder - in this example, the account
name is **username**.

```console
$ ls /Users/
username        Shared        fedadmin
```

Then, you’ll add your **username** to the `/etc/sudoers` file using `visudo`:

```console
$ sudo visudo
...
##
# User specification
##

# root and users in group wheel can run anything on any machine as any user
root        ALL = (ALL) ALL
%admin      ALL = (ALL) ALL
username    ALL = (ALL) ALL
```

Press `Esc` followed by `:wq` to save and quit `visudo`.

### Install XCode command line tools ###

Download XCode and accept the license agreement, then install the XCode
command line tools.

```console
sudo xcodebuild -license
xcode-select --install
```

### Docker ###

Download the latest stable [Docker for Mac](https://www.docker.com/docker-mac).
Install it by double-clicking the downloaded `dmg` file and dragging the
Docker application file to the `Applications` folder.

### iTerm2 (recommended) ###

To set up iTerm2 - a macOS terminal replacement with some nifty features -
visit the [iTerm2 download page](https://www.iterm2.com/downloads.html) to
get the latest stable release. Install it by double-clicking the downloaded
`zip` file and dragging the extracted `iTerm` application file to the
`Applications` folder.

Once installed, run the app and select the menu option
`iTerm2 > Make iTerm2 Default Term`.

> **Note**
> You may also `Make iTerm2 Default Term` on your standard user account.

### VPN configuration ###

Once you're set up with the lab (CAL) VPN connection, we recommend you set up
split-tunneling. Instructions and a generator script are located in the
[vpn-config-gen repository](https://github.com/cisagov/vpn-config-gen).

## User environment setup ##

For this section and following sections, log back in as your standard user.

> **Note**
> If you installed iTerm2 above, run the iTerm2 app and select the menu option
> `iTerm2 > Make iTerm2 Default Term` to make it your default too.

### Automatic package installation (recommended) ###

NOTE (DEC 2022): The [CISA `laptop` script] is out of date but still
functional.

To set up a dev environment via the [CISA `laptop` script], execute
the following in your terminal:

```bash
bash <(curl --silent https://raw.githubusercontent.com/cisagov/laptop/master/laptop)
```

This will `curl` the current install files and script. You can specify
additional packages to install by creating a `Brewfile.local`, as described in
the Readme for the `laptop` repo where an example is provided.

### Manual package installation (alternative) ###

Open Terminal and install `brew` per the instructions from
[Homebrew](https://brew.sh). You will probably have to do this with `sudo`.

```console
/bin/bash -c "$(curl --fail --silent --show-error --location https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

After installing Brew, you'll want to install other useful
packages. We recommend installing all the packages specified in the
[CISA `laptop` script repository](https://github.com/cisagov/laptop/blob/master/Brewfile).

### Environment configuration ###

For portability between computers and environments, you may want to switch
from the usual dotfiles setup to using `stow` to be able to use a personal
repository and then map your dotfiles to that directory. This makes it much
easier to sync and set up.

Using a `stow`-based setup also allows for some nifty features like
subdirectories to split out useful files into a more modular approach.

#### Prerequisites ####

These are automatically installed if you used the
[automatic package installation](#automatic-package-installation-recommended)
script above.

```console
brew install figlet pinentry-mac s3cmd stow
```

#### Install ####

Fork [cisagov's `.dotfiles` repo](https://github.com/cisagov/.dotfiles) and
clone it as shown below. Then, stow all the packages from `.dotfiles` into
your home directory per the [`.dotfiles` README](https://github.com/cisagov/.dotfiles).

```console
cd ~
git clone git@github.com:<username>/.dotfiles.git
cd ~/.dotfiles
./deploy.sh
```

### Customize your user ###

You'll want to make some changes, e.g. username/email should be set to your
own - you can do this by editing the files in your new `~/.dotfiles` folder.

> **Note**
> You don't need to rerun `stow` or `deploy.sh` after this because your
> files are already symlinked.

#### Set up your favorite IDE ####

- Install your favorite IDE and set up its preferences to your liking
- For Python development, please set up `black` for opinionated linting so
your code formatting will match the rest of the codebase
  - Note: the pre-commit hooks will automatically run `black` on commit

#### Configure `git` ####

To allow access to the saved macOS Keychain credential for command line
usage, run:

```console
git config --global credential.helper osxkeychain
```

#### Set up commit signing with GPG ####

Generate a key to sign your git commits and add it to your `~/.gitconfig`:

```console
gpg --gen-key
```

Follow the prompts for name and email address, using either your CISA
or GWE email address. The output should look like:

```console
We need to generate a lot of random bytes. It is a good idea to perform
some other action (type on the keyboard, move the mouse, utilize the
disks) during the prime generation; this gives the random number
generator a better chance to gain enough entropy.
gpg: key EXAMPLE1234ABCDE marked as ultimately trusted
gpg: revocation certificate stored as '/Users/username/path/to/.gnupg'
public and secret key created and signed.

pub   rsa3072 YYYY-MM-DD [SC] [expires: YYYY-MM-DD]
      <fingerprint characters>
uid                      User Name <user@example.com>
sub   rsa3072 YYYY-MM-DD [E] [expires: YYYY-MM-DD]
```

The alphanumeric string from the key generation output line that says
`gpg: key EXAMPLE1234ABCDE marked as ultimately trusted` is used as
your **signing key**.

Now that your new key has been generated, add it to your `~/.gitconfig`:

1. Fill your `name` and `email`, using the same values as above
1. Copy the alphanumeric string from the key generation output line that says
    `gpg: key EXAMPLE1234ABCDE marked as ultimately trusted`
1. Fill the alphanumeric signing key string in the `[user]` section:
    `signingkey = EXAMPLE1234ABCDE`

Next, export the public key via command line and add it to your GitHub account:

1. `gpg --armor --export user@example.com`
1. Copy the output, starting from `-----BEGIN PGP PUBLIC KEY BLOCK-----`
1. Add a new PGP key to your [GitHub keys page](https://github.com/settings/keys)
1. Paste the public key into the dialog and `Add GPG key`
1. Confirm your password to continue (if requested)

Lastly, enable the global configuration option for commit signing:

```console
git config --global commit.gpgsign true
```

#### Generate `ssh` key to use git on the command line ####

Reference: [GitHub: Generating a new SSH key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)

> **Warning**
> Use `ed25519` instead of `rsa`!

```console
ssh-keygen -t ed25519
```

1. Save the generated key in the default location (e.g. `~/.ssh/id_ed25519`)
1. Use a passphrase you'll remember and/or save in your keychain
1. Start the `ssh-agent` in the background and add your new credential:

    ```console
    eval "$(ssh-agent -s)"
    ssh-add -K ~/.ssh/id_ed25519
    ```

#### Add ssh key to GitHub ####

Reference: [GitHub: Adding a new SSH key to your GitHub account](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)

> **Warning**
> Use `ed25519` instead of `rsa`!

```console
# Copy the contents of the id_ed25519.pub file to your clipboard
$ pbcopy < ~/.ssh/id_ed25519.pub
```

1. Load your [GitHub Settings page for adding an SSH key](https://github.com/settings/ssh/new)
and paste the contents of your clipboard
1. Give this device a descriptive name and `Add SSH key`
1. Confirm your password to continue (if requested)

## Setup for the COOL ##

There are some additional setup steps to access the
[COOL (Cloud-Optimized Operations Lab)](https://github.com/cisagov/cool-system/):

> **Note**
> These steps are only necessary if you want to manually configure these vs.
> using the Jamf-pushed configuration.

1. [Install MIT Kerberos](https://github.com/cisagov/cool-system-internal/blob/master/Installing-MIT-Kerberos.md)
    - NOTE: If you chose Automatic Installation above, this step was already
    performed by the `laptop` script
1. [Configuring Kerberos for the COOL](https://github.com/cisagov/cool-system-internal/blob/master/Configuring-Kerberos-for-the-COOL.md)
1. [Configuring your browser for the COOL](https://github.com/cisagov/cool-system-internal/blob/master/Configuring-your-browser-for-the-COOL.md)

After you have successfully completed the tasks above, follow
[these instructions to access Guacamole](https://github.com/cisagov/cool-system-internal/blob/master/Accessing-an-assessment-environment-with-Guacamole.md).

> **Note**
> You will need to have been given access to one or more COOL environments
> to be able to access anything with Guacamole.

[CISA `laptop` script]: https://github.com/cisagov/laptop/
