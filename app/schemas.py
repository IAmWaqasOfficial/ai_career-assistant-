from typing import List

from pydantic import BaseModel
from datetime import datetime


# ---------- User Schemas ----------

class UserCreate(BaseModel):
    name: str
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True


# ---------- Roadmap Schemas ----------

class RoadmapCreate(BaseModel):
    user_id: int
    target_role: str
    current_skills: str
    duration: str
    generated_content: str | None = None


class RoadmapResponse(BaseModel):
    id: int
    user_id: int
    target_role: str
    current_skills: str
    duration: str
    generated_roadmap: str
    created_at: datetime

    class Config:
        from_attributes = True



class SkillGapRequest(BaseModel):
    target_role: str
    current_skills: str


class SkillGapResponse(BaseModel):
    match_percentage: int
    existing_skills: List[str]
    missing_skills: List[str]
    estimated_time: str
    advice: str
    improvements: List[str]