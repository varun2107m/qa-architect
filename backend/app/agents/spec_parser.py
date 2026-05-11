from shared.dsl.framework_spec import (
    FrameworkSpec
)

from shared.dsl.capability import (
    Capability
)

from shared.dsl.integration import (
    Integration
)

from shared.dsl.execution import (
    ExecutionSpec
)

from backend.app.core.normalizer import (
    normalize_value
)


def parse_to_spec(
    data
):

    # -----------------------------
    # SAFE EXTRACTION WITH DEFAULTS
    # -----------------------------

    language = data.get("language", "typescript")
    framework = data.get("framework", "playwright")
    architecture_pattern = data.get(
        "architecture_pattern",
        "pom"
    )

    automation_types = data.get(
        "automation_types",
        []
    )

    # -----------------------------
    # NORMALIZATION (CRITICAL FIX)
    # -----------------------------

    language = normalize_value(
        "language",
        language
    )

    framework = normalize_value(
        "framework",
        framework
    )

    architecture_pattern = normalize_value(
        "architecture_pattern",
        architecture_pattern
    )

    # -----------------------------
    # CAPABILITIES
    # -----------------------------

    capabilities = [
        Capability(name=cap)
        for cap in data.get(
            "capabilities",
            []
        )
    ]

    # -----------------------------
    # INTEGRATIONS
    # -----------------------------

    integrations = [
        Integration(name=integration)
        for integration in data.get(
            "integrations",
            []
        )
    ]

    # -----------------------------
    # EXECUTION DEFAULTS
    # -----------------------------

    execution_data = data.get(
        "execution",
        {}
    )

    execution = ExecutionSpec(
        parallel=execution_data.get(
            "parallel",
            True
        ),
        retries=execution_data.get(
            "retries",
            2
        ),
        headless=execution_data.get(
            "headless",
            True
        ),
        timeout=execution_data.get(
            "timeout",
            30000
        )
    )

    # -----------------------------
    # FINAL SPEC BUILD
    # -----------------------------

    return FrameworkSpec(
        framework_id="generated-fw",
        automation_types=automation_types,
        language=language,
        framework=framework,
        architecture_pattern=architecture_pattern,
        capabilities=capabilities,
        integrations=integrations,
        execution=execution
    )