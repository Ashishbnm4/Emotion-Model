from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

def recommend_task(emotion):
    if emotion in ["joy", "love"]:
        return "Creative or collaborative tasks"
    elif emotion == "neutral":
        return "Routine and planning tasks"
    else:
        return "Light workload, stress management, or support tasks"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("text")

    vec = vectorizer.transform([text])
    emotion = model.predict(vec)[0]
    task = recommend_task(emotion)

    return jsonify({
        "emotion": emotion,
        "task": task
    })
