import os
from dotenv import load_dotenv
from backend.main import app
from backend.llm_router import get_llm_info

def bootstrap(env="development"):
    print(f"🚀 Bootstrapping ClubOS Lite [{env}]")

    # Load API Key
    load_dotenv()
    if not os.getenv("OPENAI_API_KEY"):
        print("❌ Missing OPENAI_API_KEY in .env")
        return

    # Check doc status
    docs = get_llm_info()
    print("📄 Document Load Status:")
    for name, status in docs.items():
        print(f" - {name}: {status}")

    # Print health endpoint trigger
    print("\nReady. Run: python health_check.py")

if __name__ == "__main__":
    bootstrap()