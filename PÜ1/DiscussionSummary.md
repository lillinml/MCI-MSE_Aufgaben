## Project background

Aufgabenstellung in Programmierübung 2 TEAM 11

### Purpose of project

Entwicklung einer Software zur Leistungsdiagnostik in Bezug auf ausgewertete Daten eines Ergometers und auswerten der erbrachten Leistung sowie die Aufzeichnung des Elektrodiagramms

### Scope of project

Daten eines Ergometers sollen importiert, vorbearbeitet, analysiert, ausgewertet, visulasiert und abgespeichert werden.

### Other background information

Team: Lilli Niemöller, Lener Johannes
Auftraggeber: MCI Innsbruck

## Perspectives

Erfolgreicher Abschluss des Projektes und Übergabe an den Kunden.

### Who will use the system?

Diagnostiker:innen

### Who can provide input about the system?

Die Sportler:innen in Verbindung mit dem Ergometer

## Project Objectives

Erfolgreiche Auswertung und Visualisierung der Eingabedagten.
Einfache Darstellung der Daten um schnelle und genaue Diagnosen zu erstellen.

### Known business rules

Name, technische ID und Geburtsdatum der getesteten Personen soll gespeichert werden.
Sobald das Abbruchkriterium erreicht wird, sind Abläufe ungültig. Abbruchkriterium: Puls 90 % der 
maximalen Herzfrequenz (220 – Lebensalter).
Ergebnis (Plot der Herzrate und der Leistung über den Zeitraum) muss zusammen mit den verarbeiteten Daten gespeichert werden.
Erfolgreiche und abgebrochene Versuche sind getrennt zu speichern.

### System information and/or diagrams

Beispiel von aufgezeichneten EKG Daten
![](ekg_example.png)

Aus diesem muss die Herzrate bestimmt werden.

### Assumptions and dependencies

Die 6 Input Files enthalten 2 verschiedene Auswertungen von jeweils 3 Testduchgängen.
Zu jeder "ecg_data_subject" Datei gehört ein "power_data" File. 

Das "power_data" File enthält eine Auswertung über den Watt Bereich des Ergometers. Die aktuelle Leistung wurde mit 1 Hz gemessen, da 180 Messergebnisse auf 180 Sekunden vorhanden sind.
Das "ecg_data_subject" File enthält die Amplitudenwerte der Herzfrequenzmessung. Diese ergeben einen Sinus-Verlauf. Hier sind 180000 Messwertde auf 180 Sekunden vorhanden. Dies entspricht einer Frequenz von 1000Hz.

Die Leistungsmessung/EKG-Messung wurde in 3 verschiedenen Leistungsstufen durchgeführt.

1- 100 Watt +-10%
2- 200 Watt +-10%
3- 300 Watt +-10%

Paralell zu der erbrachten Leistung des Patienten wurde die Herzfrequenz gemessen. Wobei die Zeitliche Auflösung der Herzfrequenzmessung um den Faktor 1000 Höher ist, da diese sich auch schneller ändert als die Leistung die der Patient aufbringt.

Die Daten wurden mithilfe von Matplot grafisch dargestellt.

*Gut, allerdings ergebene EKG-Daten keinen Sinusverlauf. Die Einheit der EKG Messung ist mV, wäre noch wünschenswert. -YS*

### Design and implementation constraints



## Risks

Eingabewerte des Ergometers sind falsch und können nicht auf Richtigkeit überprüft werden.
Werte können falsch ausgewertet werden und dadurch können falsche Diagnosen erstellt werden.

## Known future enhancements

Auswertungsfehler ausbessern, Richtigkeit der Eingabedaten kontrollieren.
Erfahrungen aus Anwendungen mit einfließen lassen.

## References

- [Link zur Aufgabenstellung](tbd)

## Open, unresolved or TBD issues

Absprache mit Kunden 
Visuelle Anforderungen
