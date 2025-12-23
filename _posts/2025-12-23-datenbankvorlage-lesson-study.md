---
layout: post
title: Datenbankvorlage Lesson Study
date: 2025-12-23T10:30:00
image: "/assets/images/2025-12-23_lesson_study2.png"
categories:
  - unterricht
  - moodle
---

**Die Moodle-Datenbankvorlage wurde im Rahmen von Lesson Study als digitales Beobachtungsinstrument entwickelt. Sie unterstützt Lehrkräfte dabei, Schülerbeobachtungen während des Unterrichts strukturiert zu erfassen, visuell aufzubereiten und gemeinsam auszuwerten. Durch die Verbindung aus tabellarischer Dokumentation und zeitbasierter Visualisierung entsteht eine gemeinsame Datengrundlage, die den Fokus auf das Lernen der Schüler richtet und die kollegiale Unterrichtsentwicklung unterstützt.**

### Funktionen beim Hinzufügen eines Eintrags
Beim Anlegen eines neuen Eintrags in der Datenbank steht den Nutzern eine Oberfläche zur Verfügung, die das Erfassen, Visualisieren und Nachbearbeiten von Beobachtungen ermöglicht. Während der Unterrichtsbeobachtung können fortlaufend neue Beobachtungen ergänzt werden. Über ein Eingabefenster werden der Zeitpunkt der Beobachtung, der wahrgenommene Grad des Engagements sowie kurze beschreibende Notizen festgehalten. Nach dem Speichern werden die Beobachtungen automatisch in einer Tabelle und gleichzeitig in einem Zeit-Lernaktivitäts-Diagramm dargestellt. So entsteht im Verlauf der Stunde ein visueller Überblick über das Lernverhalten des Schülers. Zusätzlich steht ein Eingabefeld für allgemeine Notizen zur Verfügung.


[![Screenshot Ergebnis an der Tafel festgehalten](/assets/images/2025-12-23_lessonstudy.png)](/assets/images/2025-12-23_lessonstudy.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}


### Einzelansicht

In der Einzelansicht dient das erzeugte Diagramm der Auswertung und Reflexion der einzelnen Beobachtungen. Ergänzend zeigt eine Tabelle alle Beobachtungen in chronologischer Reihenfolge mit Uhrzeit, Engagement-Wert und kommentierenden Notizen. Über ein Ansichtssymbol lassen sich einzelne Beobachtungen in einem Lesemodus öffnen. Zusätzlich kann das Diagramm als SVG-Datei exportiert werden, um es für die gemeinsame Analyse oder Dokumentation im Lesson-Study-Team weiterzuverwenden.


### Listenansicht
[![Screenshot Ergebnis an der Tafel festgehalten](/assets/images/2025-12-23_lessonstudy2.png)](/assets/images/2025-12-23_lessonstudy2.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

In der Listenansicht werden alle Beobachtungsbögen einer Lesson Study zusammengeführt und vergleichend dargestellt. Jede Zeile der Tabelle steht für eine beobachtete Einzelperson und enthält neben dem Namen eine farbliche Kennzeichnung sowie die Anzahl der erfassten Beobachtungen. Zusätzlich ist ersichtlich, wer den jeweiligen Beobachtungsbogen erstellt hat und welche Kommentare von anderen Nutzern hinterlegt wurden.
Zentrales Element der Ansicht ist ein kombiniertes Zeit-Engagement-Diagramm, in dem alle Beobachtungen gemeinsam visualisiert werden. Die Punkte sind farblich den jeweiligen Schülern zugeordnet und zeigen, zu welchen Zeitpunkten welches Engagement wahrgenommen wurde. Gestrichelte Verbindungslinien machen den zeitlichen Ablauf sichtbar. Treffen mehrere Beobachtungen exakt zur gleichen Zeit und mit gleichem Engagement zusammen, werden sie als Cluster dargestellt und können aufgeklappt werden. Ein Klick auf einen Punkt öffnet eine Detailansicht, in der Zeitpunkt, Aktivitäts-Wert und Beobachtungstext angezeigt werden. Für die gemeinsame Auswertung im Lesson-Study-Team kann das gesamte Diagramm als SVG exportiert und weiterverwendet werden:
[![Screenshot Ergebnis an der Tafel festgehalten](/assets/images/2025-12-23_lessonstudy3.svg)](/assets/images/2025-12-23_lessonstudy3.svg){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

### Datenbankvorlage herunterladen

👉 [https://github.com/fdagner/lessonstudy__moodle-database-preset/releases](https://github.com/fdagner/lessonstudy__moodle-database-preset/releases)