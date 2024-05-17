import pytest

from mkdocs.config.defaults import MkDocsConfig


@pytest.fixture()
def mkdocs_config(tmp_path_factory):
    config = MkDocsConfig()
    config.load_dict(
        {
            "site_name": "tests",
            "docs_dir": str(tmp_path_factory.mktemp("docs", numbered=True)),
            "site_dir": str(tmp_path_factory.mktemp("site", numbered=True)),
            "plugins": {"gentags": {"path": "tags"}},
        }
    )
    errors, warns = config.validate()

    assert not errors
    assert not warns

    return config


@pytest.fixture()
def gentags(mkdocs_config):
    # fix some internals of mkdocs
    mkdocs_config.plugins._current_plugin = "test-gentags"
    return mkdocs_config["plugins"]["gentags"]
