import requests
from ics import Calendar
from datetime import datetime, timedelta
import os
import re
import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
import pytz
import sys
import threading

# Argumente vom Plugin erhalten
vault_path = sys.argv[1]
active_file = sys.argv[2]

# Liste der ICS-Links
ics_urls = [
    'https://edu.classyplan.app/export.php?type=ics&personal=1&u=5057531257&t=361c4382-ebd9-47b7-b691-c4ce0b1c4a4b',
    'https://calendar.google.com/calendar/ical/florian.dagner%40gmail.com/private-6cef76c03565dc03ba4b559144e1e462/basic.ics',
]

notes_folder = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')), 'Tagesnotizen')
placeholder = "<!-- CALENDAR_ENTRIES -->"
template_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')), 'Vorlagen', 'Tagesnotiz.md')

def generate_event_id(event):
    return f"{event.begin.strftime('%Y-%m-%d %H:%M')}-{event.uid or event.name}"

def import_ics(start_date, end_date):
    all_events = []
    total_steps = len(ics_urls) + (end_date - start_date).days + 1
    current_step = 0

    # Update progress display
    def update_progress():
        nonlocal current_step
        current_step += 1
        progress_var.set((current_step / total_steps) * 100)
        root.update_idletasks()

    # Function to show error messages safely on the GUI thread
    def show_error(message):
        messagebox.showwarning("Warning", message)
        print(message)  # Also print the error to the console for debugging

    for ics_url in ics_urls:
        try:
            print(f"Attempting to load calendar from {ics_url}...")
            response = requests.get(ics_url)
            response.raise_for_status()  # Will raise an exception for HTTP errors (e.g. 404, 500)
            
            # Check for iCal content by inspecting if it contains VEVENTs
            if 'BEGIN:VEVENT' not in response.text or 'END:VEVENT' not in response.text:
                raise ValueError(f"Response does not contain valid iCal data.")
            
            calendar = Calendar(response.text)
            all_events.extend(calendar.events)
            
        except requests.exceptions.RequestException as e:
            show_error(f"Network error: The calendar from {ics_url} could not be loaded. Error: {e}")
        except ValueError as e:
            show_error(f"Invalid calendar content from {ics_url}. Error: {e}")
        except Exception as e:
            show_error(f"An unexpected error occurred while loading {ics_url}. Error: {e}")
        
        update_progress()

    # Sort events by start date
    all_events.sort(key=lambda event: event.begin)

    local_tz = pytz.timezone('Europe/Berlin')
    current_date = start_date

    while current_date <= end_date:
        note_file_name = current_date.strftime("%Y-%m-%d") + ".md"
        note_file_path = os.path.join(notes_folder, note_file_name)
        os.makedirs(notes_folder, exist_ok=True)

        if not os.path.exists(note_file_path):
            create_file = messagebox.askyesno("Create File", f"The file for {current_date} does not exist. Should it be created?")
            if not create_file:
                current_date += timedelta(days=1)
                update_progress()
                continue

            try:
                with open(template_path, "r") as template_file:
                    template_content = template_file.read()
            except Exception as e:
                messagebox.showerror("Error", f"Template could not be loaded: {e}")
                current_date += timedelta(days=1)
                update_progress()
                continue

            content = template_content.replace("{{title}}", current_date.strftime('%Y-%m-%d'))
            content = content.replace(placeholder, f"{placeholder}\n")

            try:
                with open(note_file_path, "w") as f:
                    f.write(content)
            except Exception as e:
                messagebox.showerror("Error", f"File could not be created: {e}")
                current_date += timedelta(days=1)
                update_progress()
                continue

        with open(note_file_path, "r") as f:
            content = f.read()

        # Check if the placeholder is missing
        placeholder_missing = placeholder not in content

        if placeholder_missing:
            # Show a warning if the placeholder is initially missing in the file
            messagebox.showwarning("Placeholder Missing", f"The file {note_file_name} does not contain a placeholder for calendar entries. The placeholder and the events will be added at the end of the file.")
            content += f"\n{placeholder}\n"
            
        # Entferne alle bestehenden Kalendereinträge in der Datei
        def clear_calendar_entries(content):
            # Removes all lines from the placeholder to the next empty line or the end of the document
            return re.sub(rf"{re.escape(placeholder)}.*?(?=\n\n|$)", f"{placeholder}\n", content, flags=re.DOTALL)

        # Customize the part where the file is opened and read
        with open(note_file_path, "r") as f:
            content = f.read()

       # Remove existing calendar entries before adding new ones
        content = clear_calendar_entries(content)
        placeholder_missing = placeholder not in content

        new_entries = []
        existing_ids = re.findall(r"<!-- ID: (.*?) -->", content)
        daily_event_ids = set()

        for event in all_events:
            event_start_date = event.begin.astimezone(local_tz).date()
            event_end_date = event.end.astimezone(local_tz).date() if event.end else event_start_date
            event_dates = [event_start_date + timedelta(days=i) for i in range((event_end_date - event_start_date).days + 1)]

            if current_date in event_dates:
                # Handle full-day events
                if event.begin.time() == datetime.min.time() and (event.end is None or event.end.time() == datetime.min.time()):
                    local_start = event.begin.strftime('%m-%d')  # Full-day without time
                    local_end = event.end.strftime('%m-%d') if event.end else "Open End"
                else:
                    local_start = event.begin.strftime('%m-%d, ') + event.begin.astimezone(local_tz).strftime("%H:%M")
                    local_end = event.end.strftime('%m-%d, ') + event.end.astimezone(local_tz).strftime("%H:%M") if event.end else "Open End"

                if not event.name:
                    messagebox.showwarning("Empty Title", f"The event on {event_start_date} has no title and will be ignored.")
                    continue

                event_id = generate_event_id(event)
                daily_event_ids.add(event_id)
                entry_text = (
                    f">#### {event.name}\n"
                    f">- **Start**: {local_start}\n"
                    f">- **End**: {local_end}\n"
                    f"><!-- ID: {event_id} -->"
                )

                if event_id not in existing_ids:
                    new_entries.append(entry_text)

        updated_content = content
        for event_id in existing_ids:
            if event_id not in daily_event_ids:
                event_pattern = rf"\n*>#### .*?\n.*?<!-- ID: {re.escape(event_id)} -->*"
                updated_content = re.sub(event_pattern, "", updated_content, flags=re.DOTALL)

        if new_entries:
            # Sort new entries chronologically before adding them
            new_entries.sort(key=lambda entry: re.search(r'\d{2}-\d{2}', entry).group(0))
            updated_content = updated_content.replace(placeholder, placeholder + "\n" + "\n".join(new_entries).strip())
            updated_content = re.sub(r'\n{3,}', '\n\n', updated_content)

        with open(note_file_path, "w") as f:
            f.write(updated_content)

        current_date += timedelta(days=1)
        update_progress()

    messagebox.showinfo("Done", f"Events successfully exported for the period {start_date} to {end_date} into the daily notes.")
    root.quit()

def start_import():
    start_date = start_date_entry.get_date()
    end_date = end_date_entry.get_date()
    threading.Thread(target=lambda: import_ics(start_date, end_date)).start()

# Create main window
root = tk.Tk()
root.title("Calendar Import")

# Set window size (width x height)
window_width = 250
window_height = 150

# Get screen size
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate x and y coordinates for centered positioning
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set window position and size
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

try:
    active_date = datetime.strptime(os.path.basename(active_file).split('.')[0], '%Y-%m-%d')
except ValueError:
    active_date = datetime.now()

tk.Label(root, text="Start Date:").grid(row=0, column=0)
start_date_entry = DateEntry(root)
start_date_entry.set_date(active_date)
start_date_entry.grid(row=0, column=1)

tk.Label(root, text="End Date:").grid(row=1, column=0)
end_date_entry = DateEntry(root)
end_date_entry.set_date(active_date)
end_date_entry.grid(row=1, column=1)

progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.grid(row=2, columnspan=2, pady=10, sticky="we")

tk.Button(root, text="Import", command=start_import).grid(row=3, columnspan=2)

root.mainloop()
print("Import finished!")
