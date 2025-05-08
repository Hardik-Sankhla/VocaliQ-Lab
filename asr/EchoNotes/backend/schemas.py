# backend/schemas.py
from pydantic import BaseModel

class AudioProcessResponse(BaseModel):
    transcript: str
    summary: str
    action_items: str