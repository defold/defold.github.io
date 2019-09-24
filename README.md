# defold.github.io

New www.defold.com leveraging GitHub Pages and Jekyll+Liquid to generate a static site. This project pulls in additional content from a couple of repositories using the `update.py` file:

```
python update.py [--download] docs codepad refdoc examples assets
```

* docs - Import manuals, tutorials and FAQ from github.com/defold/doc
* codepad - Import CodePad from github.com/defold/codepad
* refdoc - Import API reference from latest release at d.defold.com
* examples - Import examples from github.com/defold/examples
* assets - Import Asset Portal content from github.com/defold/awesome-defold
