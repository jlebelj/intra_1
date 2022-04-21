# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot

# Importer la boite de dialogue

import formulaire_dialogue_listview

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################


class Fenetre_listview_cour(QtWidgets.QDialog, formulaire_dialogue_listview.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_listview_cour, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Liste des étudiant.e.s")

    @pyqtSlot()
    def on_BT_quitter_cour_clicked(self):
        self.close()

    @pyqtSlot()
    def on_BT_confirmer_cour_clicked(self):
















