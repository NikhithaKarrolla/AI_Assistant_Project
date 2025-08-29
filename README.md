# AI Assistant – Prompt Engineering Major Project

This project is a basic AI Assistant (CLI + Web) showcasing prompt engineering across multiple functions:
- Answer Factual Questions
- Summarize Text
- Generate Creative Content
- Provide Advice

It includes:
- A Flask web app with a clean UI
- A CLI tool
- Well-structured prompt variants for each function
- A simple feedback loop (stored in `feedback_store.json`)
- A PowerPoint-ready outline (docs/User_Guide_Outline.md) and a script to export a .pptx if `python-pptx` is available

## Quick Start (Web App)

1) **Install dependencies (Python 3.9+ recommended)**  
```bash
pip install -r requirements.txt
```

2) **Set your OpenAI API key**  
Create a `.env` file by copying `.env.example`, then put your key:
```
OPENAI_API_KEY=sk-...
MODEL=gpt-4o-mini
```

3) **Run the server**  
```bash
python app.py
```
Open http://127.0.0.1:5000 in your browser.

## Quick Start (CLI)

```bash
python cli.py
```

## Files & Folders

- `app.py` – Flask web app
- `cli.py` – Command-line interface
- `services.py` – OpenAI API wrapper and core logic
- `prompts.py` – Prompt templates (3 per function)
- `templates/` – Jinja2 templates for Flask
- `static/style.css` – Minimal styles
- `feedback_store.json` – Feedback log (auto-created)
- `requirements.txt` – Python dependencies
- `.env.example` – Environment variables sample
- `docs/User_Guide_Outline.md` – PPT-ready content
- `docs/make_ppt_if_possible.py` – Optional script to generate a PowerPoint if `python-pptx` is installed

## Features Mapped to Requirements

1. **Functionality (≥3 functions)**  
   - Answer Questions, Summarize Text, Generate Creative Content, Provide Advice (4 total).

2. **Prompt Design (≥3 prompts per function)**  
   - See `prompts.py` – each function has 3 distinct prompt styles varying length, specificity, tone, and context.

3. **User Interaction**  
   - **Web**: Choose a function, input your text, get clear responses.  
   - **CLI**: Simple numeric menu with loop.  

4. **Feedback Loop**  
   - After each response, you can mark "Helpful? yes/no" and leave an optional comment.  
   - Logged in `feedback_store.json` with timestamps and prompt variant used.

5. **Documentation**  
   - `docs/User_Guide_Outline.md` contains the slide-by-slide content you can paste into a PPT.  
   - `docs/make_ppt_if_possible.py` will generate `User_Guide_AI_Assistant.pptx` **if** `python-pptx` is available.

## Notes
- You can change the model in `.env` (`MODEL=...`). Default is `gpt-4o-mini` if set; otherwise falls back to `gpt-3.5-turbo`.
- If you don't have Flask, use the CLI version.
- Feedback file grows over time; you can clear it by deleting `feedback_store.json`.

Enjoy building and iterating on your AI Assistant!
