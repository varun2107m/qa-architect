import yaml
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parents[3]


REGISTRY_PATH = BASE_PATH / "registry"


def load_yaml(file_path):

    with open(file_path, "r") as file:
        return yaml.safe_load(file)


def load_registry(category):

    registry_data = {}

    category_path = REGISTRY_PATH / category

    for file in category_path.glob("*.yaml"):

        data = load_yaml(file)

        registry_data[data["name"]] = data

    return registry_data


def load_frameworks():
    return load_registry("frameworks")


def load_languages():
    return load_registry("languages")
