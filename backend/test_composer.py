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

from backend.app.engine.composition_engine import (
    compose_framework
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
    execution=ExecutionSpec()
)

modules = compose_framework(spec)

print("\n=== COMPOSED MODULES ===\n")

for module in modules:
    print(module)