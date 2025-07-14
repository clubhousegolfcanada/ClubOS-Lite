from utils.llm_client import call_llm
from utils.embedder import get_chunks, get_top_chunks

class ClubhouseInfoLLM:
    def __init__(self):
        self.name = "ClubhouseInfoLLM"
        self.prompt = """You are the internal knowledge source for Clubhouse 24/7 Golf. Answer clearly and concisely using the latest internal SOPs, policies, tech, and tone. Reference documents when needed."""
        self.doc = "backend/documents/clubhouse_sop_full.md"
        self.chunks = []
        self.reload()

    def reload(self):
        try:
            with open(self.doc, "r") as f:
                text = f.read()
            self.chunks = get_chunks(text)
        except:
            self.chunks = ["[Document not found]"]

    def ask(self, question, stream=False):
        context = self.search_context(question)
        full_prompt = f"{self.prompt}\n\n{context}\n\nUser: {question}"
        return call_llm("gpt-4o", full_prompt, stream=stream)

    def search_context(self, question):
        top_chunks = get_top_chunks(question, self.chunks)
        return "\n\n".join(top_chunks)