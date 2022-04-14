# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue
import interface_casier
from casier import  *
#instanciation
lst_casier = []
from main import ls_Etudiants

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def cacher_labels_erreur_c(objet):
    objet.MS_e_num_c1.setVisible(False)
    objet.MS_e_num_c2.setVisible(False)



######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetre_casier(QtWidgets.QDialog, interface_casier.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_casier, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Casier")
        cacher_labels_erreur_c(self)


    @pyqtSlot()
    def on_BT_BT_ajouter_c_clicked(self):
        cas = Casier()
        cas.taille = self.CB_taille.currentText()
        cas.localisation = self.CB_localisation.currentText()
        cas.Num_casier = self.line_num_c.text()
        for e in ls_Etudiants:
            if e.casier == e.casier:
                self.line_num_c = e.casier.Num_casier
                self.CB_taille = e.casier.taille
                self.CB_localisation = e.casier.localisation
            else:
                # clear line num etudiant
                # message erreur
                verifier_casier = verifier_lst_casier(cas.Num_casier)
                if verifier_casier is True:
                    self.line_num_c.clear()
                    self.MS_e_num_c2.setVisible(True)
                if cas.Num_casier == "":
                    self.line_num_c.clear()
                    self.MS_e_num_c1.setVisible(True)
                if cas.Num_casier != "":
                    lst_casier.append(cas)













