---
layout: page
title: "ByCS-Kursbild-Generator (beta)"
permalink: /kursbild-generator/
categories: [moodle]
---

 <style>
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
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .control-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
        }

        select, input {
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        .color-inputs, .size-inputs, .pattern-selection {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 10px;
            padding: 8px;
       }

       .color-inputs input {
        padding: 0px;
       }

        button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            margin-top: 10px;
        }
        button:hover {
            background-color: #45a049;
        }
        .preview {
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            overflow: hidden;
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
        #download-btn {
            background-color: #2196F3;
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
    </style>

<div class="container">
    <div class="controls">
        <div class="control-group">
            <label>Abmessungen</label>
            <div class="size-inputs">
                <div>
                    <label for="width">Breite (px)</label>
                    <input type="number" id="width" value="1200" min="400" max="2000">
                </div>
                <div>
                    <label for="height">Höhe (px)</label>
                    <input type="number" id="height" value="250" min="100" max="800">
                </div>
            </div>
        </div>
        <div class="control-group color-section">
            <label>Farbverlauf</label>
            <select id="gradient-type" style="max-width: 250px">
                <option value="linear">Linear (Links nach Rechts)</option>
                <option value="linear-top-bottom">Linear (Oben nach Unten)</option>
                <option value="radial">Radial (Mitte nach Außen)</option>
                <option value="diagonal">Diagonal</option>
                <option value="none">Kein Farbverlauf</option>
            </select>         
            <div class="color-inputs" id="color-selection">
                <div>
                    <label for="primary-color">Primärfarbe</label>
                    <input type="color" id="primary-color" value="#3498db">
                    <label><input type="checkbox" id="primary-transparent"> Transparent</label>
                </div>
                <div class="secondary-color-container" id="secondary-color-container">
                    <label for="secondary-color">Sekundärfarbe</label>
                    <input type="color" id="secondary-color" value="#2ecc71">
                    <label><input type="checkbox" id="secondary-transparent"> Transparent</label>
                </div>
        </div>
        <div class="control-group">
            <label>Hintergundmuster</label>
            <div class="pattern-selection" id="pattern-selection">
                <label><input type="radio" name="pattern" value="none" checked> Kein Muster</label>
                <label><input type="radio" name="pattern" value="waves"> Wellen</label>
                <label><input type="radio" name="pattern" value="circles"> Kreise</label>
                <label><input type="radio" name="pattern" value="dots"> Punkte</label>
            </div>
        </div>
        <div id="animation-options" class="hidden">
        <div class="control-group">
            <label>Animationstyp</label>
            <select id="animation-type">
                <option value="none">Keine</option>
                <option value="translate">Bewegung links nach rechts</option>
                <option value="translate2">Bewegung oben nach unten</option>
                <option value="rotate">Rotation</option>
                <option value="fade">Ausblenden</option>
                <option value="diagonal">Diagonal</option>
            </select>
        </div> 
        <div class="control-group">
            <label>Animationsgeschwindigkeit</label>
            <select id="animation-speed">
                <option value="slow">Langsam</option>
                <option value="medium" selected>Mittel</option>
                <option value="fast">Schnell</option>
            </select>
        </div>
     </div>
        <div class="control-group">
            <label>Bild-Element hochladen (SVG)</label>
            <input type="file" id="image-upload" accept="image/svg+xml">
            <div id="image-controls" class="hidden">
            <label for="image-size">Bildgröße:</label>
            <input type="range" id="image-size" class="image-size-slider" min="25" max="250" value="50">
            <label for="image-position">Bildposition x:</label>
            <input type="range" id="image-position" class="image-position-slider" min="-100" max="100" value="50">
            <label for="image-position">Bildposition y:</label>
            <input type="range" id="image-position-y" class="image-position-slider" min="-200" max="200" value="0">
            </div>
        </div>
      <button id="generate-btn">Header generieren</button>
    </div>
    <div class="preview">
        <h3>Vorschau</h3>
        <div id="svg-container"></div>
        <div class="download-section">
            <button id="download-btn">Als SVG herunterladen</button>
            <p>
  <small>
      Die erzeugten Bilder stehen (abhängig vom hochgeladenen Bildelement) unter der Lizenz <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.de" target="_blank" rel="license noopener noreferrer">CC0 1.0</a>.
  </small>
</p>
        </div>
    </div>


</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const downloadBtn = document.getElementById('download-btn');
    const svgContainer = document.getElementById('svg-container');
    const imageUpload = document.getElementById('image-upload');
    const imageSizeSlider = document.getElementById('image-size');
    const imagePositionSlider = document.getElementById('image-position');
    const imagePositionSliderY = document.getElementById('image-position-y');
    const gradientType = document.getElementById('gradient-type');
    const secondaryColorContainer = document.getElementById('secondary-color-container');
    const primaryColor = document.getElementById('primary-color');
    const secondaryColor = document.getElementById('secondary-color');
    let uploadedImage = null;
    generateBtn.addEventListener('click', generateHeader);
    downloadBtn.addEventListener('click', downloadSVG);
    imageUpload.addEventListener('change', handleImageUpload);
    gradientType.addEventListener('change', toggleSecondaryColor);
    primaryColor.addEventListener('input', generateHeader);
    secondaryColor.addEventListener('input', generateHeader);
    document.getElementById('primary-transparent').addEventListener('change', generateHeader);
    document.getElementById('secondary-transparent').addEventListener('change', generateHeader);
    document.getElementById('pattern-selection').addEventListener('change', generateHeader);
    document.getElementById('animation-type').addEventListener('change', generateHeader);
    document.getElementById('animation-speed').addEventListener('change', generateHeader);
    document.getElementById('width').addEventListener('input', generateHeader);
    document.getElementById('height').addEventListener('input', generateHeader);
    imageSizeSlider.addEventListener('input', generateHeader); 
    imagePositionSlider.addEventListener('input', generateHeader);
    imagePositionSliderY.addEventListener('input', generateHeader);
    function toggleSecondaryColor() {
        if (gradientType.value === 'none') {
            secondaryColorContainer.classList.add('disabled');
        } else {
            secondaryColorContainer.classList.remove('disabled');
        }
        generateHeader();
    }
function handleImageUpload(event) {
    const file = event.target.files[0];
    if (file && file.type === 'image/svg+xml') {
        const reader = new FileReader();
        reader.onload = function(e) {
            const uploadedSVGContent = e.target.result;
            const parser = new DOMParser();
            const doc = parser.parseFromString(uploadedSVGContent, 'image/svg+xml');
            const svgElement = doc.documentElement;
            uploadedImage = svgElement.innerHTML;
            // Bildsteuerung anzeigen
            document.getElementById('image-controls').classList.remove('hidden');
            generateHeader();
        };
        reader.readAsText(file);
    } else {
        alert('Bitte eine SVG-Datei hochladen.');
    }
}
    function generateHeader() {
        const width = document.getElementById('width').value;
        const height = document.getElementById('height').value;
        const primaryTransparent = document.getElementById('primary-transparent').checked;
        const secondaryTransparent = document.getElementById('secondary-transparent').checked;
        const primaryColorObjValue = document.getElementById('primary-transparent').checked;
        const primaryColorValue = primaryTransparent ? 'transparent' : document.getElementById('primary-color').value;
        const secondaryColorValue = secondaryTransparent ? 'transparent' : document.getElementById('secondary-color').value;
        const pattern = document.querySelector('input[name="pattern"]:checked').value;
        const speed = document.getElementById('animation-speed').value;
        const animationType = document.getElementById('animation-type').value;
        const imageSize = imageSizeSlider.value;
        const imagePosition = imagePositionSlider.value;
        const imagePositionY = imagePositionSliderY.value;
        const width_upload = width / 4;
        const height_upload = height/4;
        const gradientTypeValue = gradientType.value;
        const duration = speed === 'slow' ? 15 : speed === 'fast' ? 5 : 10; 
        // Generiere den korrekten Farbverlauf basierend auf der Auswahl
        let gradientDef = '';
        let fillColor = '';
        if (gradientTypeValue === 'none') {
            // Kein Farbverlauf, verwende die Primärfarbe als einfache Füllung
            fillColor = `fill="${primaryColorValue}"`;
        } else {
            // Erstelle einen Farbverlauf und verwende ihn als Füllung
            const gradientId = 'bg-gradient';
            fillColor = `fill="url(#${gradientId})"`;          
            if (gradientTypeValue === 'linear') {
                gradientDef = `
                <linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="0%">
                    <stop offset="0%" stop-color="${primaryColorValue}" />
                    <stop offset="100%" stop-color="${secondaryColorValue}" />
                </linearGradient>`;
            } else if (gradientTypeValue === 'linear-top-bottom') {
                gradientDef = `
                <linearGradient id="${gradientId}" x1="0%" y1="0%" x2="0%" y2="100%">
                    <stop offset="0%" stop-color="${primaryColorValue}" />
                    <stop offset="100%" stop-color="${secondaryColorValue}" />
                </linearGradient>`;
            } else if (gradientTypeValue === 'radial') {
                gradientDef = `
                <radialGradient id="${gradientId}" cx="50%" cy="50%" r="70%" fx="50%" fy="50%">
                    <stop offset="0%" stop-color="${primaryColorValue}" />
                    <stop offset="100%" stop-color="${secondaryColorValue}" />
                </radialGradient>`;
            } else if (gradientTypeValue === 'diagonal') {
                gradientDef = `
                <linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="${primaryColorValue}" />
                    <stop offset="100%" stop-color="${secondaryColorValue}" />
                </linearGradient>`;
            }
        }       
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="100%" height="100%">
        <defs>
            ${gradientDef}
            ${createPattern(pattern, primaryColorValue, duration, animationType)}
        </defs>
        <rect width="100%" height="100%" ${fillColor} />
        <rect width="100%" height="100%" fill="url(#${pattern}-pattern)" />
        ${uploadedImage ? `
        <g transform="translate(${(width - width * imagePosition / 100) - (width_upload * imageSize / 100)}, ${(imagePositionY * height / 100) + (height_upload * imageSize / 100)}) scale(${imageSize / 4 / 100})">
            ${uploadedImage}
        </g>
        ` : ''}
        </svg>`;
        svgContainer.innerHTML = svg;
    }
    function createPattern(type, color, duration, animation) {
    const duration_translate = duration;
    const duration_scale = duration*8;
    const duration_rotate = duration*32;
    const duration_fade = duration;   
    // Farbmanipulation für das Muster
    let patternColor = color;
    // Farbe in RGB konvertieren
    const r = parseInt(color.slice(1, 3), 16);
    const g = parseInt(color.slice(3, 5), 16);
    const b = parseInt(color.slice(5, 7), 16);
    const brightness = (r * 299 + g * 587 + b * 114) / 1000;  
    if (brightness > 128) {
        // Farbe abdunkeln für helle Hintergründe
        const darkerR = Math.max(0, r - 50);
        const darkerG = Math.max(0, g - 50);
        const darkerB = Math.max(0, b - 50);
        patternColor = `rgba(${darkerR}, ${darkerG}, ${darkerB}, 0.7)`;
    } else {
        // Farbe aufhellen für dunkle Hintergründe
        const lighterR = Math.min(255, r + 50);
        const lighterG = Math.min(255, g + 50);
        const lighterB = Math.min(255, b + 50);
        patternColor = `rgba(${lighterR}, ${lighterG}, ${lighterB}, 0.7)`;
    }   
    // Rest der Funktion bleibt gleich, nur mit neuer patternColor
    let shape = '';
    if (type === 'none') {
        shape = `  
        `;
    } else if (type === 'waves') {
        shape = `
            <path d="M-50 25 C-30 10, -10 10, 0 25 C10 40, 30 40, 50 25 C70 10, 90 10, 100 25 C110 40, 130 40, 150 25 C170 10, 190 10, 200 25 C210 40, 230 40, 250 25" 
                stroke="${patternColor}" stroke-width="5" fill="none" />
            <path d="M150 25 C170 10, 190 10, 200 25 C210 40, 230 40, 250 25 C270 10, 290 10, 310 25 C320 40, 340 40, 360 25 C370 10, 390 10, 400 25" 
                stroke="${patternColor}" stroke-width="1" fill="none" />
        `;
    } else if (type === 'circles') {
        shape = `
            <circle cx="30" cy="30" r="20" fill="none" stroke="${patternColor}" stroke-width="2" />
            <circle cx="90" cy="30" r="20" fill="none" stroke="${patternColor}" stroke-width="2" />
        `;
    } else if (type === 'dots') {
        shape = `
            <circle cx="15" cy="15" r="3" fill="${patternColor}" />
            <circle cx="45" cy="15" r="3" fill="${patternColor}" />
        `;
    }
    const size = (type === 'dots') ? 30 : (type === 'circles') ? 60 : 100;
    let anim = '';
    if (animation !== 'none') {
            // Hinzufügen von neuen Animationen
            if (animation === 'translate') {
                anim = `<animateTransform attributeName="patternTransform" type="translate" values="0,0;${size * 2},0" dur="${duration_translate}s" repeatCount="indefinite" />`;
            } else if (animation === 'translate2') {
                anim = `<animateTransform attributeName="patternTransform" type="translate" values="0,0;0,${size * 2}" dur="${duration_translate}s" repeatCount="indefinite" />`;
            } else if (animation === 'rotate') {
                anim = `<animateTransform attributeName="patternTransform" type="rotate" values="0;360" dur="${duration_rotate}s" repeatCount="indefinite" />`;
            } else if (animation === 'fade') {
                anim = `<animate attributeName="opacity" values="1;0.1;1" dur="${duration_fade}s" repeatCount="indefinite" />`;
            } else if (animation === 'diagonal') {
                anim = `<animateTransform attributeName="patternTransform" type="translate" values="0,0;${size * 2},${size * 2}" dur="${duration_translate}s" repeatCount="indefinite" />`;
            }
        }
    let patternContent = `${anim}${shape}`
    if (animation === 'fade') {
    // Wrap content in <g> only for fade animation
    patternContent = `<g>${patternContent}</g>`;
}
    return `<pattern id="${type}-pattern" patternUnits="userSpaceOnUse" width="${size * 2}" height="${size}">
        ${patternContent}
    </pattern>`;
}
// Alle Radiobuttons mit dem Namen "pattern" finden
const patternRadios = document.querySelectorAll('input[name="pattern"]');
const animationOptions = document.getElementById('animation-options');
// Event-Listener für alle Radiobuttons hinzufügen
patternRadios.forEach(radio => {
    radio.addEventListener('change', function() {
        if (this.value === 'none') {
            // Wenn "Kein Muster" ausgewählt ist, Animation ausblenden
            animationOptions.classList.add('hidden');
        } else {
            // Wenn ein Muster ausgewählt ist, Animation anzeigen
            animationOptions.classList.remove('hidden');
        }
    });
});
function downloadSVG() {
        const svg = svgContainer.innerHTML;
        const blob = new Blob([svg], { type: 'image/svg+xml' });
        const url = URL.createObjectURL(blob);
        const link = document.createElement('a');
        link.href = url;
        link.download = 'header.svg';
        link.click();
        URL.revokeObjectURL(url);
    }   
    // Initialer Aufruf um den Header zu generieren
    generateHeader();
});
</script>