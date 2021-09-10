from tabulate import tabulate

def strToList(str) -> list:
    number = str.replace(" ", "")
    liste = [int(d) for d in number]
    return liste

reihe1 = strToList(input("Erste Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe2 = strToList(input("Zweite Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe3 = strToList(input("Dritte Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe4 = strToList(input("Vierte Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe5 = strToList(input("Fünfte Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe6 = strToList(input("Sechste Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe7 = strToList(input("Siebte Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe8 = strToList(input("Achte Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))
reihe9 = strToList(input("Neunte Reihe des Sudokus eingeben (unbekannt = 0) (Leerzeichen zwischen Zahlen lassen):\n-> "))

sudoku = [reihe1, reihe2, reihe3, reihe4, reihe5, reihe6, reihe7, reihe8, reihe9]

def sudoku_anzeigen(sudoku):
    print(tabulate(sudoku, tablefmt='fancy_grid'))

def nullen_suchen():
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return [i, j]
    return False

def nummer_check(num, i, j):
    for reihe in range(9):
        if sudoku[reihe][j] == num:
            return False

    for spalte in range(9):
        if sudoku[i][spalte] == num:
            return False

    quadrat_reihe = (i // 3) * 3
    quadrat_spalte = (j // 3) * 3

    for i in range(3):
        for j in range(3):
            if sudoku[quadrat_reihe + i][quadrat_spalte + j] == num:
                return False
    return True

def rechner():
    loesung_existiert = nullen_suchen()

    if not loesung_existiert:
        return True

    i, j = loesung_existiert[0], loesung_existiert[1]
    for num in range(1, 10):
        if nummer_check(num, i, j):
            sudoku[i][j] = num
            if rechner():
                return True
            else:
                sudoku[i][j] = 0
    return False

sudoku_anzeigen(sudoku)

if rechner():
    sudoku_anzeigen(sudoku)
else:
    print("Keine Lösung gefunden")
