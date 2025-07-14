import os
import openai
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

def call_llm(model: str, prompt: str, stream: bool = False) -> str:
    try:
        if stream:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1000,
                stream=True
            )
            chunks = [chunk["choices"][0]["delta"].get("content", "") for chunk in response if "choices" in chunk]
            return "".join(chunks).strip()
        else:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=1000,
            )
            return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"[LLM error: {e}]"