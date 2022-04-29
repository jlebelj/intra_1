####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Description de la classe Etudiant
####################################################################################

class Local:
    """
    Classe Etudiant

    """

    ###################################
    #####  MÉTHODE CONSTRUCTEUR  #####
    ###################################
    def __init__(self, p_type_local = "", p_numero_local = "", p_lieu_local = "", p_dimemnsion_local = "", p_nb_place = ""):
        """
                Méthode de type Constructeur avec paramètres et valeurs par défaut
                Définition des attributs publics d'un étudiant
        """
        self.Type_local = p_type_local
        self.__numero_local = p_numero_local
        self.Lieu_local = p_lieu_local
        self.__dimension_local = p_dimemnsion_local
        self.__nb_place = p_nb_place


    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################


    def get_numero_local(self):
        return self.__numero_local
    def set_numero_local(self, num_cour):
        if len(num_cour) == 5:
            if num_cour[0].isalpha() and num_cour[1] == "-" and num_cour[2:].isnumeric():
                self.__numero_local = num_cour
    Numero_local = property(get_numero_local, set_numero_local)

    def get_dimension_local(self):
        return self.__dimension_local
    def set_dimension_local(self, dimension):
        if dimension.isnumeric() is True and dimension > 0:
            self.__dimension_local = dimension
    Dimension = property(get_dimension_local, set_dimension_local)

    def get_nb_place(self):
        return self.__nb_place
    def set_nb_place(self, nb):
        if nb.isnumeric() is True and nb < 25:
            self.__nb_placec = nb
    Nb_place = property(get_nb_place, set_nb_place)















