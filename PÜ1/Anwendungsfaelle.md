# Beschreibung der Anwendungsfälle

## UML-Diagramm

![](UML_UseCase_Ergometer.svg)

## Tabellen


### UC 2.2. - Vorverarbeitung der Daten


|                                | Erklärung                                                                                                                                                                               | Beispiel                                                                                                                                         |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Name und Identifikationsnummer | Anwendungsfälle haben einen Namen und werden nach Sachgruppen geordnet durchnummeriert                                                                                                  | UC 2.2. - Vorverarbeiten der Daten                                                                                                                |
| Beschreibung                   | Hier erfolgt eine kurze Beschreibung, was im Anwendungsfall passiert.                                                                                                                   | Daten werden auf Plausibilität geprüft.    |
| Beteiligte Akteure             | Akteure sind beteiligte Personen oder Systeme außerhalb des beschriebenen Systems.                                                                                                      | Software (Prüfcode) + Speicher                                                                                                                    |
| Status                         | Der Status sagt aus, wie weit die Arbeit an dem Anwendungsfall gediehen ist                                                                                                             | In Arbeit                                                                                                                                        |
| Verwendete Anwendungsfälle     | Wenn der Anwendungsfall auf andere Anwendungsfälle zurückgreift, werden diese Fälle hier aufgezählt.                                                                                    | UC 1.0 UC 2.1                                                                                                         |
| Auslöser                       | Der fachliche Grund bzw. die Gründe dafür, dass dieser Anwendungsfall ausgeführt wird.                                                                                                  | Vorverarbeitung der Daten ist wichtig, um Fehler im weiteren Verlauf zu verhindern.                                                                                           |
| Vorbedingungen                 | Alle Bedingungen, die erfüllt sein müssen, damit dieser Anwendungsfall ausgeführt werden kann.                                                                                          | Daten sind vollständig vorhanden (UC 1.0)  Daten wurden eingelesen (UC2.1)
| Invarianten                    | Alle Bedingungen, die innerhalb und durch den Anwendungsfall nicht verändert werden dürfen, also auch in einem Misserfolgs- oder Fehlerszenario immer noch gewährleistet werden müssen. | Eingelesene Daten werden nicht nicht verändert sondern nur kontrolliert um keine Daten zu verfälschen
| Nachbedingung/Ergebnis         | Der Zustand, der nach einem erfolgreichen Durchlauf des Anwendungsfalls erwartet wird.                                                                                                  | Die Daten sind vorbereitet und gültig und werden weiterverarbeitet.                                                                    |
| Standardablauf                 | Die Diagnostiker:in führt das Programm aus, welche alle neuen Daten zu Leistungstests einliest und nacheinander aufbereitet. Bestätigt, dass kein Abbruchkriterium vorliegt und die Daten werden gespeichert                                       | Daten werden nach erfolgreichem Durchlauf in seperaten Ordnern gespeichert um eine Trennung von wahren und falschen Daten zu schaffen
| Alternative Ablaufschritte     | Dies sind Szenarien, die sich außerhalb des Standardablaufs auch bei der (versuchten) Zielerreichung des Anwendungsfalls ereignen können.                                               | Daten sind ungültig und sind nicht zu gebrauchen im weiteren Verlauf.                                                                         |
| Hinweise                       | Kurze Erklärungen zum besseren Verständnis, Hinweise zu Nebeneffekten, Mengengerüsten soweit erforderlich und alles andere, das nicht weiter oben dargestellt werden kann.              | keine                                                                                                                                            |
| Änderungsgeschichte            | Versionierung, Name des Autors, Datum                                                                                                                                                   | 18.03.2022 - Lilli Niemöller, Johannes Lener                                                                                                                  |
|                                |                                                                                                                                                                                         |                                                                                                                                                  |
*Gut! -YS*

### Weitere sind zu befüllen
