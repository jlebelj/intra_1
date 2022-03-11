
#Importation du module sys nécessaire à l'exécution de l'application
import sys

#Importation du fichier du ui converti en pv
import classe
import code_interface_genere as F

# importation des classes necessaires
from classe import *

# declaration des donnees globale
lst_Etudiant = []

#Importation des librairies nécessaires à QtDesigne
from PyQt5 import QtWidgets, QtCore


def valider_num(nom_E):
    if nom_E.isalpha():
        return True
    else:
        return False

def valider_nom(num_E):
    if num_E.isnumeric():
        return True
    else:
        return False


class FenetreQt(QtWidgets.QMainWindow,F.Ui_MainWindow):
    def __init__(self, parent = None):
        super(FenetreQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion de scolarité")

    @QtCore.pyqtSlot()
    def on_ButtonOk_clicked(self):
        #self.lblOUT.setText("Bonjour " + Texte)
        num_E = self.line_num.t()
        nom_E = self.line_nom.text()

        if valider_num(num_E) and valider_num(nom_E):
            Etud = Etudiant(nom_E, num_E)
            lst_Etudiant.append(Etud)
            self.TB_answer.setText(Etud.__str__())
        else :







def main():
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreQt()
    form.show()
    app.exec()
if __name__ == "__main__":
    main()

