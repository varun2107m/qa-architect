import os
import yaml


def load_module(template_dir):

    module_path = os.path.join(
        template_dir,
        "module.yaml"
    )

    with open(module_path) as file:
        return yaml.safe_load(file)
    