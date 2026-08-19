from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# -------- HOME / TEST --------

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "success",
        "message": "MEDIX Plant Backend is Running 🌱"
    })


# -------- PLANT PREDICTION --------

@app.route("/predict/plant", methods=["POST"])
def plant_prediction():
    return jsonify({
        "status": "success",
        "plant": "Tomato",
        "disease": "Early Blight",
        "confidence": 0.94
    })


# -------- RUN SERVER --------

if __name__ == "__main__":
    app.run(debug=True)
