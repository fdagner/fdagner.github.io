---
layout: post
title: Datenbankvorlage Terminfinder
date: 2026-08-30T17:00:00
image: "/assets/images/2026-08-30_terminfinder.png"
categories:
  - moodle
---

**Wer mit mehreren Personen Termine abstimmen muss, kennt das Problem: Für „Wann könnt ihr?" gibt es zig externe Tools. Die Idee ist nun, die Abstimmung innerhalb von Moodle zu belassen, mit einer einfach einzurichtenden Datenbankvorlage.**


### Funktionen

Für jeden vorgeschlagenen Termin lässt sich mit einem Klick die Rückmeldung markieren. Dabei werden sowohl ganztägige als auch uhrzeitgenaue Termine unterstützt und in der Übersicht getrennt dargestellt. 
Zusätzlich kann jeder einen kurzen Kommentar hinzufügen. Alle Rückmeldungen werden automatisch zu einer Übersichtstabelle zusammengefasst, wobei der Termin mit den meisten positiven Rückmeldungen automatisch mit einem Stern hervorgehoben wird. Für den am besten passenden oder auch jeden beliebigen Termin lässt sich per Klick ein Kalendereintrag als iCal-Datei (.ics) mit eigenem Titel, Ort und Dauer erzeugen. Und schließlich gibt es eine E-Mail-Vorlage zum Kopieren: einen fertigen Einladungstext inklusive automatisch generierter Links.


[![Screenshot Bewertungskategorie](/assets/images/2026-08-30_terminfinder.png)](/assets/images/2026-08-30_terminfinder.png){: style="width: 100%;max-width: 750px;display: block; margin: 0 auto"}

### Handhabung für Organisatoren

1. **Vorlage importieren**: Neue Datenbank-Aktivität anlegen, im Reiter „Vorlagensätze" das Terminfinder-Preset importieren.
2. **Termine eintragen**: Die vorgeschlagenen Termine werden im Feld "events" hinterlegt, im Format `YYYY-MM-DDTHH:MM` (z. B. `2026-06-15T14:00`) für Termine mit Uhrzeit oder `YYYY-MM-DD` für ganztägige Termine. Für eine bequeme Eingabe der Termine gibt es ein [Tool von Birgit Lachner](https://codeberg.org/BirgitLachner/Termin-Generator).
3. **Einen Testeintrag anlegen**: Auf „Eintrag hinzufügen" gehen und entweder einen eigenen echten Eintrag machen (die eigene Verfügbarkeit eintragen) oder testhalber ausfüllen.
4. **Einladung verschicken**: Auf der Seite der Listenansicht erscheint nun ein Kasten „E-Mail-Vorlage zum Kopieren". Er enthält einen fertigen Text mit zwei automatisch erzeugten Links:
   - einen Link direkt zum Eintragen der eigenen Verfügbarkeit,
   - einen Link zur aktuellen Gesamtübersicht aller Rückmeldungen.

   Der Text lässt sich per Klick auf „Text kopieren" in die Zwischenablage übernehmen und in eine E-Mail, einen Messenger-Chat oder eine Moodle-Ankündigung einfügen.
5. **Rückmeldungen verfolgen**: Sobald Rückmeldungen eintrudeln, füllt sich die Übersichtstabelle in der Listenansicht. Der am besten passende Termin wird hervorgehoben, für Notizen gibt es ein kleines Kommentar-Icon je Zeile.
6. **Termin fixieren**: Über den Zähler in der Zeile „Anzahl" lässt sich der gewünschte Termin direkt als Kalendereintrag exportieren.

### Handhabung für Teilnehmer

Für alle, die eingeladen werden, ist der Ablauf denkbar einfach:

1. Link aus der E-Mail öffnen (führt direkt zu „Eintrag hinzufügen").
2. Für jeden vorgeschlagenen Termin die Rückmeldung hinterlassen.
3. Optional eine kurze Notiz hinterlassen.
4. Speichern – fertig.

Über die Listenansicht lässt sich jederzeit die aktuelle Gesamtübersicht einsehen, um zu sehen, wie der Stand ist oder ob es schon einen klaren Favoriten gibt.

### Warum in Moodle und nicht in einem externen Tool?

- **Keine zusätzlichen Accounts**: Gewohnte Nutzung der vorhandenen Plattform.
- **Datenschutz**: Die Daten verlassen die Moodle-Instanz nicht.
- **Keine Installation nötig**: Es handelt sich um ein reines Datenbank-Preset, kein zusätzliches Plugin, das erst freigeschaltet werden müsste. Zusätzlich können die üblichen Einstellungen genutzt werden, z. B. Einträge freischalten, Anzahl der Einträge begrenzen, Nutzer anonymisieren usw.

Wer regelmäßig Termine mit größeren Gruppen abstimmen muss, spart sich mit dieser Vorlage den Umweg über externe Terminfindungs-Tools – und bleibt dabei komplett in der gewohnten Lernplattform.


### Datenbankvorlage herunterladen

👉 [https://github.com/fdagner/meetingpoll_moodle-database-preset/releases](https://github.com/fdagner/meetingpoll_moodle-database-preset/releases)
