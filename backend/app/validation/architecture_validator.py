from pathlib import Path


def validate_pom_structure(
    framework_path
):

    base_page = (
        Path(framework_path) /
        "base.page.ts"
    )

    return {
        "valid": base_page.exists()
    }