from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = "mi_token_secreto_123"

@app.route("/webhook", methods=["GET"])
def verify():
    # Meta manda esto para verificar
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if token == VERIFY_TOKEN:
        return challenge, 200
    return "Token incorrecto", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    # Aquí te llegarán los mensajes de WhatsApp
    data = request.get_json()
    print(data)  # Para ver los mensajes en los logs de Render
    return "ok", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
