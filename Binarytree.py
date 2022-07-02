import pandas as pd
import time

produkte = pd.read_csv("test.csv", delimiter=";")
pn = produkte["PN"] #falls andere csv PN ändern
lager = produkte["LAGER"]
lagerliste = lager.values.tolist()
pnliste = pn.values.tolist()


class Knoten:
    def __init__(self, daten, Lager):
        self.links = None
        self.rechts = None
        self.daten = daten
        self.Lager = Lager


    def insert(self, daten, Lager):
            if self.daten:
                if daten < self.daten:
                    if self.links is None:
                        self.links = Knoten(daten, Lager)
                    else:
                        self.links.insert(daten, Lager)
                elif daten > self.daten:
                    if self.rechts is None:
                        self.rechts = Knoten(daten, Lager)
                    else:
                        self.rechts.insert(daten, Lager)
            else:
                self.daten = daten


    def PrintTree(self):
        if self.links:
            self.links.PrintTree()
        print(self.daten, self.Lager),
        if self.rechts:
            self.rechts.PrintTree()

    def findaten(self, value):
        if value < self.daten:
            if self.links is None:
                return str(value)+" Not Found"
            return self.links.findaten(value)
        elif value > self.daten:
            if self.rechts is None:
                return str(value)+" Not Found"
            return self.rechts.findaten(value)
        else:
            print(str(self.daten) + ' is found in ' + self.Lager)



baum = Knoten(100, "1f")
baum.insert(5, "1f")
file = "1test1.xlsx"
pl = len(pnliste)

i = 0
while i <= pl:
    baum.insert(pnliste[0 + i], lagerliste[0 + i])
    i =i +1
    if i == pl:
        break








def dat_import():
    return

def dat_such():
    print("Datensuche")
    userinput = input("Welche Produktnummer suchen Sie? ")
    print(baum.findaten(int(userinput)))

def dat_anzeige():
    print("Datenanzeige")
    baum.PrintTree()

def dat_fügen():
    print("Daten hinzufügen")
    userinput = int(input("Produktnummer: "))
    userinput2 = input("Lagerplatz: ")
    baum.insert(userinput, userinput2)

def dat_lösch():
    print("Daten löschen")
    baum.PrintTree()
    userinput = int(input("Zu löschendes Datum: "))






def main():
    print("Datenbank wird gestartet...")
    time.sleep(1.22222)


if __name__ == "__main__":
    main()
    lager_liste = lagerliste
    pn_liste = pnliste
    userinput = ""
    while userinput != "x":
            userinput = input(
                "Daten importieren (1), \n" "Daten suchen (2), \n" "Daten anzeige (3), \n" "Daten hinzufügen (4), \n" "Daten löschen (5), \n " "Help (6), " "Beenden: (x)")
            print("Datenbank wird geladen...")
            if userinput == "1":
                dat_import()
            if userinput == "2":
                dat_such()

            if userinput == "3":
                dat_anzeige()

            if userinput == "4":
                dat_fügen()
            
            if userinput == "5":
                dat_lösch()
            """
            if userinput == "6":
                #help()

    else:
        print("Falsch")
"""






