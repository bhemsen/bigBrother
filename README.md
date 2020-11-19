# bigBrother
RaspberryPi(Joy-Pi)   Überwachungssystem mit RFID Einlassregelung und Raumtemperaturkontrolle


Die Umsetzung der Datenaufnahme erfolgt durch die gegebenen Sensoren des Joy-Pi's. Die Daten werden mit Python-Scripten verarbeitet und in einer MySql-Datenbank gespeichert. 
Das auslesen der Daten wird mit PHP realisiert und durch AJAX Aufrufe (Javascript) dem Frotend zur Verfügung gestellt. 

Zusätzlich zu den vorhandenen Konfigurationen haben wir einen Apache2 Webserver aufgesetzt (PHP, MySQL, PHPMYADMIN). Als root-Verzeichnes des Apache ist der sensoro-Ordner des Repository's konfiguriert.

*Darstellung*
Die Daten werden in einem Webinterface dargetellt. 
Verwendete Frameworks zur besseren Darstellung:
 - Bootstrap 4.5.3
 - Chart.js 2.8.0

Erreichbar ist die Website unter http://localhost/ auf dem Pi selbst - die Erreichbarkeit lässt sich in der apache2.conf anpassen. 
Dargestellt wird: 
 - Livestream der verbauten Kamera (realisiert über ein <iframe> dessen Source nachgeladen wird, nachdem die Seite vollständig geladen ist)
 - Log der letzten 20 RFID Auslesungen inklusive Status und Refresh-Button um neue Einträge nachzuladen ohne einen Pagereload zu machen
 - Aktuelle Temperatur und Luftfeuchtigkeit
 - Diagramme zur Überwachung der Temperatur und Luftfeuchtigkeit im Kontext des aktuellen Tages und Durchschnittstemperatur/-luftfeuchtigkeit der letzten 7 Tage
 - Formular zum Ändern der Temperaturobergrenze und Tagesgrenze nach der gelöscht wird
 

*Datenbank*

In Verbindung mit dem Apache Webserver wird eine MySql/MariaDB Datenbank benutzt. Das Instalationsscribt befindet sich im Repository(SQLSCRIPT.sql). Dort wird zunächst ein host-neutraler Nutzer(webadmin@%) angelegt, ihm alle Rechte gewährt, die Datenbank sensoro erstellt, die benötigten Tabellen angelegt und die Spalten konfiguriert. Mir diesem Nutzer werden Einträge erstellt, ausgelesen und bearbeitet. 


*Python-Scripte*

Die main.py startet eine Verbindung mit einer Datenbank - realisiert durch Aufruf der Klasse Database.py. Außerdem werden 2 Threads als Daemon gestartet. 

  - Thread1 ruft in einer Infinite-Loop die Funktion der Klasse Database.py insertTemperatureAndHumidity auf, die als Übergabeparameter eine Instanz des DHT11 chips benötigt. Diese Methoden der Instanz auf, die sowohl die Temperatur, als auch Luftfeuchtigkeit auslesen und speichert die ausgelesenen Daten in der Datenbank temperature - realisiert durch ein Prepared-Statement (INSERT)- und wartet 15 sec. Beendet wird der Thread durch STRG + C

  - Thread2 ruft in einer Infinite-Loop die Funktion der Klasse Database.py cleanUp auf, die als Übergabeparameter die Anzahl Tage benötigt, nach der die Daten aus der Datenbank gelöscht werden sollen. Dies wird realisiert mit einem Prepared-Statement (Delete), das die alle Einträge löscht, die Älter sind als die übermittelte Anzahl(Standart 7) und wartet einen halben Tag. Beendet wird der Thread durch STRG + C
  
Gestartet wird mit python3 main.py (im Projektordner /home/pi/bigBrother)

Das Auslesen der RFID-Chips ist serpariert, um unabhängig vom main.py Script zu sein. In einer Infinite-Loop sucht der Scanner nach Chips und ließt rangehaltene alle 2sec aus. Die ausgelesenen Daten werden mit den Daten der Datenbak verglichen und je nach Fall (bekannt erlaubt, bekannt nicht erlaubt, unbekannt) werden uterschiedliche Mekdungen auf dem LCD Display ausgegeben. Das Ergebnis wird mittels Prpared-Statement an die Datenbank übermittelt und in der entrylog tabelle gespeichert.
Die main.py und das Auslesen der Chips können gleichzeitig laufen.

Gestartet wird mit python3 RFID_auslesen_LCD.py (im Projektordner /home/pi/bigBrother)

Das Beschreiben/Überschreiben der RFID-Chips ist ebenfalls separiert, da es nicht mit gleichzeitig mit dem Auslesescript laufen darf. Außerdem ist es kein Automatisierter Prozess und muss manuell angestoßen werden, wenn es benötigt wird. Es scannt Chips, die an den Sensor gehalten werden ließt deren Authentication-Code aus und schreibt an die Position[8] ein Array mit 16 zufälligen Zahlen, Fragt den Beutzer nach input für den Namen und das SecurityLevel uns speichert die Einträge in der Datenbank (rfid)
Dieses script ist ausgelagert, da es eine andere Konfiguration des Pin-Boards benötigt.

Gestartet wird mit python3 sensoro/writeRFID/Write.py (im Projektordner /home/pi/bigBrother)

