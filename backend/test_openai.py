from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv("backend/.env")

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "hello"
        }
    ]
)

print(response.choices[0].message.content)
