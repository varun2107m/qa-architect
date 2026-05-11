NORMALIZATION_MAP = {

    "architecture_pattern": {

        "Page Object Model": "pom",
        "page object model": "pom",

        "POM": "pom",
        "pom": "pom",

        "enterprise": "pom",
        "Enterprise": "pom",

        "enterprise level": "pom",
        "Enterprise Level": "pom"
    },

    "framework": {

        "Playwright": "playwright",
        "playwright": "playwright",

        "Selenium": "selenium",
        "selenium": "selenium",

        "Cypress": "cypress",
        "cypress": "cypress"
    },

    "language": {

        "TypeScript": "typescript",
        "typescript": "typescript",

        "JavaScript": "javascript",
        "javascript": "javascript",

        "Python": "python",
        "python": "python",

        "Java": "java",
        "java": "java"
    },

    "capability": {

        "retries": "retries",
        "retry": "retries",

        "reporting": "reporting",

        "screenshots": "screenshots",

        "parallel execution": "parallel_execution",

        "api testing": "api_testing",

        "fixtures": "fixtures",

        "hooks": "hooks",

        "docker": "docker",

        "ci/cd": "cicd",

        "tagging": "tagging"
    },

    "integration": {

        "Docker": "docker",
        "docker": "docker",

        "Jenkins": "jenkins",
        "jenkins": "jenkins",

        "GitHub Actions": "github_actions",
        "github actions": "github_actions"
    }
}


def normalize_value(
    category,
    value
):

    if value is None:
        return value

    mapping = NORMALIZATION_MAP.get(
        category,
        {}
    )

    normalized = mapping.get(
        value,
        value
    )

    if (
        category == "architecture_pattern"
        and normalized == value
    ):

        normalized = "pom"

    print(
        f"NORMALIZING [{category}] "
        f"{value} -> {normalized}"
    )

    return normalized
