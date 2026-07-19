---
layout: post
title: Updates Datenbankvorlagen Juni 2026
date: 2026-06-28T9:00:00
image: "/assets/images/2026-06-10_selbstregulation.png"
categories:
  - moodle
---

**Ein paar Neuerungen in den Datenbankvorlagen Graph, Mindmap und Exit-Ticket.**

## 1. Graph

Die [Vorlage "Graph"](https://github.com/fdagner/graph__moodle-database-preset) visualisiert Zuordnungen zu Kategorien als Graph. Knoten verbinden sich zum Beispiel nach gemeinsamen Interessen. 

[![Screenshot Aufgabe](/assets/images/2026-06-28_graph2.png)](/assets/images/2026-06-28_graph2.png){: style="width: 100%;max-width: 750px;display: block; margin: 0 auto"}


### Neue Funktionen

- Bisher mussten neue Felder an mehreren Stellen in den Templates manuell eingetragen werden. Jetzt reicht es, in der Moodle-Datenbankaktivität ein neues (und geeignetes) Feld anzulegen oder zu löschen – die Vorlage erkennt es automatisch und nimmt es in den Graph auf. Es ist kein Anpassen von Code nötig.
- Ein Klick auf den Detektiv-Button in der Toolbar blendet alle Namen im Graph aus – die Verbindungen zu den Kategorie-Knoten bleiben sichtbar. Man kann dann anhand der Merkmale raten, wer sich hinter welchem Fragezeichen verbirgt. Ein Klick auf das „?" deckt den Namen auf.

[![Screenshot Aufgabe](/assets/images/2026-06-28_graph.png)](/assets/images/2026-06-28_graph.png){: style="width: 100%;max-width: 750px;display: block; margin: 0 auto"}


## 2. Mindmap
Mit der [Vorlage "Mindmap"](https://github.com/fdagner/mindmap_moodle-database-preset-) können Nutzer Mindmaps erstellen, die in der Listenansicht zu einer gemeinsamen Mindmap kombiniert werden können.

[![Screenshot Aufgabe](/assets/images/2026-06-28_mindmap.svg)](/assets/images/2026-06-28_mindmap.svg){: style="width: 100%;max-width: 750px;display: block; margin: 0 auto"}

### Neue Funktionen
- Neuer Import-Button im Bearbeiten-Modus unterstützt Import von Mermaid-Mindmap-Code. Knotenformen (root((...)), [...], {{...}} usw.) werden dabei bereinigt; ::icon(...), %%-Kommentare und Klassendirektiven werden übersprungen.
- Knoten sind nun direkt in der Mindmap verschiebbar (kein Wechsel in den Listenmodus nötig). 
- Neuer Hilfe-Button zeigt eine Kurzanleitung an.


## 3. Exit-Ticket
Mit der [Vorlage "Exit-Ticket"](https://github.com/fdagner/exitticket_moodle-database-preset) können Schüler Exit-Tickets erstellen. Exit-Tickets sind kurze Aufgabenstellungen, die am Ende einer Unterrichtseinheit eingesetzt werden können.

### Neue Funktionen
Die Feedansicht wurde durch eine Kachelansicht ersetzt. Eingetragene Kategorien werden markiert angezeigt, der Eintrag ist per Modal aufrufbar.