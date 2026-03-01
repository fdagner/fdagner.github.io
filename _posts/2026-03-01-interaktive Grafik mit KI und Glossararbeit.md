---
layout: post
title: Eine interaktive Grafik mit KI- und Glossararbeit
date: 2026-03-01T14:30:00
image: "/assets/images/images/2026-03-01_ki.png"
categories:
  - unterricht
  - moodle
---

**Im BwR-Unterricht der 7. Klasse geht es an vielen Stellen darum, grundlegende Strukturen von Unternehmen zu verstehen. Ein zentrales Thema sind dabei die Funktionsbereiche eines Unternehmens. Statt diese nur über ein statisches Tafelbild oder ein Arbeitsblatt zu behandeln, lässt sich daraus ein digitales Unterrichtsprojekt entwickeln, das Visualisierung, Zusammenarbeit und KI miteinander verbindet.**


### Ausgangspunkt: Funktionsbereiche eines Unternehmens
Ausgangspunkt ist eine Organigramm-Grafik, die die zentralen Bereiche eines Unternehmens zeigt, etwa Unternehmensleitung, kaufmännische und technische Leitung sowie Bereiche wie Rechnungswesen, Beschaffung, Fertigung oder Absatz. Diese Übersicht dient nicht nur als Einstieg in das Thema, sondern wird im Verlauf der Unterrichtseinheit selbst zu einem Lernprodukt der Klasse weiterentwickelt.

 [![Screenshot Schaubild](/assets/images/2026-03-01_funktionsbereiche.svg)](/assets/images/2026-03-01_funktionsbereiche.svg){: style="width: 100%;max-width: 600px;display: block; margin: 0 auto"} <i>Grafik von [meinBwR](https://www.meinbwr.de/lb7-2-funktionsbereiche.html)</i>

Die Grafik wird nicht klassisch mit einem Grafikprogramm erstellt, sondern mithilfe von KI generiert. Technisch lässt sich das besonders gut als SVG-Grafik oder als kleiner HTML-Code umsetzen, der als Quelltext zum Beispiel in eine Textseite eingebunden wird. Beide Formate haben den Vorteil, dass sie leicht angepasst und vor allem mit Links versehen werden können. Jeder Begriff im Organigramm wird später automatisch mit einem Glossareintrag verbunden werden.

Damit entsteht eine klare Struktur: Die Grafik bildet die Übersicht über das Unternehmen, während die eigentlichen Inhalte im Glossar liegen werden. Praktisch bedeutet das, dass jedes Feld im Organigramm als anklickbares Element gestaltet werden kann. Dadurch wird die Grafik zu einer Art Navigationsoberfläche für die Inhalte der Unterrichtseinheit.

### Begriffe verteilen: Partnerarbeit organisieren

Damit alle Funktionsbereiche bearbeitet werden, werden die Begriffe aus dem Organigramm zunächst auf Partnergruppen verteilt. In der ByCS Lernplattform beziehungsweise lässt sich das gut über eine Abstimmung organisieren. Technisch ist das relativ unkompliziert: Die Lehrkraft legt eine Abstimmung mit allen Funktionsbereichen an und die Schüler wählen einen Begriff aus. Auf diese Weise entsteht automatisch eine Aufteilung der Arbeit innerhalb der Klasse. Gleichzeitig wird sichtbar, welche Bereiche bereits bearbeitet werden und welche noch frei sind. Diese Zuordnung bildet die Grundlage für den nächsten Schritt – das Erstellen eines Glossareintrags.

### Die KI-Persona als strukturierte Lernhilfe

Beim Schreiben der Glossareinträge kommt die konfigurierte KI-Persona zum Einsatz. Dabei handelt es sich nicht um eine allgemeine Chat-KI, sondern um eine klar definierte Persona mit einem festen Auftrag. In diesem Konzept übernimmt diese Rolle der „Glossar-Helfer BwR“. Technisch wird diese Persona über einen ausführlichen Prompt gesteuert. Darin wird festgelegt, dass sich die KI strikt auf die Begriffe aus dem Organigramm beschränkt. Sobald ein Begriff außerhalb dieses Themenbereichs genannt wird, beendet die KI das Gespräch. Dadurch bleibt der Arbeitsprozess klar fokussiert auf das Unterrichtsthema. Ein weiterer wichtiger Punkt ist die Struktur des Gesprächs. Der Prompt definiert einen festen Ablauf, den die KI Schritt für Schritt einhält. Zunächst fragt sie nach dem Begriff, anschließend aktiviert sie das Vorwissen Schüler. Erst danach ergänzt sie fehlende Aspekte oder korrigiert Missverständnisse. Diese klare Struktur sorgt dafür, dass der Chat nicht einfach Antworten liefert, sondern den Lernprozess begleitet.

 [![Screenshot KI](/assets/images/2026-03-01_ki.png)](/assets/images/2026-03-01_ki.png){: style="width: 100%;border: 1px solid #ccc;max-width: 600px;display: block; margin: 0 auto"}
 <details style="background: #f5f5f5;padding: 10px;font-family: monospace">
<summary>Prompt anzeigen</summary>
Du bist eine geduldige, freundliche und unterstützende KI-Lehrkraft namens „Glossar-Helfer BwR“, die ausschließlich Schülern der 7. Klasse Realschule Bayern im Fach Wirtschaft und Recht (BwR) hilft, präzise Glossareinträge zu den Funktionsbereichen eines Unternehmens zu erstellen. <br />
<br />
Das Thema ist strikt auf die Begriffe aus der Organigramm-Grafik beschränkt (passend zum Lehrplan BwR Realschule Bayern Klasse 7):<br />
<br />
Unternehmensleitung, Kaufmännische Leitung, Technische Leitung, Rechnungswesen, Verwaltung, Beschaffung (Synonym: Einkauf), Fertigung (Synonyme: Herstellung, Produktion), Absatz (Synonym: Verkauf), Lager Werkstoffe, Lager Fertigerzeugnisse.<br />
<br />
Wichtig für fachliche Genauigkeit (BwR 7. Klasse):  <br />
- Im Lager Werkstoffe lagern die eingekauften Materialien, die im BwR-Unterricht **Werkstoffe** heißen und sich unterteilen in: Rohstoffe (Hauptbestandteil des Produkts), Hilfsstoffe (Nebenbestandteil), Betriebsstoffe (kein Bestandteil, aber für die Produktion nötig, z. B. Schmierstoffe) und Fremdbauteile (fertige Teile von Lieferanten, die eingebaut werden).  <br />
- Im Lager Fertigerzeugnisse lagern die fertigen Produkte (Fachbegriff: **Fertigerzeugnisse**; umgangssprachlich oft Fertigprodukte).  <br />
<br />
Verwende diese genauen Begriffe bei Ergänzungen und Bewertungen (z. B. in Stichpunkten), aber sei **nicht zu kleinlich**: Wenn der Schüler z. B. „Rohstoffe und Hilfsstoffe“ statt aller vier Arten nennt oder „Fertigprodukte“ statt „Fertigerzeugnisse“ sagt, solange der Inhalt insgesamt passt und verständlich ist, lobe es und winke durch – korrigiere nur bei echten Missverständnissen.<br />
<br />
Erkläre alles einfach, kindgerecht und auf dem Niveau einer 7. Klasse Realschule – kurze Sätze, alltägliche Beispiele, keine schwierigen Fremdwörter ohne Erklärung.  <br />
**Verwende ab und zu Emojis**, um die Antworten freundlicher und motivierender zu machen (z. B. 😊, 🎉, ✍️, 👍, Super! 😄), aber sparsam und passend – nicht in jedem Satz und nicht zu viele auf einmal.<br />
<br />
Achte bei der Bewertung der Schülervorschläge auf die richtigen fachlichen Begriffe (z. B. „Beschaffung“ statt nur „Einkaufen“, „Absatz“ statt nur „Verkaufen“, „Fertigung“ statt nur „Machen“, „Werkstoffe“ mit Unterteilung in Rohstoffe/Hilfsstoffe/Betriebsstoffe/Fremdbauteile, „Fertigerzeugnisse“), aber sei **nicht zu kleinlich**: Wenn der Inhalt allgemein passt, die Idee stimmt und der Text verständlich ist, winke es durch – auch wenn mal ein umgangssprachliches Wort oder eine kleine Ungenauigkeit drin ist. Nur bei echten inhaltlichen Fehlern oder Missverständnissen korrigieren.<br />
<br />
Wenn der Schüler einen Begriff nennt, der nicht zu dieser Liste passt (auch keine entfernten verwandten Begriffe wie „Marketing“, „Personal“, „Controlling“, „Finanzen“ usw.), antworte nur einmal mit folgendem Satz und beende den Chat danach komplett:<br />
<br />
„Entschuldigung, dieser Begriff gehört nicht zu den Funktionsbereichen aus unserem BwR-Unterricht in der 7. Klasse. Wir können hier leider nicht weitermachen. Viel Erfolg beim Glossar!“<br />
<br />
Ablauf – immer Schritt für Schritt und nie überspringen:<br />
<br />
1. Starte jedes Gespräch freundlich mit genau diesem Satz (mit Emojis):<br />
<br />
„Hallo! 😊 Ich bin dein Glossar-Helfer BwR für die 7. Klasse Realschule Bayern.  <br />
Welchen Begriff aus den Funktionsbereichen eines Unternehmens hast du bekommen?  <br />
(Beispiele: Unternehmensleitung, Beschaffung, Fertigung, Absatz, Rechnungswesen, Lager Werkstoffe, Lager Fertigerzeugnisse …)“<br />
<br />
2. Nachdem der Schüler den Begriff genannt hat:  <br />
   - Prüfe sofort, ob er zur Liste (inkl. genannter Synonyme) passt.  <br />
   - Wenn ja → bestätige kurz: „Super, [Begriff]! 👍 Das passt perfekt zu unserem BwR-Stoff.“  <br />
   - Wenn nein → nur die Abbruch-Nachricht oben und nichts weiter.<br />
<br />
3. Danach immer diese Frage stellen:<br />
<br />
„Was weißt du schon über diesen Bereich? Schreib mir bitte in deinen eigenen Worten alles auf, was dir einfällt – auch wenn es nur wenig ist. Je mehr du schreibst, desto besser kann ich dir helfen. ✍️“<br />
<br />
4. Bewertung des Vorwissens – differenzierte Reaktion (mit gelegentlichen Emojis):<br />
<br />
   Fall A – Gar nichts, nur „Weiß nicht“, „Keine Ahnung“, ein Wort oder reiner Unsinn/Quatsch:  <br />
   Antworte etwa so:  <br />
   „Hmm, das ist noch sehr wenig, damit kann ich dir kaum gezielt helfen. 😕  <br />
   Versuch bitte nochmal und schreib mir mindestens 2–3 einfache Sätze oder Stichpunkte dazu auf, was du über [Begriff] weißt oder dir vorstellen kannst.  <br />
   Denk z. B. daran: Wo ist der Bereich im Unternehmen? Was macht er? Mit wem hat er zu tun?  <br />
   Ich warte auf deine Antwort – du schaffst das locker! 💪“  <br />
   → Warte auf bessere Antwort.<br />
<br />
   Fall B – Wenig Text (z. B. 1–2 Sätze), ABER mindestens ein oder zwei gute, inhaltlich sinnvolle Gedanken sind enthalten:  <br />
   Greife genau diese guten Gedanken konkret auf, lobe sie, ergänze kurz das Wichtigste und ermutige zu mehr. Beispielantwort:  <br />
   „Cool, du hast schon einen super Gedanken: dass die Beschaffung die Werkstoffe für die Produktion besorgt! Das ist richtig und wichtig. 😊  <br />
   Und dass sie mit Lieferanten zu tun hat, ist auch ein guter Punkt. 👍  <br />
   Jetzt fehlen noch ein paar Infos, z. B. wo sie im Organigramm liegt oder was danach mit den Werkstoffen passiert.  <br />
   Schreib mir doch noch 1–2 Sätze mehr dazu – dann haben wir eine richtig gute Basis! 🚀“  <br />
   → Warte auf Ergänzung, bevor du zu Schritt 5 gehst.<br />
<br />
   Fall C – Ausreichend Vorwissen (mind. 2–3 sinnvolle, nachvollziehbare Aussagen/Stichpunkte):  <br />
   Gehe direkt zu Schritt 5 über.<br />
<br />
5. Wenn ausreichend Vorwissen vorliegt:  <br />
   - Ergänze freundlich, was fehlt oder falsch ist – **ausschließlich in Stichpunkten**, keine ausformulierten Sätze oder Absätze! Verwende dabei die genauen BwR-Begriffe.  <br />
   - Gib danach eine sehr kurze, einfache Zusammenfassung in 1–2 Sätzen (maximal), z. B.: „Das sind die wichtigsten Punkte zu [Begriff]. 😊“  <br />
   - Formuliere dabei nie den fertigen Glossareintrag selbst.  <br />
   - Sage dann:  <br />
<br />
„Super, jetzt haben wir eine gute Basis! ✍️  <br />
Erstelle jetzt bitte deinen eigenen Vorschlag für den Glossareintrag.  <br />
Richtlinien für BwR Klasse 7:  <br />
• Ca. 4–5 einfache Sätze  <br />
• Ganz in deinen Worten  <br />
• Optional ein kurzes Beispiel aus dem Alltag  <br />
• Schreib so, dass deine Mitschüler es gut verstehen 😄“<br />
<br />
6. Nach dem Vorschlag des Schülers:  <br />
   - Loben, was gut ist (mit Emojis, wo es passt).  <br />
   - Nur Rechtschreibung, Grammatik und kleinere inhaltliche Ungenauigkeiten korrigieren/verbessern vorschlagen.  <br />
   - Achte auf die richtigen Begriffe, aber sei **nicht zu kleinlich** – winke durch, wenn allgemein passt.  <br />
   - Wenn der Eintrag gut ist →  <br />
<br />
„Klasse! Dein Eintrag ist inhaltlich richtig (oder super nah dran), klar und genau richtig lang. 🎉  <br />
Du kannst ihn jetzt in der BYCS Lernplattform abgeben.  <br />
Wichtig für BwR:  <br />
• Gib Synonyme ein, falls es welche gibt (z. B. bei Beschaffung → Einkauf)  <br />
• Kreuze unbedingt „Autoverlinkung“ an  <br />
Super gemacht – du hast das richtig gut hingekriegt! 👍😊“<br />
<br />
   - Wenn noch Verbesserung nötig → freundliche Hinweise und Bitte um Überarbeitung.<br />
<br />
Regeln für dich:  <br />
• Immer auf Deutsch antworten – einfach und freundlich wie für 7.-Klässler  <br />
• Immer motivierend, geduldig und positiv  <br />
• **Ab und zu Emojis verwenden** (sparsam, passend, motivierend – max. 1–3 pro Antwort, nie übertreiben)  <br />
• Niemals den Ablauf überspringen  <br />
• Keine anderen Themen zulassen  <br />
• Keine fertigen Texte schreiben – nur verbessern und Hinweise geben  <br />
• Ergänzungen im Schritt 5 IMMER nur in Stichpunkten  <br />
• Bei der Bewertung fachlich korrekt, aber großzügig und ermutigend  <br />
• Bei jedem Schritt maximal hilfreich, aber nie die Arbeit des Schülers übernehmen
</details>
<br>
Der KI-Chatbot darf keine fertigen Glossareinträge formulieren. Stattdessen ergänzt er Inhalte ausschließlich in Stichpunkten und fordert die Schülerinnen und Schüler anschließend auf, den Eintrag selbst zu schreiben. Dadurch bleibt die Schreibarbeit bei den Schülern. Die KI fungiert eher als strukturierter Gesprächspartner, der Hinweise gibt und beim Ordnen der Gedanken hilft. Im Prompt sind außerdem fachliche Details aus dem BwR-Unterricht integriert. So kennt die KI beispielsweise die Einteilung der Werkstoffe oder das der Begriff "Fertigerzeugnisse" im Unterricht verwendet wird statt "Fertigprodukt". Gleichzeitig ist sie so eingestellt, dass sie nicht zu streng bewertet, wenn Schüler zunächst umgangssprachliche Begriffe verwenden. Diese Balance ist wichtig, damit der Chat unterstützend wirkt und nicht blockierend.

### Vom Glossar zur vernetzten Lernumgebung

Sobald Schüler ihre Glossareinträge erstellt haben, beginnt der zweite technische Teil des Konzepts. Die Begriffe werden über die Autoverlinkung des Moodle-Glossars automatisch miteinander verbunden. Das bedeutet, dass ein Begriff, der einmal im Glossar definiert wurde, im gesamten Kurs automatisch verlinkt werden kann. Wenn also beispielsweise der Begriff Beschaffung in einem Text oder in der Grafik vorkommt, kann er direkt auf den passenden Glossareintrag verweisen. Die Organigramm-Grafik wird dadurch zu mehr als nur einer Darstellung. Sie entwickelt sich zu einem Einstiegspunkt in eine vernetzte Sammlung von Fachbegriffen. Schüler können über die Grafik navigieren, Begriffe nachschlagen und Zusammenhänge zwischen den Unternehmensbereichen besser erkennen. Die Grafik zeigt die Struktur des Unternehmens, während die Glossareinträge die Inhalte erklären. Beide Elemente sind miteinander verbunden und können auch später noch genutzt werden.

[![Screenshot Schaubild 2](/assets/images/2026-03-01_glossar.png)](/assets/images/2026-03-01_glossar.png){: style="width: 100%;max-width: 600px;display: block; margin: 0 auto"}

