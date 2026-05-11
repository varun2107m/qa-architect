import json
from pathlib import Path


def validate_manifest_dependencies(
    framework_path
):

    manifest_path = (
        Path(framework_path) /
        "framework.manifest.json"
    )

    if not manifest_path.exists():

        return {
            "valid": False,
            "reason": "Manifest missing"
        }

    with open(manifest_path, "r") as file:
        manifest = json.load(file)

    dependencies = manifest.get(
        "dependencies",
        []
    )

    return {
        "valid": len(dependencies) > 0,
        "dependency_count": len(dependencies)
    }