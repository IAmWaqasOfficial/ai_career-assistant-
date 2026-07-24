from sqlalchemy.orm import Session

from app import models, schemas
from app.security import hash_password, verify_password


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):

    hashed_password = hash_password(user.password)

    new_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def login_user(db: Session, user: schemas.UserLogin):

    existing_user = get_user_by_email(db, user.email)

    if existing_user is None:
        return None

    if not verify_password(user.password, existing_user.password):
        return None

    return existing_user

def create_roadmap(db: Session, roadmap: schemas.RoadmapCreate, generated_text: str):

    new_roadmap = models.Roadmap(
        user_id=roadmap.user_id,
        target_role=roadmap.target_role,
        current_skills=roadmap.current_skills,
        duration=roadmap.duration,
        generated_roadmap=generated_text
    )

    db.add(new_roadmap)
    db.commit()
    db.refresh(new_roadmap)

    return new_roadmap


def get_all_roadmaps(db: Session, user_id: int):
    return db.query(models.Roadmap).filter(
        models.Roadmap.user_id == user_id
    ).all()


def get_roadmap_by_id(db: Session, roadmap_id: int):
    return db.query(models.Roadmap).filter(
        models.Roadmap.id == roadmap_id
    ).first()


def delete_roadmap(db: Session, roadmap_id: int):

    roadmap = get_roadmap_by_id(db, roadmap_id)

    if roadmap is None:
        return None

    db.delete(roadmap)
    db.commit()

    return roadmap