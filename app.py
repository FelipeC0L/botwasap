from flask import Flask, request
import os

app = Flask(__name__)
VERIFY_TOKEN = os.environ.get("VERIFY_TOKEN")

@app.route("/", methods=["GET"])
def home():
    return "Bot vivo", 200

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    print("ALGO LLEGO AL WEBHOOK") # Para saber si llega algo
    if request.method == "GET":
        token = request.args.get("hub.verify_token")
        challenge = request.args.get("hub.challenge")
        print(f"GET con token: {token}")
        if token == VERIFY_TOKEN:
            return challenge
        return "Token invalido", 403
    
    if request.method == "POST":
        data = request.get_json()
        print(f"POST DATA: {data}") # Aquí debe salir el mensaje
        return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
