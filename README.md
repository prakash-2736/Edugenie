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

## Deploy & Get a Demo Link

You need a **public URL** for Skillwallet / mentor demos. Here are the best free options:

### Option 1: Render.com (Recommended — Free, Permanent Link)

Best for student projects. Gives you a URL like `https://edugenie.onrender.com`.

1. Push your project to **GitHub** (do NOT commit `.env` — it's gitignored)
2. Go to [render.com](https://render.com) → Sign up → **New +** → **Web Service**
3. Connect your GitHub repo
4. Settings:
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan:** Free
5. Add **Environment Variables:**
   - `GEMINI_API_KEY` = your key
   - `GEMINI_MODEL` = `gemini-2.5-flash`
6. Click **Deploy**

Or use the included `render.yaml` — on Render choose **New Blueprint** and point to your repo.

> Free tier sleeps after 15 min idle. First load may take ~30 seconds to wake up.

---

### Option 2: Railway.app (Easy, Free Credits)

1. Go to [railway.app](https://railway.app) → New Project → Deploy from GitHub
2. Add env vars: `GEMINI_API_KEY`, `GEMINI_MODEL`
3. Railway auto-detects Python. Set start command:
   ```
   uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
4. Generate a public domain in **Settings → Networking**

---

### Option 3: Hugging Face Spaces (Good for AI Demos)

1. Create a new **Docker Space** at [huggingface.co/spaces](https://huggingface.co/spaces)
2. Upload project files or connect Git repo
3. The included `Dockerfile` works out of the box
4. Add `GEMINI_API_KEY` as a **Space Secret** (Settings → Secrets)
5. Your demo link: `https://huggingface.co/spaces/YOUR_USERNAME/edugenie`

---

### Option 4: Quick Temporary Demo (ngrok — 2 minutes)

For instant demo during a presentation without deploying:

```bash
# Terminal 1 — run app
source .venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000

# Terminal 2 — expose to internet
ngrok http 8000
```

ngrok gives a temporary URL like `https://abc123.ngrok-free.app` (valid while your PC is running).

Install ngrok: [ngrok.com/download](https://ngrok.com/download)

---

### Option 5: Docker (Any VPS / Cloud)

```bash
docker build -t edugenie .
docker run -p 8000:8000 -e GEMINI_API_KEY=your_key edugenie
```

Or with docker-compose:

```bash
# Make sure .env has GEMINI_API_KEY
docker compose up --build
```

Works on AWS EC2, DigitalOcean, Google Cloud VM, etc.

---

## Deployment Checklist

| Step | Action |
|------|--------|
| 1 | Push code to GitHub (exclude `.env`) |
| 2 | Set `GEMINI_API_KEY` as env var on hosting platform |
| 3 | Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT` |
| 4 | Test all 5 features on the live URL |
| 5 | Share demo link in your project report / Skillwallet |

---

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
