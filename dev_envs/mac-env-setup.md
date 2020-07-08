# Dev Env Installation

## Initial Account Setup

For this section, log in as your Administrator account.

Note: It's not uncommon for folks to use the admin account to make their standard account into an Administrator for at least the setup portion.

### XCode          

Download XCode and Accept the License Agreement, then install the XCode Command Line Tools.

```bash
sudo xcodebuild -license
xcode-select --install
```

### Docker

Download the latest stable [Docker for Mac](https://www.docker.com/docker-mac). Install it by double-clicking the downloaded `dmg` file and dragging to the `Applications` folder.

### iTerm2

To set up iTerm2 - a MacOS terminal replacement with some nifty features, visit the [iTerm2 download page](https://www.iterm2.com/downloads.html) to get the latest stable release. Install it by double-clicking the downloaded `dmg` file and dragging to the `Applications` folder.

Once you've installed it, run the iTerm2 app and select the menu option `iTerm2 > Make iTerm2 Default Term`. NOTE: This setting may need to also be done in your standard user.

## Account Permissions

If you have a Standard user account, you’ll need to allow it access to run `sudo` commands. First, you’ll want to take note of your account name by viewing the folders listed inside of the `/Users/` folder - in this example, the account name is **username**. 

```bash                
$ ls /Users/
username        Shared        fedadmin
```

Then, you’ll add your **username** to the `/etc/sudoers` file using `visudo` like this:

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

We recommend you set up split-tunneling for your lab (CAL) VPN connection. Instructions and a generator script are located in the [vpn-config-gen repository](https://github.com/cisagov/vpn-config-gen).

## Dev Environment Setup

For this section and following sections, log back into your standard user.

### Automatic Installation

To set up a dev environment via the [CISA `laptop` script](https://github.com/cisagov/laptop/), execute the following in your terminal:

```sh
bash <(curl -s https://raw.githubusercontent.com/cisagov/laptop/master/laptop)
```

### Manual Installation

#### Brew installation

Open Terminal and install `brew` per the instructions from [Homebrew](https://brew.sh). You probably have to do this as an admin user or with `sudo`.

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

After installing Brew, you'll want to install other useful packages. For some ideas, visit the [CISA `laptop` script repository](https://github.com/cisagov/laptop/)

### Stow and dotfiles

For portability between computers and environments, you may want to switch from the usual dotfiles setup to using `stow` to be able to use a personal repository and then map your dotfiles to that directory. This makes it much easier to sync and set up.

Using a `stow` based setup also allows for some nifty features like subdirectories to split out useful files into a more modular approach.

```sh
brew install stow

brew install s3cmd
brew install figlet
brew install pinentry-mac
```

Fork [Mark Feldhousen's `.dotfiles` repo](https://github.com/felddy/.dotfiles) and clone it as shown below. Then, stow all the packages from `.dotfiles` into your home directory.

```bash
cd ~
git clone git@github.com:<username>/.dotfiles.git
cd ~/.dotfiles
stow -v --stow **/
```

You'll want to make some changes, e.g. username/email should be set to your own - you can do this by editing the files in your `.dotfiles` folder.

Generate a GPG key to sign your git commits etc and add it to the `.gitconfig` file - follow the prompts:

```bash
gpg --gen-key
```

### Set up your favorite IDE

- Install your favorite IDE and set up its preferences to your liking
- For python development, please set up `black` for opinionated linting so your code formatting will match the rest of the codebase

### Configure `git`

To allow access to the saved OSX Keychain credential for command line usage, run:

> git config --global credential.helper osxkeychain

- TBD: Add pre-commit hooks etc for the dev team setup

