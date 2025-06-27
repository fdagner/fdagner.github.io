---
layout: post
title: "SCORM für Moodle erstellen (experimentell)"
date: 2025-06-27T08:00:00
image: "/assets/images/2025-06-27_scorm.png"
categories:
  - Moodle
---
**Kann man nicht einfach ein kleines Spiel bauen, bei dem Schüler Punkte sammeln – und Moodle übernimmt die Bewertung? Diese Frage tauchte beim letzten Moodle-Meeting auf. Besonders spannend ist die Idee, einfache Browser-Spiele mit automatischer Punkteübertragung zu kombinieren – ideal für Gamification, Wiederholungen oder als kleine Motivation zwischendurch.**

### SCORM – Was ist das?
Ein SCORM-Paket ist im Grunde nur ein ZIP-Archiv mit HTML-Dateien, einer `imsmanifest.xml` und ein paar technischen Angaben. Man kann es komplett selbst bauen – oder einfacher: ein vorhandenes Beispiel nehmen und anpassen oder es einer KI überlassen.


### So funktioniert's

Ein SCORM-Paket ist technisch gesehen nur ein ZIP-Archiv mit folgendem Aufbau:

```
/deinspiel.html
/scormapiwrapper.js
/imsmanifest.xml
```

Die notwendigen Bestandteile:

1. Deine HTML-Datei mit dem Spiel oder Inhalt  
2. JavaScript-Code, der mit der SCORM-API kommuniziert  
3. Eine imsmanifest.xml, die SCORM und Moodle die Struktur erklärt  

### Eigenes Projekt anpassen
Wenn man sein eigenes SCORM-Spiel erstellen will, solltest man im Wrapper die `setScore`-Funktion so anpassen:

```js
setScore: function(score, maxScore = 10) {
  if (!initialized) return false;
  
  API.LMSSetValue("cmi.core.score.max", maxScore.toString());
  API.LMSSetValue("cmi.core.score.min", "0"); // Optional
  API.LMSSetValue("cmi.core.score.raw", score.toString());
  
  return API.LMSCommit("") === "true";
}
```
Der Aufruf im Spiel könnte dann z. B. so aussehen:

```js
SCORM.setScore(punkte, 10); // Maximal 10 Punkte
```
Am Spielende sollte Folgendes passieren:

```js
function spielBeenden(punkte) {
  SCORM.setScore(punkte, 10);  // Punkte übergeben
  SCORM.setCompleted();        // Status setzen (alternativ: setPassed())
  SCORM.finish();              // Sitzung beenden
}
```

🔗 **GitHub-Repository**  
👉 [https://github.com/fdagner/zahlen_raten_scorm](https://github.com/fdagner/zahlen_raten_scorm)

Dieses Repository enthält ein Beispiel für ein SCORM-kompatibles Spiel mit Punkteübertragung nach Moodle. In den Einstellungen in Moodle sollte man "Beste Bewertung" auf den Wert 10 stellen.

[![Screenshot Scorm](/assets/images/2025-06-27_scorm.png)](/assets/images/2025-06-27_scorm.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}







