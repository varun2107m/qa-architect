import os
import json
import re

from openai import OpenAI
from dotenv import load_dotenv

from backend.app.agents.prompt_builder import (
    SYSTEM_PROMPT
)

load_dotenv("backend/.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def extract_json(content):

    content = content.strip()

    content = re.sub(
        r"```json",
        "",
        content
    )

    content = re.sub(
        r"```",
        "",
        content
    )

    content = content.strip()

    start = content.find("{")

    end = content.rfind("}")

    if start == -1 or end == -1:
        raise ValueError(
            "No JSON found in response"
        )

    return content[start:end + 1]


def analyze_requirements(
    user_prompt
):

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0
    )

    content = (
        response
        .choices[0]
        .message
        .content
    )

    cleaned_json = extract_json(
        content
    )

    return json.loads(
        cleaned_json
    )

