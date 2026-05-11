from fastapi import APIRouter

from backend.app.validation.framework_validator import (
    validate_framework
)

router = APIRouter()


@router.get("/validate")
def validate_framework_route():

    result = validate_framework(
        "generated/api-framework"
    )

    return result