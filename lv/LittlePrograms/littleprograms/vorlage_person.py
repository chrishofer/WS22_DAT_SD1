class Person:
    def __init__(self, vname, zname):
        self.vname = vname
        self.zname = zname

    def get_info(self):
        return f'{self.vname} {self.zname}'

class Student(Person):
    def get_info(self):
        return f'Student*in {self.vname} {self.zname}'

class Oeh_Mitglied(Student):
    def protestieren(selfs):
        return f'Proetestiert besonders engagiert fuer Studi Rechte'


# Lektor*in mit Fachbereich fehlt
class Lektor(Person):
    def __init__(self, vname: str, zname: str, fb: str):
        super().__init__(vname, zname)
        self.fachbereich = fb
    def get_info(self):
        return f'Lektor*in {self.vname} {self.zname} im Fachbereich {self.fachbereich}'

# Mentor*in fehlt
class Mentor(Lektor):
    # kein init da keine eigenen neuen attribute
    def get_info(self):
        return f'Mentor*in {self.vname} {self.zname} kann gut zuhören'


if __name__ == '__main__':
    s = Student("Rudi", "Studi")
    m = Mentor("Sandra", "Ehm", "Data Science")
    oeh = Oeh_Mitglied("Manuell", "Oeh")
    print(m.get_info())
    bunch_of_persons = []
    bunch_of_persons.append(s)
    bunch_of_persons.append(m)
    bunch_of_persons.append(oeh)

    for p in bunch_of_persons:
        print(p.get_info())

