from pydantic import BaseModel


class ExecutionSpec(BaseModel):

    parallel: bool = False

    retries: int = 0

    headless: bool = True

    timeout: int = 30000
    