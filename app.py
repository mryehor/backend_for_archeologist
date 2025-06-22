from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')  # отдаём HTML вместо JSON

@app.route('/dig')
def dig():
    findings = [
        "💎 Драгоценный камень",
        "🗿 Статуэтка",
        "🪙 Монета",
        "📜 Древний свиток",
        "🪨 Камень"
    ]
    return jsonify({"result": random.choice(findings)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
