---
layout: post
title: "Effiziente Nutzung von KI für die Erstellung von Moodle-Inhalten"
date: 2024-12-28 13:33:00 +0100
categories: [Moodle, KI]
---

### Herausforderungen beim Erstellen von Inhalten mit KI
Angenommen, wir möchten ein Glossar zu den wesentlichen Begriffen des Grundgesetzes erstellen, das später in Moodle für Spiele, Tests und H5P verwendet werden soll. Die Erstellung von Inhalten dieser Moodle-Aktivitäten kann herausfordernd sein, insbesondere wenn es um die Einhaltung spezifischer Syntaxanforderungen geht. Auch wenn KI-Modelle immer leistungsfähiger werden, gibt es nach wie vor Probleme bei der Generierung fehlerfreier und strukturiert korrekter Daten.

[![Glossar zum Grundgesetz](/assets/images/2024-12-28-grundgesetz.png)](/assets/images/2024-12-28-grundgesetz.png)

*Inhalte für ein Glossar in Moodle können leicht mit der KI generiert werden, die XML-Syntax ist aber komplex und die benötigte Ausgabe des Textes sehr lang.*

#### Strikte Syntaxanforderungen
Die Erstellung strukturierter Inhalte wie XML-Dateien (für Moodle-Glossare), Testfragen oder H5P-Syntax durch KI kann durch kleine Fehler in der Formatierung, wie zum Beispiel fehlende schließende Tags oder Attribute, zum Scheitern führen. Auch wenn KI-Modelle immer präziser werden, ist es schwierig, eine fehlerfreie Syntax zu gewährleisten, vor allem bei komplexeren Formaten.

#### Herausforderung des Promptings
Um der KI klare Vorgaben zu machen, sind präzise Prompts erforderlich. Ein zu allgemeiner Prompt kann zu unstrukturierten und fehlerhaften Ausgaben führen. Trotz präziser Anweisungen bleibt das Risiko von Fehlern, insbesondere bei komplexeren und verschachtelten Strukturen.

#### Hoher Ressourceneinsatz der KI-Nutzung
KI-Modelle erfordern erhebliche Rechenressourcen, was den Einsatz der Technologie nicht nur technisch anspruchsvoll, sondern auch ressourcenintensiv macht. Daher sollte KI nur dann eingesetzt werden, wenn es wirklich notwendig ist, um nicht unnötige Energie zu verbrauchen.

### CSV-Moodle-Konverter
Ein effektiver Ansatz zur Minimierung des Ressourcenaufwands ist die Verwendung von CSV-Dateien, die von der KI generiert werden. Diese können dann "offline" weiterverarbeitet werden, um die spezifische Moodle-Syntax zu erfüllen. 

Der [CSV-Moodle-Konverter](/csv-moodle-konverter) erleichtert diesen Prozess, indem er automatisch die notwendigen Formate erstellt, die für die Nutzung in Moodle erforderlich sind.

#### Importdatei für Glossar
Die CSV-Daten werden so umgewandelt, dass sie direkt in ein Moodle-Glossar importiert werden können.

#### Text für H5P
Es wird ein Text erstellt, der in H5P-Aktivitäten wie "Fill in The Blanks" oder "Drag the Words" verwendet werden kann. Die Begriffe werden in Textlücken umgewandelt, die für diese interaktiven Übungen verwendet werden können.

#### Importdatei für Tests
Aus den CSV-Daten werden automatisch Fragen im GIFT-Format erstellt. Diese können direkt in die Moodle-Testaktivität importiert werden.

### Beispiel
Mit einem einfachen Prompt kann eine KI die benötigten Daten generieren:

> Erstelle ein Glossar zu den wesentlichen Begriffen des Grundgesetztes. Das Glossar soll als csv wie folgt aufgebaut sein: Begriff; Definition. Der Begriff darf nicht in der Definition vorhanden sein. Erstelle 30 Glossareinträge zeilenweise.
>

Das Ergebnis könnte folgendermaßen aussehen:

