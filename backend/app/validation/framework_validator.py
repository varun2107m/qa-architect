from backend.app.validation.structure_validator import (
    validate_structure
)

from backend.app.validation.dependency_validator import (
    validate_manifest_dependencies
)

from backend.app.validation.architecture_validator import (
    validate_pom_structure
)

from backend.app.validation.health_scorer import (
    calculate_health_score
)

from backend.app.validation.repair_engine import (
    auto_create_missing_folders
)


def validate_framework(
    framework_path
):

    validations = []

    structure = validate_structure(
        framework_path
    )

    validations.append(structure)

    dependencies = (
        validate_manifest_dependencies(
            framework_path
        )
    )

    validations.append(dependencies)

    architecture = validate_pom_structure(
        framework_path
    )

    validations.append(architecture)

    health_score = calculate_health_score(
        validations
    )

    if not structure["valid"]:

        auto_create_missing_folders(
            framework_path,
            structure["missing"]
        )

    return {
        "health_score": health_score,
        "validations": validations
    }