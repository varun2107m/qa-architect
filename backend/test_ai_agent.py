from backend.app.agents.orchestration_agent import (
    generate_from_prompt
)


prompt = """
Generate a scalable Playwright framework using TypeScript.

Include:
- retries
- reporting
- docker
- web automation
- pom architecture
"""

result = generate_from_prompt(
    prompt,
    "generated/ai-framework"
)

print("\n=== AI RESULT ===\n")

print(result)
