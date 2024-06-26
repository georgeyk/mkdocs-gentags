# mkdocs-gentags

![](https://github.com/georgeyk/mkdocs-gentags/actions/workflows/tests.yml/badge.svg?branch=main)
![](https://github.com/georgeyk/mkdocs-gentags/actions/workflows/lint.yml/badge.svg?branch=main)
[![pypi](https://img.shields.io/pypi/v/mkdocs-gentags.svg)](https://pypi.python.org/pypi/mkdocs-gentags)
[![versions](https://img.shields.io/pypi/pyversions/mkdocs-gentags.svg)](https://github.com/georgeyk/mkdocs-gentags)
[![license](https://img.shields.io/github/license/georgeyk/mkdocs-gentags.svg)](https://github.com/georgeyk/mkdocs-gentags/blob/main/LICENSE)

---

A [mkdocs][1] plugin to generate tags from metadata (aka frontmatter).

Generates virtual files for tags, and inject context in the page objects to
facilitate rendering in custom templates. The virtual files behave as normal
files, they can be linked, indexed and so on.

In particular, this plugin is useful for those who want to customize their tags page.

For more information, installation steps and examples, see the [documentation][2].

## Related

Similar plugins:

- https://github.com/jldiaz/mkdocs-plugin-tags
- https://github.com/timmeinerzhagen/mkdocs-meta-manager


[1]: https://www.mkdocs.org
[2]: https://georgeyk.github.io/mkdocs-gentags/
