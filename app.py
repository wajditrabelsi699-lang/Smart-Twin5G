from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Smart Twin 5G AI is online!"}

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("text", "")
    reply = f"You said: {user_input}"
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run()
