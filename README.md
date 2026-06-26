# EduGenie – AI Powered Learning Assistant

Google Gemini powered educational assistant built with **FastAPI**, **Jinja2**, and vanilla HTML/CSS/JS.

## Features

- **Question Answering** – direct answer, explanation, extra learning points
- **Topic Explanation** – definition, simple explanation, example, key points
- **Interactive Quiz** – create MCQs, answer them, submit for score & review
- **Summarization** – short summary, key points, important concepts
- **Learning Path** – beginner → intermediate → advanced roadmap with resources

## Local Setup

```bash
cd EduGenie
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Copy `.env.example` to `.env` and set your Gemini API key:

```
GEMINI_API_KEY=your_key_here
GEMINI_MODEL=gemini-2.5-flash
```

## Run Locally

```bash
uvicorn main:app --reload
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## Deployed Website Link

open [https://edugenie-k4z7.onrender.com/](Edugenie)

or 

open [https://edugenie-opal.vercel.app/](Edugenie)



## API Endpoints

| Method | Endpoint | Body |
|--------|----------|------|
| GET | `/` | Homepage |
| GET | `/qa`, `/explain`, `/quiz`, `/summarize`, `/learning-path` | Feature pages |
| POST | `/qa` | `{ "question": "..." }` |
| POST | `/explain` | `{ "topic": "..." }` |
| POST | `/quiz` | `{ "topic_or_text": "...", "num_questions": 5 }` |
| POST | `/quiz/submit` | `{ "quiz_id": "...", "answers": ["A","B",...] }` |
| POST | `/summarize` | `{ "text": "..." }` |
| POST | `/learn/recommendations` | `{ "topic": "..." }` |

## Sample Test Inputs

- **QnA:** "What is photosynthesis?"
- **Explain:** "Recursion in programming"
- **Quiz:** "Python lists and dictionaries"
- **Summarize:** Paste any educational paragraph (10+ chars)
- **Learning Path:** "Machine Learning"

## Project Structure

```
EduGenie/
├── main.py
├── config.py / utils.py / schemas.py
├── qna.py / explanation_module.py / quiz_module.py
├── summary_module.py / learning_path.py
├── templates/          # Jinja2 pages
├── static/             # CSS + JS
├── Dockerfile          # Docker deploy
├── render.yaml         # Render.com deploy
├── docker-compose.yml
├── Procfile            # Railway / Heroku
├── requirements.txt
└── .env                # local only — never commit
```
