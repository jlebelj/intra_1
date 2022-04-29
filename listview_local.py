# Importer la librairie QtWidgets de QtDesigner.
from PyQt5 import QtWidgets
# Pour le gestionnaire d'événement
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QStandardItemModel, QStandardItem
# Importer la boite de dialogue
import interface_pop_local
# importer classe
from local import *
from Etudiant import *


#######################################
###### DÉFINITIONS DES FONCTIONS ######
#######################################
lst_local = [Local(""),]

######################################################
###### DÉFINITIONS DE LA CLASSE Fenetrelistview ######
######################################################

class Fenetre_listview_local(QtWidgets.QDialog, interface_pop_local.Ui_Dialog):
    def __init__(self, parent=None):
        super(Fenetre_listview_local, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Local")
        self.MS_e_num_v.setVisible(False)
        self.MS_e_num_inex.setVisible(False)
        for e in lst_local:
            self.CB_cour.addItem(e)

    @pyqtSlot()
    def on_BT_quitter_local_clicked(self):
        self.close()

    @pyqtSlot()
    def on_BT_confirmer_cour_clicked(self):
        pass



























