from flask import Flask, request, jsonify
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

# -------- HUMAN --------
@app.route('/predict/human', methods=['POST'])
def human():
    return jsonify({
        "result": "Possible Skin Disease",
        "advice": "Consult dermatologist"
    })

# -------- PLANT --------
@app.route('/predict/plant', methods=['POST'])
def plant():
    return jsonify({
        "result": "Leaf Disease Detected",
        "treatment": "Use fungicide spray"
    })

# -------- REPORT --------
@app.route('/analyze/report', methods=['POST'])
def report():
    return jsonify({
        "analysis": "Report analyzed. Values look normal."
    })

if __name__ == "__main__":
    app.run()
