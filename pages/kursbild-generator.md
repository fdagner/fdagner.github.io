---
layout: page
title: "ByCS-Kursbild-Generator (beta)"
permalink: /kursbild-generator/
categories: [moodle]
---
<style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
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
        #download-btn, #generate-btn {
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
                    <input type="number" id="width" value="1800" min="800" max="2000">
                </div>
                <div>
                    <label for="height">Höhe (px)</label>
                    <input type="number" id="height" value="360" min="100" max="800">
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
                <label><input type="radio" name="pattern" value="dabs"> Sprenkel</label>
                <label><input type="radio" name="pattern" value="stars"> Sternenhimmel</label>
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
            <input type="file" id="image-upload" accept="image/svg+xml"><br><br>
            <div id="image-controls" class="hidden">
            <label for="image-size">Bildgröße:</label>
            <input type="range" id="image-size" class="image-size-slider" min="25" max="200" value="100">
            <label for="image-position" class="hidden">Bildposition x:</label>
            <input type="range" id="image-position" class="image-position-slider hidden" min="0" max="100" value="50">
            <label for="image-position" class="hidden">Bildposition y:</label>
            <input type="range" id="image-position-y" class="image-position-slider hidden" min="-100" max="100" value="0">
            <br>
            <button id="reset-position-btn">Position zurücksetzen</button>
            </div>
        </div>
    </div>
    <div class="preview">
        <h3>Vorschau</h3>
        <div id="svg-container"></div>
        <div class="download-section">
            <button id="download-btn">Als SVG herunterladen</button>
            <button id="generate-btn">Kursbild aktualisieren</button>
        </div>
        <small>
      Die erzeugten Bilder stehen (abhängig vom hochgeladenen Bildelement) unter der Lizenz <a href="https://creativecommons.org/publicdomain/zero/1.0/deed.de" target="_blank" rel="license noopener noreferrer">CC0 1.0</a>.
  </small>
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
    });
    </script>
