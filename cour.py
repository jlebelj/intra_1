####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Description de la classe Etudiant
####################################################################################

class Cour:
    """
    classe cour
    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################

    def __init__(self, c_sigle = "", c_titre = "", c_nb_heure = ""):
        self.__sigle_cour = c_sigle
        self.__titre_cour = c_titre
        self.__nb_heure = c_nb_heure


    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ####                                          ####
    ##################################################

    def get_sigle(self):
        return self.__sigle_cour
    def set_sigle(self, sigle_cour):
        if len(sigle_cour) == 5:
            if sigle_cour[0].isalpha() and sigle_cour[1:].isnumeric():
                self.__sigle_cour = sigle_cour
    Cour = property(get_sigle, set_sigle)

    def get_titre(self):
        return self.__titre_cour
    def set_titre(self, titre_cour):
        if len(titre_cour) <= 60:
            self.__titre_cour = titre_cour
    Titre = property(get_titre, set_titre)

    def get_nb_heure(self):
        return self.__nb_heure
    def set_nb_heure(self, nb_heure_cour):
        if nb_heure_cour.isnumeric() is True:
            self.__nb_heure = nb_heure_cour
    Nb_heure = property(get_nb_heure, set_nb_heure)


    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self) :
        """
                Méthode spéciale d'affichage. À utiliser avec print(objet)
                :return: Chaine à afficher
        """
        output = ("*************************\n")
        output += (f"Sigle du cour: {self.__sigle_cour}\n")
        output += (f"Titre du cour: {self.__titre_cour}\n")
        output += (f"Nombre d'heure du cour: {self.__nb_heure}\n")
        return output









