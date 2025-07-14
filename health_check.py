import os
from dotenv import load_dotenv
from backend.wrappers import emergency_llm, booking_llm, trackman_llm, response_tone_llm, vanilla_llm
from backend.utils.embedder import model as embedding_model

load_dotenv()

def check_api_key():
    return "OPENAI_API_KEY" in os.environ and os.environ["OPENAI_API_KEY"].startswith("sk-")

def check_documents():
    docs = [
        "backend/documents/emergency_protocol.md",
        "backend/documents/booking_flow_v3.md",
        "backend/documents/trackman_ops_manual.md",
        "backend/documents/tone_rules.md",
        "backend/documents/vanilla.md"
    ]
    return all(os.path.exists(doc) for doc in docs)

def check_wrappers():
    try:
        _ = emergency_llm.EmergencyLLM()
        _ = booking_llm.BookingLLM()
        _ = trackman_llm.TrackManLLM()
        _ = response_tone_llm.ResponseToneLLM()
        _ = vanilla_llm.VanillaLLM()
        return True
    except:
        return False

def check_embedding_model():
    try:
        _ = embedding_model.encode(["test"])
        return True
    except:
        return False

if __name__ == "__main__":
    print("🔍 Running Health Check...")
    print("✅ API Key Loaded:" if check_api_key() else "❌ API Key Missing or Invalid")
    print("✅ Documents Found:" if check_documents() else "❌ Missing Documents")
    print("✅ Wrappers Load:" if check_wrappers() else "❌ Wrapper Init Failed")
    print("✅ Embedding Model Ready:" if check_embedding_model() else "❌ Embedding Model Failed")