import os.path

from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import ConfigurationError
from mkdocs.plugins import BasePlugin, get_plugin_logger
from mkdocs.structure.pages import Page
from mkdocs.structure.files import Files, File
from mkdocs.utils import meta

from mkdocs_gentags.config import GenTagsConfig

logger = get_plugin_logger(__name__)


class GenTagsPlugin(BasePlugin[GenTagsConfig]):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # tag_name -> backrefrence path -> backreference file
        self._data = {}
        # tag name -> tag file
        self._files = {}

    def _cleanup_files(self, files):
        for fp in self._files.values():
            if fp.src_uri in files:
                files.remove(fp)
        return files

    def _generate_tag_file(self, file, meta, config):
        for tag in meta.get("tags", []):
            tag_name = tag.lower().strip()

            if tag_name in self._data:
                self._data[tag_name][file.src_uri] = file
            else:
                self._data[tag_name] = {file.src_uri: file}

                tag_path = os.path.join(self.config.path, f"{tag_name}.md")
                tag_file = File.generated(
                    src_uri=tag_path, content=f"# {tag_name}\n", config=config
                )
                # FIXME: something is failing when abs_src_path is None
                tag_file.abs_src_path = os.path.join(config["docs_dir"], tag_path)

                self._files[tag_name] = tag_file

    def _generate_tag_index_file(self, config):
        if not self._files:
            if self.config.verbose:
                logger.info("no tags found, skipping tag index")
            return

        tag_index_file = File.generated(
            src_uri=os.path.join(self.config.path, "index.md"),
            content="# tags\n",
            config=config,
        )
        self._files[""] = tag_index_file
        # FIXME: something is failing when abs_src_path is None
        tag_index_file.abs_src_path = os.path.join(
            config["docs_dir"], tag_index_file.src_uri
        )

        if self.config.verbose:
            logger.info(f"generated tag index at: {tag_index_file.src_uri}")

    #
    # Hooks
    #

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        tags_path = os.path.join(config["docs_dir"], self.config.path)
        if os.path.exists(tags_path):
            raise ConfigurationError(f"The path '{tags_path}' already exists.")

        return config

    def on_files(self, files: Files, config: MkDocsConfig) -> Files:
        files = self._cleanup_files(files)
        for file in files:
            if file.is_documentation_page():
                _, metadata = meta.get_data(file.content_string)
                self._generate_tag_file(file, metadata, config)

        self._generate_tag_index_file(config)

        for tag_file in self._files.values():
            if tag_file.src_uri in files:
                logger.info(f"skipping on existing file: {tag_file.src_uri}")
                continue

            files.append(tag_file)

        return files

    def on_page_markdown(
        self, markdown: str, page: Page, config: MkDocsConfig, files: Files
    ) -> str:
        if page.file in self._files.values():
            tagname = os.path.basename(page.file.src_uri).replace(".md", "")
            if tagname == "index":
                # tag data is a dict of tag files objects -> list of backlinks
                page.meta["tags_data"] = {
                    self._files[tag]: self._data[tag].values() for tag in self._data
                }
                if self.config.tags_index_template:
                    page.meta["template"] = self.config.tags_index_template
            else:
                page.meta["tag_name"] = tagname
                page.meta["tag_backlinks"] = self._data[tagname].values()
                if self.config.tags_template:
                    page.meta["template"] = self.config.tags_template

        return markdown
