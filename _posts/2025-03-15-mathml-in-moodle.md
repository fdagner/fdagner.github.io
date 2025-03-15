---
layout: post
title: MathML in Moodle
date: 2025-03-15T14:00:00
categories:
  - Moodle
  - Unterricht
  - OER
---

**Auch im kaufmännischen Bereich braucht man mitunter Darstellungen von mathematischen Ausdrücken – etwa bei der Zinsformel, bei der Prozentrechnung oder bei Kalkulationen. Je nach Anwendung kann LaTeX auch an seine Grenzen stoßen, wenn es um einfache Integration und Barrierefreiheit geht. Eine Alternative dazu ist MathML, das vor allem durch seine direkte HTML5-Integration und Barrierefreiheit überzeugt.**


MathML steht für Mathematical Markup Language und ist eine Auszeichnungssprache speziell für mathematische Ausdrücke – ähnlich wie HTML für Text und Webseiten.

MathML Core gehört zum HTML5-Standard und wird seit 2023 von [allen großen Browsern in wesentlichen Teilen unterstützt](https://caniuse.com/mathml). Damit funktioniert es plattformübergreifend. 

## Vorteile von MathML

- Barrierefreiheit:
MathML wird von modernen Screenreadern erkannt. Die Skalierung erfolgt hochauflösend.
- HTML5-Integration:
Da MathML ein offizieller Teil von HTML5 ist, lässt es sich direkt in Webseiten einbetten.
- Anpassbar über CSS:
MathML-Formeln lassen sich optisch an das eigene Design anpassen (zum Beispiel größere Schriftgröße, farbliche Hervorhebung von Variablen).

### Beispiel Prozentrechnung:

<math displaystyle="true">
        <mtable>
            <mtr>
                <mtd>
                    <mtext>2.000,00 €</mtext>
                </mtd>
                <mtd>
                    <mo>&#8793;</mo>
                </mtd>
                <mtd>
                    <mtext>100 %</mtext>
                </mtd>
            </mtr>
            <mtr>
                <mtd>
                    <mtext>x</mtext>
                </mtd>
                <mtd>
                    <mo>&#8793;</mo>
                </mtd>
                <mtd>
                    <mtext>19 %</mtext>
                </mtd>
            </mtr>
        </mtable>
    </math>
  <br>
    <math displaystyle="true">
        <mo>&#x21D2;</mo> <!-- ⇒ -->
        <mtext>2.000,00 €</mtext>
        <mo>&#x00D7;</mo> <!-- × -->
        <mtext>19 %</mtext>
        <mo>=</mo>
        <mtext>x</mtext>
        <mo>&#x00D7;</mo> <!-- × -->
        <mtext>100 %</mtext>
    </math>
    <br><br>
    <math displaystyle="true">
        <mo>&#x21D2;</mo> <!-- ⇒ -->
        <mtext>x</mtext>
    <mo>=</mo>
        <mfrac>
            <mrow><mtext>2.000,00 €</mtext>
                <mspace width="0.25em"/>
                <mo>&#x00D7;</mo> <!-- × -->
                <mspace width="0.25em"/>
            <mtext>19 %</mtext></mrow>
            <mtext>100 %</mtext>
        </mfrac>
    </math>
    <br><br>
    <math>
        <mo>&#x21D2;</mo> <!-- ⇒ -->
        <mtext>x</mtext>
        <mo>=</mo>
        <mtext>380,00 €</mtext>
    </math>

In Chromium-Browsern funktioniert die Text-Ausrichtung in den Zellen der MathML-Tabellen nicht. Daher ist MathML (momentan) noch nicht für Kalkulationen geeignet.

### Beispiel Moodle-Test
Bei Moodle-Tests (zum Beispiel Lückentext/Cloze) kann MathML direkt im Quelltext eingebunden werden, was die Erstellung mathematischer Aufgaben vereinfacht.

[![Screenshot Test. Eingabe](/assets/images/2025-03-15-mathml.png)](/assets/images/2025-03-15-mathml.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

[![Screenshot Test: Ausgabe](/assets/images/2025-03-15-mathml2.png)](/assets/images/2025-03-15-mathml2.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

Den MathML-Code aus dem Beispiel bekommt man mit dem [BwR-Helfer \| Zinsformel](https://oer.fdagner.de/bwr/zinsformel.html).

## MathML erstellen
Die Erstellung von MathML kann auf verschiedene Weisen erfolgen. Das manuelle Schreiben ist umständlich und zeitaufwendig.
Im Moodle der ByCS Lernplattform kann man im TinyMCE mathematische Audrücke mit dem Gleichungseditor in TeX erstellen. Die erstellte Formel kann auch den MathML-Code ausgeben:

[![Screenshot Tex-Formel](/assets/images/2025-03-15-mathml3.png)](/assets/images/2025-03-15-mathml3.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

Hier ergeben sich  Probleme, daher folgende Hinweise:
- MathML muss im HTML-Modus eingefügt und dort bearbeitet werden.
- Es wird ein <code>style="display: block;"</code> hinzugefügt, was prinzipiell richtig ist, aber in Moodle den Bruchstrich über den ganzen Container zieht.
- Moodle setzt außen rum einen overflow-auto-Container, was standardmäßig unschöne und unnötige Scrollbalken setzt.
- <code>style="display: block;"</code> sollte demnach (momentan) mit <code>style="overflow: hidden;"</code> ersetzt werden.
- Prinzipiell sollte man [MathML Core](https://wiki.selfhtml.org/wiki/MathML#MathML_Core) verwenden, was anscheinend aber auch der Fall ist.

## Fazit
MathML bietet eine moderne, barrierefreie und flexibel anpassbare Möglichkeit, mathematische Formeln darzustellen.
Im Gegensatz zu LaTeX, das für viele Druck- und Wissenschaftsanwendungen ideal ist, punktet MathML vor allem dann, dass Formeln direkt in HTML eingebunden und einfach angepasst werden können. Dank MathML Core und der Integration in den HTML5-Standard wird MathML zunehmend von aktuellen Browsern unterstützt. Dennoch gibt es Unterschiede in der Darstellung und noch nicht alle MathML-Features werden von allen Browsern gleichermaßen interpretiert.

<hr>
<i>Quellen</i>
- SELFHTML (2025-03-14). MathML. Abgerufen am 15.03.2025 von [https://wiki.selfhtml.org/wiki/MathML#MathML_Core](https://wiki.selfhtml.org/wiki/MathML#MathML_Core)
- SELFHTML (2024-07-09). MathML/Einsteiger-Tutorial. Abgerufen am 15.03.2025 von [https://wiki.selfhtml.org/wiki/MathML/Einsteiger-Tutorial](https://wiki.selfhtml.org/wiki/MathML/Einsteiger-Tutorial)
- W3C (2024-09-17). W3C Math Home. Abgerufen am 15.03.2025 von [https://www.w3.org/Math/](https://www.w3.org/Math/)