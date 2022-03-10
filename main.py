
#Importation du module sys nécessaire à l'exécution de l'application
import sys

#Importation du fichier du ui converti en pv
import code_interface_genere as F

#Importation des librairies nécessaires à QtDesigne
from PyQt5 import QtWidgets

class FenetreQt(QtWidgets.QMainWindow,F.Ui_MainWindow):
    def __init__(self, parent = None):
        super(FenetreQt, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Fenetre principale")
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = FenetreQt()
    form.show()
    app.exec()
if __name__ == "__main__":
    main()

def on_ButtonOk_clicked(self):
    Texte = self.txtIN.text()

    self.lblOUT.setText("Bonjour " + Texte)

@QtCore.pyqtSlot()
def on_ButtonOk_clicked(self):
    Texte = self.txtIn.text()
    self.lblOUT.setText("Bonjour " + Texte)