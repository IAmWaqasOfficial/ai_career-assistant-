import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_roadmap(target_role, current_skills, duration):

    prompt = f"""
You are an AI career coach.

Create a short and structured learning roadmap.

Target Role:
{target_role}

Current Skills:
{current_skills}

Duration:
{duration}

Rules:
- Keep the response concise.
- Use months and bullet points.
- No long explanations.
- Focus on technologies, concepts, and projects.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


def analyze_skill_gap(target_role, current_skills):

    prompt = f"""
You are an expert AI career coach.

Analyze the user's current skills against the target role.

Target Role:
{target_role}

Current Skills:
{current_skills}

Return ONLY valid JSON.

Use this exact structure:

{{
  "match_percentage": 0,
  "existing_skills": [],
  "missing_skills": [],
  "estimated_time": "",
  "advice": "",
  "improvements": []
}}

Rules:
- Do not return markdown.
- Do not use ```json.
- Do not explain anything outside the JSON.
- match_percentage must be between 0 and 100.
- existing_skills should contain only skills the user already has.
- missing_skills should contain only missing skills.
- estimated_time should be realistic.
- advice should be short (2-3 sentences).
- improvements should contain 3-5 practical suggestions.
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text