# QA Architect - AI Agent Instructions

## Project Overview
QA Architect is an AI-powered QA automation framework generator that converts natural language requirements into complete, production-ready test automation frameworks. It supports multiple frameworks (Playwright, Selenium, Cypress), languages (TypeScript, JavaScript, Python, Java), and architecture patterns (POM, Screenplay).

## Architecture
Multi-stage processing pipeline:
1. VS Code extension captures user requirements
2. FastAPI backend processes via AI agents (OpenAI GPT-4o)
3. Framework composition from YAML registries and Jinja2 templates
4. File generation creates complete project structures

## Development Setup
- Backend requires Python 3.14+ with venv at `/backend/venv/`
- Install dependencies: `pip install fastapi uvicorn openai pydantic jinja2 pyyaml python-dotenv`
- Set `OPENAI_API_KEY` in `.env` file
- Run from workspace root to ensure correct Python paths

## Build and Test Commands
- **Backend server**: `cd backend && uvicorn app.api.main:app --host 127.0.0.1 --port 8001 --reload`
- **Backend tests**: Run individual `python test_*.py` files in `/backend/`
- **VS Code extension**: `cd vscode-extension && npm install && npm run compile`

## Coding Conventions
- **Python**: Use Pydantic BaseModel for data validation, normalize inputs via `core/normalizer.py`, multi-line function signatures
- **YAML**: Registry files in `/registry/` with consistent structure (name, type, languages, supports, etc.)
- **Jinja2**: Templates in `/templates/` with `trim_blocks=True, lstrip_blocks=True`
- **Error handling**: Try/except with traceback.print_exc() and HTTPException for API routes

## Key Files and Patterns
- [backend/app/agents/orchestration_agent.py](backend/app/agents/orchestration_agent.py) - Main AI pipeline coordinator
- [shared/dsl/framework_spec.py](shared/dsl/framework_spec.py) - Core data models (Pydantic)
- [backend/app/core/normalizer.py](backend/app/core/normalizer.py) - Input normalization mappings
- [backend/app/generator/renderer.py](backend/app/generator/renderer.py) - Jinja2 template rendering
- [registry/frameworks/playwright.yaml](registry/frameworks/playwright.yaml) - Framework registry example
- [templates/common/README.md.j2](templates/common/README.md.j2) - Jinja2 template example

## Common Pitfalls
- Always normalize user inputs through `normalizer.py` to avoid lookup failures
- Verify registry YAML matches template files to prevent generation errors
- Backend must run on port 8001 for VS Code extension communication
- Run Python commands from workspace root or set PYTHONPATH correctly
- Ensure `.env` file exists with valid OPENAI_API_KEY

## Documentation
- API documentation auto-generated at `http://127.0.0.1:8001/docs` when backend runs
- Generated framework examples in `/generated/` demonstrate output structure
- Registry YAML files are self-documenting through their structure</content>
<parameter name="filePath">/Users/varunmalhotra/Desktop/qa-architect/AGENTS.md