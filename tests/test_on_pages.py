from mkdocs.structure.files import get_files
from mkdocs.structure.pages import Page

from .utils import create_file_with_tags


class TestOnPageMarkdown:
    def test_tags_index_page(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", ["hello"])
        files = get_files(mkdocs_config)
        files = gentags.on_files(files, mkdocs_config)
        tag_index_file = [f for f in files if f.src_uri == "tags/index.md"][0]
        tag_file = [f for f in files if f.src_uri == "tags/hello.md"][0]
        tag_index_page = Page("tags", tag_index_file, mkdocs_config)

        retval = gentags.on_page_markdown("", tag_index_page, mkdocs_config, files)

        assert retval == ""
        assert tag_index_page.meta["template"] == gentags.config.tags_index_template
        assert "tags_data" in tag_index_page.meta
        assert tag_file in tag_index_page.meta["tags_data"]
        assert len(tag_index_page.meta["tags_data"][tag_file]) == 1
        assert tag_index_page.meta["tags_data"][tag_file][0].src_uri == "index.md"

    def test_tags_page(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", ["hello"])
        files = get_files(mkdocs_config)
        files = gentags.on_files(files, mkdocs_config)
        tag_file = [f for f in files if f.src_uri == "tags/hello.md"][0]
        tag_page = Page("hello", tag_file, mkdocs_config)

        retval = gentags.on_page_markdown("", tag_page, mkdocs_config, files)

        assert retval == ""
        assert tag_page.meta["template"] == gentags.config.tags_template
        assert "tag_name" in tag_page.meta
        assert tag_page.meta["tag_name"] == "hello"
        assert "tag_backlinks" in tag_page.meta
        assert len(tag_page.meta["tag_backlinks"]) == 1
        assert tag_page.meta["tag_backlinks"][0].src_uri == "index.md"

    def test_skip_non_tag_pages(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", ["hello"])
        files = get_files(mkdocs_config)
        files = gentags.on_files(files, mkdocs_config)
        index_file = [f for f in files if f.src_uri == "index.md"][0]
        index_page = Page("index", index_file, mkdocs_config)

        retval = gentags.on_page_markdown("index", index_page, mkdocs_config, files)

        assert retval == "index"
        assert "template" not in index_page.meta
        assert "tag_name" not in index_page.meta
        assert "tag_backlinks" not in index_page.meta
        assert "tags_data" not in index_page.meta
