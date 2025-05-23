class Rettangolo:
    def __init__(self, base, altezza, colore):
        self.base = base
        self.altezza = altezza
        self.colore = colore

    def area(self):
        return self.base * self.altezza

    def stampa_info(self):
        print("Base:", self.base)
        print("Altezza:", self.altezza)
        print("Colore:", self.colore)
        print("Area:", self.area())