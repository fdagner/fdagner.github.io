import os
import requests

# Ziel-URL für die PDF-Datei
pdf_url = "https://www.gesetze-bayern.de/Content/Pdf/BayRSO?all=True"

# Dynamische Festlegung des Speicherpfads
notes_folder = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')), 'Dokumente')
file_path = os.path.join(notes_folder, 'RSO.pdf')  # Speicherort für die PDF-Datei

# Funktion zum Herunterladen der PDF
def download_pdf():
    try:
        response = requests.get(pdf_url, stream=True)
        if response.status_code == 200:
            # Verzeichnis sicherstellen
            os.makedirs(notes_folder, exist_ok=True)
            # PDF speichern
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"PDF erfolgreich heruntergeladen und gespeichert unter: {file_path}")
        else:
            print(f"Fehler beim Herunterladen der PDF: Statuscode {response.status_code}")
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")

if __name__ == "__main__":
    download_pdf()
