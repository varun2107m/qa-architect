from backend.app.core.registry_loader import (
    load_frameworks
)


frameworks = load_frameworks()


def validate_framework_language(
    framework_name,
    language
):

    framework = frameworks.get(framework_name)

    if not framework:
        return False

    supported_languages = framework.get(
        "languages",
        []
    )

    return language in supported_languages


def validate_architecture_pattern(
    framework_name,
    pattern
):

    framework = frameworks.get(framework_name)

    if not framework:
        return False

    patterns = framework.get(
        "architecture_patterns",
        []
    )

    return pattern in patterns
