from pydantic import BaseModel
from typing import Dict, Any


class Integration(BaseModel):

    name: str

    config: Dict[str, Any] = {}
    