from flask import Flask, request, jsonify
from flows import (
    iniciar_requisitos,
    manejar_tramite,
    iniciar_registro,
    manejar_registro
)

app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json()
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

    
if __name__ == "__main__":
    app.run(debug=True)