class Hund:  # Namen werden mit CamelCase groß geschrieben (Bsp. HundMitKatze)
    species = "Canis lupus familiaris"  # Klassenattribut (oder auch stat. Attribut genannt)

    # init Methode wird aufgerufen wenn neues objekt erzeugt wird
    def __init__(self, n: str, a: int):
        self.name = n  # Parameter n wird auf Instanzattribut gespeichert (jedes Objekt/Instanz hat eigene Version davon)
        self.age = a
        # hier koette beliebig komplexer code stehen der auch andere objekete erzeugt
        # oder methoden aufruft, datenbanken befragt oder elon musk eine email schickt

    def gib_laut(self, text: str):
        print(f'{self.name} bellt ganz laut {text}')

if __name__ == '__main__':
    rex = Hund("Komissar Rex", 14)
    lassie = Hund("Lassie", 12)

    rex.gib_laut("Hallo gibt mir bitte eine Extrawurstsemmel")

    # Zugriff auf dsa Klassenattribut
    print(Hund.species)
    print(Hund.__dict__)
    # Instanzattribut Zugriff auf age
    print(rex.age)
    print(lassie.age)
    # wir können aber auch auf Klassenattribute (ACHTUNG NUR lesend) über Istanz zugreifen
    print(rex.species)
    print(lassie.__dict__) # python schaut im __dict__ der Istanz nach ob es das Ding nach dem . kennt
    # sonst schaut es im __dict__ der Klasse weiter


    # was passiert wenn wir das ACHTUNG NUR lesend ignorieren??
    # pfui nicht nachmachen
    #lassie.species = "Kaetzchen" # fügt ein neues Instanzattribut hinzu und ändert nicht das Klassenattribut
    #print(lassie.__dict__)

    # Take home message: Klassenattribute über Klassen zugreifen (notfalls lesend über Instanz)
    # Instanzattribute über Instanz zugreifen

