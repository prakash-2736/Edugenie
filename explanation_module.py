from typing import Any

from utils import call_gemini, parse_gemini_json


def explain_topic(topic: str) -> dict[str, Any]:
    prompt = f"""You are EduGenie, a friendly educational assistant for students.

Explain the following topic/concept in a beginner-friendly way.
Return ONLY valid JSON with this exact structure (no markdown fences):
{{
  "definition": "A clear one-sentence definition",
  "simple_explanation": "An easy-to-understand explanation in simple language",
  "example": "A practical example that helps understanding",
  "key_points": ["point 1", "point 2", "point 3", "point 4"]
}}

Topic: {topic}"""

    raw = call_gemini(prompt)
    return parse_gemini_json(raw)
