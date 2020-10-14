# defold.github.io

New www.defold.com leveraging GitHub Pages and Jekyll+Liquid to generate a static site. The structure of the static site as well as many of the pages are stored in this repository. Some other parts of the site such as content of the learn section and the asset portal is hosted in other GitHub repositories:

* Assets - www.defold.com/assets -> github.com/defold/awesome-defold
* Learn
  * Manuals - www.defold.com/manuals -> github.com/defold/doc
  * Tutorials - www.defold.com/tutorials -> github.com/defold/doc
  * FAQ - www.defold.com/faq -> github.com/defold/doc
  * Examples - www.defold.com/examples -> github.com/defold/examples
* Codepad - www.defold.com/codepad -> github.com/defold/codepad

# HOW TO UPDATE THE SITE WITH NEW CONTENT
The site uses the `update.py` script from this repository to update the site with updated content from external sources/repositories.

## Requirements
You need to make sure to have the following dependencies installed before using `update.py`:

* Python 2.7.x
* Lunr.py (search)
* Requests (http requests)

Install `lunr.py` and `requests` using:

```
pip install --user lunr==0.5.5
pip install --user requests
pip install --user pyyaml
pip install --user markdown==2.6.7
pip install --user pygments==2.1.3
```

## Usage
The `update.py` script should be run from a terminal. The syntax is as follows:

```
python update.py [--download] docs codepad refdoc examples assets
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
* `assets` - Import Asset Portal content from github.com/defold/awesome-defold
* `searchindex` - Generates the search index
* `commit` - Commit changes to GitHub (for CI use)


# HOW TO TEST THE SITE LOCALLY
It is recommended that you generate and test the site locally before pushing the changes to the repository. You generate and test the site locally by running `serve.sh`.

## Requirements
You need to make sure you have the following dependencies installed before attempting to generate the site locally using `serve.sh`:

* Ruby
* bundler gem
* jekyll
* github-pages gem

### 1 Install Ruby
Most macOS versions ship with Ruby preinstalled. It is however recommended that you install a separate Ruby version as you will very likely run into permission issues if trying to install any Ruby gems with the system version of Ruby.
The quickest way to install a new Ruby version on macOS/Linux us to use `rbenv` or `ruby`. To install it on macOS you first need to install `brew`:

#### 1.1 Install brew (macOS)
Open a terminal window and install `brew` by running the following command:

```sh
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

#### 1.2 Install ruby

```sh
	brew install ruby
```

Also add the it to the PATH vaiable in you shell profile (e.g. `~/.zshrc`):

```sh
export PATH="/usr/local/opt/ruby/bin:$PATH"
```

#### 1.3 Install rbenv (deprecated)
Open a terminal window and install `rbenv` by running the following commands:

```sh
	# use brew to install rbenv
	brew install rbenv
	# install rbenv shell support every time a shel is started
	echo 'eval "$(rbenv init -)"' >> ~/.bash_profile
```

Now close the terminal window. Open a new terminal window and install a new Ruby version (this version corresponds to the one defined in the `.ruby-version` file of this repository):

```sh
	# use rbenv to install ruby 2.6.5
	rbenv install 2.6.5
```

### 2 Install gems
Open a terminal window and install the required Ruby gems by running the following command:

```sh
	gem install bundler jekyll github-pages
```

This will install the gems defined in the Gemfile (`bundler`, `jekyll`, `github-pages`). You are now ready to launch the site locally.


## Usage
Launch/serve the site locally using:

As a first step, you need to install dependencies:

```sh
    bundle install
```


```
./serve.sh
```

Once the site has been built you can test it by pointing your browser to localhost:4000.

You can use the `update.py` script to pull in and process content from external sources (docs, asset portal etc)

## How to test local reference documentation

Copy the `refdoc.zip` to the main folder:

        $ cp $DYNAMO_HOME/share/ref-doc.zip refdoc_alpha.zip
        $ cp $DYNAMO_HOME/share/ref-doc.zip refdoc_beta.zip
        $ cp $DYNAMO_HOME/share/ref-doc.zip refdoc_stable.zip
        $ ./update.py refdoc
        $ ./serve.sh

# Automatic site update using GitHub Actions
The site uses [GitHub actions](https://github.com/defold/defold.github.io/actions) to automatically trigger `update.py` when an external source/repository has been updated. The script is also triggered once every hour to update the asset portal star count for GitHub hosted assets. The following workflows/jobs have been set up using GitHub Actions:

* [Update site](https://github.com/defold/defold.github.io/blob/master/.github/workflows/update_site.yml) - on change in external repository (triggered using the repository_dispatch event)
  * Assets - Triggered from [awesome-defold workflow](https://github.com/defold/awesome-defold/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Docs (manuals, tutorials, faq) - Triggered from [doc workflow](https://github.com/defold/doc/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Docs (examples) - Triggered from [examples workflow](https://github.com/defold/examples/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.
  * Codepad - Triggered from [codepad workflow](https://github.com/defold/codepad/blob/master/.github/workflows/trigger-site-rebuild.yml) on change.


# Search

## Site search
The site search is based on [Lunr.js](https://github.com/olivernn/lunr.js). The search index is generated using the [Python equivalent of Lunr](https://github.com/yeraydiazdiaz/lunr.py). Version 0.5.5 of lunr.py uses Lunr.js version 2.3.6.

## Page search
Functionality for searching and marking within a single page using [Mark.js](https://markjs.io/).


# Credits

This site uses the following assets:

* [Octicons](https://octicons.github.com/)
