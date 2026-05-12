from backend.app.core.framework_registry import SUPPORTED_FRAMEWORKS


def resolve_framework_stack(framework, language):

    framework = str(framework or "playwright").lower().strip()
    language = str(language or "typescript").lower().strip()

    framework_map = SUPPORTED_FRAMEWORKS.get(framework)

    if not framework_map:
        print(f"[WARN] Unsupported framework: {framework}. Falling back to playwright/typescript.")
        return "playwright-ts"

    template_key = framework_map.get(language)

    if not template_key:
        print(
            f"[WARN] Unsupported language '{language}' for framework '{framework}'. "
            "Falling back to playwright/typescript."
        )
        return "playwright-ts"

    return template_key
