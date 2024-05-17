import os.path
from textwrap import dedent


def create_file_with_tags(mkdocs_config, pathname, tags):
    path = os.path.join(mkdocs_config["docs_dir"], pathname)
    with open(path, "w") as fp:
        if tags:
            tags_content = "\n".join([f"- {tag}" for tag in tags])
            fp.write(dedent("---\n" "tags:\n" f"{tags_content}\n" "---\n"))
        fp.write("# hello\n")
