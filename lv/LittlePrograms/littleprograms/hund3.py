class Hund:  # Namen werden mit CamelCase groß geschrieben (Bsp. HundMitKatze)
    species = "Canis lupus familiaris"  # Klassenattribut (oder auch stat. Attribut genannt)
    zaehler = 0  # zählen wie viele Hundeobjekte es gibt

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value

    @property
    def chip(self):
        return self.__chip

    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n: str, a: int, c: str):
        self.name = n  # Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eigene Version davon)
        self.age = a # theortisch könnte ich self.__age = -77 machen (ist aber doof - nciht machen)

        # muss auf __chip verändert werden, da wir auf .chip nicht zuweisen dürfen
        self.__chip = c  # jeder hund erhält eindeutige chip nummer
        # hier koette beliebig komplexer code stehen der auch andere objekete erzeugt
        # oder methoden aufruft, datenbanken befragt oder elon musk eine email schickt

        Hund.zaehler += 1

    def __str__(self):
        return f'{self.name} ist schon {self.age} Jahre alt'

    def __repr__(self):
        return f'Hund(name={self.name}, age={self.age}'

    def __del__(self):
        Hund.zaehler -= 1

    # bezieht sich nur auf die Methode/funktion/objekt direkt darunter
    @classmethod
    def print_anzahl_hunde(cls):
        print(f'Hier gibt es {cls.zaehler} glückliche Hunde')

    def gib_laut(self, text: str):
        print(f'{self.name} bellt ganz laut {text}')

    def knurren(self):
        print(f'knurr')


class Corgi(Hund):
    # es wird standardmäßig nur ein init aufgerufen (spezialität von python)
    # wenn wir gar kein init hätten dann würde das init von der elternklasse (Hund) aufgerufen werden
    def __init__(self, name: str, age: int, chip: str, iq : int):
        # hier müssen wir unsere initialisierung machen - wir müssen explizit das init unserer basisklasse aufrufen
        # dafür gibt es zwei möglichkeiten (weniger schön)
        # Hund.__init__(self, name, age, chip)
        # die schöne variante - achtung wirklich mit () - mit super() Bezug zu meiner Basisklasser
        super().__init__(name, age, chip)
        self.iq = iq

    def gib_laut(self, text: str):
        print(f'{self.name} ist {self.iq} Punkte intelligent und bellt deshalb etwas weniger laut {text} um andere Tiere nicht zu stören')


if __name__ == '__main__':
    rex = Hund("Komissar Rex", 14, "ABC")
    lassie = Hund("Lassie", 12, "DEF")

    print(rex.chip)

    c = Corgi("Cheddar", 13, "CHIPID", 120)

    c.knurren()
    c.gib_laut("winke winke")
