# defold.github.io

New www.defold.com leveraging GitHub Pages and Jekyll+Liquid to generate a static site. The structure of the static site as well as many of the pages are stored in this repository. Some other parts of the site such as content of the learn section and the asset portal is hosted in other GitHub repositories:

* Assets - [defold.com/assets](https://defold.com/assets) -> [github.com/defold/asset-portal](https://github.com/defold/asset-portal)
* Showcase - [defold.com/showcase](https://defold.com/showcase) -> [github.com/defold/games-showcase](https://github.com/defold/games-showcase)
* Learn
  * Manuals - [defold.com/manuals](https://defold.com/manuals) -> [github.com/defold/doc](https://github.com/defold/doc)
  * Tutorials - [defold.com/tutorials](https://defold.com/tutorials) -> [github.com/defold/doc](https://github.com/defold/doc)
  * FAQ - [defold.com/faq/faq](https://defold.com/faq/faq) -> [github.com/defold/doc](https://github.com/defold/doc)
  * Examples - [defold.com/examples](https://defold.com/examples) -> [github.com/defold/examples](https://github.com/defold/examples)
* Codepad - [defold.com/codepad](https://defold.com/codepad) -> [github.com/defold/codepad](https://github.com/defold/codepad)

# HOW TO UPDATE THE SITE WITH NEW CONTENT
The site uses the `update.py` script from this repository to update the site with updated content from external sources/repositories.

## Requirements
You need to make sure to have the following dependencies installed before using `update.py`:

* Python 3.x
* Requests (http requests)
* PyYAML, Markdown, Pygments

Install dependencies using:

```sh
pip3 install --user requests
pip3 install --user pyyaml
pip3 install --user markdown==3.4.1
pip3 install --user pygments==2.13.0
```

## Usage
The `update.py` script should be run from a terminal. The syntax is as follows:

```sh
python3 update.py [--download] docs codepad refdoc examples asset-portal games-showcase
```

You can use this script when testing locally (see below). The script is also used by GitHub Actions when automatically updating the site when one of the external sources/repositories have changed (see below).

### Options
The script accepts the following options:

* `--download` - Download the required files for each command. If the option is omitted the files are expected to already exist on disk ready for processing.
* `--githubtoken` - GitHub authentication token when committing changes.

### Commands
The script accepts the following commands:

* `docs` - Import manuals, tutorials and FAQ from github.com/defold/doc
* `codepad` - Import CodePad from github.com/defold/codepad
* `refdoc` - Import API reference from latest release at d.defold.com
* `examples` - Import examples from github.com/defold/examples
* `asset-portal` - Import Asset Portal content from github.com/defold/asset-portal
* `games-showcase` - Import Showcase content from github.com/defold/games-showcase
* `commit` - Commit changes to GitHub (for CI use)


# HOW TO TEST THE SITE LOCALLY
It is recommended that you generate and test the site locally before pushing the changes to the repository. You generate and test the site locally by running `serve.sh`.

## Requirements
You need to make sure you have the following dependencies installed before attempting to generate the site locally using `serve.sh`:

* Ruby
* bundler gem
* jekyll
* github-pages gem
* Pagefind (for search indexing)

### 1 Install Ruby
Most macOS versions ship with Ruby preinstalled. It is however recommended that you install a separate Ruby version as you will very likely run into permission issues if trying to install any Ruby gems with the system version of Ruby.

The recommended approach is to use Homebrew to install Ruby:

#### 1.1 Install brew (macOS)
If you don't have Homebrew installed, open a terminal window and install it:

```sh
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

#### 1.2 Install Ruby

```sh
brew install ruby
```

Add Ruby to your PATH by adding this line to your shell profile (e.g. `~/.zshrc`):

```sh
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
```

Then restart your terminal or run:
```sh
source ~/.zshrc
```

#### 1.3 Alternative: Using rbenv
If you prefer to use rbenv for Ruby version management:

```sh
# Install rbenv
brew install rbenv

# Add rbenv to shell profile
echo 'eval "$(rbenv init -)"' >> ~/.zshrc

# Restart terminal or reload profile
source ~/.zshrc

# Install Ruby version specified in .ruby-version file
rbenv install $(cat .ruby-version)
rbenv local $(cat .ruby-version)
```

### 2 Install gems
The site uses bundler to manage gem dependencies. Install bundler first, set config directory, then install all dependencies:

```sh
gem install bundler
bundle config set --local path 'vendor/bundle'
bundle install
```

**Note:** If you encounter errors related to missing `csv` or `logger` gems (common with Ruby 3.4+), these have been added to the Gemfile and will be installed automatically with `bundle install`.

### 3 Install Pagefind
The site uses Pagefind for search functionality. Install it using:

```sh
pip3 install "pagefind[extended]"
```

The `serve.sh` script will automatically check for Pagefind installation and provide installation instructions if missing.


## Usage
Launch/serve the site locally:

```sh
./serve.sh
```

Once the site has been built you can test it by pointing your browser to [localhost:4000](http://localhost:4000).

**Note:** If you're using Homebrew Ruby, you may need to set the PATH in your terminal session:
```sh
export PATH="/opt/homebrew/opt/ruby/bin:$PATH"
./serve.sh
```

You can use the `update.py` script to pull in and process content from external sources (docs, asset portal etc)

## How to test local reference documentation

Copy the `refdoc.zip` to the main folder:

```sh
cp $DYNAMO_HOME/share/ref-doc.zip refdoc_alpha.zip
cp $DYNAMO_HOME/share/ref-doc.zip refdoc_beta.zip
cp $DYNAMO_HOME/share/ref-doc.zip refdoc_stable.zip
./update.py refdoc
./serve.sh
```

## How to test local documentaion

By setting the `DM_DOC_DIR` environment variable, you can load the documentation directory from your local folder:

```sh
DM_DOC_DIR=/Users/username/work/doc python3 update.py docs
```

# Automatic site update using GitHub Actions
The site uses [GitHub Actions](https://github.com/defold/defold.github.io/actions) to automatically trigger `update.py` when an external source/repository has been updated. CI then builds the Jekyll site, generates the Pagefind index, and deploys the built `_site` to GitHub Pages via `actions/deploy-pages`. Ensure the repository Pages settings use “GitHub Actions” for build & deployment.

The script is also triggered once every hour to update the asset portal star count for GitHub hosted assets. The following workflows/jobs have been set up using GitHub Actions:

* [Update site](https://github.com/defold/defold.github.io/blob/master/.github/workflows/update_site.yml) - on change in external repository (triggered using the repository_dispatch event)
  * Asset-portal - Triggered from [asset-portal workflow](https://github.com/defold/asset-portal/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Games-showcase - Triggered from [games-showcase workflow](https://github.com/defold/games-showcase/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Docs (manuals, tutorials, faq) - Triggered from [doc workflow](https://github.com/defold/doc/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Docs (examples) - Triggered from [examples workflow](https://github.com/defold/examples/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Codepad - Triggered from [codepad workflow](https://github.com/defold/codepad/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.


# Search

## Site search
The site search is powered by [Pagefind](https://pagefind.app), a static site search library. Pagefind automatically generates a search index during the site build process and provides a fast, client-side search interface with filtering and metadata support.

## Page search
Functionality for searching and marking within a single page using [Mark.js](https://markjs.io/).


# Credits

This site uses the following assets:

* [Octicons](https://octicons.github.com/)
