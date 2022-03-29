import datetime
class Etudiant:
    def __init__(self, nom_etudiant: str, numero_etudiant: str, programme_etudiant, age_etudiant: int):
        self.__nom = nom_etudiant
        self.__num = numero_etudiant
        self.programme = programme_etudiant
        self.__age = age_etudiant

    def __str__(self):
        output = ("*************************\n")
        output += (f"Nom de l`etudiant: {self.__nom}\n")
        output += (f"Numero etudiant: {self.__num}\n")
        output += (f"Programme de l'etudiant: {self.programme}\n")
        output += (f"Age de l'etudiant: {self.__age}\n")
        output += ("*************************\n")
        return output


    def get_nom(self):
        return self.__nom
    def set_nom(self, nom_E):
        if nom_E.isalpha() == True:
            self.__nom = nom_E
    Nom = property(get_nom, set_nom)


    def get_num(self):
        return self.__num
    def set_num(self, num_E):
        if num_E is int:
            self.__num = num_E
    Num = property(get_num, set_num)



    def get_age(self):
        return self.__age
    def set_age(self, date_N):
        if datetime.date.today().year - date_N.year() > 18:
            return True
        elif datetime.date.today().year - date_N.year == 18:
            if datetime.date.today().month == date_N.month():
                return True
            elif datetime.date.today().month == date_N.month():
                if datetime.date.today().day >= date_N.day():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    Age = property(get_age, set_age)