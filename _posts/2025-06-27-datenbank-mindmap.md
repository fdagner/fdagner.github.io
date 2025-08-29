---
layout: post
title: "Datenbankvorlage: Mindmap"
date: 2025-08-29T12:00:00
image: "/assets/images/2025-08-29_mindmap1.png"
categories:
  - Moodle
  - Unterricht
---
**Mindmaps sind ein tolles Werkzeug, um Ideen zu organisieren, Lerninhalte zu visualisieren und kreatives Denken zu fördern. In der ByCS Lernplattform oder in Moodle mit der Datenbankaktivität sind die Mindmaps sicher gespeichert und entsprechen den DSGVO-Regeln. Darüber hinaus bietet die Datenbankaktivität nahtlose Integration in den Unterricht.**

[![Screenshot Mindmap](/assets/images/2025-08-29_mindmap1.png)](/assets/images/2025-08-29_mindmap1.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}


### Vorlage herunterladen

👉 [https://github.com/fdagner/mindmap_moodle-database-preset-/releases](https://github.com/fdagner/mindmap_moodle-database-preset-/releases)

### Struktur der Datenbankvorlage
Um die Struktur der Mindmap zu speichern und zu bearbeiten, wird im Hintergrund die Mindmap als Text in einem Kurztextfeld gespeichert. Eine Textarea als Datenbankfeld scheidet aus, da Moodle immer den Editor nachlädt und dort u. a. html-Tags einfügt oder Zeilenumbrüche konvertiert. Die Syntax des Textes orientiert sich an der Mermaid-Syntax. Da das Feld allerdings ein einzeiliges Inputfeld ist und die Mermaid-Syntax mehrzeilig ist, müssen Änderungen vorgenommen werden:

- Der Code beginnt mit dem Wort mindmap, gefolgt von einer Liste von Knoten, die durch \| getrennt sind.
- Jeder Knoten wird durch seinen Text beschrieben. Der Hauptknoten wird als root(Text) geschrieben, z. B. root(Hauptknoten).
- Unterknoten werden durch Tilden (~) eingerückt, um ihre Hierarchie zu zeigen. Zum Beispiel:

```
mindmap|root(Hauptknoten)|~Thema1|~~Unterthema1|~Thema2
```
Hier hat der Hauptknoten zwei Unterthemen (Thema1 und Thema2), und Thema1 hat ein eigenes Unterthema (Unterthema1).
Der angepasste Mermaid-Code wird verwendet, um die Daten in die visuelle Darstellung (SVG) oder die Listenansicht zu übersetzen und ermöglicht auch Funktionen wie das Exportieren in (richtigen) Mermaid-Code.

### Mindmap als SVG

Die SVG ist die visuelle Darstellung der Mindmap. Der Hauptknoten liegt in der Mitte. Unterthemen verzweigen abwechselnd nach rechts und links.
Bei der Entwicklung wurde bewusst auf externe JavaScript-Bibliotheken (wie Mermaid.js oder andere Grafik-Frameworks) verzichtet. Moderne Bibliotheken verwenden oft ESM-Module (EcmaScript Modules), die in die Datenbankaktivität nicht mehr so leicht integriert werden können. Eine Verlinkung scheidet aus Datenschutzgründen oder lokal aus Gründen der Anwenderfreundlichkeit aus. Ohne externe Bibliothek kann außerdem die Mindmap auf die spezifischen Bedürfnisse angepasst werden. Die Datenbankvorlage ist dennoch kompatibel: es kann direkt ein Mermaid-Code exportiert werden. Selbstverständlich kann die Mindmap auch als SVG gespeichert werden.

Die Farben werden automatisch zugeordnet und können nicht einzeln definiert werden. Das ist Absicht, damit sich die Schüler auf den Inhalt konzentieren und fokussieren. Damit aber nicht alle Mindmaps gleich aussehen, können Farbschemen ausgewählt werden. In der Java-Script-Vorlage können diese Schemen angepasst oder ergänzt werden:

```js
const BRANCH_COLORS_SCHEMES = {
    'Standard': {
        level0: '#667eea',
        colors: ['#00BFFF', '#2ecc71', '#f39c12', '#ec5353', '#e84393', '#1abc9c', '#9b59b6', '#e67e22', '#3498db']
    },
    'Hell': {
        level0: '#f5f5f5',
        colors: ['#f0f8ff', '#f4d9cc', '#fffacd', '#ffe4e1', '#f5f5f5', '#f0e6ff', '#f0fff0', '#f5fffa', '#fff5ee', '#f5f5dc', '#fffaf0', '#f8f8ff', '#f0e68c', '#e6e6fa', '#fff0f5', '#e0ffff', '#f0ffff', '#faebd7']
...
```

Level0 ist die Farbe für den Hauptknoten, die Knoten in Level 1 erhalten die Farbe aus der Liste in der angegebenen Reihenfolge. Weitere Knoten erben die Farbe aus Level 1. Im Datenbankfeld zum Farbschema muss dann das entsprechende Schema im Auswahlfeld ergänzt werden:

[![Screenshot Mindmap Farbschema](/assets/images/2025-08-29_mindmap3.png)](/assets/images/2025-08-29_mindmap3.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

Wenn man auf einen Knoten der SVG klickt, erscheint ein kleines Menü (Overlay) direkt darunter. Hier finden sich die Funktionen zur Textbearbeitung, Hinzufügen eines Knotens und Löschen eines Knoten/Astes. Das Overlay macht die Bearbeitung direkt in der grafischen Ansicht einfach, ohne dass man in den Listenmodus wechseln muss.

[![Screenshot Mindmap Overlay](/assets/images/2025-08-29_mindmap4.png)](/assets/images/2025-08-29_mindmap4.png){: style="width: 75%;max-width: 800px;display: block; margin: 0 auto"}


### Listenmodus

Die Listenfelder sind die textbasierte Ansicht der Mindmap, die durch Klicken auf das Listensymbol aktiviert werden. Sie zeigen alle Knoten als bearbeitbare Eingabefelder an. Die Knoten sind hierarchisch angeordnet: Der Hauptknoten steht oben, Unterthemen sind eingerückt, je nach ihrer Ebene. Das hat einige Vorteile:
- Knoten können schneller erstellt und bearbeitet werden.
- Per Drag-&-Drop können ganze Äste verschoben werden. Hierzu kann man am linken Rand das Eingabefeld ziehen und dieses dann in ein anderes Eingabefeld ablegen.
- Die Darstellung ist barriereärmer als mit SVG.

Die Listenfelder bieten eine einfache Möglichkeit, die Mindmap textbasiert zu bearbeiten, besonders wenn die Struktur klar und übersichtlich sein soll. Schüler können sich hier ganz auf den Inhalt konzentieren.

[![Screenshot Mindmap Listenmodus](/assets/images/2025-08-29_mindmap2.png)](/assets/images/2025-08-29_mindmap1.png){: style="width: 50%;max-width: 800px;display: block; margin: 0 auto"}



