---
layout: post
title: "Dinge geregelt kriegen: #2 Die Wiedervorlage in Obsidian"
date: 2025-02-10 20:00:00 +0100
categories:
  - Obsidian
---

Obsidian ist ein großartiges Tool zur Organisation von Notizen, aber es kann auch dabei helfen, Dinge nicht aus den Augen zu verlieren. Eine wichtige Methode dafür ist die **Wiedervorlage** – also die Möglichkeit, sich Notizen oder Aufgaben an einem bestimmten Datum automatisch wieder anzeigen zu lassen.

## Warum eine Wiedervorlage nützlich ist

Kennst du das? Du machst dir Notizen zu einer Fortbildung, einem geplanten Telefonat oder einer Aufgabe, die du irgendwann erledigen musst – aber wenn der richtige Zeitpunkt kommt, hast du sie längst vergessen oder suchst ewig danach. Eine Wiedervorlage löst dieses Problem, indem sie relevante Notizen oder Aufgaben automatisch an dem Tag anzeigt, an dem du sie brauchst.

Das hilft bei:  
✅ **Terminen**: Eine Notiz zu einer Fortbildung kann am Veranstaltungstag wieder auftauchen – mit Link zum Material und Skript.  
✅ **Aufgabenplanung**: Eine Aufgabe, die nicht sofort erledigt werden muss, kann für einen späteren Tag vorgemerkt werden.  
✅ **Geplanten Telefonaten**: Wichtige Informationen oder Fragen für das Gespräch sind direkt zur Hand.  
✅ **Langfristigen Projekten**: Einzelne Meilensteine oder nächste Schritte tauchen zum richtigen Zeitpunkt auf.

### **Welche Plugins sind nötig?**

✅ **Daily Notes** → Erstellt automatisch eine neue Tagesnotiz mit aktuellem Datum.  
✅ **Dataview** → Listet Notizen, die für das heutige Datum relevant sind.  
✅ **Tasks** → Zeigt geplante Aufgaben für den aktuellen Tag an.

### Notizen mit Wiedervorlage abrufen (Dataview)

```
> [!CAUTION] Wiedervorlage
> ```dataview
> LIST
> FROM ""
> WHERE Datum = date(this.file.name) OR Wiedervorlage = date(this.file.name) 
> ```
> 
> ```tasks
> filter by function task.scheduled.moment?.isSame(moment('{{title}}'), 'day') || false
>
```

Damit die **Wiedervorlage** funktioniert, müssen die **Eigenschaften (Meta-Daten)** in den Notizen gespeichert sein. Diese Meta-Daten stehen immer am Anfang einer Notiz im YAML-Format und sehen so aus:

```
--- 
Datum: 2025-03-15
---
```

<div class="youtube-placeholder" data-video="VIDEO-ID"> <button onclick="loadYouTube(this)">Video laden</button> </div> 

<script> function loadYouTube(button) { var videoId = button.parentElement.getAttribute("data-video"); var iframe = document.createElement("iframe"); iframe.setAttribute("width", "560"); iframe.setAttribute("height", "315"); iframe.setAttribute("src", "https://www.youtube-nocookie.com/embed/" + videoId + "?autoplay=1"); iframe.setAttribute("frameborder", "0"); iframe.setAttribute("allowfullscreen", "true"); button.parentElement.replaceWith(iframe); } </script>