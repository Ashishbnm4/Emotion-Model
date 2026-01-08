from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

# Load model files
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def recommend_task(emotion):
    if emotion in ["joy", "love"]:
        return "Creative or collaborative tasks"
    elif emotion == "neutral":
        return "Routine and planning tasks"
    else:
        return "Light workload, stress management, or support tasks"

@app.route("/", methods=["GET", "POST"])
def home():
    emotion = None
    task = None

    if request.method == "POST":
        text = request.form.get("text")
        if text:
            vec = vectorizer.transform([text])
            emotion = model.predict(vec)[0]
            task = recommend_task(emotion)

    return render_template("index.html", emotion=emotion, task=task)

@app.route("/health")
def health():
    return "OK"

# ❌ DO NOT call app.run() on Render
# Render + Gunicorn will handle it
