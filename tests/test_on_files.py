import os.path

from mkdocs.structure.files import get_files

from .utils import create_file_with_tags


class TestOnFiles:
    def test_without_tags(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", [])
        files = get_files(mkdocs_config)
        assert len(files) == 1

        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 1

    def test_one_tag(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", ["hello"])

        files = get_files(mkdocs_config)
        assert len(files) == 1

        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 3

        assert "tags/index.md" in files
        p = os.path.join(mkdocs_config["docs_dir"], "tags/index.md")
        assert os.path.exists(p) is False

        assert "tags/hello.md" in files
        p = os.path.join(mkdocs_config["docs_dir"], "tags/hello.md")
        assert os.path.exists(p) is False

    def test_ignore_non_markdown(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.pdf", ["hello"])
        files = get_files(mkdocs_config)
        assert len(files) == 1

        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 1
        assert "tags/index.md" not in files
        assert "tags/hello.md" not in files

    def test_normalize_tags(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", ["hello", "one"])
        create_file_with_tags(mkdocs_config, "other.md", ["HellO", "two"])

        files = get_files(mkdocs_config)
        assert len(files) == 2

        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 6

        assert "tags/index.md" in files
        assert "tags/hello.md" in files
        assert "tags/one.md" in files
        assert "tags/two.md" in files

    def test_skip_existing_filename(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "other.md", ["other"])
        gentags.config.path = ""

        files = get_files(mkdocs_config)
        assert len(files) == 1

        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 2
        assert "other.md" in files
        # it's not the tag file
        p = os.path.join(mkdocs_config["docs_dir"], "other.md")
        assert os.path.exists(p)
        # but index is
        assert "index.md" in files
        p = os.path.join(mkdocs_config["docs_dir"], "index.md")
        assert os.path.exists(p) is False

    def test_re_runs(self, gentags, mkdocs_config):
        create_file_with_tags(mkdocs_config, "index.md", ["one"])
        files = get_files(mkdocs_config)
        assert len(files) == 1

        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 3
        assert "tags/index.md" in files
        assert "tags/one.md" in files

        create_file_with_tags(mkdocs_config, "index.md", ["one", "two"])
        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 4
        assert "tags/index.md" in files
        assert "tags/one.md" in files
        assert "tags/two.md" in files

        create_file_with_tags(mkdocs_config, "index.md", ["two"])
        files = gentags.on_files(files, mkdocs_config)
        assert len(files) == 3
        assert "tags/index.md" in files
        assert "tags/two.md" in files
