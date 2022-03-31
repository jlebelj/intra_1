
#Importation du module sys nécessaire à l'exécution de l'application
import sys
import datetime
#Importation du fichier du ui converti en pv
from PyQt5.QtGui import QStandardItemModel

import classe
import code_interface_genere as F
import code_interface_pop

# importation des classes necessaires
from classe import *

# declaration des donnees globale
lst_Etudiant = []

currentDateTime = datetime.datetime.now()   #
date = currentDateTime.date()               # date aujourd'hui
date_auj = int(date.strftime("%Y"))         #


#Importation des librairies nécessaires à QtDesigne
from PyQt5 import QtWidgets, QtCore

def verifier_etudiant(num_E):
    for e in lst_Etudiant:
        if e.count > 0:
            return True
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
        etud = Etudiant()
        num_E = self.line_num.text()
        nom_E = self.line_nom.text()
        programme_E = self.CB_choix.currentText()
        date_N = self.DE_age.date() # date naissance etudiant
        #if valider_num(num_E) and valider_nom(nom_E):
        print("0")
        etud.Age = date_N
        print("0.1")
        print(date_N)
        if etud.Age == date_N:
            print("hit1")
            etud.Nom = nom_E
            print(etud.Nom)
            if etud.Nom == nom_E:
                print("hit2")
                etud.Num = num_E
                if etud.Num == num_E:
                    print("hit3")
                    lst_Etudiant.append(etud)
                    self.TB_answer.clear()
                    for e in lst_Etudiant:
                        self.TB_answer.append(e.__str__())
                else:
                    print("Mhit1")
                    self.MS_erreur_num.setText("Erreur! Donnees entrees incorrectes1")
                    self.line_num.clear()
            else:
                print("Mhit2")
                self.MS_erreur_num.setText("Erreur! Donnees entrees incorrectes2")
                self.line_num.clear()
        else:
            print("Mhit3")
            self.MS_erreur_age.setText("Erreur! Donnees entrees incorrectes3")
            self.line_age.clear()

"""    @QtCore.pyqtSlot()
    def on_BT_modifier_clicked(self):
        num_E = self.line_num.text()
        nom_E = self.line_nom.text()
        programme_E = self.CB_choix.currentText()
        if valider_num(num_E) and valider_nom(nom_E):
            for e in lst_Etudiant:
                if e.num == num_E:
                    e.programme = programme_E
                    e.nom = nom_E
                    self.TB_answer.clear()
                    for e in lst_Etudiant:
                        self.TB_answer.append(e.__str__())
        else:
            self.MS_erreur.setText("Erreur! Donnees entrees incorrectes")
            self.line_num.clear()
            self.line_nom.clear()
            self.TB_answer.clear()

    @QtCore.pyqtSlot()
    def on_BT_supprimer_clicked(self):
        num_E = self.line_num.text()
        if valider_num(num_E):
            for e in lst_Etudiant:
                if num_E == e.num:
                    lst_Etudiant.remove(e)
                    self.TB_answer.clear()
                    for e in lst_Etudiant:
                        self.TB_answer.append(e.__str__())
        else:
            self.MS_erreur.setText("Erreur! Donnees entrees incorrectes")
            self.line_num.clear()
            self.line_nom.clear()

    @QtCore.pyqtSlot()
    def on_BT_sauvegarder_clicked(self):
        num_E = self.line_num.text()
        nom_E = self.line_nom.text()
        date_N = self.DE_age.date().year()
        age_E = age_E = date_auj - date_N
        programme_E = self.CB_choix.currentText()
        with open("f.txt", "w") as f:
            f.write(self.TB_answer.toPlainText())

    def on_BT_voir_liste_clicked(self):
        dialog = Fenetre_list_view()
        model = QStandardItemModel()
        dialog.Pop_lst_e.setModel(model)
        for e in lst_Etudiant:
            item = (e.num + "*" + e.nom + "*" + e.age + "*" + e.programme)
            model.appendRow(item)
        dialog.show()
        dialog.exec_()

"""




# classe fenetre list view
class Fenetre_list_view(QtWidgets.QDialog, code_interface_pop.Ui_Dialog):
    def __init__(self, parent = None):
        super(Fenetre_list_view, self).__init__(parent)
        self.setupUi(self)







def main():
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreQt()
    form.show()
    app.exec()

if __name__ == "__main__":
    main()

