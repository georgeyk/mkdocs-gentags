from mkdocs.config import base
from mkdocs.config import config_options as co


class GenTagsConfig(base.Config):
    # general flags
    path = co.Type(str, default="tags")
    tags_index_template = co.Type(str, default="tags.html")
    tags_template = co.Type(str, default="tag.html")

    # Testing flags
    verbose = co.Type(bool, default=False)
