import pandas as pd
import time


print("Datenbank bitte hinzufügen...")
try:
    produkte = pd.read_csv(input(""), delimiter=";")
    pn = produkte["PN"]
    lager = produkte["LAGER"]
    lagerliste = lager.values.tolist()
    pnliste = pn.values.tolist()
except:
    print("Falscher Datentyp. Es wird eine 'csv' Datei erwartet")




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

    def delete(self, key):
        if key < self.daten:
            if self.links != None:
                neuesLinks = self.links.delete(key)
                self.links = neuesLinks
                return self
            else:
                if self.links != None:
                    return None
                else:
                    return self
        elif key > self.daten:
            if self.rechts != None:
                neuesRechts = self.rechts.delete(key)
                self.rechts = neuesRechts
                return self
            else:
                if self.rechts != None:
                    return None
                else:
                    return self
        else:
            if self.links == None:
                return self.rechts
            elif self.rechts == None:
                return self.links
            else:
                anders = self.anders()
                self.daten = anders.daten
                self.rechts = self.rechts.delete(self.daten)
                return self

    def anders(self):
        if self.rechts.linkesKind == None:
            return self.rechts
        else:
            return self.rechts.kleinstes()

    def kleinstes(self):
        if self.links.links == None:
            return self.links
        else:
            return self.links.kleinstes()


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
file = produkte
pl = len(pnliste)

i = 0
while i <= pl:
    baum.insert(pnliste[0 + i], lagerliste[0 + i])
    i =i +1
    if i == pl:
        break












def dat_such():
    print("Datensuche")
    userinput = input("Welche Produktnummer suchen Sie? ")
    try:
        print(baum.findaten(int(userinput)))
    except:
        print("Bitte eine Produktnummer angeben!")

def dat_anzeige():
    print("Datenanzeige")
    baum.PrintTree()

def dat_fügen():
    print("Daten hinzufügen")
    try:
        userinput = int(input("Produktnummer: "))
        userinput2 = input("Lagerplatz: ")
        baum.insert(userinput, userinput2)
    except:
        print("Bitte eine valide Produktnummer und Lagernummer angeben!")
        main()



def dat_lösch():
    print("Daten löschen")
    baum.PrintTree()
    userinput = int(input("Zu löschendes Datum: "))
    baum.delete(userinput)

def help():
    print("Wobei brauchen Sie Hilfe?")
    print("Daten suchen (1), \n" "Daten Anzeige (2), \n" "Daten hinzufügen (3), \n" "Daten löschen (4)")
    userinput = input()
    if userinput == "1":
        print("Daten suchen")
        print("Bei der Datensuche erwartet das Programm, dass Sie die gesuchte Produktnummer eingeben")
    if userinput == "2":
        print("Daten Anzeige")
        print("Das Programm zeigt Ihnen den kompletten Baum und alle seine Daten an")
    if userinput == "3":
        print("Daten hinzufügen")
        print("Bei dem Hinzufügen von Daten, erwartet das Programm eine bestimmte Schreibweise: \n" "Beispiel: 187 d5 \n" "Die Zahl '187' steht für die Produktnummer und 'd5' für den Produktstandort")
    if userinput == "4":
        print("Daten löschen")
        print("Bei dem Löschen von Daten, zeigt das Programm Ihnen den gesamten Baum, und Sie werden dann aufgefordert die Produktnummer zu nennen, welche Sie löschen wollen ")


def main():
    print("Datenbank wird gestartet...")
    time.sleep(1.22222)


if __name__ == "__main__":
    main()
    lager_liste = lagerliste
    pn_liste = pnliste
    userinput = ""
    while userinput != "x":
            userinput = input("Daten suchen (1), \n" "Daten Anzeige (2), \n" "Daten hinzufügen (3), \n" "Daten löschen (4), \n " "Help (5), " "Beenden: (x)")
            print("Datenbank wird geladen...")

            if userinput == "1":
                dat_such()

            if userinput == "2":
                dat_anzeige()

            if userinput == "3":
                dat_fügen()
            
            if userinput == "4":
                dat_lösch()

            if userinput == "5":
                help()

    else:
        print("Ende")







