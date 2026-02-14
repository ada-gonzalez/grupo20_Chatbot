REQUISITOS = {
    "1": {
        "nombre": "vacunacion",
        "sinonimos": ["vacuna", "vacunas", "vacunacion", "vacunar"],
        "respuesta": "Para vacunación se requiere DUI y carnet de vacunación (si se posee)."
    },
    "2": {
        "nombre": "control prenatal",
        "sinonimos": ["control prenatal", "prenatal", "control"],
        "respuesta": "Para control prenatal se solicita DUI y prueba de emparazo positivo."
    },
    "3": {
        "nombre": "referencia",
        "sinonimos": ["referencia", "remision", "referencias", "medica", "remitieron"],
        "respuesta": "Para referencia médica se requiere DUI y referencia externa original."
    }
}

MENSAJES_REGISTRO = {
    "inicio": "Con gusto 😊 Para registrar tu solicitud necesito algunos datos.",

    "nombre": "¿Cuál es tu nombre?",

    "descripcion": (
        "Gracias. Ahora cuéntame brevemente tu situación o consulta, por favor."
    ),

    "contacto": (
        "¿Deseas dejarnos un medio de contacto para dar seguimiento?\n"
        "📞 Teléfono o 📧 correo.\n"
        "Es opcional, Si prefieres no hacerlo, escribe *no*."
    ),

    "confirmacion": (
        "Por favor confirma la información:\n\n"
        "👤 Nombre: {nombre}\n"
        "📝 Consulta: {descripcion}\n"
        "📬 Contacto: {contacto}\n\n"
        "¿Es correcto?\n"
        "Responde *sí* para confirmar o *no* para cancelar."
    ),

    "exito": ("✅ Tu solicitud fue registrada correctamente. Gracias por comunicarte con CSDC."),

    "cancelado": ("Registro cancelado. Si necesitas ayuda más adelante, aquí estaré 😊")
}

