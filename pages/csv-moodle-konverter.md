---
layout: page
title: "CSV-Moodle-Konverter"
permalink: /csv-moodle-konverter/
categories: [moodle]
---
<div>
    <p>Mit dem Konverter kann man CSV-Daten in verschiedene Moodle-Import-Formate umwandeln. Verwenden Sie als Trennzeichen ein Semikolon.</p>
    <label for="csvInput">CSV-Daten eingeben:</label><br><br>
    <textarea id="csvInput" rows="10" cols="80"
        placeholder="Begriff1;Definition1&#10;Begriff2;Definition2"></textarea><br><br>
    <h2>Importdatei für Glossar</h2>
    <label>
        <input type="checkbox" id="useDynaLink" checked> Einträge automatisch verlinken
    </label><br>
    <label>
        <input type="checkbox" id="caseSensitive" checked> Groß-/Kleinschreibung
    </label><br>
    <label>
        <input type="checkbox" id="fullMatch" checked> Nur vollständige Wörter
    </label><br><br>
    <button id="generateButton">XML-Glossar generieren</button><br><br>
    <h2>Text für H5P</h2>
    <p>Es wird ein Text erstellt, der in "Fill in The Blanks" bzw. "Drag the Words" verwendet werden kann. Die Begriffe
        werden dabei als Textlücke generiert.</p>
    <p>Format: *Begriff* Definition</p>
    <label>
        <input type="checkbox" id="breakBetweenConceptAndDefinition" checked>
        Zeilenumbruch zwischen Begriff und Definition
    </label>
    <br><br>
    <button id="generateH5PButton">H5P-Lückentext generieren</button><br><br>
    <h2>Import-Datei für Test</h2>
    <p>Aus den Daten werden im GIFT-Format für die Aktivität Test Fragen mit dem Fragetyp Kurzantwort erstellt. Der
        Fragetitel ist gleich der gesuchten Kurzantwort. Den Titel sehen Schüler nicht.</p>
    <p>Format: ::Begriff:: Definition {=Begriff}\n</p>
    <button id="generateGiftButton">GIFT-Format generieren</button><br>
    <script>
    document.getElementById('useDynaLink').addEventListener('change', function () {
        const isChecked = this.checked;
        document.getElementById('caseSensitive').disabled = !isChecked;
        document.getElementById('fullMatch').disabled = !isChecked;
        // Optional: Deselect other checkboxes when disabled
            if (!isChecked) {
                document.getElementById('caseSensitive').checked = false;
                document.getElementById('fullMatch').checked = false;
            }
        });
    </script>
    <script>
        document.getElementById('generateButton').addEventListener('click', () => processInput('XML'));
        document.getElementById('generateH5PButton').addEventListener('click', () => processInput('H5P'));
        document.getElementById('generateGiftButton').addEventListener('click', () => processInput('GIFT'));
        function processInput(format) {
            const csvInput = document.getElementById('csvInput').value.trim();
            if (!csvInput) {
                alert("Bitte CSV-Daten eingeben.");
                return;
            }
            const rows = csvInput.split('\n');
            if (rows.length < 1 || !isValidCSV(rows)) {
                alert("Die CSV-Daten haben nicht das erwartete Format. Jede Zeile muss ein Begriff und eine Definition enthalten, getrennt durch ';'.");
                return;
            }
            let content = '';
            switch (format) {
                case 'XML':
                    const useDynaLink = document.getElementById('useDynaLink').checked ? 1 : 0;
                    const caseSensitive = document.getElementById('caseSensitive').checked ? 1 : 0;
                    const fullMatch = document.getElementById('fullMatch').checked ? 1 : 0;
                    const xmlEntries = rows.map(row => {
                        const [concept, definition] = parseRow(row);
                        return concept && definition ? `
          <ENTRY>
            <CONCEPT>${escapeXml(concept)}</CONCEPT>
            <DEFINITION>${escapeXml(definition)}</DEFINITION>
            <FORMAT>1</FORMAT>
            <USEDYNALINK>${useDynaLink}</USEDYNALINK>
            <CASESENSITIVE>${caseSensitive}</CASESENSITIVE>
            <FULLMATCH>${fullMatch}</FULLMATCH>
            <TEACHERENTRY>1</TEACHERENTRY>
          </ENTRY>` : '';
                    }).join('');
                    content = `<?xml version="1.0" encoding="UTF-8" ?>
    <GLOSSARY>
      <INFO>
        <NAME>Automatisch generiertes Glossar</NAME>
        <INTRO>&lt;p&gt;Dieses Glossar wurde automatisch generiert.&lt;/p&gt;</INTRO>
        <INTROFORMAT>1</INTROFORMAT>
        <ALLOWDUPLICATEDENTRIES>0</ALLOWDUPLICATEDENTRIES>
        <DISPLAYFORMAT>dictionary</DISPLAYFORMAT>
        <SHOWSPECIAL>1</SHOWSPECIAL>
        <SHOWALPHABET>1</SHOWALPHABET>
        <SHOWALL>1</SHOWALL>
        <ALLOWCOMMENTS>1</ALLOWCOMMENTS>
        <USEDYNALINK>${useDynaLink}</USEDYNALINK>
        <DEFAULTAPPROVAL>0</DEFAULTAPPROVAL>
        <GLOBALGLOSSARY>0</GLOBALGLOSSARY>
        <ENTBYPAGE>10</ENTBYPAGE>
        <ENTRIES>${xmlEntries}
        </ENTRIES>
      </INFO>
    </GLOSSARY>`;
                    downloadFile(content, 'glossary.xml', 'application/xml');
                    break;
                case 'H5P':
                    const breakBetween = document.getElementById('breakBetweenConceptAndDefinition').checked;
                    content = rows.map(row => {
                        const [concept, definition] = parseRow(row);
                        if (concept && definition) {
                            return breakBetween
                                ? `*${concept}*\n${definition.trim()}`
                                : `*${concept}* ${definition.trim()}`;
                        }
                        return '';
                    }).join('\n\n');
                    downloadFile(content, 'h5p_cloze_text.txt', 'text/plain');
                    break;
                case 'GIFT':
                    content = rows.map(row => {
                        const [concept, definition] = parseRow(row);
                        return concept && definition ? `::${concept}:: ${definition.trim()} {=${concept}}\n` : '';
                    }).join('\n');
                    downloadFile(content, 'gift_short_answer.txt', 'text/plain');
                    break;
            }
        }
        function isValidCSV(rows) {
            return rows.every(row => {
                const columns = row.split(';');
                return columns.length >= 2 && columns[0].trim() && columns[1].trim();
            });
        }
        function parseRow(row) {
            return row.split(';').map(col => col.trim());
        }
        function escapeXml(unsafe) {
            return unsafe.replace(/[<>&'"]/g, char => {
                const xmlEntities = { '<': '&lt;', '>': '&gt;', '&': '&amp;', "'": '&apos;', '"': '&quot;' };
                return xmlEntities[char];
            });
        }
        function downloadFile(content, fileName, mimeType) {
            const blob = new Blob([content], { type: mimeType });
            const link = document.createElement('a');
            link.href = URL.createObjectURL(blob);
            link.download = fileName;
            link.click();
            URL.revokeObjectURL(link.href);
        }
    </script>
</div>