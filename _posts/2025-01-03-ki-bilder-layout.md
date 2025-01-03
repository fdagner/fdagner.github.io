---
layout: post
title: "KI-Grafiken lokal erzeugen: Einheitliches Layout für den Unterricht"
date: 2025-01-03 14:00:00 +0100
categories: [KI, Unterricht]
---
**Künstliche Intelligenz (KI) bietet spannende Möglichkeiten, um Grafiken und Fotos für den Unterricht zu generieren. Mit KI-generierten Bildern können Inhalte visualisiert und Szenarien dargestellt werden. Häufig möchte man einen bestimmten Stil erreichen oder die Ergebnisse layoutgetreu erstellen, das heißt die Grafiken sollen vom Stil und den Farben zueinander passen.**

Die [Stable Diffusion web UI](https://github.com/AUTOMATIC1111/stable-diffusion-webui) ist ein grafische Oberfläche, die es ermöglicht, die Funktionen von Stable Diffusion lokal auf dem eigenen Rechner zu nutzen.
Verschiedene Stile können über eine oder mehrere CSV-Dateien definiert und verwendet werden. Diese Datei enthält benutzerdefinierte Stile, die auf die Eingabeaufforderungen angewendet werden können. Die Dateistruktur ist einfach:

- Name des Stils: Eine kurze Beschreibung, die den Stil eindeutig identifiziert.
- Prompt-Inhalt: Der spezifische Text, der den Stil definiert (z. B. „impressionistisches Gemälde“ oder „moderner 3D-Render“) mit dem Platzhalter {prompt} für den Prompt, den der Benutzer eingibt.
- Negativ-Prompt zur Feinsteuerung der Bildinhalte.

Auszug aus einer styles.csv:

```csv
name,prompt,negative_prompt
Anime,"anime style illustration of {prompt}, beautiful intricate details, 8k resolution, vibrant colors, professional, high quality","ugly, deformed, noisy, blurry, grainy, low resolution, amateur"
Cinematic,"cinematic representation of {prompt}, epic, dramatic lighting, 4k resolution, sharp focus, rich colors, professional cinematography","low quality, shaky, amateur, overexposed, underexposed, blurry"
```

### Übersicht von allen Styles erstellen

Bei vielen Stilen kann man leicht den Überblick verlieren. Stable Diffusion bietet die Möglichkeit, mehrere Stile mit einem festen Seed in einem Plot zu visualisieren. Dies ist besonders nützlich, um die Wirkung verschiedener Stile zu vergleichen:

![Bild erstellt mit recraft.ai: Person erklärt etwas (Symbolbild)](/assets/images/2025-01-03-styles_grid.png){: style="width: 600px;display: block; margin: 0 auto"}

Unter Script wird der "X/Y/Z plot" (eine Art Stapelverarbeitung) aktiviert. Bei "X type" wählen wir "Styles" und bei den "X values" wählen wir alle vordefinierten Stile aus. Der Prompt ist "Forklift truck". Die KI erzeugt nun nacheinander Bilder eines Gabelstaplers mit demselben Prompt und demselben Seed. Das Ergebnis ist ein Raster mit Bildern, die alle den gleichen Inhalt, aber unterschiedliche Stile zeigen. Das Raster hilft später bei der Auswahl des am besten geeigneten Stils.

### Layoutgleiche Bilderserien generieren

Es ist auch möglich, variable Prompt-Inhalte mit Styles in X-Y-Z-Richtung zu kombinieren und so verschiedene Bildserien mit einheitlichem Design zu erstellen:

![Bild erstellt mit recraft.ai: Person erklärt etwas (Symbolbild)](/assets/images/2025-01-03-xyz_grid.png){: style="width: 600px;display: block; margin: 0 auto"}

Im Beispiel wurden drei Bilderserien erstellt: 
Bei selber Seed in X-Richtung laufen dabei die Styles in Y-Richtung durch und erzeugen mit den Prompts in Z-Richtung "Truck", "Building of a company" und "Young business woman works in office" die Grafiken in Serie.




