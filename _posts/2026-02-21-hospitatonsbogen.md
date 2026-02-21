---
layout: post
title: Hospitationsbogen
date: 2026-02-21T19:30:00
image: "/assets/images/2026-02-21_hospitation.png"
categories:
  - unterricht
---

**Der Beurteilungszeitraum ist bald vor dem Abschluss und ich brauchte ein zuverlässiges Tool für Hospitationen – einen strukturierten Bogen, der Ankreuzoptionen für schnelle Einschätzungen bietet, aber auch Freiraum für Notizen lässt.**

Die Idee entstand aus der Notwendigkeit, Hospitationen effizienter zu gestalten: Ich wollte einen [digitalen Bogen als Browsertool](https://oer.fdagner.de/hospitation/) programmieren, der vollständig lokal und geräteunabhängig im Browser läuft. Kein Server, keine Cloud – alle Daten werden sicher im Browser gespeichert, via LocalStorage, was Offline-Nutzung ermöglicht und Datenschutz gewährleistet. Zusätzlich soll es als Progressive Web App (PWA) installiert werden können, um es wie eine native App offline zu nutzen. So kann man unterwegs hospitieren, ohne Abhängigkeit vom Internet.

 In der Konzeption startete ich mit dem [K+5-Modell](https://mebis.bycs.de/digitale-schule-der-zukunft/leitfaden/unterricht/impulse-fuer-die-unterrichtsentwicklung-setzen/gemeinsames-qualitaetsverstaendnis-fuer-unterricht-mit-digitalen-medien), das ich implementierte, um digitale Elemente im Unterricht zu betonen. Es wurde bei ersten Besuchen getestet, fühlte sich aber oft unpassend an – zu ungenau, nicht immer auf das Wesentliche fokussiert und schwer anzuwenden. Deshalb wechselte ich zum [Unterrichtsfeedbackbogen Tiefenstrukturen (UFB) des IBBW](https://ibbw-bw.de/Lde/Startseite/Empirische-Bildungsforschung/unterrichtsfeedbackbogen_tiefenstrukturen), der aus empirischer Bildungsforschung stammt. Er fragt gezielt nach Kernaspekten wie kognitive Aktivierung, Unterstützung und Klassenführung, ist praxisnah und unterstützt Unterrichtsentwicklung durch fundierte Feedbacks.

 [![Screenshot Auswertung](/assets/images/2026-02-21_hospitation2.png)](/assets/images/2026-02-21_hospitation2.png){: style="width: 100%;max-width: 600px;display: block; margin: 0 auto"}

[Hospitation](https://oer.fdagner.de/hospitation/) bietet folgende Features: 
- Erfassung und Speicherung der Stammdaten (Klasse, Fach, Lehrer), des Stundenverlaufs mit Sozialformen, Freitextfeldern für Notizen und Upload von Fotos.
- Strukturierte Bewertung der Tiefenstrukturen.
- Visuelle Auswertungen mit Diagrammen für schnelle Übersichten. 
- Export der Ergebnisse: Drucken, als PDF exportieren, lokal als JSON sichern oder als Markdown ausgeben.

[![Screenshot Auswertung](/assets/images/2026-02-21_hospitation.png)](/assets/images/2026-02-21_hospitation.png){: style="width: 100%;max-width: 600px;display: block; margin: 0 auto"}


### Repository

👉 [https://github.com/fdagner/hospitation](https://github.com/fdagner/hospitation)