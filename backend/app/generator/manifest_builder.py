import json


def build_manifest(spec):

    manifest = {
        "framework": spec.framework,
        "language": spec.language,
        "architecture_pattern": spec.architecture_pattern,
        "capabilities": [
            capability.name
            for capability in spec.capabilities
        ],
        "integrations": [
            integration.name
            for integration in spec.integrations
        ],
        "automation_types": spec.automation_types
    }

    return json.dumps(
        manifest,
        indent=2
    )

