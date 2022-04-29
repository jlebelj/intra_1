from local import *

class Local_normal (Local):
    def __init__(self, p_type_local = "", p_numero_local = "", p_lieu_local = "", p_dimemnsion_local = "",
                p_nb_place = "", p_nb_table = 0):
        Local.__init__(self, p_type_local, p_numero_local, p_lieu_local, p_dimemnsion_local, p_nb_place)
        self.__nb_table = p_nb_table


    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_nb_table(self):
        return self.__nb_table
    def set_nb_table(self, p_nb):
        if p_nb == 1 or p_nb == 2:
            self.__nb_table = p_nb
    Marque = property(get_nb_table, set_nb_table)




    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        chaine = (f" Nombre de table: {self.__nb_table}")
        return chaine