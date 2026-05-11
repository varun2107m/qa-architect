from backend.app.core.registry_loader import (
    load_frameworks
)

frameworks = load_frameworks()


def calculate_framework_score(
    framework_name,
    required_capabilities
):

    framework = frameworks.get(framework_name)

    if not framework:
        return 0

    supported = framework.get(
        "supports",
        []
    )

    score = 0

    for capability in required_capabilities:

        if capability in supported:
            score += 1

    return score
