import datetime
import json
class Etudiant:
    def __init__(self, nom_etudiant = "", numero_etudiant = "", programme_etudiant = "", age_etudiant = 0):
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
            self.__age = datetime.date.today().year - date_N.year()
        elif datetime.date.today().year - date_N.year == 18:
            if datetime.date.today().month == date_N.month():
                self.__age = datetime.date.today().year - date_N.year()
            elif datetime.date.today().month == date_N.month():
                if datetime.date.today().day >= date_N.day():
                    self.__age = datetime.date.today().year - date_N.year()
                else:
                    pass
            else:
                pass
        else:
            pass
    Age = property(get_age, set_age)




    def serialiser(self, p_fichier):
        """
        Méthode permttant de sérialiser un objet de la classe Etudiant
        ::param p_fichier : Le nom du fichier qui contiendra l'objet sérialisé
        """
        with open(p_fichier , "w") as fichier:
            json.dump(self.__dict__, fichier)


    def deserialiser(self, p_fichier):
        """
            Méthode permttant de désérialiser un objet de la classe Etudiant
            ::param p_fichier : Le nom du fichier qui contient l'objet sérialisé
                """

        with open(p_fichier , "r") as fichier :
            self.__dict__ = json.load(fichier)

#Sérialiser l'objet instancié
#etud=Etudiant("1234567","Hasna","informatique")
#etud.serialiser("FichierSerialiser1.json")

#Désérialisation

#etud1 = Etudiant()

#etud1.deserialiser("FichierSerialiser1.json")

#print(etud1)