import os
import json
import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Nombre del Google Sheet (configurable por entorno)
SPREADSHEET_NAME = os.environ.get("SPREADSHEET_NAME", "Solicitudes Chatbot CSDC - AmiBot")

def get_sheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds_json = os.environ.get("GOOGLE_CREDS_JSON")
    if not creds_json:
        raise Exception("Faltan credenciales: define GOOGLE_CREDS_JSON en variables de entorno")

    creds_info = json.loads(creds_json)
    creds = Credentials.from_service_account_info(creds_info, scopes=scopes)

    client = gspread.authorize(creds)
    spreadsheet = client.open(SPREADSHEET_NAME)
    sheet = spreadsheet.sheet1

    return sheet


def guardar_solicitud(nombre, descripcion, contacto):
    sheet = get_sheet()
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    sheet.append_row([
        fecha,
        nombre,
        descripcion,
        contacto
    ])
