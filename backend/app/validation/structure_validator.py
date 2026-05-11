from pathlib import Path


REQUIRED_FOLDERS = [
    "src",
    "src/pages",
    "src/tests"
]


def validate_structure(
    framework_path
):

    missing = []

    for folder in REQUIRED_FOLDERS:

        path = (
            Path(framework_path) / folder
        )

        if not path.exists():
            missing.append(folder)

    return {
        "valid": len(missing) == 0,
        "missing": missing
    }