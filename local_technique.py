from local import *

class Local_technique (Local):
    def __init__(self, p_type_local = "", p_numero_local = "", p_lieu_local = "", p_dimemnsion_local = "",
                p_nb_place = "", p_marque_ordi = "", p_nb_ordi = 0, p_projecteur = False):
        Local.__init__(self, p_type_local, p_numero_local, p_lieu_local, p_dimemnsion_local, p_nb_place)
        self.__marque_ordi = p_marque_ordi
        self.__nb_ordi = p_nb_ordi
        self.Projecteur = p_projecteur

    ##################################################
    ####   Propriétés, accesseurs et mutateurs    ####
    ##################################################

    def get_marque_ordi(self):
        return self.__marque_ordi
    def set_marque_ordi(self, p_marque):
        if len(p_marque) < 100:
            self.__marque_ordi = p_marque
    Marque = property(get_marque_ordi, set_marque_ordi)


    def get_nb_ordi(self):
        return self.__nb_ordi
    def set_nb_ordi(self, p_nb_ordi): # faire try pour savoir si int dans main pop up window
        if 0 < p_nb_ordi < 25:
            self.__nb_ordi = p_nb_ordi
    Nb_ordi = property(get_nb_ordi, set_nb_ordi)





    ############################################
    #####  MÉTHODES SPÉCIALES OU MAGIQUES  #####
    ############################################

    def __str__(self):
        chaine = (f" marque ordinateur: {self.__marque_ordi} nombre d'ordinateur: {self.__nb_ordi} "
                    f"Projecteur: {self.Projecteur}")
        return chaine