import json

from fastapi import APIRouter, HTTPException

from app.schemas import SkillGapRequest, SkillGapResponse
from app.ai.llm import analyze_skill_gap

router = APIRouter()


@router.post("/analyze", response_model=SkillGapResponse)
def analyze(request: SkillGapRequest):
    try:
        # Get response from Gemini
        result = analyze_skill_gap(
            target_role=request.target_role,
            current_skills=request.current_skills
        )

        # Convert JSON string to Python dictionary
        data = json.loads(result)

        # Return validated response
        return SkillGapResponse(**data)

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Skill Gap Analysis Failed: {str(e)}"
        )