<script>
document.addEventListener('DOMContentLoaded', function() {
    const generateBtn = document.getElementById('generate-btn');
    const downloadBtn = document.getElementById('download-btn');
    const svgContainer = document.getElementById('svg-container');
    const imageUpload = document.getElementById('image-upload');
    const imageSizeSlider = document.getElementById('image-size');
    const imagePositionSlider = document.getElementById('image-position');
    const imagePositionSliderY = document.getElementById('image-position-y');
    const resetPositionBtn = document.getElementById('reset-position-btn'); // Neuer Button
    const gradientType = document.getElementById('gradient-type');
    const secondaryColorContainer = document.getElementById('secondary-color-container');
    const primaryColor = document.getElementById('primary-color');
    const secondaryColor = document.getElementById('secondary-color');
    let uploadedImage = null;
    let uploadedImageAspectRatio = 1;
    let isDragging = false;
    let currentX, currentY;
    let initialX, initialY;
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
    resetPositionBtn.addEventListener('click', resetPosition); // Event-Listener für den Button
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
                uploadedImage = e.target.result;
                const parser = new DOMParser();
                const svgDoc = parser.parseFromString(uploadedImage, 'image/svg+xml');
                const svgElement = svgDoc.documentElement;
                let svgWidth = svgElement.getAttribute('width') || svgElement.getAttribute('viewBox')?.split(' ')[2];
                let svgHeight = svgElement.getAttribute('height') || svgElement.getAttribute('viewBox')?.split(' ')[3];
                if (svgWidth && typeof svgWidth === 'string') svgWidth = parseFloat(svgWidth);
                if (svgHeight && typeof svgHeight === 'string') svgHeight = parseFloat(svgHeight);
                if (!svgElement.getAttribute('viewBox') && svgWidth && svgHeight) {
                    svgElement.setAttribute('viewBox', `0 0 ${svgWidth} ${svgHeight}`);
                }
                if (svgWidth && svgHeight) {
                    uploadedImageAspectRatio = svgHeight / svgWidth;
                }
                uploadedImage = svgElement.outerHTML;
                document.getElementById('image-controls').classList.remove('hidden');
                generateHeader();
            };
            reader.readAsText(file);
        } else {
            alert('Bitte eine SVG-Datei hochladen.');
        }
    }
    function generateHeader() {
        const width = parseInt(document.getElementById('width').value);
        const height = parseInt(document.getElementById('height').value);
        const primaryTransparent = document.getElementById('primary-transparent').checked;
        const secondaryTransparent = document.getElementById('secondary-transparent').checked;
        const primaryColorValue = primaryTransparent ? 'transparent' : primaryColor.value;
        const secondaryColorValue = secondaryTransparent ? 'transparent' : secondaryColor.value;
        const pattern = document.querySelector('input[name="pattern"]:checked').value;
        const speed = document.getElementById('animation-speed').value;
        const animationType = document.getElementById('animation-type').value;
        const imageSize = parseInt(imageSizeSlider.value);
        const imagePosition = parseInt(imagePositionSlider.value);
        const imagePositionY = parseInt(imagePositionSliderY.value);
        const gradientTypeValue = gradientType.value;
        const duration = speed === 'slow' ? 15 : speed === 'fast' ? 5 : 10;
        let gradientDef = '';
        let fillColor = '';
        if (gradientTypeValue === 'none') {
            fillColor = `fill="${primaryColorValue}"`;
        } else {
            const gradientId = 'bg-gradient';
            fillColor = `fill="url(#${gradientId})"`;
            if (gradientTypeValue === 'linear') {
                gradientDef = `<linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="0%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></linearGradient>`;
            } else if (gradientTypeValue === 'linear-top-bottom') {
                gradientDef = `<linearGradient id="${gradientId}" x1="0%" y1="0%" x2="0%" y2="100%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></linearGradient>`;
            } else if (gradientTypeValue === 'radial') {
                gradientDef = `<radialGradient id="${gradientId}" cx="50%" cy="50%" r="70%" fx="50%" fy="50%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></radialGradient>`;
            } else if (gradientTypeValue === 'diagonal') {
                gradientDef = `<linearGradient id="${gradientId}" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="${primaryColorValue}" /><stop offset="100%" stop-color="${secondaryColorValue}" /></linearGradient>`;
            }
        }
        let uploadedImageElement = '';
        if (uploadedImage) {
            const imgWidth = width / 4 * imageSize / 100;
            const imgHeight = imgWidth * uploadedImageAspectRatio;
            // Positionierung: Slider 0 = linker Rand bei -imgWidth, Slider 100 = rechter Rand bei width
            const posX = (imagePosition / 100) * (width + imgWidth) - imgWidth;
            const posY = ((imagePositionY + 100) / 200) * (height + imgHeight) - imgHeight;
            const parser = new DOMParser();
            const svgDoc = parser.parseFromString(uploadedImage, 'image/svg+xml');
            const svgElement = svgDoc.documentElement;
            svgElement.setAttribute('width', "100%");
            svgElement.setAttribute('height', "100%");
            uploadedImageElement = `
                <foreignObject 
                    id="draggable-image" 
                    x="${posX}" 
                    y="${posY}"
                    width="${imgWidth}" 
                    height="${imgHeight}" 
                    style="overflow: visible; cursor: move;"
                >
                    ${svgElement.outerHTML}
                </foreignObject>
            `;
        }
        const svg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${width} ${height}" width="100%" height="100%">
            <defs>${gradientDef}${createPattern(pattern, primaryColorValue, duration, animationType)}</defs>
            <rect width="100%" height="100%" ${fillColor} />
            <rect width="100%" height="100%" fill="url(#${pattern}-pattern)" />
            ${uploadedImageElement}
        </svg>`;
        svgContainer.innerHTML = svg;
        if (uploadedImage) {
            const draggable = document.getElementById('draggable-image');
            if (draggable) {
                draggable.removeEventListener('mousedown', startDragging);
                document.removeEventListener('mousemove', drag);
                document.removeEventListener('mouseup', stopDragging);
                draggable.removeEventListener('touchstart', startDragging);
                document.removeEventListener('touchmove', drag);
                document.removeEventListener('touchend', stopDragging);
                draggable.addEventListener('mousedown', startDragging);
                document.addEventListener('mousemove', drag);
                document.addEventListener('mouseup', stopDragging);
                draggable.addEventListener('touchstart', startDragging, { passive: false });
                document.addEventListener('touchmove', drag, { passive: false });
                document.addEventListener('touchend', stopDragging, { passive: false });
            }
        }
    }
    function startDragging(e) {
        e.preventDefault();
        isDragging = true;
        const rect = svgContainer.getBoundingClientRect();
        if (e.type === 'touchstart') {
            initialX = e.touches[0].clientX - rect.left;
            initialY = e.touches[0].clientY - rect.top;
        } else {
            initialX = e.clientX - rect.left;
            initialY = e.clientY - rect.top;
        }
        const draggable = document.getElementById('draggable-image');
        currentX = parseFloat(draggable.getAttribute('x'));
        currentY = parseFloat(draggable.getAttribute('y'));
    }
    function drag(e) {
        if (!isDragging) return;
        e.preventDefault();
        const rect = svgContainer.getBoundingClientRect();
        const width = parseInt(document.getElementById('width').value);
        const height = parseInt(document.getElementById('height').value);
        const imgWidth = (width / 4 * parseInt(imageSizeSlider.value) / 100);
        const imgHeight = imgWidth * uploadedImageAspectRatio;
        let newX, newY;
        if (e.type === 'touchmove') {
            newX = e.touches[0].clientX - rect.left;
            newY = e.touches[0].clientY - rect.top;
        } else {
            newX = e.clientX - rect.left;
            newY = e.clientY - rect.top;
        }
        const dx = newX - initialX;
        const dy = newY - initialY;
        const updatedX = currentX + dx;
        const updatedY = currentY + dy;
        // Begrenze die Position: linker Rand bei -imgWidth, rechter Rand bei width
        const boundedX = Math.max(-imgWidth, Math.min(updatedX, width));
        const boundedY = Math.max(-imgHeight, Math.min(updatedY, height));
        const draggable = document.getElementById('draggable-image');
        draggable.setAttribute('x', boundedX);
        draggable.setAttribute('y', boundedY);
        // Berechne die Slider-Werte basierend auf der aktuellen Position
        const posXPercentage = ((boundedX + imgWidth) / (width + imgWidth)) * 100; // 0-100
        const posYPercentage = (((boundedY + imgHeight) / (height + imgHeight)) * 200) - 100; // -100 bis 100
        imagePositionSlider.value = Math.round(Math.max(0, Math.min(100, posXPercentage)));
        imagePositionSliderY.value = Math.round(Math.max(-100, Math.min(100, posYPercentage)));
    }
    function stopDragging() {
        isDragging = false;
    }
    // Neue Funktion zum Zurücksetzen der Position
    function resetPosition() {
        imagePositionSlider.value = 50; // Mitte auf X-Achse (0 bis 100)
        imagePositionSliderY.value = 0; // Mitte auf Y-Achse (-100 bis 100)
        generateHeader(); // Header neu generieren, um die Änderung anzuwenden
    }
    function createPattern(type, color, duration, animation) {
        const duration_translate = duration;
        const duration_scale = duration * 8;
        const duration_rotate = duration * 32;
        const duration_fade = duration;
        let patternColor = color;
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
        let shape = '';
        if (type === 'none') {
            shape = ``;
        } else if (type === 'waves') {
            shape = `<path d="M-50 25 C-30 10, -10 10, 0 25 C10 40, 30 40, 50 25 C70 10, 90 10, 100 25 C110 40, 130 40, 150 25 C170 10, 190 10, 200 25 C210 40, 230 40, 250 25" stroke="${patternColor}" stroke-width="5" fill="none" /><path d="M150 25 C170 10, 190 10, 200 25 C210 40, 230 40, 250 25 C270 10, 290 10, 310 25 C320 40, 340 40, 360 25 C370 10, 390 10, 400 25" stroke="${patternColor}" stroke-width="1" fill="none" />`;
        } else if (type === 'circles') {
            shape = `<circle cx="30" cy="30" r="20" fill="none" stroke="${patternColor}" stroke-width="2" /><circle cx="90" cy="30" r="20" fill="none" stroke="${patternColor}" stroke-width="2" />`;
        } else if (type === 'dots') {
            shape = `<circle cx="15" cy="15" r="3" fill="${patternColor}" /><circle cx="45" cy="15" r="3" fill="${patternColor}" />`;
        } else if (type === 'dabs') {
            shape = `<circle cx="50" cy="20" r="2" fill="${patternColor}" /><circle cx="70" cy="30" r="2" fill="${patternColor}" /><circle cx="90" cy="40" r="2" fill="${patternColor}" /><circle cx="110" cy="50" r="2" fill="${patternColor}" />`;
        } else if (type === 'stars') {
            shape = `<circle cx="10" cy="10" r="2" fill="${patternColor}" /><circle cx="30" cy="50" r="2" fill="${patternColor}" /><circle cx="70" cy="80" r="2" fill="${patternColor}" /><circle cx="120" cy="20" r="2" fill="${patternColor}" /><circle cx="150" cy="60" r="2" fill="${patternColor}" />`;
        }
        const size = (type === 'dots') ? 30 : (type === 'circles') ? 60 : 100;
        let anim = '';
        if (animation !== 'none') {
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
        let patternContent = `${anim}${shape}`;
        if (animation === 'fade') {
            patternContent = `<g>${patternContent}</g>`;
        }
       return `<pattern id="${type}-pattern" patternUnits="userSpaceOnUse" width="${size * 2}" height="${size}">${patternContent}</pattern>`;
    }
    const patternRadios = document.querySelectorAll('input[name="pattern"]');
    const animationOptions = document.getElementById('animation-options');
    patternRadios.forEach(radio => {
        radio.addEventListener('change', function() {
            animationOptions.classList.toggle('hidden', this.value === 'none');
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
    generateHeader();
});
</script>