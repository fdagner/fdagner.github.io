---
layout: post
title: Python Web Editor
date: 2025-03-08T12:30:00
categories:
  - OER
  - Unterricht
---

## Einleitung

**Zum Halbjahr habe ich die Schule gewechselt und kurzfristig eine 8. Klasse im Fach Informationstechnologie übernommen. Im Modulverteilungsplan steht jetzt das "Modellieren und Codieren von Algorithmen" an. Die Schüler brauchen eine einfache Möglichkeit, um erste Programmiererfahrungen zu sammeln – idealerweise direkt in der ByCS-Lernplattform, die ich für meine Kurse ohnehin nutze.**

**In der Schule setzen wir auf Python als Programmiersprache, und die Schulrechner sind bereits entsprechend ausgestattet. Trotzdem ist es praktisch, wenn Schüler unabhängig von der Schulsoftware arbeiten können. Ein passendes Tool zu finden, das sowohl niederschwellig als auch datenschutzkonform ist, war gar nicht so einfach. Schließlich habe ich mich für eine Lösung mit [Brython](https://brython.info) entschieden.**

## Modellieren und Codieren von Algorithmen

Im Rahmen des Moduls 2.6.1 sollen die Schüler:

- algorithmische Grundbausteine und Notationsformen nutzen, um Abläufe strukturiert darzustellen,
- auf Basis von Modellen Quellcode in einer Entwicklungsumgebung schreiben,
- mit Variablen, Datentypen, Funktionen und Kommentaren arbeiten,
- ihre Programme überprüfen und Fehler beheben.
    
Hierfür werden verschiedene Notationsformen (z. B. Struktogramme, Pseudocode, Programmablaufpläne) sowie eine textuelle Programmiersprache verwendet. Eine zentrale Rolle spielt dabei eine geeignete Entwicklungsumgebung.

## Einen Python-Editor integrieren

Gerade zur Einführung ist es sinnvoll, dass Schüler ohne große Hürden erste Programmiererfahrungen sammeln können. Perfekt abgestimmt wäre also eine Lösung, die sich nahtlos in den Kurs der Lernplattform einbinden ließe. 


### Python-Editor mit Brython

[Brython](https://brython.info) ist eine Implementierung von Python 3 für den Browser. Dadurch können Schüler direkt in der ByCS-Lernplattform Python-Code schreiben und ausführen, ohne zusätzliche Software zu installieren. Der an die Lernplattform angepasste Editor basiert über GitHub verfügbar: [GitHub-Projekt: Python Web Editor](https://github.com/fdagner/python_web_editor/tree/main). Der Editor kann auch [direkt getestet werden](https://oer.fdagner.de/python_web_editor/?file=hello.py).

[![Screenshot Python Editor](/assets/images/2025-03-06-python-web-editor.png)](/assets/images/2025-03-06-python-web-editor.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

### Funktionsweise und Features des Editors

### Code Editing mit Ace Editor
Der Editor nutzt den Ace Editor mit Syntaxhervorhebung für Python. Dadurch wird der Code besser lesbar und die Schüler können Fehler leichter erkennen.

### Automatische Code-Speicherung
Der Code wird automatisch im lokalen Speicher des Browsers gespeichert. Dadurch bleibt der Fortschritt erhalten, auch wenn die Seite neu geladen wird.

### Datei-Handling
- Wenn eine Datei über eine URL-Parameter (z. B. `?file=myscript.py`) angegeben wird, lädt der Editor die entsprechende Datei aus dem `py/`-Verzeichnis des Servers.
- Der Code kann als `.py`-Datei über einen Download-Button heruntergeladen werden.
    
### Python-Code ausführen
Der Python-Code kann direkt im Browser mit Brython ausgeführt werden. Beim Klick auf den „Run“-Button wird das Skript ausgeführt, und die Ausgabe erscheint im Ausgabecontainer. Fehler werden ebenfalls angezeigt.

### Reset-Funktion
Der „Reset“-Button leert den Editor und entfernt den gespeicherten Code aus dem lokalen Speicher. Falls eine Datei aus dem Server geladen wurde, wird sie erneut geladen.

### Vollbildmodus
Ein Klick auf den „Fullscreen“-Button ermöglicht den Vollbildmodus, um den Editor zu maximieren und die Code-Eingabe angenehmer zu gestalten.

### Code-Ausgabe
Die Ausgabe des ausgeführten Codes erscheint in einem separaten Bereich. Falls Fehler auftreten, werden sie dort ebenfalls ausgegeben.

### Debugging
- Es kann ein Haltepunkt gesetzt werden.
- Der Code wird inklusive der Haltepunkte-Zeile ausgeführt, sodass Schüler gezielt bestimmte Abschnitte inspizieren können.

### Integration in die Lernplattform (Norbert-Forster-Methode)

Der Editor kann unkompliziert in die ByCS-Lernplattform integriert werden, indem er als ZIP-Datei hochgeladen und in Moodle entpackt wird. Anschließend wird die `index.html` als Hauptdatei gesetzt. Der Link zur `index.html` kann dann überall im Kurs als Inlineframe eingebunden werden, sodass die Schüler direkt darauf zugreifen können.

Dank des URL-Parameters können immer wieder kleinere Aufgaben und Vorlagen den Schülern bereit gestellt werden.

[![Screenshot Python Editor](/assets/images/2025-03-06-python-web-editor-aufgabe.png)](/assets/images/2025-03-06-python-web-editor-aufgabe.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

## Didaktische Konzeption – Vorteile und Nachteile

### Vorteile:


- **Niedrigschwelliger Einstieg**: Schüler können sofort loslegen, ohne Setups oder Installationen.
- **Plattformunabhängig**: Funktioniert auf jedem Gerät mit einem modernen Browser.
- **Integrierbar in die ByCS-Plattform**: Einfach als eingebettetes Element nutzbar in den verschiedenen Aktivitäten.
    
### Nachteile:

- **Eingeschränkte Debugging-Möglichkeiten**: Kein vollwertiges Debugging wie in einer klassischen Entwicklungsumgebung.
- **Nicht für produktive Entwicklung geeignet**: Komplexere Projekte sollten in einer echten Entwicklungsumgebung wie Python IDLE durchgeführt werden.
    

Daher ist es sinnvoll, den Editor für erste Schritte und kleinere Übungen zu nutzen, während für weiterführende Projekte eine echte Entwicklungsumgebung verwendet wird.

## Fazit

Die Integration eines Python-Editors in die ByCS-Lernplattform ermöglicht einen unkomplizierten Einstieg in die textuelle Programmierung. Durch den Einsatz von [Brython](https://brython.info) in einem lokalen Setting kann ein datenschutzfreundliches und niederschwelliges Tool bereitgestellt werden, das sich gut für den Schulalltag eignet.