```
Begriff;Definition
Menschenwürde;Der unveräußerliche Kern, der jedem Menschen ein unantastbares Dasein garantiert.
Grundrechte;Die zentralen Freiheiten und Rechte, die allen Menschen zustehen und den Staat binden.
Freiheitsrechte;Schutz vor staatlichen Eingriffen in das private und öffentliche Leben.
Gleichheitsgrundsatz;Das Prinzip, dass alle Menschen vor dem Gesetz gleich sind.
Rechtsstaat;Ein System, in dem die Ausübung staatlicher Gewalt durch Gesetze begrenzt ist.
Demokratie;Eine Herrschaftsform, in der die Macht vom Volk ausgeht.
Bundesstaat;Eine Staatsform, die aus mehreren teilsouveränen Gliedstaaten besteht.
Republik;Eine Staatsform ohne Monarchen, in der die Macht durch gewählte Vertreter ausgeübt wird.
Ewigkeitsklausel;Die Regelung, dass bestimmte Verfassungsgrundsätze nicht abgeschafft werden dürfen.
Meinungsfreiheit;Das Recht, eigene Ansichten ohne staatliche Zensur zu äußern.
Pressefreiheit;Das Recht von Medien, unabhängig und ohne staatliche Kontrolle zu berichten.
Versammlungsfreiheit;Die Möglichkeit, sich friedlich und ohne Waffen zu treffen.
Religionsfreiheit;Die Freiheit, eine Glaubensrichtung zu wählen oder keine zu haben.
Berufsfreiheit;Das Recht, einen Beruf frei zu wählen und auszuüben.
Eigentumsgarantie;Die rechtliche Sicherung von privatem Besitz.
Asylrecht;Der Schutz für Verfolgte, die in einem anderen Land Zuflucht suchen.
Wahlrecht;Die Befugnis, an politischen Abstimmungen teilzunehmen.
Gewaltenteilung;Die Aufteilung der Staatsgewalt auf verschiedene unabhängige Organe.
Gesetzgebung;Der Prozess, durch den verbindliche Regeln geschaffen werden.
Exekutive;Die ausführende Gewalt, die die Gesetze umsetzt.
Judikative;Die rechtsprechende Gewalt, die die Einhaltung der Gesetze überwacht.
Legislative;Die gesetzgebende Gewalt, die Vorschriften beschließt.
Bundestag;Das zentrale Parlament, das die Interessen der Bürger vertritt.
Bundesrat;Die Institution, die die Länder auf Bundesebene repräsentiert.
Verfassungsgericht;Das höchste Gericht, das über die Einhaltung der Grundordnung wacht.
Sozialstaat;Ein Staat, der soziale Sicherheit und Gerechtigkeit fördert.
Schutz der Familie;Die Förderung und Anerkennung familiärer Gemeinschaften.
Kinderrechte;Die besonderen Freiheiten und Schutzansprüche von Minderjährigen.
Bundespräsident;Das Staatsoberhaupt, das repräsentative Aufgaben übernimmt.
Wehrpflicht;Die gesetzliche Pflicht zur Verteidigung des Staates.
```
Die Daten können dann mit dem [CSV-Moodle-Konverter](/csv-moodle-konverter) in verschiedene Formate konvertiert werden.
Mit einer einzigen KI-generierten CSV hat man die folgenden Möglichkeiten:

- Glossar
- Spiele aus Glossar (Hangman, Kreuzworträtsel...)
- Übung in H5P
- Test

[![Kreuzworträtsel aus Glossar](/assets/images/2024-12-28-grundgesetz-game.png)](/assets/images/2024-12-28-grundgesetz-game.png)

*Spiele und Rätsel können in Moodle direkt aus Glossaren oder Fragensammlungen erstellt werden.*


[![Kreuzworträtsel aus Glossar](/assets/images/2024-12-28-grundgesetz-h5p.png)](/assets/images/2024-12-28-grundgesetz-h5p.png)

*Die Syntax für H5P-Lückentexte ist noch relativ einfach...*

[![Kreuzworträtsel aus Glossar](/assets/images/2024-12-28-grundgesetz-test.png)](/assets/images/2024-12-28-grundgesetz-test.png)

*...aus der selben CSV lassen sich aber auch Kurzantwortfragen für den Test erstellen, deren Syntax etwas komplexer ist.*

### Fazit
Die Verwendung von KI zur Erstellung strukturierter Inhalte erfordert ein Bewusstsein für die Stärken und Schwächen der Modelle. Während die Erstellung von CSV-Dateien aufgrund ihrer Einfachheit weniger problematisch ist, benötigen komplexere Formate präzise Prompts und nachgelagerte Validierung. Ein bewusster und ressourcenschonender Einsatz von KI kann nicht nur zu besseren Ergebnissen führen, sondern auch den Energieverbrauch und die Umweltbelastung durch hohe Rechenleistung minimieren.