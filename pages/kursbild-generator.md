---
layout: page
title: "Kursbild-Designer"
permalink: /kursbild-generator/
categories: [Moodle]
image: "/assets/images/2025-04-06-kursbild.png"
---
<style>
        h1 {
            text-align: center;
            color: #333;
        }
        .container {
            display: flex;
            flex-direction: column;
            gap: 20px;
            min-width: 350px;
        }
        .controls {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        .control-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
        }
       select,
        input {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .color-inputs,
        .size-inputs,
        .pattern-selection {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            padding: 8px;
        }
        /* Für mittlere Bildschirme: nur zwei Spalten */
        @media (max-width: 768px) {
            .color-inputs,
            .size-inputs,
            .pattern-selection {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        /* Für kleine Bildschirme: eine Spalte */
        @media (max-width: 480px) {
            .color-inputs,
            .size-inputs,
            .pattern-selection {
                grid-template-columns: 1fr;
            }
        }
        #text-color,
        .color-inputs input {
            padding: 0px;
        }
        button {
            background-color: #4caf50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            margin-top: 10px;
        }
        #svg-container {
            width: 100%;
            border: 1px solid #ddd;
            overflow: hidden;
            position: relative;
        }
        .download-section {
            margin-top: 20px;
            text-align: center;
        }
        #download-btn,
        #download-png-btn,
        #generate-btn {
            background-color: #2196f3;
        }
        #download-btn:hover {
            background-color: #0b7dda;
        }
        .pattern-selection label {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        .pattern-selection input[type="radio"] {
            margin: 0;
        }

        .image-size-slider {
            margin-top: 10px;
        }
        .color-section {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .secondary-color-container {
            transition: opacity 0.3s;
        }

        .disabled {
            opacity: 0.5;
            pointer-events: none;
        }
        .hidden {
            display: none;
        }
        /* Style für die Navigation */
        .navigation {
            display: flex;
            flex-direction: row;
            flex-wrap: wrap;
            justify-content: space-around;
            margin-bottom: 20px;
            padding: 10px;
            border-bottom: dashed 2px #ccc;
        }
        /* Tablet: 2 Elemente pro Zeile */
        @media (max-width: 768px) {
            .navigation {
                justify-content: space-between;
            }
            .navigation>* {
                flex: 0 0 48%;
                margin-bottom: 10px;
            }
        }
        /* Smartphone: 1 Element pro Zeile */
        @media (max-width: 480px) {
            .navigation>* {
                flex: 0 0 100%;
            }
        }
        .tab-button {
            padding: 10px 20px;
            cursor: pointer;
            border: 1px solid #ccc;
            background-color: #f4f4f4;
            color: #656565;
        }
       .tab-button:hover {
            background-color: #ddd;
        }

        .tab-button.active {
            background-color: #3498db;
            color: white;
        }
        /* Style für den Inhalt der Tabs */
        .tab-content {
            display: none;
            margin-bottom: 12px;
            width: 600px;
        }
        .tab-content.active {
            display: block;
        }
        details {
            margin-bottom: 1em;
            background: #f9f9f9;
            border: 1px solid #ccc;
            padding: 10px 15px;
            border-radius: 4px;
        }
        summary {
            cursor: pointer;
            font-weight: bold;
            outline: none;
        }
        summary::-webkit-details-marker {
            margin-right: 10px;
        }
        /* Modal Styles */
        .modal {
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            display: none;
        }
        .modal-content {
            background-color: white;
            margin: 15% auto;
            padding: 20px;
            border-radius: 8px;
            width: 80%;
            max-width: 400px;
            text-align: center;
            position: relative;
        }
        .close {
            position: absolute;
            right: 10px;
            top: 10px;
            background: none;
            border: none;
            font-size: 24px;
            cursor: pointer;
            color: #aaa;
            font-weight: bold;
        }
        .close:hover {
            color: #000;
        }
       .modal-content label {
            display: block;
            margin: 10px 0 5px;
        }
        .modal-content input[type="range"] {
            width: 100%;
        }
        .modal-content button {
            margin: 5px;
        }
        #modal-delete {
            background-color: #f44336;
        }
        #modal-delete:hover {
            background-color: #d32f2f;
        }
        .modal-content button {
            margin: 5px;
            padding: 8px 12px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        #modal-bring-forward,
        #modal-send-back {
            background-color: #ffc107;
            /* Gelb für Layer-Verschiebung */
            color: #333;
        }
        #modal-bring-forward:hover:not(:disabled),
        #modal-send-back:hover:not(:disabled) {
            background-color: #e0a800;
        }
        #modal-bring-forward:disabled,
        #modal-send-back:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        #modal-bring-forward:disabled:hover,
        #modal-send-back:disabled:hover {
            background-color: #ccc;
            /* Tooltip via title-Attribut (nativ im Browser) */
        }
        #modal-duplicate {
            background-color: #9c27b0;
        }
        #modal-duplicate:hover {
            background-color: #7b1fa2;
        }
    </style>
<div class="controls">
        <div class="navigation">
            <button class="tab-button" onclick="openTab(event, 'options')">
                Größe
            </button>
            <button class="tab-button" onclick="openTab(event, 'colors')">
                Farben
            </button>
            <button class="tab-button" onclick="openTab(event, 'pattern')">
                Muster
            </button>
            <button class="tab-button" onclick="openTab(event, 'image')">
                Bildelemente
            </button>
            <button class="tab-button" onclick="openTab(event, 'text')">
                Text
            </button>
        </div>
<div class="tab-content" id="options">
            <div class="control-group">
                <label for="preset">Optimiert für</label>
                <select id="preset">
                    <option value="1800x390">Kursbild im Kurs</option>
                    <option value="1800x600">Kursbild in der Übersicht</option>
                    <option value="900x520">Drive Space</option>
                    <option value="600x600">Quadratisch</option>
                    <option value="1600x900">Lernlandkarte</option>
                    <option value="custom">Benutzerdefiniert</option>
                </select>
            </div>
            <div class="control-group hidden" id="custom-dimensions">
                <label>Abmessungen</label>
                <div class="size-inputs">
                    <div>
                        <label for="width">Breite (px)</label>
                        <input type="number" id="width" value="1800" min="200" max="2000" />
                    </div>
                    <div>
                        <label for="height">Höhe (px)</label>
                        <input type="number" id="height" value="360" min="100" max="900" />
                    </div>
                </div>
            </div>
        </div>
        <div class="tab-content" id="colors">
            <div class="control-group color-section">
                <label>Farbverlauf</label>
                <select id="gradient-type" style="max-width: 250px">
                    <option value="linear">Linear (Links nach Rechts)</option>
                    <option value="linear-top-bottom">Linear (Oben nach Unten)</option>
                    <option value="radial">Radial (Mitte nach Außen)</option>
                    <option value="diagonal">Diagonal</option>
                    <option value="none">Ohne</option>
                </select>
                <div class="color-inputs" id="color-selection">
                    <div>
                        <label for="primary-color">Primärfarbe</label>
                        <input type="color" id="primary-color" value="#3498db" />
                        <label><input type="checkbox" id="primary-transparent" />
                            Transparent</label>
                    </div>
                    <div class="secondary-color-container" id="secondary-color-container">
                        <label for="secondary-color">Sekundärfarbe</label>
                        <input type="color" id="secondary-color" value="#2ecc71" />
                        <label><input type="checkbox" id="secondary-transparent" />
                            Transparent</label>
                    </div>
                </div>
            </div>
        </div>
