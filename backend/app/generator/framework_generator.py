import os
import json

from backend.app.engine.composition_engine import compose_framework
from backend.app.generator.file_writer import write_file
from backend.app.generator.renderer import render_template


def create_folders(output_dir, folders):

    for folder in folders:

        os.makedirs(
            os.path.join(output_dir, folder),
            exist_ok=True
        )


def safe_render(source, context):

    try:
        return render_template(source, context)

    except Exception as error:

        print(f"[WARN] Failed to render {source}: {error}")

        return f"// Failed to render template: {source}\n"


def generate_framework(spec, output_dir):

    os.makedirs(
        output_dir,
        exist_ok=True
    )

    modules = compose_framework(spec)

    all_folders = []
    all_files = []

    for module in modules:

        all_folders.extend(
            module.get("folders", [])
        )

        all_files.extend(
            module.get("files", [])
        )

    create_folders(
        output_dir,
        all_folders
    )

    context = {
        "framework": getattr(spec, "framework", "playwright"),
        "language": getattr(spec, "language", "typescript"),
        "architecture_pattern": getattr(spec, "architecture_pattern", "enterprise"),
        "capabilities": getattr(spec, "capabilities", []),
        "integrations": getattr(spec, "integrations", []),
        "automation_types": getattr(spec, "automation_types", [])
    }

    created_files = []

    for file_config in all_files:

        source = file_config.get("source")
        target = file_config.get("target")

        if not source or not target:
            continue

        content = safe_render(
            source,
            context
        )

        target_path = os.path.join(
            output_dir,
            target
        )

        write_file(
            target_path,
            content
        )

        created_files.append(target)

    manifest = {
        "framework": context["framework"],
        "language": context["language"],
        "architecture_pattern": context["architecture_pattern"],
        "template_used": modules[0].get("template_key"),
        "folders_generated": len(set(all_folders)),
        "files_generated": len(created_files),
        "files": created_files
    }

    write_file(
        os.path.join(output_dir, "framework.manifest.json"),
        json.dumps(manifest, indent=2)
    )

    return {
        "status": "success",
        "mode": "MULTI_FRAMEWORK_TEMPLATE_MODE",
        "output_dir": output_dir,
        "template_used": modules[0].get("template_key"),
        "folders_generated": len(set(all_folders)),
        "files_generated": len(created_files)
    }



