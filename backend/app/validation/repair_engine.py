from pathlib import Path


def auto_create_missing_folders(
    framework_path,
    missing_folders
):

    for folder in missing_folders:

        path = (
            Path(framework_path) / folder
        )

        path.mkdir(
            parents=True,
            exist_ok=True
        )

    return {
        "repaired": True,
        "created": missing_folders
    }
