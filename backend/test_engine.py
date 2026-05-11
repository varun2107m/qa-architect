from backend.app.engine.capability_engine import (
    get_frameworks_supporting
)

from backend.app.engine.compatibility_engine import (
    validate_framework_language,
    validate_architecture_pattern
)

from backend.app.engine.recommendation_engine import (
    recommend_framework
)


print("\n=== Capability Matching ===\n")

print(
    get_frameworks_supporting(
        "parallel_execution"
    )
)

print("\n=== Compatibility Check ===\n")

print(
    validate_framework_language(
        "playwright",
        "typescript"
    )
)

print(
    validate_framework_language(
        "cypress",
        "java"
    )
)

print("\n=== Pattern Validation ===\n")

print(
    validate_architecture_pattern(
        "selenium",
        "keyword"
    )
)

print(
    validate_architecture_pattern(
        "playwright",
        "keyword"
    )
)

print("\n=== Recommendation ===\n")

print(
    recommend_framework(
        [
            "parallel_execution",
            "tracing",
            "api_testing"
        ]
    )
)
