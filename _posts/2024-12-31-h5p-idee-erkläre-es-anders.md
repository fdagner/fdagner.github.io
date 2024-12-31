---
layout: post
title: "H5P-Idee: Erklär's anders (TABU)"
date: 2024-12-31 12:00:00 +0100
categories: [H5P, Unterricht]
---
![Bild erstellt mit recraft.ai: Person erklärt etwas (Symbolbild)](/assets/images/2024-12-31-tabu.png){: width="250" }

**Das Spiel TABU ist ein klassisches Wortspiel, das den kreativen Einsatz von Sprache fördert und die Fähigkeit zur Kommunikation unter Druck herausfordert. In dem Spiel müssen Spieler Begriffe erklären, ohne bestimmte, sogenannte „verbotene“ Wörter zu verwenden. Diese Einschränkungen machen das Erklären von Begriffen besonders herausfordernd, da die Spieler sich auf ihre Sprachgewandtheit und Kreativität verlassen müssen. Ziel des Spiels ist es, dass das eigene Team möglichst viele Begriffe innerhalb eines begrenzten Zeitrahmens korrekt errät.** 

### Spielablauf
Karten enthalten jeweils einen Begriff, den es zu erklären gilt, sowie eine Liste von "verbotenen Wörtern", die nicht benutzt werden dürfen. 

- Ein Spieler zieht eine Karte und versucht, den Begriff seinem Team zu erklären, ohne die verbotenen Wörter zu verwenden. 
- Das Team hat eine festgelegte Zeit (zum Beispiel 1 Minute), um so viele Begriffe wie möglich zu erraten. Wird ein verbotenes Wort verwendet, gibt es keine Punkte für die Karte.
- Für jeden korrekt erratenen Begriff erhält das Team einen Punkt. Nicht erratene Begriffe oder Verstöße gegen die Tabu-Wörter bringen keine Punkte.
- Das Team mit den meisten Punkten nach einer vorher festgelegten Anzahl von Runden gewinnt.

### TABU im Unterricht
Im Spiel müssen die Schüler Begriffe erklären, ohne auf die direkten, verbotenen Wörter zurückzugreifen. Die Schüler lernen dabei, komplexe Begriffe mit einfachen Worten zu erklären. Einfaches Auswendiglernen von Definitionen reicht nicht aus – es erfordert, dass der Erklärende die Zusammenhänge, Merkmale und Eigenschaften des Begriffs genau kennt, um eine treffende Erklärung zu liefern, ohne auf die verbotenen Wörter zurückzugreifen. Das Spiel ist daher besonders gut geeignet, um Fachbegriffe zu wiederholen. Die spontane Anwendung hilft, das Wissen aus dem Langzeitgedächtnis abzurufen und in realen Kommunikationssituationen zu verwenden – was für das tatsächliche Verständnis von Fachthemen wichtig ist.

### Erstellung der H5P

Die H5P-Version des Spiels habe ich „Erklär's anders“ genannt. Der Name TABU ist wahrscheinlich urheberrechtlich geschützt, daher muss ein alternativer Name gewählt werden. Die Begriffe, die den Schülern zur Verfügung gestellt werden, stammen aus einer Liste von Fachbegriffen, die den Schülern auch als Glossar bereitgestellt wird. Die Fachbegriffe spiegeln das grundlegende Wissen aus der 7. Jahrgangsstufe wider. Die KI hilft dabei, für jeden dieser Begriffe passende „verbotene“ Wörter zu erstellen. 

Die Erstellung erfolgt analog zu der Vorgehensweise, die ich für die [H5P-Zeitleiste](/2024/12/29/H5P-mit-KI/) beschrieben habe. Da die Liste sehr lang sein kann, hat ChatGPT die komplette Ausgabe zunächst verweigert, aber dann den Vorschlag gemacht die Liste als Datei anzubieten. Es kann also sinnvoll sein, die Begriffe in Etappen erstellen zu lassen. Vielleicht wäre mittelfristig auch ein allgemeines Skript interessant, dass die JSON-Syntax aus CSV-Daten implementiert. So könnte man Begriffe und verbotene Wörter in einer Tabelle vorbereiten und automatisch in das H5P-Format übertragen. Dies würde den Aufwand weiter reduzieren und die Flexibilität bei der Erstellung der Karten erhöhen.

Interessant ist in diesem Zusammenhang, dass die Grafik und die Lizenzangaben in der JSON übernommen werden und die Grafik nur einmal hochgeladen werden muss, da alle Karten auf die selbe Grafik verweisen. Die H5P wird dadurch schlanker als bei manueller Erstellung in Lumi.

Als weiteres Material benötigt man einen Zeitgeber und eine akkustische Glocke, Tröte oder dergleichen. Dann kann der Spielspaß schon losgehen.

[![H5P](/assets/images/2024-12-31-tabu-h5p.png)](https://apps.zum.de/apps/37898){: style="width: 500px;display: block; margin: 0 auto"}

*Die H5P "Erklär's anders" gibt es auf ZUM-Apps (Bild anklicken)*