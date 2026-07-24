from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import engine, Base
from app import models
from app.routers import auth, roadmap
from app.routers import auth, roadmap, skill_gap

# Create database tables
Base.metadata.create_all(bind=engine)

# Create FastAPI app
app = FastAPI(title="AI Career Assistant API")

# -----------------------------
# CORS Configuration
# -----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Development Only)
    allow_credentials=True,
    allow_methods=["*"],  # Allow GET, POST, PUT, DELETE, OPTIONS
    allow_headers=["*"],  # Allow all headers
)

# Register Routers
app.include_router(auth.router)
app.include_router(roadmap.router)
app.include_router(skill_gap.router, prefix="/skill-gap", tags=["Skill Gap"])

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to AI Career Assistant API"
    }