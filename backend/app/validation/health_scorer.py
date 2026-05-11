def calculate_health_score(
    validations
):

    total = len(validations)

    passed = 0

    for validation in validations:

        if validation.get("valid"):
            passed += 1

    return round(
        (passed / total) * 100,
        2
    )
