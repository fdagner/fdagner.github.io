import requests
from ics import Calendar
from datetime import datetime, timedelta
import os
import re
import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import pytz
import sys

# Argumente vom Plugin erhalten
vault_path = sys.argv[1]
active_file = sys.argv[2]

# Liste der ICS-Links
ics_urls = [
    'https://edu.classyplan.app/export.php?type=ics&personal=1&u=5057531257&t=361c4382-ebd9-47b7-b691-c4ce0b1c4a4b',
    'https://calendar.google.com/calendar/ical/florian.dagner%40gmail.com/private-6cef76c03565dc03ba4b559144e1e462/basic.ics',
    # Weitere Links hier hinzufügen
]

# Ordner für die Tagesnotizen
notes_folder = r'C:\Users\flori\bycsdrive\Persönlich\_Obsidian\Tagesnotizen'
placeholder = "<!-- CALENDAR_ENTRIES -->"

# Funktion zum Ausführen des Imports
def import_ics(start_date, end_date):
    # Für jeden ICS-Link Kalenderdaten abrufen und speichern
    all_events = []
    for ics_url in ics_urls:
        response = requests.get(ics_url)
        response.raise_for_status()
        calendar = Calendar(response.text)
        all_events.extend(calendar.events)

    # Zeitzone der lokalen Umgebung abrufen
    local_tz = pytz.timezone('Europe/Berlin')  # Beispiel für die Berliner Zeitzone, passe sie bei Bedarf an

    # Für jeden Tag im angegebenen Zeitraum
    current_date = start_date
    while current_date <= end_date:
        note_file_name = current_date.strftime("%Y-%m-%d") + ".md"
        note_file_path = os.path.join(notes_folder, note_file_name)

        # Falls der Ordner nicht existiert, wird er erstellt
        os.makedirs(notes_folder, exist_ok=True)

        # Datei erstellen oder Abfrage, falls sie nicht existiert
        if not os.path.exists(note_file_path):
            create_file = messagebox.askyesno("Datei erstellen", f"Die Datei für {current_date} existiert nicht. Soll sie erstellt werden?")
            if not create_file:
                current_date += timedelta(days=1)
                continue
            else:
                with open(note_file_path, "w") as f:
                    f.write(f"# {current_date.strftime('%Y-%m-%d')} - Kalender Termine\n\n{placeholder}\n")

        # Dateiinhalt laden
        with open(note_file_path, "r") as f:
            content = f.read()

        # Prüfen, ob der Platzhalter existiert, andernfalls hinzufügen
        if placeholder not in content:
            content += f"\n{placeholder}\n"

        # Neue und bestehende Einträge sammeln
        new_entries = []
        existing_ids = re.findall(r"<!-- ID: (.*?) -->", content)
        updated_content = content

        for event in all_events:
            if event.begin.date() == current_date:
                # Konvertiere die Zeit in die lokale Zeitzone
                local_start = event.begin.to("local").strftime("%H:%M")
                local_end = event.end.to("local").strftime("%H:%M") if event.end else "Open End"
                event_id = f"{event.name}-{event.begin.format('YYYY-MM-DD HH:mm')}"

                entry_text = (
                    f">#### {event.name}\n"
                    f">- **Start**: {local_start}\n"
                    f">- **Ende**: {local_end}\n"
                    f">- **Beschreibung**: {event.description or 'Keine Beschreibung'}\n"
                    f"><!-- ID: {event_id} -->"
                )

                # Prüfen, ob der Termin bereits existiert
                existing_entry = re.search(rf">#### {re.escape(event.name)}\n.*?<!-- ID: {re.escape(event_id)} -->", updated_content, re.DOTALL)
                if existing_entry:
                    # Wenn sich der Text geändert hat, aktualisiere den Eintrag
                    if existing_entry.group(0).replace('>', '') != entry_text.replace('>', ''):
                        updated_content = updated_content.replace(existing_entry.group(0), entry_text)
                else:
                    # Füge den neuen Eintrag hinzu
                    new_entries.append(entry_text)

        # Entfernen von gelöschten Terminen
        for event_id in existing_ids:
            if not any(f"{event.name}-{event.begin.format('YYYY-MM-DD HH:mm')}" == event_id for event in all_events if event.begin.date() == current_date):
                event_pattern = rf">#### .*?\n.*?<!-- ID: {re.escape(event_id)} -->"
                updated_content = re.sub(event_pattern, "", updated_content, flags=re.DOTALL)

        # Neue Einträge an den Platzhalter einfügen
        if new_entries:
            updated_content = updated_content.replace(placeholder, placeholder + "\n" + "\n".join(new_entries))

        # Unerwünschte Zeilenumbrüche entfernen
        updated_content = re.sub(r'\n{2,}', '\n\n', updated_content)  # Mehrfache Zeilenumbrüche durch einen ersetzen
        updated_content = updated_content.strip() + "\n"  # Sicherstellen, dass am Ende ein Zeilenumbruch ist

        # Datei mit aktualisiertem Inhalt überschreiben
        with open(note_file_path, "w") as f:
            f.write(updated_content)

        # Zum nächsten Tag wechseln
        current_date += timedelta(days=1)

    messagebox.showinfo("Fertig", f"Termine erfolgreich für den Zeitraum {start_date} bis {end_date} in die Tagesnotizen exportiert.")
    root.quit()  # Beendet die Anwendung nach dem Klick auf "OK"

def submit_dates():
    start_date = start_date_entry.get_date()
    end_date = end_date_entry.get_date()
    import_ics(start_date, end_date)

# Hauptfenster erstellen
root = tk.Tk()
root.title("Kalender Import")

# Startdatum und Enddatum aus dem aktuellen Dateinamen extrahieren
try:
    active_date = datetime.strptime(os.path.basename(active_file).split('.')[0], '%Y-%m-%d')
except ValueError:
    active_date = datetime.now()

# Startdatum eingeben
tk.Label(root, text="Startdatum:").grid(row=0, column=0)
start_date_entry = DateEntry(root)
start_date_entry.set_date(active_date)
start_date_entry.grid(row=0, column=1)

# Enddatum eingeben (Standard: gleiches Datum wie Startdatum)
tk.Label(root, text="Enddatum:").grid(row=1, column=0)
end_date_entry = DateEntry(root)
end_date_entry.set_date(active_date)
end_date_entry.grid(row=1, column=1)

# Button zum Importieren
tk.Button(root, text="Importieren", command=submit_dates).grid(row=2, columnspan=2)

root.mainloop()  # Startet das GUI-Fenster
print("Die Termine wurden erfolgeich aktualisiert!")