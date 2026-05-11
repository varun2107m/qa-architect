from pydantic import BaseModel
from typing import Dict, Any


class Capability(BaseModel):

    name: str

    enabled: bool = True

    config: Dict[str, Any] = {}
    