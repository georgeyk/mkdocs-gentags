# Development

## Setup

Create a `virtualenv` and install `hatch` with your favorite tools.

Create the "hatch" environment with:

```bash
hatch env create default
```

Load your environment with:

```bash
hatch shell test.py3.11
```

Run tests with:

```bash
hatch run test:test
```


## Docs

In your dev environment, use the `mkdocs` commands as usual.

```bash
# build documentation
mkdocs build

# start the local server
mkdocs serve
```

To deploy:

```bash
mkdocs gh-deploy
```


## Packaging

In your dev environment, use the `build` and `publish` commands.

```bash
# set a new version
hatch version <new version>

# test, commit & push changes
...

# build package
hatch build
# `dist/` folder should exists and contains the package files

# publish
hatch publish
```
