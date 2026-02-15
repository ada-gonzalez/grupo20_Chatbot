REQUISITOS = {
    "1": {
        "nombre": "vacunacion",
        "sinonimos": ["vacuna", "vacunas", "vacunacion", "vacunar"],
        "respuesta": (
            "🩺 *Vacunación*\n\n"
            "Para realizar el trámite de vacunación, necesitas:\n"
            "• DUI\n"
            "• Carnet de vacunación (si lo posees)\n\n"
            "Si no tienes el carnet, el personal te indicará cómo continuar."
        )
    },
    "2": {
        "nombre": "control prenatal",
        "sinonimos": ["control prenatal", "prenatal", "control"],
        "respuesta": (
            "😊 *Control prenatal*\n\n"
            "Para el control prenatal, se solicita:\n"
            "• DUI\n"
            "• Prueba de embarazo positiva\n\n"
            "Si tienes dudas sobre los documentos, puedes consultarlo en el centro de salud."
        )
    },
    "3": {
        "nombre": "referencia",
        "sinonimos": ["referencia", "remision", "referencias", "medica", "remitieron"],
        "respuesta": (
            "📄 *Referencia médica*\n\n"
            "Para gestionar una referencia médica, necesitas:\n"
            "• DUI\n"
            "• Referencia externa original\n\n"
            "Recuerda llevar el documento en físico el día de tu visita."
        )
    }
}

MENSAJES_REGISTRO = {
    "inicio": (
        "¡Perfecto! 😊 Para registrar tu solicitud necesito hacerte unas preguntas rápidas."
    ),

    "nombre": (
        "Para comenzar, ¿me indicas tu nombre y un apellido?"
    ),

    "descripcion": (
        "Gracias. Ahora cuéntame brevemente tu situación o consulta para poder orientarte mejor."
    ),

    "contacto": (
        "¿Deseas dejarnos un medio de contacto para dar seguimiento a tu solicitud?\n"
        "Puedes escribir un 📞 teléfono o un 📧 correo.\n\n"
        "Este dato es opcional. Si prefieres no compartirlo, responde *no*."
    ),

    "confirmacion": (
        "Por favor verifica que la información sea correcta:\n\n"
        "👤 *Nombre:* {nombre}\n"
        "📝 *Consulta:* {descripcion}\n"
        "📬 *Contacto:* {contacto}\n\n"
        "¿Todo está bien?\n"
        "Responde *sí* para confirmar o *no* para cancelar."
    ),

    "exito": (
        "✅ ¡Listo! Tu solicitud fue registrada correctamente.\n"
        "Gracias por comunicarte con CSDC. Te estaremos apoyando en lo que necesites."
    ),

    "cancelado": (
        "Entendido, el registro fue cancelado.\n"
        "Si necesitas ayuda más adelante, aquí estaré para apoyarte 😊"
    )
    }
