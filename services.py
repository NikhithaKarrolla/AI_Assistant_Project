# services.py
import os
import json
import datetime
from dotenv import load_dotenv

# Load .env
load_dotenv()

# Groq SDK
from groq import Groq

# Config
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = os.getenv("MODEL", "llama-3.1-8b-instant")
FEEDBACK_FILE = "feedback.json"

if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY is not set. Add it to .env or your environment variables.")

# Initialize client
client = Groq(api_key=GROQ_API_KEY)

def _build_prompt(function, payload):
    """Constructs a simple instruction prompt depending on chosen function."""
    if function == "answer":
        return f"Answer the following question clearly and concisely:\n\n{payload.get('question','')}"
    if function == "summarize":
        # keep short, prefer bullets
        return f"Summarize the following text in 2-4 bullet points or 2-3 sentences:\n\n{payload.get('text','')}"
    if function == "create":
        return f"Create a creative piece based on this prompt:\n\n{payload.get('prompt','')}\n\nMake it engaging."
    if function == "advice":
        return f"Provide practical, step-by-step advice on this topic:\n\n{payload.get('topic','')}"
    return "Invalid function."

def run_function(function, payload, temperature=0.7, max_tokens=512):
    """
    Calls Groq chat completion and returns a dict:
      { "output": "...", "variant": MODEL }
    """
    prompt = _build_prompt(function, payload)

    try:
        resp = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens   # ✅ FIXED
        )
        # Extract text (Groq SDK uses a similar shape to OpenAI)
        output = resp.choices[0].message.content
    except Exception as e:
        # Friendly error message returned to app
        output = f"[Error] Groq API request failed: {e}"

    return {"output": output, "variant": MODEL}

def log_feedback(entry):
    """Append feedback entry to feedback.json"""
    data = []
    if os.path.exists(FEEDBACK_FILE):
        try:
            with open(FEEDBACK_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception:
            data = []

    entry_copy = dict(entry)
    entry_copy.setdefault("timestamp", datetime.datetime.utcnow().isoformat())
    data.append(entry_copy)

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

# Optional quick test when running this file directly:
if __name__ == "__main__":
    print("Quick Groq test (no guarantees on quotas):")
    r = run_function("answer", {"question": "What is the capital of India?"})
    print(r["output"])
