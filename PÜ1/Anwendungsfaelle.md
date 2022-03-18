# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.2. - Vorverarbeitung der Daten


|                                | Erklärung                                                                                                                                                                               | Beispiel                                                                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Name und Identifikationsnummer | Anwendungsfälle haben einen Namen und werden nach Sachgruppen geordnet durchnummeriert                                                                                                  | UC 2.2. - Vorverarbeiten der Daten                                                                                                                |
| Beschreibung                   | Hier erfolgt eine kurze Beschreibung, was im Anwendungsfall passiert.                                                                                                                   | Daten werden auf Plausibilität geprüft.    |
| Beteiligte Akteure             | Akteure sind beteiligte Personen oder Systeme außerhalb des beschriebenen Systems.                                                                                                      | Die Software                                                                                                                    |
| Status                         | Der Status sagt aus, wie weit die Arbeit an dem Anwendungsfall gediehen ist                                                                                                             | In Arbeit                                                                                                                                        |
| Verwendete Anwendungsfälle     | Wenn der Anwendungsfall auf andere Anwendungsfälle zurückgreift, werden diese Fälle hier aufgezählt.                                                                                    | UC 2.1, UC 2.2, UC 2.3, UC 2.4, UC 2.6, UC 2.6                                                                                                          |
| Auslöser                       | Der fachliche Grund bzw. die Gründe dafür, dass dieser Anwendungsfall ausgeführt wird.                                                                                                  | Nachbereitung einer Leistungsdiagnose durch Diagnostiker:in                                                                                           |
| Vorbedingungen                 | Alle Bedingungen, die erfüllt sein müssen, damit dieser Anwendungsfall ausgeführt werden kann.                                                                                          | Daten sind vollständig vorhanden (UC 1.0)  Daten wurden eingelesen (UC2.1)
| Invarianten                    | Alle Bedingungen, die innerhalb und durch den Anwendungsfall nicht verändert werden dürfen, also auch in einem Misserfolgs- oder Fehlerszenario immer noch gewährleistet werden müssen. | Originial-Aufzeichnung bleiben vorhanden, bis verarbeitete Daten gespeichert werden                                                                        |
| Nachbedingung/Ergebnis         | Der Zustand, der nach einem erfolgreichen Durchlauf des Anwendungsfalls erwartet wird.                                                                                                  | Grafiken und Auswertungen sind gespeichert. Eingangsordner ist leer.                                                                    |
| Standardablauf                 | Die Diagnostiker:in führt das Programm aus, welche alle neuen Daten zu Leistungstests einliest und nacheinander aufbereitet. Bestätigt, dass kein Abbruchkriterium vorliegt und die Daten werden gespeichert                                       | Alle Leistungsstufen werden nacheinander durchlaufen. Überprüfung, ob Widerstandswerte eingehalten. Daten werden gespeichert.                     |
| Alternative Ablaufschritte     | Dies sind Szenarien, die sich außerhalb des Standardablaufs auch bei der (versuchten) Zielerreichung des Anwendungsfalls ereignen können.                                               | Diagnostiker:in erkennt Abbruchgrund und gibt diesen ein. Eingabe wird dokumentiert und mit Daten gespeichert.                                                                         |
| Hinweise                       | Kurze Erklärungen zum besseren Verständnis, Hinweise zu Nebeneffekten, Mengengerüsten soweit erforderlich und alles andere, das nicht weiter oben dargestellt werden kann.              | keine                                                                                                                                            |
| Änderungsgeschichte            | Versionierung, Name des Autors, Datum                                                                                                                                                   | 0.01; 10.01.2022.; Julian Huber                                                                                                                  |
|                                |                                                                                                                                                                                         |                                                                                                                                                  |

### Weitere sind zu befüllen
