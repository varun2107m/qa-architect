from shared.dsl.framework_spec import FrameworkSpec
from shared.dsl.capability import Capability
from shared.dsl.integration import Integration
from shared.dsl.execution import ExecutionSpec


spec = FrameworkSpec(
    framework_id="fw-001",
    automation_types=["web", "api"],
    language="typescript",
    framework="playwright",
    architecture_pattern="pom",
    capabilities=[
        Capability(name="reporting"),
        Capability(name="retry")
    ],
    integrations=[
        Integration(name="docker"),
        Integration(name="jenkins")
    ],
    execution=ExecutionSpec(
        parallel=True,
        retries=2
    )
)

print(spec.model_dump_json(indent=2))
