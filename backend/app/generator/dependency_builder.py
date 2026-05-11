def build_dependencies(spec):

    dependencies = []

    framework = spec.framework.lower()
    language = spec.language.lower()

    if framework == "playwright":

        dependencies.extend([
            "@playwright/test"
        ])

    if language == "typescript":

        dependencies.extend([
            "typescript",
            "ts-node"
        ])

    capabilities = [
        capability.name.lower()
        for capability in spec.capabilities
    ]

    if "reporting" in capabilities:

        dependencies.append(
            "allure-playwright"
        )

    return dependencies

