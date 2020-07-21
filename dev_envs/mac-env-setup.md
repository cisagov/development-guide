# Dev Env Installation

## Initial Account Setup

For this section, log in as your Administrator account.

Note: It's not uncommon for folks to use the admin account to make their
standard account into an Administrator for at least the setup portion.

### XCode

Download XCode and Accept the License Agreement, then install the XCode
Command Line Tools.

```bash
sudo xcodebuild -license
xcode-select --install
```

### Docker

Download the latest stable [Docker for Mac](https://www.docker.com/docker-mac).
Install it by double-clicking the downloaded `dmg` file and dragging to the
`Applications` folder.

### iTerm2 (recommended)

To set up iTerm2 - a MacOS terminal replacement with some nifty features, visit
the [iTerm2 download page](https://www.iterm2.com/downloads.html) to get the
latest stable release. Install it by double-clicking the downloaded `dmg` file
and dragging to the `Applications` folder.

Once you've installed it, run the iTerm2 app and select the menu option
`iTerm2 > Make iTerm2 Default Term`. NOTE: You may also need to set this
setting as your Standard user account.

## Account Permissions

If you have a Standard user account, you’ll need to allow it access to run
`sudo` commands. First, you’ll want to take note of your account name by
viewing the folders listed inside of the `/Users/` folder - in this example,
the account name is **username**.

```bash
$ ls /Users/
username        Shared        fedadmin
```

Then, you’ll add your **username** to the `/etc/sudoers` file using `visudo`
like this:

```sh
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

### VPN Configuration

Once you're set up with the lab (CAL) VPN connection, we recommend you set up
split-tunneling. Instructions and a generator script are located in the
[vpn-config-gen repository](https://github.com/cisagov/vpn-config-gen).

## Dev Environment Setup

For this section and following sections, log back into your standard user.

### Automatic Installation (recommended)

To set up a dev environment via the [CISA `laptop` script](https://github.com/cisagov/laptop/),
execute the following in your terminal:

```sh
bash <(curl --silent https://raw.githubusercontent.com/cisagov/laptop/master/laptop)
```

This will `curl` the current install files and script. You can specify
additional packages to install by creating a `Brewfile.local`, as described in
the Readme for the `laptop` repo where an example is provided.

### Manual Installation (alternative)

#### Install Homebrew and packages

Open Terminal and install `brew` per the instructions from
[Homebrew](https://brew.sh). You will probably have to do this with `sudo`.

```sh
/bin/bash -c "$(curl --fail --silent --show-error --location https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

After installing Brew, you'll want to install other useful packages. We
recommend installing all the packages specified in the [CISA `laptop` script repository](https://github.com/cisagov/laptop/).

### Stow and dotfiles

For portability between computers and environments, you may want to switch
from the usual dotfiles setup to using `stow` to be able to use a personal
repository and then map your dotfiles to that directory. This makes it much
easier to sync and set up.

Using a `stow` based setup also allows for some nifty features like
subdirectories to split out useful files into a more modular approach.

#### Prerequisites

These are automatically installed if you used the Automatic installation script above.

```sh
brew install stow

brew install s3cmd
brew install figlet
brew install pinentry-mac
```

#### Setup

Fork [cisagov's `.dotfiles` repo](https://github.com/cisagov/.dotfiles) and
clone it as shown below. Then, stow all the packages from `.dotfiles` into
your home directory per the [`.dotfiles` README](https://github.com/cisagov/.dotfiles).

```bash
cd ~
git clone git@github.com:<username>/.dotfiles.git
cd ~/.dotfiles
./deploy.sh
```

You'll want to make some changes, e.g. username/email should be set to your
own - you can do this by editing the files in your new `~/.dotfiles` folder.
You don't need to rerun `stow` or `deploy.sh` after this because your files
are symlinked.

Generate a GPG key to sign your git commits etc and add it to the `.gitconfig`
file - follow the prompts:

```bash
gpg --gen-key
```

### Set up your favorite IDE

- Install your favorite IDE and set up its preferences to your liking
- For python development, please set up `black` for opinionated linting so
your code formatting will match the rest of the codebase - the pre-commit
hooks will automatically run this as well.

### Configure `git`

To allow access to the saved OSX Keychain credential for command line usage, run:

```bash
git config --global credential.helper osxkeychain
```

#### Generate ssh key to use git on the command line

1. This mainly follows the Github [Generating a new SSH key](https://docs.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#adding-your-ssh-key-to-the-ssh-agent)
documentation, except we use `ed25519` instead of `rsa`.

```bash
ssh-keygen -t ed25519
```

1. Save it in the default location (e.g. `~/.ssh/id_ed25519`)
1. Use a passphrase you'll remember
1. Start the `ssh-agent` in the background and add your new credential:

```bash
eval "$(ssh-agent -s)"
ssh-add -K ~/.ssh/id_ed25519
```

- TBD: Add pre-commit hooks etc for the dev team setup

#### Add ssh key to GitHub

1. This mainly follows the Github [Adding a new SSH key to your GitHub account](https://docs.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
documentation, except we use `ed25519` instead of `rsa`.

```bash
$ pbcopy < ~/.ssh/id_ed25519.pub
# Copies the contents of the id_ed25519.pub file to your clipboard
```

1. Load your [Github Settings page for adding an SSH key](https://github.com/settings/ssh/new)
and paste the contents of your clipboard.
1. Give this device a descriptive name and `Add SSH key`.
1. Confirm your password to continue.

### Setup for the COOL

There are some additional setup steps to access the
[COOL (Cloud-Optimized Operations Lab)](https://github.com/cisagov/cool-system/wiki/):

1. [Install MIT Kerberos](https://github.com/cisagov/cool-system/wiki/Installing-MIT-Kerberos)
    - NOTE: This step was already performed by the `laptop` script if you chose
    Automatic Installation above
1. [Configuring Kerberos for the COOL](https://github.com/cisagov/cool-system/wiki/Configuring-Kerberos-for-the-COOL)
1. [Configuring your browser for the COOL](https://github.com/cisagov/cool-system/wiki/Configuring-your-browser-for-the-COOL)

After you have successfully completed the tasks above, follow
[these instructions to access Guacamole](https://github.com/cisagov/cool-system/wiki/Accessing-an-assessment-environment-with-Guacamole).
