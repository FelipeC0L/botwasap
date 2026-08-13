from flask import Flask, request
import requests
import os

app = Flask(_name_)

VERIFY_TOKEN = "mi_token_secreto_123"  # Debe ser igual al de Meta
ACCESS_TOKEN = "TU_TOKEN_LARGO_DE_META"  # El que empieza con EAA...
PHONE_NUMBER_ID = "TU_PHONE_NUMBER_ID"  # Lo ves en WhatsApp > Configuration

@app.route("/webhook", methods=["GET"])
def verify():
    # Esto es para que Meta verifique el webhook
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")
    
    if token == VERIFY_TOKEN:
        return challenge  # Si coincide, devuelve el challenge
    return "Token invalido", 403

@app.route("/webhook", methods=["POST"])
def webhook():
    # Aquí llegan los mensajes
    data = request.get_json()
    return "ok", 200

if _name_ == "_main_":
    app.run()
