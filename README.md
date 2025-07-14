# ClubOS Lite

ClubOS Lite is a modular, role-based LLM switchboard for operational triage, tone control, and SOP reference.  
Built for internal automation and lightweight execution — not bloated apps or generic AI chat.

## 🔧 Key Features

- ✅ FastAPI backend with 5 GPT-4o LLM wrappers
- ✅ SOP document embeddings + contextual search
- ✅ Role-based logic for Booking, Emergency, TrackMan, etc.
- ✅ Endpoint memory, self-test, logs, and doc reload
- ✅ Auth token protection (`?auth=dev123`)
- ✅ Claude Opus 4–ready structure
- ✅ Deploy via `bash deploy.sh` or Docker

## 📦 File Structure

- `backend/`: All app logic (wrappers, router, utils)
- `frontend/`: Basic UI (can be replaced with ClubOS frontend)
- `deploy.sh`: One-line install + run
- `docker-compose.yml`: Optional containerization
- `project.json`: Claude-readable system manifest
- `.env`: OpenAI API keys (excluded from Git)

## 🧪 Dev Endpoints

- `/ask?auth=dev123` – Ask a question to a routed LLM
- `/test` – Check memory + LLMs
- `/status` – Live usage/log/memory
- `/reload-docs` – Re-embed SOPs without restarting
- `/selftest` – Sample queries to verify behavior
- `/docs-list` – Lists attached docs per LLM

---

## 🚀 Deployment

```bash
bash deploy.sh
# OR
docker-compose up --build
```

Open your browser at http://localhost:8000

---

## 🧠 Claude: Next Steps

Replace `frontend/index.html` with ClubOS custom UI if desired.  
Enable streaming on frontend (backend is ready).  
Or build lightweight admin panel for SOP state and logs.

---

Built for internal ops. Not customer-facing junk.