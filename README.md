QA Architect AI

AI-powered enterprise QA automation framework generator with:

VS Code Extension
FastAPI backend
Enterprise framework scaffolding
Playwright architecture generation
Features
Generate enterprise QA framework structures
VS Code command integration
Playwright + TypeScript scaffolding
API testing support
Hooks and fixtures support
Reporting structure
Docker and CI/CD folders
Reusable utilities and enterprise architecture
Project Structure
qa-architect/
│
├── backend/
│
├── vscode-extension/
│
├── templates/
│
├── generated/
│
└── README.md
Prerequisites

Install:

Python 3.10+
Node.js 18+
VS Code
npm
Setup Instructions
1. Clone Repository
git clone https://github.com/varun2107m/qa-architect.git

cd qa-architect
2. Setup Backend
cd backend

python3 -m venv venv

source venv/bin/activate

Install dependencies:

pip install -r requirements.txt
3. Configure Environment Variables

Create:

backend/.env

Add:

OPENAI_API_KEY=your_openai_key_here
4. Start Backend Server

From project root:

cd ~/Desktop/qa-architect

source backend/venv/bin/activate

uvicorn backend.app.api.main:app --port 8001

Expected:

Uvicorn running on http://127.0.0.1:8001

Keep terminal running.

5. Setup VS Code Extension

Open NEW terminal:

cd vscode-extension

Install dependencies:

npm install

Compile extension:

npm run compile
6. Configure VS Code Debugging

Create:

vscode-extension/.vscode/launch.json

Add:

{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Run QA Architect Extension",
      "type": "extensionHost",
      "request": "launch",
      "runtimeExecutable": "/Applications/Visual Studio Code.app/Contents/MacOS/Electron",
      "args": [
        "--extensionDevelopmentPath=${workspaceFolder}"
      ],
      "outFiles": [
        "${workspaceFolder}/dist/**/*.js"
      ]
    }
  ]
}
7. Run Extension

Open ONLY:

qa-architect/vscode-extension

in VS Code.

Go to:

Run → Start Debugging

Select:

Run QA Architect Extension

This opens:

Extension Development Host
8. Generate Framework

Inside Extension Development Host:

Cmd + Shift + P

Run:

Generate QA Framework

Example prompt:

Generate enterprise Playwright framework with API testing, hooks, fixtures, docker and reporting
Generated Framework Location

Frameworks are generated in:

generated/test-framework
Enterprise Structure Generated
src/
  api/
  pages/
  hooks/
  fixtures/
  services/
  validations/
  models/
  locators/
  factories/
  utils/
  helpers/
  config/
  constants/
  data/
  tests/

reports/
logs/
screenshots/
videos/
test-results/

.github/workflows/
docker/
scripts/
Current Status

Current version supports:

Enterprise folder scaffolding
Playwright framework generation
Extension-triggered generation
Backend orchestration
