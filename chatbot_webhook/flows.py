import unicodedata
import re
from chatbot_webhook.data import REQUISITOS, MENSAJES_REGISTRO
from chatbot_webhook.sheets import guardar_solicitud



#todo el texto en minúsculas, sin tildes ni símbolos
def normalizar_texto(texto):
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    texto = re.sub(r"[^a-z0-9\s]", "", texto)
    return texto.strip()

user_states = {}

##INTENCION 3: requisitos_tramite##
#Menu de tramites disponibles
def iniciar_requisitos(user_id):
#Si el usuario en la nube llega vacío
    if not user_id:
        user_id = "anon"
    user_states[user_id] = {
        "flow": "requisitos",
        "step": "esperando_tramite"
    }
    return {
        "fulfillmentText": (
            "Claro 😊 ¿Qué trámite deseas consultar?\n\n"
            "1️⃣ Vacunación\n"
            "2️⃣ Control prenatal\n"
            "3️⃣ Referencia\n\n"
            "Puedes responder con el número o el nombre del trámite."
        )
    }

#Entender el tramite
def resolver_tramite(user_input):
    texto = normalizar_texto(user_input)

    # Si escribió un número
    if texto in REQUISITOS:
        return REQUISITOS[texto]["respuesta"]

    #Buscar en sinonimos
    for tramite in REQUISITOS.values():
        sinonimos = tramite["sinonimos"]
        if any(alias in texto for alias in sinonimos):
            return tramite["respuesta"]

    return None

#Devolver una respuesta al tramite
def manejar_tramite(user_id, user_message):
    state = user_states.get(user_id)

    if not state:
        return None

    if state.get("flow") != "requisitos":
        return None

    if state.get("step") != "esperando_tramite":
        return None
    respuesta = resolver_tramite(user_message)

    if respuesta:
        del user_states[user_id]
        return {"fulfillmentText": respuesta}

    return {
        "fulfillmentText": (
            "No logré identificar el trámite :(\n"
            "Responde con el número o el nombre:\n"
            "1️⃣ Vacunación\n"
            "2️⃣ Control prenatal\n"
            "3️⃣ Referencia"
        )
    }

##INTENCIÓN 4: registrar_solicitud##

def iniciar_registro(user_id):
    user_states[user_id] = {
        "flow": "registro",
        "step": "nombre",
        "data": {}
    }

    return {
        "fulfillmentText": (
            MENSAJES_REGISTRO["inicio"]
            + "\n\n"
            + MENSAJES_REGISTRO["nombre"]
        )
    }


def manejar_registro(user_id, user_message):
    state = user_states.get(user_id)
    if not state or state.get("flow") != "registro":
        return None

    step = state["step"]
    data = state["data"]

    # PASO 1 — Nombre
    if step == "nombre":
        data["nombre"] = user_message
        state["step"] = "descripcion"

        return {"fulfillmentText": MENSAJES_REGISTRO["descripcion"]}

    # PASO 2 — Descripción
    if step == "descripcion":
        data["descripcion"] = user_message
        state["step"] = "contacto"

        return {"fulfillmentText": MENSAJES_REGISTRO["contacto"]}

    # PASO 3 — Contacto opcional
    if step == "contacto":
        if user_message.lower() in ["no", "ninguno", "prefiero no"]:
            data["contacto"] = "No proporcionado"
        else:
            data["contacto"] = user_message

        state["step"] = "confirmacion"

        return {
            "fulfillmentText": MENSAJES_REGISTRO["confirmacion"].format(
                nombre=data["nombre"],
                descripcion=data["descripcion"],
                contacto=data["contacto"]
            )
        }

    # PASO 4 — Confirmación
    # Versión por si guardar la solicitud en la nube falla
    if step == "confirmacion":
        respuesta_norm = normalizar_texto(user_message)

        if respuesta_norm in ["si", "sii"]:
            try:
                guardar_solicitud(
                    nombre=data["nombre"],
                    descripcion=data["descripcion"],
                    contacto=data["contacto"]
                )
                del user_states[user_id]
                return {"fulfillmentText": MENSAJES_REGISTRO["exito"]}
            except Exception as e:
                print("Error guardando solicitud:", e)
                return {"fulfillmentText": "Tu solicitud no pudo guardarse en este momento 😅 Intenta más tarde."}

        if respuesta_norm == "no":
            del user_states[user_id]
            return {"fulfillmentText": MENSAJES_REGISTRO["cancelado"]}

        return {"fulfillmentText": "Por favor responde *sí* o *no*."}
