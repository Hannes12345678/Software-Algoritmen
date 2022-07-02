class Knoten:
    def __init__(self, daten):
        self.links = None
        self.rechts = None
        self.daten = daten



baum = Knoten(1)
baum.links = Knoten(2)
baum.rechts = Knoten(3)
baum.links.links = Knoten(4)
baum.links.rechts = Knoten(5)
baum.rechts.links