<div class="tab-content" id="pattern">
            <div class="control-group">
                <label>Hintergundmuster</label>
                <div class="pattern-selection" id="pattern-selection">
                    <label><input type="radio" name="pattern" value="ohne" checked />
                        Ohne</label>
                    <label><input type="radio" name="pattern" value="waves" /> Wellen</label>
                    <label><input type="radio" name="pattern" value="circles" />
                        Kreise</label>
                    <label><input type="radio" name="pattern" value="dots" /> Punkte</label>
                    <label><input type="radio" name="pattern" value="dabs" />
                        Sprenkel</label>
                    <label><input type="radio" name="pattern" value="stars" />
                        Sternenhimmel</label>
                    <label><input type="radio" name="pattern" value="lines" /> Linien</label>
                    <label><input type="radio" name="pattern" value="grid" /> Gitter</label>
                    <label><input type="radio" name="pattern" value="crosses" />
                        Kreuze</label>
                </div>
            </div>
            <label>Animationstyp</label>
            <select id="animation-type">
                <option value="none">Ohne</option>
                <option value="translate">Bewegung links nach rechts</option>
                <option value="translate2">Bewegung oben nach unten</option>
                <option value="fade">Ausblenden</option>
            </select>
            <br /><br />
            <label>Animationsgeschwindigkeit</label>
            <select id="animation-speed">
                <option value="slow">Langsam</option>
                <option value="medium" selected>Mittel</option>
                <option value="fast">Schnell</option>
            </select>
        </div>
<div class="tab-content" id="image">
            <label>Bild-Elemente hochladen (SVG)</label>
            <input type="file" id="image-upload" accept="image/svg+xml" multiple /><br /><br />
            <p>
                Klicke auf ein hochgeladenes Bild in der Vorschau, um es zu bearbeiten
                Positioniere per Drag & Drop.
            </p>
        </div>
<div class="tab-content" id="text">
            <div class="control-group">
                <div class="control-group">
                    <label for="text-input">Text hinzufügen:</label>
                    <input type="text" id="text-input" placeholder="Hier Text eingeben..." />
                </div>
                <!-- Text-Steuerelemente, anfangs ausgeblendet -->
                <div id="text-controls" class="hidden">
                    <div class="control-group">
                        <label for="text-size">Textgröße:</label>
                        <input type="range" id="text-size" min="10" max="500" value="40" />
                    </div>
                    <div>
                        <label for="text-color">Textfarbe</label>
                        <input type="color" id="text-color" value="#ffffff" />
                    </div>
                    <div class="control-group">
                        <label for="text-font">Schriftart:</label>
                        <select id="text-font">
                            <option value="Arial, sans-serif">Arial</option>
                            <option value="'Times New Roman', serif">
                                Times New Roman
                            </option>
                            <option value="'Courier New', monospace">Courier New</option>
                            <option value="Georgia, serif">Georgia</option>
                            <option value="Verdana, sans-serif">Verdana</option>
                            <option value="Impact, sans-serif">Impact</option>
                        </select>
                    </div>
                    <br />
                    <div class="control-group hidden">
                        <label for="text-position">Horizontale Position:</label>
                        <input type="range" id="text-position" min="0" max="100" value="50" />
                    </div>
                    <div class="control-group hidden">
                        <label for="text-position-y">Vertikale Position:</label>
                        <input type="range" id="text-position-y" min="-100" max="100" value="0" />
                    </div>
                    <button id="reset-text-position-btn" class="button">
                        Text zentrieren
                    </button>
                </div>
            </div>
        </div>
    </div>
<div class="preview">
        <h3>Vorschau</h3>
        <div id="svg-container"></div>
        <div class="download-section">
            <button id="download-btn">SVG</button>
            <button id="download-png-btn">PNG</button>
            <button id="generate-btn">Aktualisieren</button>
        </div>
</div>
<br /><br />
<h3>FAQ – Häufig gestellte Fragen</h3>
<details>
        <summary>Welche Grafiken eignen sich als Bildelemente?</summary>
        <p>
            Die Grafiken müssen im SVG-Format vorliegen. Geeignete Dateien kannst du
            aus dem Repository "Imagehub" in der ByCS-Lernplattform herunterladen.
        </p>
    </details>
<details>
        <summary>
            Wie kann ich aus dem Repository "Imagehub" in der ByCS-Lernplattform
            SVG-Grafiken herunterladen?
        </summary>
        <p>
            Gehe in der Lernplattform zu
            <a href="https://www.bycs.de/hilfe-und-tutorials/lernplattform/meine-dateien-fuer-lernende/index.html">Meine
                Dateien</a>
            und füge dort aus dem Imagehub die gewünschten Grafiken zu deinen
            Dateien hinzu. Nach dem Speichern kannst du Sie von dort bequem
            herunterladen. Achtung: Das Repository steht nur bayerischen Lehrkräften
            zu Verfügung.
        </p>
    </details>
<details>
        <summary>
            Wie funktioniert die Positionierung des Bild- und Textelements?
        </summary>
        <p>
            - Sobald du ein SVG hochgeladen hast, erscheint im Vorschaubereich dein
            Bild als ein verschiebbares Element.<br />
            - Du kannst das Bild und den Text mit der Maus oder per Finger (auf
            Touchscreens) verschieben.<br />
            - Die Bild- und Textgröße lässt sich über den Schieberegler
            einstellen.<br />
            - Mit dem Button „Position zurücksetzen“ wird die Bild- oder
            Textposition auf den Standard (zentrale Platzierung) zurückgesetzt.
        </p>
    </details>
