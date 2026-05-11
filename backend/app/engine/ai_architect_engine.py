# backend/app/engine/ai_architect_engine.py

def build_architecture(spec):

    capabilities = getattr(spec, "capabilities", [])

    architecture = {

        "folders": [

            # Core
            "src/pages",
            "src/components",
            "src/flows",
            "src/tests",

            # API
            "src/api",
            "src/services",

            # Framework utilities
            "src/utils",
            "src/helpers",
            "src/constants",
            "src/config",

            # Enterprise patterns
            "src/fixtures",
            "src/hooks",
            "src/factories",
            "src/models",
            "src/validations",
            "src/locators",

            # Test data
            "src/data",

            # Environment management
            "environments",

            # Reporting
            "reports",
            "logs",
            "screenshots",
            "videos",
            "test-results",

            # DevOps
            ".github/workflows",
            "docker",
            "scripts"
        ],

        "files": [

            {
                "path": "README.md",
                "type": "readme"
            },

            {
                "path": "playwright.config.ts",
                "type": "playwright_config"
            },

            {
                "path": "package.json",
                "type": "package_json"
            },

            {
                "path": "tsconfig.json",
                "type": "tsconfig"
            },

            {
                "path": ".gitignore",
                "type": "gitignore"
            },

            {
                "path": "src/pages/base.page.ts",
                "type": "base_page"
            },

            {
                "path": "src/utils/logger.ts",
                "type": "logger"
            },

            {
                "path": "src/api/api.client.ts",
                "type": "api_client"
            },

            {
                "path": "src/hooks/test.hooks.ts",
                "type": "hooks"
            },

            {
                "path": "src/fixtures/test.fixture.ts",
                "type": "fixture"
            },

            {
                "path": ".github/workflows/playwright.yml",
                "type": "github_actions"
            },

            {
                "path": "docker/docker-compose.yml",
                "type": "docker"
            },

            {
                "path": "environments/qa.env",
                "type": "env"
            },

            {
                "path": "environments/stage.env",
                "type": "env"
            },

            {
                "path": "environments/prod.env",
                "type": "env"
            }
        ]
    }

    return architecture

