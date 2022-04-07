# Programmierübung

## PÜ5 - Testing und Logging


### Aufgabenstellung 

Inzwischen hat es ihr Team geschafft den Code des Hackathons zu refactorn und hat einige Klassen und Methoden angelegt, um die Aufgabe zu lösen.

### Aufgaben



1. Öffnen Sie die Datei ```main_4_object_oriented.py``` und machen Sie sich mit den Klassen und Methoden vertraut. Nutzen Sie die angelegten Methoden, um ein funktionierendes Programm zusammenzusetzen und speichern Sie dieses in ```main_5_object_oriented_running.py``` 
2. Der Auftraggeber hält die angezeigt Zusammenfassung für nicht vollständig. Er hätte außerdem noch gerne den Durchschnitt und die Varianz der Herzrate angezeigt. Ergänzen sie die Methode ```create_summary``` der Klasse ```Test```
3. Der Auftraggeber möchte, dass die Interaktion mit dem System überwacht wird. Hierzu soll ein log-File angelegt werden, dass das Einlesen jeder Datei mit Uhrzeit und Subject_ID protokolliert. Außerdem soll jeder Test, der manuell als ungültig markiert wurde, mit Uhrzeit dokumentiert werden.
4. Schreiben Sie eine neue Methode, welche eine schönere Grafik erzeugt und diese auch speichert. Speichern sie dies in der Datei ```main_5_object_oriented_running_logging.py```
5. Die Ergebnisse sollen weiterhin datenbasiert als JSON abgelegt werden. Allerdings sollen die Daten nicht mehr als flache JSON-Datei, sondern als Baum strukturiert abgelegt werden. Der Wurzel-Knoten ist der Test, der sich darunter weiter in die Versuchsperson verzweigt. Zudem soll der Pfad zu den gespeicherten Plots abgelegt werden. Schreiben sie hierfür eine alternative Methode zu save_data(self).
