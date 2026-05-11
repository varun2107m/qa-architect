from pydantic import BaseModel


class PromptRequest(BaseModel):

    prompt: str

    output_dir: str = "generated/api-framework"