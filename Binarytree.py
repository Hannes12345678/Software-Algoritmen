import pandas as pd

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
            print(str(self.daten) + ' is found')



baum = Knoten(100, "")
baum.insert(5, "1f")
file = "1test1.xlsx"
pl = len(pnliste)

i = 0
while i <= pl:
    baum.insert(pnliste[0 + i], lagerliste[0 + i])
    i =i +1
    if i == pl:
        baum.PrintTree()
        break







