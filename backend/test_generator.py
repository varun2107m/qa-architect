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

from backend.app.generator.framework_generator import (
    generate_framework
)


spec = FrameworkSpec(
    framework_id="fw-001",
    automation_types=["web"],
    language="typescript",
    framework="playwright",
    architecture_pattern="pom",
    capabilities=[
        Capability(name="reporting")
    ],
    integrations=[
        Integration(name="docker")
    ],
    execution=ExecutionSpec(
        parallel=True,
        retries=2
    )
)

result = generate_framework(
    spec,
    "generated/sample-framework"
)

print(result)