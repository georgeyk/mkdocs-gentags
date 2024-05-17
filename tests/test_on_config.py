import os.path
import pytest
from mkdocs.exceptions import ConfigurationError


class TestOnConfig:
    def test_path_already_exists(self, gentags, mkdocs_config):
        os.makedirs(os.path.join(mkdocs_config["docs_dir"], "tags"))

        with pytest.raises(ConfigurationError):
            gentags.on_config(mkdocs_config)

    def test_path_is_empty(self, gentags, mkdocs_config):
        gentags.config.path = ""

        assert gentags.on_config(mkdocs_config) is mkdocs_config

    def test_template_defaults(self, gentags):
        assert gentags.config.tags_index_template == "tags.html"
        assert gentags.config.tags_template == "tag.html"

    def test_missing_tags_index_template(self, gentags, mkdocs_config):
        gentags.config.tags_index_template = ""
        gentags.on_config(mkdocs_config)

        assert gentags.config.tags_index_template == "main.html"

    def test_missing_tags_template(self, gentags, mkdocs_config):
        gentags.config.tags_template = ""
        gentags.on_config(mkdocs_config)

        assert gentags.config.tags_template == "main.html"
