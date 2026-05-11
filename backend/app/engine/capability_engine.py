from backend.app.core.registry_loader import (
    load_frameworks
)

frameworks = load_frameworks()


def get_frameworks_supporting(capability):

    compatible = []

    for framework_name, framework_data in frameworks.items():

        supported = framework_data.get("supports", [])

        if capability in supported:
            compatible.append(framework_name)

    return compatible