from pydantic import BaseModel
from typing import List, Dict, Any

from shared.dsl.capability import Capability
from shared.dsl.integration import Integration
from shared.dsl.execution import ExecutionSpec


class FrameworkSpec(BaseModel):

    framework_id: str

    automation_types: List[str]

    language: str

    framework: str

    architecture_pattern: str

    capabilities: List[Capability]

    integrations: List[Integration]

    execution: ExecutionSpec

    metadata: Dict[str, Any] = {}
    