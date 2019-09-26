# defold.github.io

New www.defold.com leveraging GitHub Pages and Jekyll+Liquid to generate a static site.

## Usage
This project pulls in additional content from a couple of repositories using the `update.py` script:

```
python update.py [--download] docs codepad refdoc examples assets
```

### Options
The script accepts the following options:

* `--download` - Download the required files for each command. If the option is omitted the files are expected to already exist on disk ready for processing.

### Commands
The script accepts the following commands:

* `docs` - Import manuals, tutorials and FAQ from github.com/defold/doc
* `codepad` - Import CodePad from github.com/defold/codepad
* `refdoc` - Import API reference from latest release at d.defold.com
* `examples` - Import examples from github.com/defold/examples
* `assets` - Import Asset Portal content from github.com/defold/awesome-defold
* `searchindex` - Generates the search index


# Testing locally
Follow the Jekyll install instructions to build and test the site locally before pushing changes to this repository:

https://jekyllrb.com/docs/github-pages/


# Search

## Site search
The site search is based on [Lunr.js](https://github.com/olivernn/lunr.js). The search index is generated using the [Python equivalent of Lunr](https://github.com/yeraydiazdiaz/lunr.py). Install the python version using:

```
pip install --user lunr==0.5.5
```

Version 0.5.5 of lunr.py uses Lunr.js version 2.3.6.

## Page search
Functionality for searching and marking within a single page using [Mark.js](https://markjs.io/).
