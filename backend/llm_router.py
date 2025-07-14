from wrappers import WRAPPERS
from utils.slack_notify import send_slack_ping
from wrappers.booking_llm import BookingLLM
from wrappers.trackman_llm import TrackManLLM
from wrappers.response_tone_llm import ResponseToneLLM
from wrappers.vanilla_llm import VanillaLLM

LLM_MAP = {
    "EmergencyLLM": EmergencyLLM(),
    "BookingLLM": BookingLLM(),
    "TrackManLLM": TrackManLLM(),
    "ResponseToneLLM": ResponseToneLLM(),
    "VanillaLLM": VanillaLLM()
}

KEYWORDS = {
    "power": "EmergencyLLM",
    "wifi": "EmergencyLLM",
    "refund": "BookingLLM",
    "promo": "BookingLLM",
    "trackman": "TrackManLLM",
    "rewrite": "ResponseToneLLM",
    "tone": "ResponseToneLLM"
}

memory_store = {name: [] for name in LLM_MAP}

def route_question(text: str, llm: str, stream: bool = False, enforce_tone: bool = False):
    selected = ''
    selected = ""
    if llm == "SelectorLLM":
        for keyword, mapped_llm in KEYWORDS.items():
            if keyword in text.lower():
                selected = mapped_llm
                break
        selected = selected or "ClubhouseInfoLLM"
    else:
        selected = llm

    memory_store[selected].append(text)
    output = LLM_MAP[selected].ask(text, stream=stream)
    if enforce_tone: output = ResponseToneLLM().ask(output)
    return output

def reset_memory():
    for key in memory_store:
        memory_store[key] = []

def get_llm_info():
    out = {}
    for name, obj in LLM_MAP.items():
        try:
            with open(obj.doc, "r") as f:
                out[name] = f"{len(f.read().split())} words"
        except:
            out[name] = "doc not found"
    return out

def reload_docs(target=None):
    if target:
        if target in LLM_MAP:
            LLM_MAP[target].reload()
            return {target: "reloaded"}
        return {"error": f"LLM not found: {target}"}
    for name in LLM_MAP:
        LLM_MAP[name].reload()
    return {"status": "all reloaded"}
