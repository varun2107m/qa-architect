def compose_framework(spec):

    framework = getattr(spec, "framework", "playwright")
    language = getattr(spec, "language", "typescript")
    capabilities = getattr(spec, "capabilities", [])

    modules = []

    # -----------------------------
    # BASE MODULE (ALWAYS INCLUDED)
    # -----------------------------
    modules.append({
        "folders": [
            "src/pages",
            "src/tests",
            "src/utils",
            "src/config"
        ],
        "files": [
            {
                "source": "frameworks/playwright/base.page.ts.j2",
                "target": "src/pages/base.page.ts"
            },
            {
                "source": "frameworks/playwright/playwright.config.ts.j2",
                "target": "playwright.config.ts"
            }
        ]
    })

    # -----------------------------
    # OPTIONAL CAPABILITIES (SAFE)
    # -----------------------------
    capability_map = {

        "retries": {
            "folders": [],
            "files": []
        },

        "reporting": {
            "folders": ["reports"],
            "files": []
        },

        "docker": {
            "folders": [],
            "files": [
                {
                    "source": "frameworks/playwright/docker-compose.yml.j2",
                    "target": "docker-compose.yml"
                }
            ]
        },

        "api_testing": {
            "folders": ["src/api"],
            "files": []
        },

        "fixtures": {
            "folders": ["src/fixtures"],
            "files": []
        },

        "hooks": {
            "folders": ["src/hooks"],
            "files": []
        }
    }

    for cap in capabilities or []:

        module = capability_map.get(cap)

        if module:
            modules.append(module)
        else:
            print(f"[WARN] Unknown capability skipped: {cap}")

    return modules

