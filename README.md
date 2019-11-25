# defold.github.io

New www.defold.com leveraging GitHub Pages and Jekyll+Liquid to generate a static site. The structure of the static site as well as many of the pages are stored in this repository. Some other parts of the site such as content of the learn section and the asset portal is hosted in other GitHub repositories:

* Assets - www.defold.com/assets -> github.com/defold/awesome-defold
* Learn
  * Manuals - www.defold.com/manuals -> github.com/defold/doc
  * Tutorials - www.defold.com/tutorials -> github.com/defold/doc
  * FAQ - www.defold.com/faq -> github.com/defold/doc
  * Examples - www.defold.com/examples -> github.com/defold/examples
* Codepad - www.defold.com/codepad -> github.com/defold/codepad

## Site update script
The site uses the `update.py` script from this repository to update the site with updated content from external sources/repositories:

```
python update.py [--download] docs codepad refdoc examples assets
```

You can use this script when testing locally (see below). The script is also used by GitHub Actions when automatically updating the site when one of the external sources/repositories have changed (see below).

### Dependencies
The `update.py` script depends on `lunr.py` (search) and `requests` (http requests). Install using:

```
pip install --user lunr==0.5.5
pip install --user requests
```

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


# Testing locally
Follow the Jekyll install instructions to build and test the site locally before pushing changes to this repository:

https://jekyllrb.com/docs/github-pages/

Use the `update.py` script to pull in and process content from external sources and then launch/serve the site locally using:

```
./serve.sh
```

Once the site has been built you can test it by pointing your browser to localhost:4000.


# Automatic site update using GitHub Actions
The site uses [GitHub actions](https://github.com/defold/defold.github.io/actions) to automatically trigger `update.py` when an external source/repository has been updated. The script is also triggered once every hour to update the asset portal star count for GitHub hosted assets. The following workflows/jobs have been set up using GitHub Actions:

* [Update star count](https://github.com/defold/defold.github.io/blob/master/.github/workflows/update_stars.yml) - hourly workflow
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
