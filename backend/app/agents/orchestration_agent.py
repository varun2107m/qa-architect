from types import SimpleNamespace

from backend.app.generator.framework_generator import generate_framework


def detect_framework(prompt):

    prompt_lower = prompt.lower()

    if "rest assured" in prompt_lower or "restassured" in prompt_lower:
        return "rest assured"

    if "selenium" in prompt_lower:
        return "selenium"

    if "cypress" in prompt_lower:
        return "cypress"

    if "appium" in prompt_lower:
        return "appium"

    if "pytest" in prompt_lower:
        return "pytest"

    if "playwright" in prompt_lower:
        return "playwright"

    return "playwright"


def detect_language(prompt, framework):

    prompt_lower = prompt.lower()

    if "java" in prompt_lower:
        return "java"

    if "python" in prompt_lower:
        return "python"

    if "javascript" in prompt_lower or "js" in prompt_lower:
        return "javascript"

    if "typescript" in prompt_lower or "ts" in prompt_lower:
        return "typescript"

    if framework in ["selenium", "rest assured", "restassured", "appium"]:
        return "java"

    if framework == "pytest":
        return "python"

    if framework == "cypress":
        return "typescript"

    return "typescript"


def detect_capabilities(prompt):

    prompt_lower = prompt.lower()

    capabilities = []

    if "api" in prompt_lower:
        capabilities.append("api_testing")

    if "fixture" in prompt_lower or "fixtures" in prompt_lower:
        capabilities.append("fixtures")

    if "hook" in prompt_lower or "hooks" in prompt_lower:
        capabilities.append("hooks")

    if "report" in prompt_lower or "reporting" in prompt_lower:
        capabilities.append("reporting")

    if "docker" in prompt_lower:
        capabilities.append("docker")

    if "ci" in prompt_lower or "cd" in prompt_lower or "pipeline" in prompt_lower:
        capabilities.append("cicd")

    if "screenshot" in prompt_lower or "screenshots" in prompt_lower:
        capabilities.append("screenshots")

    if "video" in prompt_lower or "videos" in prompt_lower:
        capabilities.append("videos")

    if "parallel" in prompt_lower:
        capabilities.append("parallel_execution")

    if "log" in prompt_lower or "logging" in prompt_lower:
        capabilities.append("logging")

    return capabilities


def generate_from_prompt(prompt, output_dir):

    framework = detect_framework(prompt)
    language = detect_language(prompt, framework)
    capabilities = detect_capabilities(prompt)

    spec = SimpleNamespace(
        framework=framework,
        language=language,
        architecture_pattern="enterprise",
        capabilities=capabilities,
        integrations=[],
        automation_types=["ui", "api"]
    )

    generation = generate_framework(
        spec,
        output_dir
    )

    return {
        "analysis": {
            "framework": framework,
            "language": language,
            "architecture_pattern": "enterprise",
            "capabilities": capabilities,
            "automation_types": ["ui", "api"]
        },
        "generation": generation
    }


