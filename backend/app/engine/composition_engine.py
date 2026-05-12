import os
import yaml

from backend.app.core.framework_resolver import resolve_framework_stack


BASE_DIR = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../../"
    )
)

FRAMEWORK_TEMPLATE_DIR = os.path.join(
    BASE_DIR,
    "templates",
    "frameworks"
)


def load_module(template_key):

    module_path = os.path.join(
        FRAMEWORK_TEMPLATE_DIR,
        template_key,
        "module.yaml"
    )

    if not os.path.exists(module_path):

        print(
            f"[WARN] Missing module.yaml for {template_key}. "
            "Falling back to playwright-ts."
        )

        template_key = "playwright-ts"

        module_path = os.path.join(
            FRAMEWORK_TEMPLATE_DIR,
            template_key,
            "module.yaml"
        )

    with open(
        module_path,
        "r",
        encoding="utf-8"
    ) as file:

        module = yaml.safe_load(file)

    module["template_key"] = template_key

    prepared_files = []

    for file_config in module.get("files", []):

        if not isinstance(file_config, dict):
            continue

        source = file_config.get("source")
        target = file_config.get("target")

        if not source or not target:
            continue

        prepared_files.append(
            {
                "source": f"frameworks/{template_key}/{source}",
                "target": target
            }
        )

    module["files"] = prepared_files

    return module


def compose_framework(spec):

    framework = getattr(spec, "framework", "playwright")
    language = getattr(spec, "language", "typescript")
    capabilities = getattr(spec, "capabilities", [])

    template_key = resolve_framework_stack(
        framework,
        language
    )

    print(f"[INFO] TEMPLATE KEY = {template_key}")

    modules = [
        load_module(template_key)
    ]

    capability_folders = {
        "reporting": ["reports"],
        "docker": ["docker"],
        "api_testing": ["src/api"],
        "fixtures": ["src/fixtures"],
        "hooks": ["src/hooks"],
        "cicd": [".github/workflows"],
        "screenshots": ["screenshots"],
        "videos": ["videos"],
        "logging": ["logs"],
        "parallel_execution": []
    }

    for capability in capabilities or []:

        folders = capability_folders.get(
            str(capability).lower(),
            []
        )

        if folders:

            modules.append(
                {
                    "name": capability,
                    "folders": folders,
                    "files": []
                }
            )

    return modules



