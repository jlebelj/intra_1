

class Casier:
    def __init__(self, numero_casier = "", taille_casier = "", localisation_casier = "", prix_casier = 20):
        self.__num = numero_casier
        self.taille = taille_casier
        self.localisation = localisation_casier
        self.__prix = prix_casier

    def get_num_casier(self):
        return self.__num
    def set_num_casier(self, numero_casier):
        if len(numero_casier) == 5:
            if numero_casier[0].isalpha() and numero_casier[1:].isnumeric():
                self.__num = numero_casier
    Num_casier = property(get_num_casier, set_num_casier)

    def get_prix(self):
        return self.__prix
    def set_prix(self):
        pass
    Prix_casier = property(get_prix)





    def __str__(self):
        chaine = (f" {self.__num} \n taille: {self.taille} \n localistion: {self.localisation} \n prix: {self.__prix} "
                f"\n*************************")
        return