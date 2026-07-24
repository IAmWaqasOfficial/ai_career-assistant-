from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.ai.llm import generate_roadmap
from app.database import get_db
from app import crud, schemas

router = APIRouter(
    prefix="/roadmaps",
    tags=["Roadmaps"]
)



@router.post("/generate")
def generate_roadmap_api(
    roadmap: schemas.RoadmapCreate
):
    generated_text = generate_roadmap(
        roadmap.target_role,
        roadmap.current_skills,
        roadmap.duration
    )

    return {
        "generated_content": generated_text
    }

@router.post("/save", response_model=schemas.RoadmapResponse)
def save_roadmap_api(
    roadmap: schemas.RoadmapCreate,
    db: Session = Depends(get_db)
):
    return crud.create_roadmap(
        db,
        roadmap,
        roadmap.generated_content
    )



@router.get("/{user_id}", response_model=list[schemas.RoadmapResponse])
def get_user_roadmaps(
    user_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_all_roadmaps(db, user_id)


# ---------------- Get Single Roadmap ----------------

@router.get("/detail/{roadmap_id}", response_model=schemas.RoadmapResponse)
def get_roadmap(
    roadmap_id: int,
    db: Session = Depends(get_db)
):
    roadmap = crud.get_roadmap_by_id(db, roadmap_id)

    if roadmap is None:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found"
        )

    return roadmap


# ---------------- Delete Roadmap ----------------

@router.delete("/{roadmap_id}")
def delete_roadmap(
    roadmap_id: int,
    db: Session = Depends(get_db)
):
    roadmap = crud.delete_roadmap(db, roadmap_id)

    if roadmap is None:
        raise HTTPException(
            status_code=404,
            detail="Roadmap not found"
        )

    return {
        "message": "Roadmap deleted successfully"
    }