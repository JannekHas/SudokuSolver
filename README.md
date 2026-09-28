# SudokuSolver

Ein Sudoku-Löser für die Konsole, geschrieben in Python. Ich habe ihn gebaut, als ich mit Python angefangen habe.

Du gibst das Sudoku Zeile für Zeile ein, das Programm zeigt es an und füllt dann die Lücken.

## Benutzung

Du brauchst Python 3 und das Paket `tabulate`:

    pip install tabulate
    python main.py

Das Programm fragt nacheinander nach den neun Zeilen. Die Zahlen werden mit Leerzeichen getrennt eingegeben, eine 0 steht für ein leeres Feld:

    Erste Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):
    -> 5 3 0 0 7 0 0 0 0

Danach zeigt es zuerst das eingegebene Sudoku und dann die Lösung. Gibt es keine, steht dort "Keine Lösung gefunden".

## So funktioniert es

Backtracking: Das Programm sucht das erste leere Feld und probiert die Zahlen 1 bis 9. Für jede prüft es, ob sie schon in der Zeile, der Spalte oder dem 3x3-Block steht. Passt eine, geht es zum nächsten leeren Feld. Kommt es nicht weiter, nimmt es den letzten Schritt zurück und probiert die nächste Zahl.

## Was fehlt

Die Eingabe wird nicht geprüft. Ein Buchstabe oder eine falsche Anzahl Zahlen in einer Zeile bringt das Programm zum Absturz. Die Texte sind auf Deutsch.
