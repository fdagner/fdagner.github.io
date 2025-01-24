---
layout: post
title: "Daten in ByCS Drive verschlüsseln mit Veracrypt oder Cryptomator"
date: 2025-01-24 22:50:00 +0100
categories: [GTD]
---

**Verschlüsselung stellt eine essenzielle Maßnahme dar, um Daten vor unbefugtem Zugriff zu schützen. Ich habe zwei Alternativen getestet, um einen Obsidian-Vault auf ByCS Drive zu verschlüsseln.** 

### ByCS Drive
[ByCS-Drive](https://www.bycs.de/uebersicht-und-funktionen/cloudspeicher/index.html) ist eine Cloud-basierte Speicherlösung, die speziell für den Einsatz in bayerischen Schulen entwickelt wurde. Sie basiert auf Owncloud und ermöglicht es sowohl Lehrern als auch Schülern, Unterrichtsmaterialien, Notizen, Aufgaben und Projekte sicher zu speichern und zu teilen.

Da die angekündigte, besonders sichere Verschlüsselungsoption noch nicht in ByCS Drive verfügbar ist, habe ich mich entschieden, Alternativen dazu zu prüfen.

Der Drive-Client bindet auf meinem Windows-Rechner automatisch ein Netzlaufwerk ein. So sind meine Dateien direkt im Datei-Explorer zugänglich. Änderungen auf dem Computer werden automatisch in der Cloud synchronisiert – und umgekehrt.

### Veracrypt und Cryptomator
Um einen [Obsidian-Vault](https://obsidian.md/) auf ByCS Drive sicher zu speichern, habe ich zwei Open-Source-Lösungen getestet:
[Veracrypt](https://www.veracrypt.fr/en/Home.html) und [Cryptomator](https://cryptomator.org/de/).

Beide verschlüsseln Daten und stellen sie als virtuelles Laufwerk zur Verfügung.

- **Veracrypt** verschlüsselt ganze Partitionen oder Container, die als virtuelle Laufwerke gemountet werden. Es bietet hohe Sicherheit, benötigt aber eine genaue Planung hinsichtlich der Containergröße. (Offizielle) mobile Apps sind nicht verfügbar.

- **Cryptomator** verschlüsselt einzelne Dateien und Ordner, was die Handhabung vereinfacht. Es lädt nur geänderte Dateien hoch und bietet mobile Apps für iOS und Android (in der kostenpflichtigen Version auch zum Bearbeiten).

### Ergebnis
Beide Programme funktionierten im Test einwandfrei. Die Dateien wurden erfolgreich mit ByCS Drive synchronisiert und keine Dateien wurden rausgefiltert. Der Obsidian-Vault konnte wie gewünscht genutzt werden. Alle Änderungen wurden korrekt auf allen Geräten aktualisiert.

### Fazit
Cryptomator punktet vor allem durch seine dateibasierte Verschlüsselung, bei der nur geänderte Dateien synchronisiert werden. Auch ist die Handhabung sehr benutzerfreundlich. Veracrypt ist für eine Cloud-Anwendung weniger flexibel, da die Containergröße im Voraus festgelegt werden muss und stets der gesamte Container bzw. die Datenblöcke synchronisiert werden müssen.

Aufgrund der besseren Integration in Cloud-Prozesse und der Benutzerfreundlichkeit setze ich nun auf Cryptomator, um meinen Obsidian-Vault zu verschlüsseln. Ich werde es weiterhin testen, um zu prüfen, wie gut es sich langfristig bewährt.