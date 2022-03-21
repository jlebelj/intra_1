
#Importation du module sys nécessaire à l'exécution de l'application
import sys
import datetime
#Importation du fichier du ui converti en pv
import classe
import code_interface_genere as F

# importation des classes necessaires
from classe import *

# declaration des donnees globale
lst_Etudiant = []

currentDateTime = datetime.datetime.now()   #
date = currentDateTime.date()               # date aujourd'hui
date_auj = int(date.strftime("%Y"))         #


#Importation des librairies nécessaires à QtDesigne
from PyQt5 import QtWidgets, QtCore


def valider_nom(nom_E):
    if nom_E.isalpha() == True:
        return True
    else:
        return False

def valider_num(num_E):
    try:
        int(num_E)
    except:
        return False
    else:
        return True



# Classe QT designer
class FenetreQt(QtWidgets.QMainWindow,F.Ui_MainWindow):
    def __init__(self, parent = None):
        super(FenetreQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Gestion de scolarité")
    @QtCore.pyqtSlot()
    def on_BT_ajouter_clicked(self):
        num_E = self.line_num.text()
        nom_E = self.line_nom.text()
        programme_E = self.CB_choix.currentText()
        date_N = self.DE_age.date().year() # date naissance etudiant
        age_E = date_auj - date_N # age etudiant
        if valider_num(num_E) and valider_nom(nom_E):
            etud = Etudiant(nom_E, num_E, programme_E, age_E)
            lst_Etudiant.append(etud)
            self.TB_answer.clear()
            for e in lst_Etudiant:
                self.TB_answer.append(e.__str__())

        else:
            self.MS_erreur.setText("Erreur! Donnees entrees incorrectes")
            self.line_num.clear()
            self.line_nom.clear()


    @QtCore.pyqtSlot()
    def on_BT_modifier_clicked(self):
        print("A")
        num_E = self.line_num.text()
        nom_E = self.line_nom.text()
        programme_E = self.CB_choix.currentText()
        print("B")
        if valider_num(num_E) and valider_nom(nom_E):
            print("C")
            for e in lst_Etudiant:
                print("D")
                if e.num == num_E:
                    e.programme = programme_E
                    e.nom = nom_E




        else:
            self.MS_erreur.setText("Erreur! Donnees entrees incorrectes")
            self.line_num.clear()
            self.line_nom.clear()






"""    @QtCore.pyqtSlot()
    def on_BT_supprimer(self):
        num_E = self.line_num.text()
        nom_E = self.line_nom.text()
        print("B")
        if valider_num(num_E) and valider_nom(nom_E):
            for e in lst_Etudiant:
                if num_E == e.:
                    num_E =
                    nom_E =
                    programme_E =



        else:
        self.MS_erreur.setText("Erreur! Donnees entrees incorrectes")
        self.line_num.clear()
        self.line_nom.clear()"""





def main():
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreQt()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()

