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

if __name__ == '__main__':
    rex = Hund("Komissar Rex", 14, "ABC")
    lassie = Hund("Lassie", 12, "DEF")

    print(rex.chip)
    # geht nicht - kann das attribut nicht setzen
    # rex.chip = "BLA"
    print(rex.age)
    rex.age = -7
    rex.age = 12
    print(rex.__age)# = 14 # nicht machen

    Hund.print_anzahl_hunde()



    rex.gib_laut("Hallo gibt mir bitte eine Extrawurstsemmel")

    print(rex)
    print(lassie)

    hunde_haus = [rex, lassie]
    print(hunde_haus)

    for h in hunde_haus:
        print(h)

    # nicht notwendig weil __str__ automatisch bei print verwendet wird
    print(lassie.__str__())

    # wie verändere ich das alter von rex?
    rex.age = 4

    hunde_haus = None
    lassie = None

    # hinweis: wenn liste vorhanden ist dann wahrscheinlich nicht schnell genug alles freigegeben - ohne liste funktioniert
    Hund.print_anzahl_hunde()
    print(Hund.zaehler)