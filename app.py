# ==============================
# 2. app.py
# ==============================

from flask import Flask, request, render_template
from emotion_detector import detect_emotion, format_emotion_result

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        text = request.form.get("text")

        if not text or text.strip() == "":
            result = {"error": "Please enter valid text"}
        else:
            response = detect_emotion(text)
            result = format_emotion_result(response)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)

