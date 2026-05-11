from backend.app.core.registry_loader import (
    load_frameworks,
    load_languages
)

frameworks = load_frameworks()

languages = load_languages()

print("\n=== Frameworks ===\n")
print(frameworks)

print("\n=== Languages ===\n")
print(languages)
