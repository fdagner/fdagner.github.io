---
layout: post
title: Datenbankvorlage Lernhilfen
date: 2025-11-01T10:30:00
image: "/assets/images/2025-11-01_lernhilfe.png"
categories:
  - OER
  - moodle
---

**Auf den schule.digital-Tagen 2025 besuchte ich zwei Inputs: „Gestufte Hilfen“ und „Gestaltung differenzierter Lernwege“. Beide Inputs stellten die Frage in den Mittelpunkt, wie Schüler individuelle Unterstützung erhalten. Judith Birke zeigte auf der MoodleMoot Global 2025 zudem die Lernhilfen-Datenbank als Beispiel – Grund genug, die bestehende, technisch veraltete Vorlage in Moodle zu reaktivieren und zu überarbeiten.**

### Wofür sind Lernhilfen gedacht?
Schüler können sich schnell Unterstützung holen und:
- gestufte Hilfen erhalten
- das nutzen, was sie gerade brauchen
- im eigenen Tempo lernen

Die Aktivität unterstützt damit Selbstregulation, Differenzierung und selbstständiges Lernen.

### Glossar oder Datenbank?
Das Moodle-Glossar mit Autoverlinkung ist für klassische Begriffe sehr praktisch: Einträge werden automatisch im Kurs verlinkt und standardmäßig unterstützt. Für komplexere Lernhilfen stößt es jedoch an seine Grenzen: gestufte Hilfen oder ausklappbare Einträge sind nicht so einfach möglich, QR-Codes können nicht automatisch erzeugt werden und die Eingabemaske ist weniger flexibel.

Bei der Lernhilfen-Datenbank kann jeder Eintrag zwei getrennte Hilfen sowie eine optionale Lösung enthalten. Die Lösung kann ausgeblendet werden und QR-Codes sowie Direktlinks werden automatisch erzeugt, sodass Schüler Inhalte bequem scannen oder anklicken können. Hier wird die Verbindung zur analogen Lernwelt hergestellt.  Das Layout mit Accordeon-Funktion sorgt für Übersichtlichkeit, und die Eingabemaske ist vollständig anpassbar.

[![Screenshot Beispiel](/assets/images/2025-11-01_lernhilfe.png)](/assets/images/2025-11-01_lernhilfe.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

### Funktionsumfang auf einen Blick

- **Bis zu zwei Hilfen + Lösung pro Eintrag**  
  Richtet sich an unterschiedliche Kompetenzniveaus und Art der Eintragung

- **Lösung durch Lehrkraft ausblendbar**  
  Verhindert sofortiges Nachschlagen der Lösung

- **QR-Code & Direktlink automatisch**  
  Scannen oder klicken – beides möglich

- **Schüler dürfen Einträge erstellen**  
  Aktivierung, kooperatives Arbeiten

- **Kommentare optional**  
  Peer-Feedback & kollaboratives Lernen

- **Freischaltfunktion**  
  Lehrkraft behält die Qualität im Blick


### Einsatzszenarien
- Unterstützung in Selbstlernphasen
- Hilfe bei Arbeitsblättern (Scannen statt Nachfragen)
- Stationenlernen oder Rallyes
- Fachübergreifend einsetzbar

### Überarbeitung
Die ursprüngliche Version war bereits einige Jahre alt und nicht mehr aktuell – insbesondere, weil die QR-Codes über eine externe API generiert wurden. Die QR-Codes werden nun lokal erzeugt. Die Kompatibilität zur aktuellen Bootstrap-Version wurde ebenso hergestellt. Neben dem QR-Code kann nun auch der Direktlink zum Datenbankeintrag kopiert werden.

Mit einem Klick auf die Überschrift erhält man sofort den Link als Text oder QR-Code:

[![Screenshot Beispiel](/assets/images/2025-11-01_lernhilfe2.png)](/assets/images/2025-11-01_lernhilfe2.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

### Vorlage herunterladen
👉 [Download der Vorlage über GitHub](https://github.com/fdagner/learningaids_moodle-database-preset/releases/)