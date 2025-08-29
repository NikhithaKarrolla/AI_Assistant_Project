from flask import Flask, render_template, request, redirect, url_for
from services import run_function, log_feedback

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        function = request.form.get("function")
        user_input = request.form.get("user_input", "").strip()

        if not function or not user_input:
            return render_template("index.html", error="Please provide both function and input.")

        # Prepare payload based on function type
        payload = {}
        if function == "answer":
            payload["question"] = user_input
        elif function == "summarize":
            payload["text"] = user_input
        elif function == "create":
            payload["prompt"] = user_input
        elif function == "advice":
            payload["topic"] = user_input
        else:
            return render_template("index.html", error="Invalid function selected.")

        # Call AI service
        result = run_function(function, payload)

        return render_template("result.html",
                               function=function,
                               user_input=user_input,
                               **result)
    return render_template("index.html")


@app.route("/feedback", methods=["POST"])
def feedback():
    helpful = request.form.get("helpful")  # "yes" or "no"
    comments = request.form.get("comments", "").strip()
    function = request.form.get("function")
    variant = request.form.get("variant")
    user_input = request.form.get("user_input")
    output = request.form.get("output")

    log_feedback({
        "function": function,
        "variant": variant,
        "helpful": helpful,
        "comments": comments,
        "user_input": user_input,
        "output": output,
    })

    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
