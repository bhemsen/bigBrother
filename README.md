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

Erreichbar ist die Website unter http://localhost/ 


*Python-Scripte:*
Die main.py startet eine Verbindung mit einer Datenbank - realisiert durch Aufruf der Klasse Database.py. Außerdem werden 2 Threads als Daemon gestartet. 

  - Thread1 ruft in einer Infinite Loop die Funktion der Klasse Database.py insertTemperatureAndHumidity auf, die als Übergabeparameter eine Instanz des DHT11 chips benötigt. Diese Methoden der Instanz auf, die sowohl die Temperatur, als auch Luftfeuchtigkeit auslesen und speichert die ausgelesenen Daten in der Datenbank temperature - realisiert durch ein Prepared-Statement (INSERT)- und wartet 15 sec. Beendet wird der Thread durch STRG + C

  - Thread2 ruft in einer Infinite Loop die Funktion der Klasse Database.py cleanUp auf, die als Übergabeparameter die Anzahl Tage benötigt, nach der die Daten aus der Datenbank gelöscht werden sollen. Dies wird realisiert mit einem Prepared-Statement (Delete), das die alle Einträge löscht, die Älter sind als die übermittelte Anzahl

