---
layout: post
title: "Vis Network mit Moodle-Datenbank"
date: 2024-12-27
categories: [Moodle, BwR]
---

### Neue Datenbankvorlage
[Matthias Giger](https://gigers.com/blog/) hat am 24.12.2024 für die Moodlebande ein verspätetes [Weihnachtsgeschenk angekündigt](https://bildung.social/deck/@matthiasgiger/113707959358693732): Eine Datenbankvorlage auf Basis von vis.js, die seit 26. Dezember verfügbar ist. Das klingt nach einer spannenden Idee!

### Was ist vis-network?
[Vis network](https://visjs.github.io/vis-network/examples/) ist eine JavaScript-Bibliothek, die es ermöglicht, Knoten in einer graphischen Darstellung zu visualisieren. Häufig wird sie für die Darstellung von Netzwerken, Beziehungen oder Hierarchien genutzt. 

### Lehrplanbezug (Beispiel)
Im Lehrplan für Betriebswirtschaftslehre in der 9. Klasse der Realschule Bayern lernen die Schüler die Aufgaben der Unternehmensführung und den hierarchischen Aufbau eines Unternehmens kennen. Ein zentraler Bestandteil ist das Organigramm, das die Struktur und die Leitungssysteme wie Liniensysteme veranschaulicht. Mit vis-network können Schüler interaktive Organigramme erstellen, die die hierarchische Struktur eines Unternehmens anschaulich darstellen. Das Tool ermöglicht es, die verschiedenen Leitungsebenen und ihre Beziehungen dynamisch zu visualisieren und so den komplexen Aufbau eines Unternehmens leichter zu verstehen.

### Argumente für vis-network
Die syntaxgebundene Erstellung, wie sie bei vis-network verwendet wird, hat den Vorteil, dass sich die Schüler gänzlich auf den Inhalt konzentrieren können, anstatt Zeit mit der Gestaltung und Anordnung von Elementen zu verbringen, wie es bei grafischen Tools wie PowerPoint der Fall ist. Die Struktur wird durch die spezielle Syntax klar definiert, was die Darstellung der Hierarchie vereinfacht und eine präzise, nachvollziehbare Gestaltung ermöglicht. Zudem können komplexe, dynamische Beziehungen zwischen verschiedenen Elementen leichter dargestellt und verändert werden, ohne dass man sich mit Layouts und visuellen Feinheiten auseinandersetzen muss.

### Anpassung der Datenbankvorlage
Ich habe die Datenbankvorlage von Matthias Giger [angepasst](/assets/database-presets/Concept-preset-20241227_1029.zip), indem ich statt eines festen "NOMEN VERB NOMEN"-Formats das Trennzeichen \*** implementiert habe. Dies ermöglicht es, auch komplexe Ausdrücke mit Leerzeichen in den Knoten darzustellen. Die angepasste Syntax lautet NOMEN\*\*\*VERB\*\*\*NOMEN. Dieser Ansatz sorgt dafür, dass mehrteilige Begriffe abgebildet werden können, ohne dass die Struktur verloren geht. Das bietet eine größere Flexibilität.

### Beispiel eines Organigramms
Um ein Organigramm zu erstellen, können Schüler die hierarchischen Beziehungen darstellen. Sie beginnen mit der Unternehmensführung an der Spitze und fügen dann die Abteilungsleiter und deren Verantwortungsbereiche hinzu. Für jedes Abteilungsleiter-Element fügen sie die darunter liegenden Positionen hinzu, wie z. B. „Verwaltung“, und „Personalabteilung“. Angegliederte Stabstellen können ebenso implementiert werden.

```
IT-Abteilung***ist angegliedert an***CEO.

CEO***ist***Abteilungsleiter Hubert.

CEO***leitet***Abteilungsleiter Norbert.

CEO***leitet***Abteilungsleiter Dilara.

CEO***leitet***Abteilungsleiter Aileen.

Abteilungsleiter Hubert***leitet***Verwaltung.

Abteilungsleiter Norbert***leitet***Personalabteilung.

Abteilungsleiter Dilara***leitet***Einkauf.

Abteilungsleiter Aileen***leitet***Vertrieb und Marketing.

Verwaltung***beschäftigt***Fritz, Lea, Aleya.

Personalabteilung***beschäftigt***Ahmet, Hans, Lisa.
```
Das Ergebnis sieht dann so aus:

[![Screenshot Beschreibung](/assets/images/2024-12-27-beispiel-organigramm.png)](/assets/images/2024-12-27-beispiel-organigramm.png)

### Vis Network und Datenschutz
Da Vis Network auf eine externe Bibliothek zugreift, stellt sich die Frage, wie personenbezogene Daten geschützt werden. Wenn Inhalte aus externen Quellen geladen werden, könnte dies Nutzerdaten an Dritte weitergeben. Es ist daher wichtig, sicherzustellen, dass alle externen Ressourcen datenschutzkonform eingebunden werden und lokal gespeichert sind. In der Datenbank-Aktivität gibt es ein vorgesehenes Feld für JavaScript. Mit der vis.js-Bibliothek funktioniert das allerdings nicht. 
Das Script muss als externe Verlinkung eingebunden werden:
```javascript
<script type="text/javascript" src="https://unpkg.com/vis-network/dist/vis-network.min.js"></script>
```
In der Vorlage von Matthias Giger wir dies in in der "Vorlage für Einzelansicht" realisiert.

Damit man dies datenschutzkonform umsetzen kann, sind die folgenden Schritte notwendig:

1. Download der Datei [https://unpkg.com/vis-network/dist/vis-network.min.js](https://unpkg.com/vis-network/dist/vis-network.min.js).
2. Oben genannten Code aus der "Vorlage für Einzelansicht" löschen
3. TinyMC-Editor aktivieren (Standardeinstellung).
4. In der Datenbankvorlage auf "Einstellungen" klicken und im Beschreibungsfeld in "Werkzeuge/Medien verwalten" die Datei hochladen.
5. "Medien verwalten" anschießend schließen.
6. Mit Einfügen/Link einen neuen Link anlegen und auf "Repositories durchsuchen..." gehen.
7. Dort findet man unter "Eingebettete Dateien" die eben hochgeladene Datei.
8. Nun setzt man den Link in das Script: 
   
    ```javascript
    <script type="text/javascript" src="https://meinemoodleseite.../.../vis-network.min.js"></script>
    ```
9.  Das Script verbleibt dabei im Feld "Beschreibung" in den Einstellungen der Aktivität.

Der Vorteil ist, dass man die Aktivität kopieren/duplizieren bzw. auch wiederherstellen kann und die js-Datei bleibt erhalten. Der Nachteil ist, dass die js-Bibliothek so nicht in einer Datenbankvorlage mitgegeben werden kann.

### Warum sollte man die Moodle-Aktivität Datenbank hierfür nutzen?
Die Verwendung von Vis Network mit der Moodle-Datenbank bietet zahlreiche Vorteile. Schüler können nicht nur ihre eigenen Abgaben einsehen, sondern auch andere Lösungen diskutieren und kommentieren. Durch die vielseitigen Einstellungsmöglichkeiten können Lehrende verschiedene Aspekte der Abgaben und Interaktionen anpassen. Schüler könnten zum Beispiel ihre eigene Lösung erst einreichen müssen, bevor sie die Lösungen anderer sehen. Diese Funktionen tragen zu einer individuellen und kooperativen Lernumgebung bei, ohne dass zusätzliche visuelle Darstellungen oder externe Tools erforderlich sind.

### Fazit
Die Nutzung von Vis Network in Moodle fördert aktives, selbstständiges Arbeiten der Schüler und ermöglicht eine interaktive und kooperative Lernumgebung. Durch datenschutzkonforme Implementierung bleiben die Vorteile erhalten, ohne gegen Datenschutzrichtlinien zu verstoßen.

---
#### Anlagen
- [Angepasste Datenbankvorlage](/assets/database-presets/Concept-preset-20241227_1029.zip) (nicht datenschutzkonform)