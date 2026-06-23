from pydantic import BaseModel
from typing import Dict,List


class FixOutput(BaseModel):
    modified_files: List[str]
    summary: str