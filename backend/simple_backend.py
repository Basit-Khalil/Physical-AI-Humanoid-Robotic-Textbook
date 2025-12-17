from flask import Flask, request, jsonify
import sys

app = Flask(__name__)

@app.route("/")
def read_root():
    return jsonify({"message": "Welcome to the Physical AI & Humanoid Robotics Book Backend!"})

# Simple chat endpoint that echoes the message
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = f"You asked: '{user_message}'. This is a basic response from the Physical AI & Humanoid Robotics assistant."
    return jsonify({"response": bot_response})

# RAG chat endpoint that echoes the message (placeholder for now)
@app.route("/chat_with_rag", methods=["POST"])
def chat_with_rag():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = f"You asked: '{user_message}'. This is a RAG-enhanced response from the Physical AI & Humanoid Robotics assistant. (RAG functionality will be implemented when the full backend is operational)"
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)