<details>
        <summary>
            Warum sollte ich die Grafik als SVG herunterladen und wann ist PNG
            sinnvoll?
        </summary>
        <p>
            SVG (Scalable Vector Graphics) bietet den Vorteil, dass die Grafiken
            verlustfrei skaliert werden können und somit auf allen Bildschirmgrößen
            gestochen scharf aussehen. Dadurch eignet sich SVG besonders gut für
            moderne Web-Anwendungen und responsive Designs.<br /><br />
            Lade das PNG herunter, wenn du es als Bild im Drive Space verwenden
            möchtest, da SVG hier nicht unterstützt wird. PNG-Dateien sind
            rasterbasiert und unterstützen keine Animationen.
        </p>
    </details>
<details>
        <summary>Unter welcher Lizenz stehen die erzeugten Grafiken?</summary>
        <p>
            Die erzeugten Bilder stehen (abhängig von den hochgeladenen Bildelementen)
            unter der Lizenz
            <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.de" target="_blank"
                rel="license noopener noreferrer">CC0 1.0</a>.
        </p>
</details>
<!-- Modal für Bildbearbeitung -->
<div id="imageModal" class="modal">
        <div class="modal-content">
            <button class="close" id="modal-close">&times;</button>
            <h3>Bild bearbeiten</h3>
            <label for="modal-size">Größe (%):</label>
            <input type="range" id="modal-size" min="25" max="300" value="100" />
            <br />
            <!-- Neue Buttons für Reihenfolge -->
            <button id="modal-bring-forward">Eine Ebene höher</button>
            <button id="modal-send-back">Eine Ebene tiefer</button>
            <br />
            <button id="modal-duplicate">Duplizieren</button>
            <br />
            <button id="modal-reset">Zentrieren</button>
            <button id="modal-delete">Löschen</button>
        </div>
    </div>
<script>
document.addEventListener("DOMContentLoaded", () => {
            const widthInput = document.getElementById("width");
            const heightInput = document.getElementById("height");
            // Wertebereich
            const widthMin = parseInt(widthInput.min);
            const widthMax = parseInt(widthInput.max);
            const heightMin = parseInt(heightInput.min);
            const heightMax = parseInt(heightInput.max);
            function validateInput(input, min, max) {
                let value = parseInt(input.value);
                if (isNaN(value)) {
                    input.value = min;
                    return;
                }
                if (value < min) {
                    input.value = min;
                    alert(`Wert zu klein! Mindestwert ist ${min}px.`);
                } else if (value > max) {
                    input.value = max;
                    alert(`Wert zu groß! Maximalwert ist ${max}px.`);
                }
            }
            widthInput.addEventListener("change", () => {
                validateInput(widthInput, widthMin, widthMax);
            });
            heightInput.addEventListener("change", () => {
                validateInput(heightInput, heightMin, heightMax);
            });
            // Funktion zur Validierung von Text (entfernt HTML-Tags)
            function validateTextInput(input) {
                let value = input.value;
                // Entfernt alle HTML-Tags aus dem Text
                const sanitizedValue = value.replace(/<\/?[^>]+(>|$)/g, "");
                // Setzt den bereinigten Text zurück, falls HTML-Tags vorhanden sind
                if (value !== sanitizedValue) {
                    input.value = sanitizedValue;
                    alert(
                        "HTML-Tags sind nicht erlaubt! Nur reiner Text ist zulässig."
                    );
                }
            }
            const textInput = document.getElementById("text-input");
            textInput.addEventListener("blur", () => {
                // 'blur' wird verwendet, wenn das Eingabefeld verlassen wird
                validateTextInput(textInput);
            });
        });
    </script>
