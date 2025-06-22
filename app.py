from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import json

with open("game_data.json", "r", encoding="utf-8") as f:
    game_data = json.load(f)
    
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')  # Serve the main HTML page

@app.route('/pickaxes')
def get_pickaxes():
    return jsonify(game_data["pickaxes"])

@app.route('/artifacts')
def get_artifacts():
    return jsonify(game_data["artifacts"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
