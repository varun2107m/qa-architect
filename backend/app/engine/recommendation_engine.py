from backend.app.core.registry_loader import (
    load_frameworks
)

from backend.app.engine.scoring_engine import (
    calculate_framework_score
)

frameworks = load_frameworks()


def recommend_framework(
    required_capabilities
):

    best_framework = None

    best_score = -1

    for framework_name in frameworks.keys():

        score = calculate_framework_score(
            framework_name,
            required_capabilities
        )

        if score > best_score:

            best_framework = framework_name

            best_score = score

    return {
        "framework": best_framework,
        "score": best_score
    }
