from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from llm_router import route_question, memory_store, reset_memory, get_llm_info
from pydantic import BaseModel
import json
import os
from datetime import datetime

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

class AskRequest(BaseModel):
    question: str
    llm: str = "auto"

@app.post("/ask")
async def ask(request: AskRequest, req: Request):
    enforce = req.query_params.get('tone') == 'strict'
    answer = route_question(request.question, request.llm, enforce_tone=enforce)
    log_interaction(request.llm, request.question, answer)
    return {"response": answer}

@app.get("/test")
def test():
    return {
        "status": "ok",
        "llms": list(memory_store.keys()),
        "memory": {k: len(v) for k, v in memory_store.items()},
        "docs": get_llm_info()
    }

@app.get("/reset-memory")
def reset():
    reset_memory()
    return {"status": "reset"}


def log_interaction(llm, question, answer):
    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "llm": llm,
        "question": question,
        "answer": answer
    }
    os.makedirs("logs", exist_ok=True)
    logfile = f"logs/history_{datetime.utcnow().date()}.jsonl"
    if os.path.exists(logfile) and os.path.getsize(logfile) > 5_000_000:
        os.rename(logfile, logfile.replace(".jsonl", "_archived.jsonl"))
    with open(logfile, "a") as f:
        f.write(json.dumps(log) + "\n")

    log = {
        "timestamp": datetime.utcnow().isoformat(),
        "llm": llm,
        "question": question,
        "answer": answer
    }
    os.makedirs("logs", exist_ok=True)
    with open("logs/history.jsonl", "a") as f:
        f.write(json.dumps(log) + "\n")
@app.get("/status")
def status():
    return {
        "llms": list(memory_store.keys()),
        "memory_preview": {k: v[-3:] for k, v in memory_store.items() if v},
        "logs": len(open("logs/history.jsonl").readlines()) if os.path.exists("logs/history.jsonl") else 0,
        "docs": get_llm_info()
    }
@app.get("/selftest")
def selftest():
    test_prompts = {
        "EmergencyLLM": "Power outage in Bay 2. What do I do?",
        "BookingLLM": "How do I refund a booking?",
        "TrackManLLM": "Launch monitor isn’t connecting.",
        "ResponseToneLLM": "Rewrite: Sorry about that. We’ll fix it soon.",
        "VanillaLLM": "What is the ClubOS Lite system?"
    }
    results = {}
    for llm, q in test_prompts.items():
        results[llm] = route_question(q, llm)
    return results
@app.post("/reload-docs")
async def reload_docs_endpoint(request: Request):
    verify_token(request)
    body = await request.json()
    llm = body.get("llm")
    return reload_docs(llm)
@app.get("/docs-list")
def docs_list(request: Request):
    verify_token(request)
    return {name: obj.doc for name, obj in LLM_MAP.items()}
@app.get("/slack-test")
def slack_test(request: Request):
    verify_token(request)
    from utils.slack_notify import send_slack_ping
    send_slack_ping("TEST", "🚨 ClubOS Lite test ping triggered manually")
    return {"status": "sent"}