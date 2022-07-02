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



baum = Knoten(10, "")
baum.insert(3, "befindet sich in Lager 1f")
baum.insert(5, "befindet sich in Lager 5d")


baum.PrintTree()

#print(baum.findaten(3))
