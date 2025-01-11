---
layout: post
title: "Lernvideos transkribieren"
date: 2025-01-10 22:00:00 +0100
categories: [H5P, KI]
---
**Video-Inhalte bieten zahlreiche Vorteile für den Unterricht, insbesondere bei der Vermittlung komplexer Themen. Barrierefreiheit ist ein zentraler Aspekt der Bildung und gesetzliche Anforderung in vielen Ländern. Besonders bei Videos spielen Transkripte eine entscheidende Rolle, um den Inhalt für alle zugänglich zu machen – sei es für Menschen mit Hörbeeinträchtigungen oder alle, die lieber Text lesen. Ebenso ist es für Nicht-Muttersprachler von großer Bedeutung, Inhalte in mehreren Sprachen zur Verfügung zu stellen. Die Verwendung von Transkripten fördert nicht nur das Verständnis der Inhalte, sondern trägt auch zu einer inklusiven und interaktiven Lernumgebung bei.**

Die Integration von Transkripten in interaktive Formate wie H5P erhöht die Lernmotivation und sorgt für eine tiefere Auseinandersetzung mit dem Fachinhalt. Eine effektive Möglichkeit, um diese Transkriptionen zu erstellen, ist der Einsatz von <i>Buzz</i>.

### Buzz einrichten
Zunächst wird [Buzz](https://chidiwilliams.github.io/buzz/docs) auf dem Computer installiert. 

>Tipp: Laden Sie Buzz nicht über den App Store von Apple herunter, da dort das Programm kostenpflichtig ist. Für Apple sowie auch für Linux und Windows gibt es im [GitHub-Repo](https://github.com/chidiwilliams/buzz) das Programm kostenlos zum Herunterladen.

In der Anwendung kann man eine Video-Datei über das Menü importieren oder einfach in die Arbeitsfläche ziehen. Nach dem Hochladen des Videos wählt man ein Modell aus. Ich habe das <i>Whisper Large-V3-Turbo-Modell</i> gewählt, da es eine hohe Genauigkeit bei der Spracherkennung bietet. Buzz beginnt nach dem Herunterladen des Modells automatisch mit der Transkription des Inhalts.

![Bildschirmabdruck von Buzz](/assets/images/2025-01-10-buzz.png){: style="width: 600px;display: block; margin: 0 auto"}

### VTT-Datei exportieren
Sobald die Transkription abgeschlossen ist, kann man mit einem Doppelklick auf den aktuellen Prozess das Transkript als VTT-Datei (Video Text Track) exportieren. Dieses Format ist mit vielen Video-Playern kompatibel und ermöglicht eine einfache Synchronisation der Texte mit dem Video. Die VTT-Datei wird auf dem Computer gespeichert.

### Transkript übersetzen
Die VTT-Datei kann mit einem Texteditor geöffnet und mithilfe einer Text-KI übersetzt werden, beispielsweise ins Englische. Mit einer Open-AI-API lässt sich die Übersetzung direkt in Buzz durchführen. Die übersetzte Datei wird anschließend in einer separaten Datei gespeichert.

### Transkript in H5P importieren
In [Lumi H5P Desktop](https://lumi.education/de/lumi-h5p-desktop-editor/) wählt man den Inhaltstyp „Interaktives Video“. Die zuvor exportierte VTT-Datei wird unter dem Klappmenü „Textspuren“ importiert. Es ist möglich, mehrere Textspuren hinzuzufügen und die Sprache jeder Spur zu spezifizieren. Ohne weitere Angaben ist die erste Textspur die Standardspur.

Ein Beispiel kann auf [ZUMApps](https://apps.zum.de/apps/38165) angesehen werden:

[![Bildschirmabdruck von ZUMApps](/assets/images/2025-01-10-h5p.png)](https://apps.zum.de/apps/38165){: style="width: 600px;display: block; margin: 0 auto"}

<i>Hinweis: ZUMApps akzeptiert (derzeit?) keine VTT-Dateien. Eine Lösung war, die Dateien vor dem Upload in .txt-Dateien umzubenennen.</i>

### Fazit
Die Möglichkeit, Transkripte in verschiedenen Sprachen bereitzustellen, fördert die Integration und Inklusion im Bildungsbereich. Besonders die Integration von interaktiven Elementen in H5P stellt sicher, dass der Lernprozess sowohl ansprechend als auch barrierefrei gestaltet wird. 
