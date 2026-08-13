from flask import Flask, request
import requests

app = Flask(_name_)

# 1. PEGA AQUÍ TUS NÚMEROS PERMITIDOS. Con 57 si eres de Colombia
CONTACTOS_PERMITIDOS = [
    "573203722984" # Solo el tuyo para probar
]

# 2. PEGA TU TOKEN PERMANENTE
TOKEN = "EAAjKlG7KMd0BSOV6bbzAvyJmSR8hUzI7QQL0ExNcIN6ICcuGKHm38HJFACAkoIZC2QJN3AqlcwTHxQ9NYrX2Uhhs9I4pLcTwrN9t5Np8PFCPBrZAlAUiatOuEA05zZCpZA04KK0mI8VCKjC45wph6QEEMtVI7n315sJsDBEdwLf16ZB28ekxKHNHryOOOd2Q9gEXVOraAs8kufLQZBULrEYZCgaDYolzviNwAPsPjGsvXe0qhaAVMYoqoaMquDYcm6i0d9Fu40E51ZAEIqoiZCUygTpXZC"

# 3. PEGA TU PHONE NUMBER ID
PHONE_ID = "1209458688925617"

def enviar_mensaje(numero, texto):
    url = f"https://graph.facebook.com/v20.0/{PHONE_ID}/messages"
    headers = {"Authorization": f"Bearer {TOKEN}"}
    data = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": texto}
    }
    requests.post(url, headers=headers, json=data)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
    try:
        msg = data["entry"][0]["changes"][0]["value"]["messages"][0]
        numero = msg["from"]
        texto = msg["text"]["body"].lower()

        # FILTRO: Si no está en la lista, ignora
        if numero not in CONTACTOS_PERMITIDOS:
            return "ok"

        # TU MENÚ
        if texto in ["hola", "menu"]:
            respuesta = """Menú Privado 🔒
1. Info
2. Soporte
3. Salir
Escribe el número"""
        elif texto == "1":
            respuesta = "Esta es la info interna"
        else:
            respuesta = "Escribe 'menu' para ver opciones"

        enviar_mensaje(numero, respuesta)
    except:
        pass
    return "ok"

@app.route("/webhook", methods=["GET"])
def verify():
    # Para verificar con Meta
    verify_token = "mi_token_secreto_123" # Inventa una palabra
    if request.args.get("hub.verify_token") == verify_token:
        return request.args.get("hub.challenge")
    return "Error"

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=3000)