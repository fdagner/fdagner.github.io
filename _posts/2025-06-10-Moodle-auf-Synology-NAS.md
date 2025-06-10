---
layout: post
title: Moodle auf Synology NAS
date: 2025-06-10T16:30:00
image: "/assets/images/2025-06-10-moodle.png"
categories:
  - moodle
---
**Um neue Plugins, Themes und Funktionen für Moodle auszuprobieren, brauchte ich eine flexible Testumgebung, die ich lokal auf meinem *Synology NAS* hosten möchte. Ein Test-Moodle erlaubt es mir, ohne Risiko für eine produktive Umgebung zu experimentieren, Anpassungen zu testen und Ideen umzusetzen. In diesem Bericht teile ich meine Erfahrungen mit der Einrichtung eines solchen Test-Systems.**

### Portainer installieren
Obwohl Synologys *Container Manager* (ehemals Docker) eine solide Lösung ist und ich meine bisherigen Docker-Anwendungen darüber installiert habe, bietet *Portainer* eine benutzerfreundlichere und schnellere Oberfläche zur Verwaltung von Docker-Containern. *Portainer* ermöglicht es, Container, Stacks und Images intuitiv zu organisieren, was die Installation und Wartung von Anwendungen erheblich erleichtert

*Portainer* ist nicht standardmäßig auf einem *Synology NAS* vorhanden und muss zuerst installiert werden. Mit der [Anleitung von Marius Hosting](https://mariushosting.com/synology-30-second-portainer-install-using-task-scheduler-docker/) ist es sehr schnell einsatzbereit.

### Moodle installieren
Die [Installation](https://mariushosting.com/how-to-install-moodle-on-your-synology-nas/) von Moodle lief grundsätzlich reibungslos. Ich habe den DDNS-Teil übersprungen, da ich Moodle vorerst nur im lokalen Netzwerk nutze. 
Für die Installation habe ich das `bitnami/moodle`-Image aus Docker Hub verwendet. Bitnami ist ein Anbieter, der vorgefertigte, optimierte Docker-Images für beliebte Anwendungen wie Moodle bereitstellt. Das `bitnami/moodle`-Image enthält eine vollständige Moodle-Installation inklusive aller notwendigen Abhängigkeiten (z. B. PHP, Apache und eine Datenbank-Integration), vorkonfiguriert für den Einsatz in Containern. Es ist wie eine „Moodle-Box“, die sofort startklar ist, was die Einrichtung auf einer NAS erheblich vereinfacht hat. Besonders praktisch: Bitnami hält das Image regelmäßig auf dem neuesten Stand, was Updates erleichtert.

Ich habe einen Moodle-Ordner im Docker-Verzeichnis auf meinem NAS erstellt, die Berechtigungen angepasst und den Docker-Code mit angepasster, lokaler Sprache in *Portainer* eingefügt. Nach dem Deploy des Stacks in *Portainer* war *Moodle* nach etwa 20 Minuten unter `https://[NAS-IP]:9490` erreichbar. Ich konnte sofort mit der Einrichtung von Kursen beginnen. 

[![Screenshot Portainer](/assets/images/2025-06-10-portainer.png)](/assets/images/2025-06-10-portainer.png){: style="width: 100%;max-width: 800px;display: block; margin: 0 auto"}

In den Log-Files kann man live mitgucken:
> - moodle 12:37:06.80 INFO  ==> Configuring Apache ServerTokens directive
> - moodle 12:37:07.50 INFO  ==> Configuring PHP options
> - moodle 12:37:07.51 INFO  ==> Setting PHP expose_php option
> - moodle 12:37:08.04 INFO  ==> Setting PHP memory_limit option
> - moodle 12:37:08.40 INFO  ==> Setting PHP post_max_size option
> - moodle 12:37:08.68 INFO  ==> Setting PHP upload_max_filesize option
> - moodle 12:37:08.88 INFO  ==> Setting PHP output_buffering option
> - moodle 12:37:09.16 INFO  ==> Validating settings in MYSQL_CLIENT_* env vars
> - moodle 12:37:09.17 INFO  ==> Validating settings in POSTGRESQL_CLIENT_* env vars
> - moodle 12:37:11.06 INFO  ==> Restoring persisted Moodle installation
> - moodle 12:37:34.80 INFO  ==> Trying to connect to the database server
> - moodle 12:37:35.66 INFO  ==> Running database upgrade
> - moodle 12:38:12.96 INFO  ==> ** Moodle setup finished! **
> - moodle 12:38:13.00 INFO  ==> ** Starting cron **
> - moodle 12:38:13.38 INFO  ==> ** Starting Apache **

### Bisherige Fehler
In der Moodle-Adminoberfläche wollte ich das deutsche Sprachpaket installieren. Doch dort bekam ich die Warnmeldung:

> Your server does not seem to fully support the following languages:  
> Deutsch (de)
> Instead, the global locale (en_AU.UTF-8) will be used to format certain strings such as dates or numbers.

Daher habe ich das deutsche Sprachpaket (`de_DE.UTF-8`)  mit der Kommandozeile in *Portainer* nachinstalliert.

### Bisherige Erkenntnisse
- Portainer: Die Verwaltung von Images über *Portainer* war viel angenehmer als mit dem Container Manager.
- Performance: Auf meinem Synology DS720+ läuft Moodle ausreichend schnell. 
- Sicherheit: Ich nutze die NAS und Moodle nur lokal, daher habe ich auf die Erreichbarkeit von außen verzichtet. Aber vielleicht realisiere ich das in Zukunft über VPN.

### Ausblick
*Moodle* auf dem *Synology NAS* zu aktualisieren, mehrere Images parallel zu nutzen und Änderungen zu erhalten könnte mit *Portainer* erstaunlich einfach sein. Updates sind unkompliziert: In *Portainer* müsste ich das neueste bitnami/moodle:latest-Image ziehen,den alten Container umbenennen und einen neuen Container mit den gleichen Einstellungen erstellen. Ich sollte dann auch separate Stacks für verschiedene Moodle-Versionen erstellen können. Mit *Code Server* und weiteren Docker-Tools ist eine rudimentäre Dev-Umgebung auf dem NAS in Reichweite.





