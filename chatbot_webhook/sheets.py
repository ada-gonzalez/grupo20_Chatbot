import gspread
from google.oauth2.service_account import Credentials
from datetime import datetime

# Ruta a la clave JSON
CREDENTIALS_FILE = "credentials/google_sheets_key.json"

# Nombre del Google Sheet
SPREADSHEET_NAME = "Solicitudes Chatbot CSDC - AmiBot"

def get_sheet():
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        CREDENTIALS_FILE,
        scopes=scopes
    )

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
