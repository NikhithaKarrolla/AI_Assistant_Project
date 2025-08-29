from services import run_function

def main():
    while True:
        print("\nWelcome to your AI Assistant!")
        print("1) Answer Questions")
        print("2) Summarize Text")
        print("3) Generate Creative Content")
        print("4) Provide Advice")
        print("5) Exit")
        choice = input("Select an option: ").strip()
        if choice == "1":
            q = input("Enter your factual question: ").strip()
            result = run_function("answer", {"question": q})
        elif choice == "2":
            t = input("Paste text to summarize: ").strip()
            result = run_function("summarize", {"text": t})
        elif choice == "3":
            p = input("Describe the creative idea (story, poem, pitches): ").strip()
            result = run_function("create", {"prompt": p})
        elif choice == "4":
            topic = input("Topic you want advice on: ").strip()
            result = run_function("advice", {"topic": topic})
        elif choice == "5":
            print("Goodbye!"); break
        else:
            print("Invalid choice. Try again."); continue

        print("\n--- Prompt Variant Used:", result["variant"])
        print("--- Response ---\n")
        print(result["output"])
        print("\nWas this helpful? (yes/no)")
        helpful = input().strip().lower()
        comments = input("Any comments (optional): ").strip()
        # Feedback is recorded by the web app; for CLI we simply display a note.
        # You can extend this by importing log_feedback and persisting here as well.
        try:
            from services import log_feedback
            log_feedback({
                "function": choice,
                "variant": result["variant"],
                "helpful": "yes" if helpful.startswith("y") else "no",
                "comments": comments,
                "user_input": q if choice == "1" else (t if choice == "2" else (p if choice == "3" else topic)),
                "output": result["output"],
            })
            print("Feedback saved. Thank you!")
        except Exception as e:
            print("Couldn't save feedback:", e)

if __name__ == "__main__":
    main()
