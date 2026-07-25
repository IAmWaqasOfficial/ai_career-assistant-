# 🤖 AI Career Assistant Backend

An AI-powered career assistant backend built with **FastAPI** and **Google Gemini AI**.

The system generates personalized career roadmaps and performs skill gap analysis based on a user's target role, current skills, and learning duration.

---

## ✨ Features

- 🔐 User registration and authentication
- 🧠 AI-powered career roadmap generation
- 🗺️ Personalized learning plans
- 📊 Skill gap analysis
- 🎯 Target-role-based career analysis
- 💾 Save generated career roadmaps
- 📚 Retrieve saved roadmaps
- 🗄️ PostgreSQL database integration
- ⚡ RESTful API architecture
- 📖 Interactive API documentation with Swagger UI

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Backend programming language |
| ⚡ FastAPI | Web framework for building APIs |
| 🧠 Google Gemini AI | AI-powered career analysis and roadmap generation |
| 🐘 PostgreSQL | Relational database |
| 🗃️ SQLAlchemy | Database ORM |
| ✅ Pydantic | Data validation and schemas |
| 🔑 JWT | Authentication and authorization |
| 🚀 Uvicorn | ASGI server |

---

## 📁 Project Structure

```text
AI-Career-Assistant/
│
├── app/
│   ├── ai/
│   │   └── llm.py              # Gemini AI integration
│   │
│   ├── routers/
│   │   ├── auth.py             # Authentication endpoints
│   │   ├── roadmap.py          # Career roadmap endpoints
│   │   └── skill_gap.py        # Skill gap analysis endpoints
│   │
│   ├── crud.py                 # Database operations
│   ├── database.py             # Database configuration
│   ├── main.py                 # FastAPI application entry point
│   ├── models.py               # SQLAlchemy database models
│   ├── schemas.py              # Pydantic schemas
│   └── security.py             # Authentication and security utilities
│
├── .env.example                # Environment variable template
├── .gitignore                  # Git ignored files
├── README.md                   # Project documentation
└── requirements.txt            # Python dependencies
