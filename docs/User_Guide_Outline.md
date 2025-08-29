# User Guide (PowerPoint Outline)

## Slide 1 – Title
**AI Assistant – Prompt Engineering Major Project**  
Author: (Your Name) | Date

## Slide 2 – Objective
- Build a basic AI Assistant capable of multiple tasks driven by prompts.
- Demonstrate effective prompt design and iteration.

## Slide 3 – Features
- Answer factual questions
- Summarize text
- Generate creative content (story/poem/pitches)
- Provide advice

## Slide 4 – Tech Stack
- Python, Flask (Web), CLI
- OpenAI API (model configurable)
- dotenv for configuration
- JSON for feedback storage

## Slide 5 – Setup
- `pip install -r requirements.txt`
- Create `.env` with `OPENAI_API_KEY` and optional `MODEL`
- Run `python app.py` for web; `python cli.py` for CLI

## Slide 6 – How It Works
- User picks a function and submits input.
- System selects one of 3 prompt variants for that function.
- Sends messages (system + user) to the model.
- Displays response, asks for feedback.

## Slide 7 – Prompt Engineering
- 3 variants per function to vary tone, specificity, and length.
- Encourages experimentation & A/B testing.
- Examples: concise factual, teacherly explain, contextual bullets; executive summary, key takeaways, TL;DR; story warm, poem minimalist, sci-fi pitch; etc.

## Slide 8 – Feedback Loop
- In-app: yes/no + optional comments.
- Stored in `feedback_store.json` with timestamps.
- Use feedback to refine prompts (swap variants, adjust tones).

## Slide 9 – Demo (Web)
- Screenshot: Home page
- Screenshot: Result + feedback

## Slide 10 – Demo (CLI)
- Menu selection
- Sample run

## Slide 11 – Extending the Project
- Add more functions (translation, email drafting, math tutor).
- Track per-variant success rates.
- Add user accounts & persistent histories.
- Guardrails (input validation, profanity filter).

## Slide 12 – Conclusion
- You now have a working AI assistant with structured prompt variants and feedback.
- Iterate based on data to improve quality.
