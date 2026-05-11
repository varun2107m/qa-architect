import os

from backend.app.engine.ai_architect_engine import build_architecture
from backend.app.generator.file_writer import write_file
from backend.app.generator.renderer import render_template


def generate_inline_file(file_type):

    templates = {

        "base_page": """import { Page } from '@playwright/test';

export class BasePage {
    constructor(protected page: Page) {}

    async navigate(url: string) {
        await this.page.goto(url);
    }
}
""",

        "config": """import { defineConfig } from '@playwright/test';

export default defineConfig({
    testDir: './src/tests',
    use: {
        screenshot: 'only-on-failure',
        video: 'retain-on-failure'
    },
    retries: 2
});
""",

        "docker": """version: '3.8'

services:
  tests:
    image: node:18
    working_dir: /app
    volumes:
      - .:/app
    command: npm test
""",

        "api_client": """import axios from 'axios';

export class ApiClient {
    get(url: string) {
        return axios.get(url);
    }

    post(url: string, data: any) {
        return axios.post(url, data);
    }
}
""",

        "auto_readme": """# Generated QA Framework

This framework was generated using AI Architect Mode.

## Features
- Playwright UI Automation
- API Testing Support
- Modular Architecture
- CI/CD Ready
"""
    }

    return templates.get(file_type, "")


def generate_framework(spec, output_dir):

    os.makedirs(output_dir, exist_ok=True)

    architecture = build_architecture(spec)

    # Create folders
    for folder in architecture["folders"]:

        os.makedirs(
            os.path.join(output_dir, folder),
            exist_ok=True
        )

    # Create files
    for file in architecture["files"]:

        path = file["path"]
        file_type = file["type"]

        content = generate_inline_file(file_type)

        write_file(
            os.path.join(output_dir, path),
            content
        )

    return {
        "status": "success",
        "mode": "AI_ARCHITECT_MODE"
    }


