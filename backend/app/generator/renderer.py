import os

from jinja2 import (
    Environment,
    FileSystemLoader
)

BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../"
    )
)

TEMPLATE_DIR = os.path.join(
    BASE_DIR,
    "templates"
)

env = Environment(
    loader=FileSystemLoader(
        TEMPLATE_DIR
    ),
    trim_blocks=True,
    lstrip_blocks=True
)


def render_template(
    template_path,
    context
):

    template = env.get_template(
        template_path
    )

    return template.render(**context)


