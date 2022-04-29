# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Importer la boite de dialogue
import interface_pop_cour
# importer classe
from cour import *
from Etudiant import *
from main import ls_Etudiants
# definition

ls_cour = [Cour("a1234","Programmation", "45"), Cour("a4321", "Ordinateur et reseau PME", "40"),
            Cour("a2143", "objet oriente", "46")]

#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################

def verifier_etudiant_liste(p_num):
    """
        Vérifie si l'étudiant existe dans la liste des étudiants
            :param p_num:  le numéro d'étudiant
            :return: True si l'étudiant est trouvé dans la liste des étudiants et False sinon
    """
    for elt in ls_Etudiants:
        if elt.NumEtud == p_num.capitalize():
            return True
    return False

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetre_listview_cour(QtWidgets.QDialog, interface_pop_cour.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_listview_cour, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiant.e.s")
        self.MS_e_num_v.setVisible(False)
        self.MS_e_num_inex.setVisible(False)
        for e in ls_cour:
            self.CB_cour.addItem(e.Titre)

    @pyqtSlot()
    def on_BT_quitter_cour_clicked(self):
        self.close()

    @pyqtSlot()
    def on_BT_confirmer_cour_clicked(self):
        model = QStandardItemModel()
        etud = Etudiant()
        etud.NumEtud = self.line_num_cour.text()
        choix_c = self.CB_cour.currentText()
        verifer_etudiant = verifier_etudiant_liste(etud.NumEtud)
        if etud.NumEtud == "":
            self.line_num_cour.clear()
            self.MS_e_num_v.setVisible(True)
        if verifer_etudiant is False:
            self.line_num_cour.clear()
            self.MS_e_num_inex.setVisible(True)
        for elt in ls_Etudiants:
            if elt.NumEtud == etud.NumEtud.capitalize():
                for c in ls_cour:
                    if c.Titre == choix_c:
                        elt.lst_cour.append(c)
                        self.list_view_cour.setModel(model)
                        for e in elt.lst_cour:
                                item = QStandardItem(e.__str__())
                                model.appendRow(item)

