<script>
        function escapeRegExp(string) {
            return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
        }
        let uploadedImages = [];
        let symbols = {}; // Speichert Symbol-Inhalte pro ID
        // offsets entfernt; stattdessen offset pro Instanz im image-Objekt
        let draggingId = null;
        let isDragging = false;
        let isClick = false;
        let startMouseX = 0;
        let startMouseY = 0;
        let currentX = 0;
        let currentY = 0;
        let initialX = 0;
        let initialY = 0;
        let dragThreshold = 5;
        let currentEditingImageId = null;
        function uniqifySvgIds(svgString, prefix) {
            const parser = new DOMParser();
            const doc = parser.parseFromString(svgString, "image/svg+xml");
            const idElements = doc.querySelectorAll("[id]");
            const idMap = new Map();
            idElements.forEach((el) => {
                const oldId = el.getAttribute("id");
                const newId = prefix + "-" + oldId;
                idMap.set(oldId, newId);
                el.setAttribute("id", newId);
            });
            const allElements = doc.querySelectorAll("*");
            allElements.forEach((el) => {
                for (let attr of el.attributes) {
                    if (
                        attr.value &&
                        attr.value.startsWith("url(#") &&
                        attr.value.endsWith(")")
                    ) {
                        const refId = attr.value.slice(5, -1);
                        if (idMap.has(refId)) {
                            el.setAttribute(attr.name, "url(#" + idMap.get(refId) + ")");
                        }
                    }
                }
            });
            return doc.documentElement.outerHTML;
        }
        function uniqifyCssClasses(svgString, prefix) {
            // Find <style> block
            const styleRegex = /<style[^>]*>([\s\S]*?)<\/style>/i;
            const styleMatch = svgString.match(styleRegex);
            if (!styleMatch) {
                return svgString;
            }
            let newStyleContent = styleMatch[1];
            const classRuleRegex = /\.\s*([a-zA-Z0-9_-]+)\s*{([^}]*)}/g;
            const classMap = {}; // oldClass -> newClass
            let match;
            // First pass: collect all unique class names and map to basename
            while ((match = classRuleRegex.exec(newStyleContent)) !== null) {
                const oldClass = match[1];
                // Assume basename is the part after the last '-', typically 'stN'
                const basename = oldClass.includes('-') ? oldClass.split('-').pop() : oldClass;
                if (!classMap[oldClass]) {
                    const newClass = prefix + "-" + basename;
                    classMap[oldClass] = newClass;
                }
            }
            // Second pass: replace in style content
            for (const [oldClass, newClass] of Object.entries(classMap)) {
                // Replace .oldClass with .newClass, followed by whitespace and then , or {
                const replaceRegex = new RegExp('\\.\\s*' + escapeRegExp(oldClass) + '\\s*(?=[,{])', 'g');
                newStyleContent = newStyleContent.replace(replaceRegex, '.' + newClass);
            }
            // Rebuild the <style> tag
            const oldStyle = styleMatch[0];
            const newStyle = oldStyle.replace(styleMatch[1], newStyleContent);
            let result = svgString.replace(styleRegex, newStyle);
            // Replace class attributes in elements
            for (const [oldClass, newClass] of Object.entries(classMap)) {
                // Regex to replace \boldClass\b with newClass in class attribute
                const classRegex = new RegExp('class\\s*=\\s*["\']([^"\']*?)\\b' + escapeRegExp(oldClass) + '\\b([^"\']*?)["\']', 'gi');
                result = result.replace(classRegex, (match, before, after) => {
                    return `class="${before}${newClass}${after}"`;
                });
            }
            return result;
    }
        document.addEventListener("DOMContentLoaded", function () {
            const generateBtn = document.getElementById("generate-btn");
            const downloadBtn = document.getElementById("download-btn");
            const downloadPngBtn = document.getElementById("download-png-btn");
            const svgContainer = document.getElementById("svg-container");
            const imageUpload = document.getElementById("image-upload");
            const gradientType = document.getElementById("gradient-type");
            const secondaryColorContainer = document.getElementById(
                "secondary-color-container"
            );
            const primaryColor = document.getElementById("primary-color");
            const secondaryColor = document.getElementById("secondary-color");
            // Text-Elemente
            const textInput = document.getElementById("text-input");
            const textSizeSlider = document.getElementById("text-size");
            const textPositionSlider = document.getElementById("text-position");
            const textPositionSliderY = document.getElementById("text-position-y");
            const textColorPicker = document.getElementById("text-color");
            const resetTextPositionBtn = document.getElementById(
                "reset-text-position-btn"
            );
            const textFontSelect = document.getElementById("text-font");
            let headerText = "";
            generateBtn.addEventListener("click", generateHeader);
            downloadBtn.addEventListener("click", downloadSVG);
            downloadPngBtn.addEventListener("click", downloadPNG);
            imageUpload.addEventListener("change", handleImageUpload);
            gradientType.addEventListener("change", toggleSecondaryColor);
            primaryColor.addEventListener("input", generateHeader);
            secondaryColor.addEventListener("input", generateHeader);
            document
                .getElementById("primary-transparent")
                .addEventListener("change", generateHeader);
            document
                .getElementById("secondary-transparent")
                .addEventListener("change", generateHeader);
            document
                .getElementById("pattern-selection")
                .addEventListener("change", generateHeader);
            document
                .getElementById("animation-type")
                .addEventListener("change", generateHeader);
            document
                .getElementById("animation-speed")
                .addEventListener("change", generateHeader);
            document
                .getElementById("width")
                .addEventListener("input", generateHeader);
            document
                .getElementById("height")
                .addEventListener("input", generateHeader);
            // Text-Event-Listener
            textInput.addEventListener("input", updateHeaderText);
            textSizeSlider.addEventListener("input", generateHeader);
            textPositionSlider.addEventListener("input", generateHeader);
            textPositionSliderY.addEventListener("input", generateHeader);
            textColorPicker.addEventListener("input", generateHeader);
            resetTextPositionBtn.addEventListener("click", resetTextPosition);
            if (textFontSelect) {
                textFontSelect.addEventListener("change", generateHeader);
            }
            // Modal-Event-Listener
            document.getElementById("modal-size").addEventListener("input", (e) => {
                if (currentEditingImageId) {
                    const img = uploadedImages.find(
                        (i) => i.id === currentEditingImageId
                    );
                    if (img) {
                        img.size = parseInt(e.target.value);
                        generateHeader();
                    }
                }
            });
            document.getElementById("modal-reset").addEventListener("click", () => {
                if (currentEditingImageId) {
                    const img = uploadedImages.find(
                        (i) => i.id === currentEditingImageId
                    );
                    if (img) {
                        img.size = 100;
                        img.posX = 50;
                        img.posY = 0;
                        img.offset = 1; // Reset offset auch
                        document.getElementById("modal-size").value = 100;
                        generateHeader();
                    }
                }
            });
            document
                .getElementById("modal-delete")
                .addEventListener("click", () => {
                    if (currentEditingImageId) {
                        uploadedImages = uploadedImages.filter(
                            (i) => i.id !== currentEditingImageId
                        );
                        closeModal();
                        generateHeader();
                    }
                });
            document
                .getElementById("modal-duplicate")
                .addEventListener("click", () => {
                    if (currentEditingImageId) {
                        const originalImg = uploadedImages.find(
                            (i) => i.id === currentEditingImageId
                        );
                        if (originalImg) {
                            // Generiere neue unique ID für die Instanz (nicht für Symbol)
                            const newInstanceId = "inst" + Date.now() + "-" + Math.floor(Math.random() * 1000);
                            // Verwende den offset der zu duplizierenden Instanz (pro Instanz)
                            const thisOffset = originalImg.offset || 1; // Fallback zu 1
                            // Versetze die Position der Kopie um den aktuellen offset der originalen Instanz
                            const newPosX = Math.max(0, Math.min(100, originalImg.posX + thisOffset));
                            const newPosY = Math.max(-100, Math.min(100, originalImg.posY + thisOffset));
                            // Füge die neue Instanz hinzu (verweist auf dasselbe Symbol), mit eigenem offset=1 für ihre Chain
                            uploadedImages.push({
                                id: newInstanceId,
                                symbolId: originalImg.symbolId,
                                size: originalImg.size,
                                posX: newPosX,
                                posY: newPosY,
                                aspectRatio: originalImg.aspectRatio,
                                offset: 1 // Jede neue Instanz startet mit eigenem offset=1
                            });
                            // Erhöhe den offset der originalen Instanz um 1 für nächste Duplizierung von ihr
                            originalImg.offset = (originalImg.offset || 1) + 1;
                            generateHeader();
                        }
                    }
                });
            document
                .getElementById("modal-close")
                .addEventListener("click", closeModal);
            const modal = document.getElementById("imageModal");
            window.addEventListener("click", (e) => {
                if (e.target === modal) {
                    closeModal();
                }
            });
            function closeModal() {
                modal.style.display = "none";
                currentEditingImageId = null;
            }
            function updateButtonStates() {
                if (!currentEditingImageId || uploadedImages.length <= 1) {
                    // Bei <=1 Image: Beide deaktivieren
                    const bringForwardBtn = document.getElementById(
                        "modal-bring-forward"
                    );
                    const sendBackBtn = document.getElementById("modal-send-back");
                    bringForwardBtn.disabled = true;
                    sendBackBtn.disabled = true;
                    bringForwardBtn.style.opacity = "0.5";
                    sendBackBtn.style.opacity = "0.5";
                    bringForwardBtn.title = ""; // Tooltip zurücksetzen
                    sendBackBtn.title = "";
                    return;
                }
                const currentIndex = uploadedImages.findIndex(
                    (i) => i.id === currentEditingImageId
                );
                const bringForwardBtn = document.getElementById(
                    "modal-bring-forward"
                );
                const sendBackBtn = document.getElementById("modal-send-back");
                // Eine Ebene höher: Deaktivieren, wenn schon letztes (Index == length-1)
                bringForwardBtn.disabled = currentIndex === uploadedImages.length - 1;
                bringForwardBtn.style.opacity = bringForwardBtn.disabled
                    ? "0.5"
                    : "1";
                bringForwardBtn.title = bringForwardBtn.disabled
                    ? "Das Bild ist schon ganz oben."
                    : "";
                // Eine Ebene tiefer: Deaktivieren, wenn schon erstes (Index == 0)
                sendBackBtn.disabled = currentIndex === 0;
                sendBackBtn.style.opacity = sendBackBtn.disabled ? "0.5" : "1";
                sendBackBtn.title = sendBackBtn.disabled
                    ? "Das Bild ist schon ganz unten."
                    : "";
            }
            document
                .getElementById("modal-bring-forward")
                .addEventListener("click", () => {
                    if (
                        currentEditingImageId &&
                        !document.getElementById("modal-bring-forward").disabled
                    ) {
                        const currentIndex = uploadedImages.findIndex(
                            (i) => i.id === currentEditingImageId
                        );
                        if (
                            currentIndex > -1 &&
                            currentIndex < uploadedImages.length - 1
                        ) {
                            // Schrittweise: Verschiebe um 1 nach vorne (Index +1)
                            const [movedImage] = uploadedImages.splice(currentIndex, 1);
                            uploadedImages.splice(currentIndex + 1, 0, movedImage); // Neu: Einfügen an +1
                            generateHeader();
                            updateButtonStates(); // Zustände updaten
                        }
                    }
                });
            document
                .getElementById("modal-send-back")
                .addEventListener("click", () => {
                    if (
                        currentEditingImageId &&
                        !document.getElementById("modal-send-back").disabled
                    ) {
                        const currentIndex = uploadedImages.findIndex(
                            (i) => i.id === currentEditingImageId
                        );
                        if (currentIndex > 0) {
                            // Schrittweise: Verschiebe um 1 nach hinten (Index -1)
                            const [movedImage] = uploadedImages.splice(currentIndex, 1);
                            uploadedImages.splice(currentIndex - 1, 0, movedImage); // Neu: Einfügen an -1
                            generateHeader();
                            updateButtonStates(); // Zustände updaten
                        }
                    }
                });
            function openModal(imgId) {
                currentEditingImageId = imgId;
                const img = uploadedImages.find((i) => i.id === imgId);
                if (img) {
                    document.getElementById("modal-size").value = img.size;
                }
                // Buttons für Reihenfolge nur aktivieren, wenn mehr als ein Image vorhanden
                const bringForwardBtn = document.getElementById(
                    "modal-bring-forward"
                );
                const sendBackBtn = document.getElementById("modal-send-back");
                if (uploadedImages.length > 1) {
                    bringForwardBtn.disabled = false;
                    sendBackBtn.disabled = false;
                    bringForwardBtn.style.opacity = "1";
                    sendBackBtn.style.opacity = "1";
                } else {
                    bringForwardBtn.disabled = true;
                    sendBackBtn.disabled = true;
                    bringForwardBtn.style.opacity = "0.5";
                    sendBackBtn.style.opacity = "0.5";
                }
                updateButtonStates(); // Zustände updaten
                modal.style.display = "block";
            }
            function updateHeaderText() {
                headerText = textInput.value;
                if (headerText.trim() !== "") {
                    document.getElementById("text-controls").classList.remove("hidden");
                }
                generateHeader();
            }
            function toggleSecondaryColor() {
                if (gradientType.value === "none") {
                    secondaryColorContainer.classList.add("disabled");
                } else {
                    secondaryColorContainer.classList.remove("disabled");
                }
                generateHeader();
            }
            function handleImageUpload(event) {
                Array.from(event.target.files).forEach((file) => {
                    if (file && file.type === "image/svg+xml") {
                        const reader = new FileReader();
                        reader.onload = function (e) {
                            let uploadedImage = e.target.result;
                            const parser = new DOMParser();
                            const svgDoc = parser.parseFromString(
                                uploadedImage,
                                "image/svg+xml"
                            );
                            const svgElement = svgDoc.documentElement;
                            let svgWidth =
                                svgElement.getAttribute("width") ||
                                svgElement.getAttribute("viewBox")?.split(" ")[2];
                            let svgHeight =
                                svgElement.getAttribute("height") ||
                                svgElement.getAttribute("viewBox")?.split(" ")[3];
                            if (svgWidth && typeof svgWidth === "string")
                                svgWidth = parseFloat(svgWidth);
                            if (svgHeight && typeof svgHeight === "string")
                                svgHeight = parseFloat(svgHeight);
                            if (
                                !svgElement.getAttribute("viewBox") &&
                                svgWidth &&
                                svgHeight
                            ) {
                                svgElement.setAttribute(
                                    "viewBox",
                                    `0 0 ${svgWidth} ${svgHeight}`
                                );
                            }
                            let aspectRatio = 1;
                            if (svgWidth && svgHeight) {
                                aspectRatio = svgHeight / svgWidth;
                            }
                            // Generiere unique Prefix für Symbol
                            const uniquePrefix =
                                "sym" + Date.now() + "-" + Math.floor(Math.random() * 1000);
                            // Uniqifiziere IDs und Klassen für das Symbol
                            let uniqContent = uniqifySvgIds(
                                svgElement.outerHTML,
                                uniquePrefix
                            );
                            uniqContent = uniqifyCssClasses(uniqContent, uniquePrefix);
                            // Speichere Symbol-Inhalt mit viewBox
                            symbols[uniquePrefix] = `<symbol id="${uniquePrefix}" viewBox="0 0 ${svgWidth || 100} ${svgHeight || 100}">${uniqContent}</symbol>`;
                            // Generiere unique ID für die erste Instanz
                            const uniqueInstanceId = "inst" + Date.now() + "-" + Math.floor(Math.random() * 1000);
                            // Füge die erste Instanz zum Array hinzu, mit offset: 1
                            uploadedImages.push({
                                id: uniqueInstanceId,
                                symbolId: uniquePrefix,
                                size: 100,
                                posX: 50,
                                posY: 0,
                                aspectRatio: aspectRatio,
                                offset: 1 // Jede Instanz startet mit offset=1
                            });
                            generateHeader();
                        };
                        reader.readAsText(file);
                    } else {
                        alert("Bitte eine SVG-Datei hochladen.");
                    }
                });
            }
            function generateHeader() {
                const width = parseInt(document.getElementById("width").value);
                const height = parseInt(document.getElementById("height").value);
                const primaryTransparent = document.getElementById(
                    "primary-transparent"
                ).checked;
                const secondaryTransparent = document.getElementById(
                    "secondary-transparent"
                ).checked;
                const primaryColorValue = primaryTransparent
                    ? "transparent"
                    : primaryColor.value;
                const secondaryColorValue = secondaryTransparent
                    ? "transparent"
                    : secondaryColor.value;
                const pattern = document.querySelector(
                    'input[name="pattern"]:checked'
                ).value;
                const speed = document.getElementById("animation-speed").value;
                const animationType = document.getElementById("animation-type").value;
                const gradientTypeValue = gradientType.value;
                const duration = speed === "slow" ? 15 : speed === "fast" ? 5 : 10;
                // Text-Parameter
                const textSize = parseInt(textSizeSlider.value);
                const textPosition = parseInt(textPositionSlider.value);
                const textPositionY = parseInt(textPositionSliderY.value);
                const textColor = textColorPicker.value;
                let textFont = "Arial, sans-serif";
                if (textFontSelect) {
                    textFont = textFontSelect.value;
                }
                let gradientDef = "";
                let fillColor = "";
                if (gradientTypeValue === "none") {
                    fillColor = `fill="${primaryColorValue}"`;
                } else {
                    const gradientId = "bg-gradient";
                    fillColor = `fill="url(#${gradientId})"`;
                    if (gradientTypeValue === "linear") {
                        gradientDef = `<linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></linearGradient>`;
                    } else if (gradientTypeValue === "linear-top-bottom") {
                        gradientDef = `<linearGradient id="${gradientId}" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></linearGradient>`;
                    } else if (gradientTypeValue === "radial") {
                        gradientDef = `<radialGradient id="${gradientId}" cx="50%" cy="50%" r="70%" fx="50%" fy="50%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></radialGradient>`;
                    } else if (gradientTypeValue === "diagonal") {
                        gradientDef = `<linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></linearGradient>`;
                    }
                }
                // Sammle alle Symbole in defs
                let symbolDefs = Object.values(symbols).join("");
                // Bildelemente erstellen mit <use>
                let uploadedImageElements = "";
                uploadedImages.forEach((image) => {
                    const imgWidth = ((width / 4) * image.size) / 100;
                    const imgHeight = imgWidth * image.aspectRatio;
                    const posX = (image.posX / 100) * (width + imgWidth) - imgWidth;
                    const posY =
                        ((image.posY + 100) / 200) * (height + imgHeight) - imgHeight;
                    uploadedImageElements += `
                <use 
                    id="draggable-image-${image.id}" 
                    data-image-id="${image.id}"
                    xlink:href="#${image.symbolId}" 
                    x="${posX}" 
                    y="${posY}"
                    width="${imgWidth}" 
                    height="${imgHeight}" 
                    style="overflow: visible; cursor: move;"
                />
            `;
                });
                // Text-Element erstellen
                let textElement = "";
                if (headerText && headerText.trim() !== "") {
                    const fontSize = Math.max(10, Math.min(500, textSize)); // Begrenze Schriftgröße zwischen 10 und 500
                    // Positionierung ähnlich wie beim Bild
                    const posX = (textPosition / 100) * width;
                    const posY = ((textPositionY + 100) / 200) * height;
                    textElement = `
                <text 
                    id="draggable-text" 
                    x="${posX}" 
                    y="${posY}" 
                    font-family="${textFont}" 
                    font-size="${fontSize}" 
                    fill="${textColor}" 
                    text-anchor="middle" 
                    dominant-baseline="middle"
                    style="cursor: move; user-select: none;"
                >${headerText}</text>
            `;
                }
                // SVG zusammenbauen
                const svg = `<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 ${width} ${height}" width="100%" height="100%">
            <defs>${gradientDef}${symbolDefs}${createPattern(
                    pattern,
                    primaryColorValue,
                    duration,
                    animationType
                )}</defs>
            <rect width="100%" height="100%" ${fillColor} />
            <rect width="100%" height="100%" fill="url(#${pattern}-pattern)" />
            ${uploadedImageElements}
            ${textElement}
        </svg>`;
                svgContainer.innerHTML = svg;
                // Drag-Events für Text-Element
                if (headerText && headerText.trim() !== "") {
                    const draggableText = document.getElementById("draggable-text");
                    if (draggableText) {
                        draggableText.addEventListener("mousedown", function (e) {
                            draggingId = "text";
                            startDragging(e, true);
                        });
                        draggableText.addEventListener(
                            "touchstart",
                            function (e) {
                                draggingId = "text";
                                startDragging(e, true);
                            },
                            { passive: false }
                        );
                    }
                }
                // Drag-Events für Bildelemente
                uploadedImages.forEach((image) => {
                    const draggable = document.getElementById(
                        `draggable-image-${image.id}`
                    );
                    if (draggable) {
                        draggable.addEventListener("mousedown", function (e) {
                            draggingId = image.id;
                            startDragging(e, false);
                        });
                        draggable.addEventListener(
                            "touchstart",
                            function (e) {
                                draggingId = image.id;
                                startDragging(e, false);
                            },
                            { passive: false }
                        );
                    }
                });
                // Gemeinsame Drag-Events
                document.addEventListener("mousemove", drag);
                document.addEventListener("mouseup", stopDragging);
                document.addEventListener("touchmove", drag, { passive: false });
                document.addEventListener("touchend", stopDragging, {
                    passive: false,
                });
            }
            function startDragging(e, isText) {
                e.preventDefault();
                isDragging = true;
                isClick = true;
                const rect = svgContainer.getBoundingClientRect();
                if (e.type === "touchstart") {
                    initialX = e.touches[0].clientX - rect.left;
                    initialY = e.touches[0].clientY - rect.top;
                    startMouseX = e.touches[0].clientX;
                    startMouseY = e.touches[0].clientY;
                } else {
                    initialX = e.clientX - rect.left;
                    initialY = e.clientY - rect.top;
                    startMouseX = e.clientX;
                    startMouseY = e.clientY;
                }
                if (isText) {
                    const draggableText = document.getElementById("draggable-text");
                    currentX = parseFloat(
                        draggableText ? draggableText.getAttribute("x") : 0
                    );
                    currentY = parseFloat(
                        draggableText ? draggableText.getAttribute("y") : 0
                    );
                } else {
                    const draggable = document.getElementById(
                        `draggable-image-${draggingId}`
                    );
                    currentX = parseFloat(draggable ? draggable.getAttribute("x") : 0);
                    currentY = parseFloat(draggable ? draggable.getAttribute("y") : 0);
                }
            }
            function drag(e) {
                if (!isDragging) return;
                e.preventDefault();
                const rect = svgContainer.getBoundingClientRect();
                const width = parseInt(document.getElementById("width").value);
                const height = parseInt(document.getElementById("height").value);
                let newX, newY;
                let clientX, clientY;
                if (e.type === "touchmove") {
                    clientX = e.touches[0].clientX;
                    clientY = e.touches[0].clientY;
                    newX = clientX - rect.left;
                    newY = clientY - rect.top;
                } else {
                    clientX = e.clientX;
                    clientY = e.clientY;
                    newX = clientX - rect.left;
                    newY = clientY - rect.top;
                }
                const dx = newX - initialX;
                const dy = newY - initialY;
                // Detect if it's a click or drag
                const mouseDX = Math.abs(clientX - startMouseX);
                const mouseDY = Math.abs(clientY - startMouseY);
                if (mouseDX > dragThreshold || mouseDY > dragThreshold) {
                    isClick = false;
                }
                if (draggingId === "text") {
                    // Text verschieben
                    const updatedX = currentX + dx;
                    const updatedY = currentY + dy;
                    // Begrenze die Position
                    const boundedX = Math.max(0, Math.min(updatedX, width));
                    const boundedY = Math.max(0, Math.min(updatedY, height));
                    const draggableText = document.getElementById("draggable-text");
                    if (draggableText) {
                        draggableText.setAttribute("x", boundedX);
                        draggableText.setAttribute("y", boundedY);
                    }
                    // Berechne die Slider-Werte
                    const posXPercentage = (boundedX / width) * 100; // 0-100
                    const posYPercentage = (boundedY / height) * 200 - 100; // -100 bis 100
                    textPositionSlider.value = Math.round(
                        Math.max(0, Math.min(100, posXPercentage))
                    );
                    textPositionSliderY.value = Math.round(
                        Math.max(-100, Math.min(100, posYPercentage))
                    );
                } else if (draggingId) {
                    // Bild verschieben
                    const img = uploadedImages.find((i) => i.id === draggingId);
                    if (img) {
                        const imgWidth = ((width / 4) * img.size) / 100;
                        const imgHeight = imgWidth * img.aspectRatio;
                        const updatedX = currentX + dx;
                        const updatedY = currentY + dy;
                        // Begrenze die Position
                        const boundedX = Math.max(-imgWidth, Math.min(updatedX, width));
                        const boundedY = Math.max(-imgHeight, Math.min(updatedY, height));
                        const draggable = document.getElementById(
                            `draggable-image-${draggingId}`
                        );
                        if (draggable) {
                            draggable.setAttribute("x", boundedX);
                            draggable.setAttribute("y", boundedY);
                        }
                        // Update array
                        img.posX = ((boundedX + imgWidth) / (width + imgWidth)) * 100;
                        img.posY =
                            ((boundedY + imgHeight) / (height + imgHeight)) * 200 - 100;
                        // Offset bleibt unverändert beim manuellen Verschieben
                    }
                }
            }
            function stopDragging() {
                if (isClick && draggingId && draggingId !== "text") {
                    openModal(draggingId);
                }
                isDragging = false;
                draggingId = null;
                isClick = false;
            }
            function resetTextPosition() {
                textPositionSlider.value = 50; // Mitte auf X-Achse
                textPositionSliderY.value = 0; // Mitte auf Y-Achse
                generateHeader();
            }
            // Rest des Codes bleibt gleich
            function createPattern(type, color, duration, animation) {
                const duration_translate = duration;
                const duration_scale = duration * 8;
                const duration_rotate = duration * 32;
                const duration_fade = duration;
                let patternColor = color;
                if (color !== "transparent") {
                    const r = parseInt(color.slice(1, 3), 16);
                    const g = parseInt(color.slice(3, 5), 16);
                    const b = parseInt(color.slice(5, 7), 16);
                    const brightness = (r * 299 + g * 587 + b * 114) / 1000;
                    if (brightness > 128) {
                        const darkerR = Math.max(0, r - 50);
                        const darkerG = Math.max(0, g - 50);
                        const darkerB = Math.max(0, b - 50);
                        patternColor = `rgba(${darkerR}, ${darkerG}, ${darkerB}, 0.7)`;
                    } else {
                        const lighterR = Math.min(255, r + 50);
                        const lighterG = Math.min(255, g + 50);
                        const lighterB = Math.min(255, b + 50);
                        patternColor = `rgba(${lighterR}, ${lighterG}, ${lighterB}, 0.7)`;
                    }
                }
                let shape = '';
                if (type === "ohne") {
                    shape = '';
                } else if (type === "waves") {
                    shape = `<path d="M-50 25 C-30 10, -10 10, 0 25 C10 40, 30 40, 50 25 C70 10, 90 10, 100 25 C110 40, 130 40, 150 25 C170 10, 190 10, 200 25 C210 40, 230 40, 250 25" stroke="${patternColor}" stroke-width="5" fill="none" /><path d="M150 25 C170 10, 190 10, 200 25 C210 40, 230 40, 250 25 C270 10, 290 10, 310 25 C320 40, 340 40, 360 25 C370 10, 390 10, 400 25" stroke="${patternColor}" stroke-width="1" fill="none" />`;
                } else if (type === "circles") {
                    shape = `<circle cx="30" cy="30" r="20" fill="none" stroke="${patternColor}" stroke-width="2" /><circle cx="90" cy="30" r="20" fill="none" stroke="${patternColor}" stroke-width="2" />`;
                } else if (type === "dots") {
                    shape = `<circle cx="15" cy="15" r="3" fill="${patternColor}" /><circle cx="45" cy="15" r="3" fill="${patternColor}" />`;
                } else if (type === "dabs") {
                    shape = `<circle cx="50" cy="20" r="2" fill="${patternColor}" /><circle cx="70" cy="30" r="2" fill="${patternColor}" /><circle cx="90" cy="40" r="2" fill="${patternColor}" /><circle cx="110" cy="50" r="2" fill="${patternColor}" />`;
                } else if (type === "stars") {
                    shape = `<circle cx="10" cy="10" r="2" fill="${patternColor}" /><circle cx="30" cy="50" r="2" fill="${patternColor}" /><circle cx="70" cy="80" r="2" fill="${patternColor}" /><circle cx="120" cy="20" r="2" fill="${patternColor}" /><circle cx="150" cy="60" r="2" fill="${patternColor}" />`;
                } else if (type === "lines") {
                    shape = `
                <line x1="30" y1="0" x2="30" y2="100%" stroke="${patternColor}" stroke-width="2" />
                <line x1="90" y1="0" x2="90" y2="100%" stroke="${patternColor}" stroke-width="2" />
            `;
                } else if (type === "grid") {
                    shape = `
                <line x1="30" y1="0" x2="30" y2="100%" stroke="${patternColor}" stroke-width="2" />
                <line x1="90" y1="0" x2="90" y2="100%" stroke="${patternColor}" stroke-width="2" />
                <line x1="0" y1="30" x2="100%" y2="30" stroke="${patternColor}" stroke-width="2" />
                <line x1="0" y1="90" x2="100%" y2="90" stroke="${patternColor}" stroke-width="2" />
            `;
                } else if (type === "crosses") {
                    shape = `
                <line x1="10" y1="10" x2="20" y2="20" stroke="${patternColor}" stroke-width="2" />
                <line x1="20" y1="10" x2="10" y2="20" stroke="${patternColor}" stroke-width="2" />
                <line x1="40" y1="10" x2="50" y2="20" stroke="${patternColor}" stroke-width="2" />
                <line x1="50" y1="10" x2="40" y2="20" stroke="${patternColor}" stroke-width="2" />
            `;
                }
                const size =
                    type === "dots" || type === "crosses"
                        ? 30
                        : type === "circles"
                            ? 60
                            : type === "grid" || type === "lines"
                                ? 60
                                : 100;
                let anim = "";
                let patternContent = shape;
                // Animationen werden auf ein <g>-Element angewendet, nicht auf patternTransform
                if (animation !== "none") {
                    if (animation === "translate") {
                        anim = `<animateTransform attributeName="transform" type="translate" values="-${size},0;0,0;" dur="${duration_translate}s" repeatCount="indefinite" />`;
                    } else if (animation === "translate2") {
                        anim = `<animateTransform attributeName="transform" type="translate" from="0 0" to="0 ${size}" dur="${duration_translate}s" repeatCount="indefinite" />`;
                    } else if (animation === "fade") {
                        anim = `<animate attributeName="opacity" values="1;0.1;1" dur="${duration_fade}s" repeatCount="indefinite" />`;
                    }
                    // Umhüllen der Formen mit einem <g>-Element, das die Animation trägt
                    patternContent = `<g>${anim}${shape}</g>`;
                    if (animation === "translate2") {
                        patternContent = `
                <g>
                    ${anim}
                    <g>${shape}</g>
                    <g transform="translate(0, -${size})">${shape}</g>
                </g>
            `;
                    }
                }
                if (type === "none") {
                    return "";
                }
                return `
        <pattern id="${type}-pattern" patternUnits="userSpaceOnUse" width="${size}" height="${size}">
            ${patternContent}
        </pattern>
    `;
            }
            function downloadSVG() {
                const svg = svgContainer.innerHTML;
                const blob = new Blob([svg], { type: "image/svg+xml" });
                const url = URL.createObjectURL(blob);
                const link = document.createElement("a");
                link.href = url;
                link.download = "header.svg";
                link.click();
                URL.revokeObjectURL(url);
            }
            function downloadPNG() {
                const width = parseInt(document.getElementById("width").value, 10);
                const height = parseInt(document.getElementById("height").value, 10);
                const svg = svgContainer.innerHTML;
                const svgBlob = new Blob([svg], { type: "image/svg+xml" });
                const svgUrl = URL.createObjectURL(svgBlob);
                const img = new Image();
                img.onload = function () {
                    const canvas = document.createElement("canvas");
                    const ctx = canvas.getContext("2d");
                    canvas.width = width;
                    canvas.height = height;
                    ctx.drawImage(img, 0, 0, width, height);
                    canvas.toBlob(function (blob) {
                        const url = URL.createObjectURL(blob);
                        const link = document.createElement("a");
                        link.href = url;
                        link.download = "header.png";
                        link.click();
                        URL.revokeObjectURL(url);
                    }, "image/png");
                };
                img.src = svgUrl;
            }
            const presetSelect = document.getElementById("preset");
            const widthInput = document.getElementById("width");
            const heightInput = document.getElementById("height");
            const customDimensions = document.getElementById("custom-dimensions");
            function setDimensions(value) {
                if (value === "custom") {
                    customDimensions.classList.remove("hidden");
                } else {
                    customDimensions.classList.add("hidden");
                    const dimensions = value.split("x");
                    if (dimensions.length === 2) {
                        widthInput.value = dimensions[0];
                        heightInput.value = dimensions[1];
                    }
                }
            }
            // Initialisiere die Dimensionen
            setDimensions(presetSelect.value);
            presetSelect.addEventListener("change", (e) => {
                setDimensions(e.target.value);
                generateHeader();
            });
            // Initial Header generieren
            generateHeader();
        });
    </script>
<script>
        function openTab(event, tabName) {
            // Alle Tab-Contents ausblenden
            var i, tabContents, tabButtons;
            tabContents = document.getElementsByClassName("tab-content");
            for (i = 0; i < tabContents.length; i++) {
                tabContents[i].classList.remove("active");
            }
            // Alle Tab-Buttons deaktivieren
            tabButtons = document.getElementsByClassName("tab-button");
            for (i = 0; i < tabButtons.length; i++) {
                tabButtons[i].classList.remove("active");
            }
            // Den aktuellen Tab anzeigen und Button aktivieren
            document.getElementById(tabName).classList.add("active");
            event.currentTarget.classList.add("active");
        }
        // Öffne die erste Option beim Laden der Seite
        document.addEventListener("DOMContentLoaded", function () {
            document.querySelector(".tab-button").click();
        });
    </script>
