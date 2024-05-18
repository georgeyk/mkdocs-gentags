# mkdocs-gentags

A [mkdocs][1] plugin to generate tags from metadata (aka _frontmatter_).

Generates virtual files for tags, and inject context in the page objects to ease rendering in custom templates. The virtual files behave as normal files, they can be linked, indexed and so on.

In particular, this plugin is useful for those who want to customize their tags page.

## Installation

In the same environment as you have `mkdocs` installed, usually with `pip`:

```shell
pip install mkdocs-gentags
```

## Configuration

In your `mkdocs.yml`:

```yaml
...
plugins:
  - gentags:
      path: tags
      tags_index_template: tags.html
      tags_template: tag.html
      verbose: false
...
```

**path**

A relative path from `docs_dir`, where the tag files (virtually) exist.
Defaults to `tags`.

**tags\_index\_template**

The template to use for the tag index page. Defaults
to `tags.html`, and if empty, it will be set to `main.html`.
The tag index page is the page that has a reference to all the other tags found.

Note that `tags.html` are not provided by this plugin, you must create a custom
template, or your theme must support it.

**tags\_template**

Similar to _tags\_index\_template_ but for individual tags.
Defaults to `tag.html`, and set to `main.html` when unset.

Each individual tag file contain a reference to every file using it (backlinks).

Note that `tag.html` are not provided by this plugin, you must create a custom
template, or your theme must support it.


**verbose**

Change plugin verbosity. Defaults to `false`.


## Template variables

**tags index page**

`tags_data`: a dictionary consisting of pairs of tag file and the list of files referring to the tag.

**tags page**

`tag_name`: the name of the tag.

`tag_backlinks`: a list of files referring to the tag.


## Example

You can check example pages under the `Example` submenu on the top of the page.

The source files are available [here](https://github.com/georgeyk/mkdocs-gentags/tree/main/docs).

The template examples are available [here](https://github.com/georgeyk/mkdocs-gentags/tree/main/theme).


[1]: https://www.mkdocs.org
