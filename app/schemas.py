from pydantic import BaseModel
from typing import Optional

class GenerateRequest(BaseModel):
    prompt: str
    character: Optional[str] = None
    style: Optional[str] = None
    model_name: str = "dummy"
    seed: int = 42

class JobResponse(BaseModel):
    job_id: str
    status: str
