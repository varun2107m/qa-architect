import os
import yaml


BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../templates"
    )
)


def load_module_manifest(
    category,
    module_name
):

    manifest_path = os.path.join(
        BASE_DIR,
        category,
        module_name,
        "module.yaml"
    )

    with open(
        manifest_path,
        "r",
        encoding="utf-8"
    ) as file:

        return yaml.safe_load(file)
    