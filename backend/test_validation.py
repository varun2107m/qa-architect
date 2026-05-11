from backend.app.validation.framework_validator import (
    validate_framework
)


result = validate_framework(
    "generated/sample-framework"
)

print("\n=== VALIDATION RESULT ===\n")

print(result)