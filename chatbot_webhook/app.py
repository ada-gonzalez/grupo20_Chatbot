from flask import Flask, request, jsonify
import os
from chatbot_webhook.flows import (
    iniciar_requisitos,
    manejar_tramite,
    iniciar_registro,
    manejar_registro
)


app = Flask(__name__)

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True) or {}
        query = data.get("queryResult", {})

        intent = query.get("intent", {}).get("displayName")
        user_message = query.get("queryText", "")
        user_id = data.get("session")

        # Iniciar flujos
        if intent == "requisitos_tramite_inicio":
            return jsonify(iniciar_requisitos(user_id))

        if intent == "registrar_solicitud_inicio":
            return jsonify(iniciar_registro(user_id))

        # Continuar con los flujos
        response = manejar_tramite(user_id, user_message)
        if response:
            return jsonify(response)

        response = manejar_registro(user_id, user_message)
        if response:
            return jsonify(response)

        return jsonify({})

    except Exception as e:
        # Log básico para depurar en la nube
        print("Error en webhook:", e)
        return jsonify({"fulfillmentText": "Ocurrió un error procesando tu solicitud 😅"}), 500


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
