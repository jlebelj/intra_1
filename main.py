####################################################################################
###  420-2G2 - Programmation orientée objet
###  Travail: Exercice 1 - Interface graphique
###  Nom: Hasna Hocini
###  No étudiant: 123456
###  No Groupe:
###  Description du fichier: Programme principal
####################################################################################


#######################################
###  IMPORTATIONS - Portée globale  ###
########+###############################

# Importer le module sys nécessaire à l'exécution.
import sys
# Pour la réinitialisation de la date dans le dateEdit
from PyQt5.QtCore import QDate

# Importer Pour le model de la listView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

# importer les interfaces graphiques
import interfacegraphique
from listview_dialog import *
from listview_cour import *
# Importer la classe Etudiant
from Etudiant import *



##########################################################
###  DÉCLARATIONS ET INITIALISATIONS - Portée globale  ###
##########################################################

# Déclarer une liste d'étudiants
ls_Etudiants = []
C1 = Casier("a1234", "Petit", "A", 20)
test = Etudiant("12", "bob", "Administration", "2000, 1, 1", C1)

C2 = Casier("a4321", "Moyen", "B", 20)
test2 = Etudiant("11", "jac", "Administration", "2000, 1, 1", C2)
ls_Etudiants.append(test)
ls_Etudiants.append(test2)

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

def verifier_lst_casier(num_casier):
    """
        Vérifie si le casier existe dans la liste des casiers
            :param num_casier:  le numéro du casier
            :return: True si le casier est trouvé dans la liste des casiers et False sinon
    """
    for n in ls_Etudiants:
        if n.casier.Num_casier == num_casier.lower():
            return True
    return False

def cacher_labels_erreur(objet):
    """
    Cacher les différents labels d'erreur
    """
    objet.label_erreur_nom.setVisible(False)
    objet.label_erreur_numero.setVisible(False)
    objet.label_erreur_date.setVisible(False)
    objet.label_erreur_Etu_Existe.setVisible(False)
    objet.label_erreur_Etu_Inexistant.setVisible(False)
    objet.MS_e_num_c1.setVisible(False)
    objet.MS_e_num_c2.setVisible(False)
    objet.MS_e_num_c3.setVisible(False)
    objet.label_erreur_fichier.setText("")

########################################################
###### DÉFINITIONS DE LA CLASSE fenetrePrincipale ######
########################################################

# Créer une classe qui hérite de Qt et de notre ui.
# Nom de ma classe (fenetrePrincipal)          # Nom de mon fichier ui
class fenetrePrincipale(QtWidgets.QMainWindow, interfacegraphique.Ui_MainWindow):
    """
    Nome de la classe : fenetrePrincipale
    Héritages :
    - QtWidgets.QMainWindow : Type d'interface créé par QtDesigner
    - interfacegraphique.Ui_MainWindow : Ma classe générée avec QtDesigner
    """

    def __init__(self, parent=None):
        """
        Constructeur de la classe
        :param parent: QtWidgets.QMainWindow et interfacegraphique.Ui_MainWindow
        """
        # Appeler le constructeur parent avec ma classe en paramètre...
        super(fenetrePrincipale, self).__init__(parent)
        # Préparer l'interface utilisateur
        self.setupUi(self)
        # Donner un titre à la fenêtre principale
        self.setWindowTitle("Gestion de scolarité")
        # Cacher tous les labels d'erreur
        cacher_labels_erreur(self)


    # Utiliser le décorateur ici pour empêcher que le code du gestionnaire d'événement du bouton ne s'éxecute deux fois
    @pyqtSlot()
    # Bouton Ajouter
    def on_pushButton_ajouter_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Ajouter
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Eudiant
        etud = Etudiant()
        cas = Casier()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        etud.NomEtud = self.lineEdit_nom.text().capitalize()
        etud.NumEtud = self.lineEdit_numero.text()
        etud.DateNaiss= self.dateEdit_DNaiss.date()
        etud.Programme = self.comboBox_programme.currentText()
        cas.taille = self.CB_taille.currentText()
        cas.localisation = self.CB_localisation.currentText()
        cas.Num_casier = self.line_num_c.text().lower()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_etudiant = verifier_etudiant_liste(etud.NumEtud)
        verifier_casier = verifier_lst_casier(cas.Num_casier)
        # Si le numéro d'étudiant est valide mais existe déjà dans la liste des étudiants (on ne peut donc pas l'ajouter)
        if verifier_casier is True and cas.Num_casier != "":
            self.line_num_c.clear()
            self.MS_e_num_c2.setVisible(True)
        if verifier_etudiant is True and etud.NumEtud != "":
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            self.lineEdit_numero.clear()
            self.label_erreur_Etu_Existe.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if etud.NomEtud == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if etud.NumEtud == "":
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setVisible(True)
        # Si la date de naissance est invalide, afficher un message d'erreur
        if etud.DateNaiss == "":
            self.label_erreur_date.setVisible(True)
        if cas.Num_casier == "":
            self.line_num_c.clear()
            self.MS_e_num_c1.setVisible(True)
        # Si les informations entrées sont valides et l'étudiant n'existe pas dans la liste des étudiants
        if etud.NomEtud != "" and etud.NumEtud != "" and etud.DateNaiss != "" and verifier_etudiant is False \
                and cas.Num_casier != "" and verifier_casier is False:
            #Ajouter l'objet instancié à la liste des étudiants
            ls_Etudiants.append(etud)
            # Ajouter les informations de l'étudiant entré au TextBrowser
            self.textBrowser_afficher.append(etud.__str__() + cas.__str__())
            # Réinitialiser les lineEdits du nom, du numéro d'étudiant et du dateEdit
            self.lineEdit_numero.clear()
            self.lineEdit_nom.clear()
            self.dateEdit_DNaiss.setDate(QDate(2000, 1, 1))
            self.line_num_c.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_BT_cour_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetre_listview_cour() # nomde la classe du pop up
        # Préparer la listview
        model = QStandardItemModel()
        #Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

    @pyqtSlot()
    # Bouton Modifier
    def on_pushButton_modifier_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Modifier
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Eudiant
        etud = Etudiant()
        cas = Casier()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        etud.NomEtud = self.lineEdit_nom.text().capitalize()
        etud.NumEtud = self.lineEdit_numero.text()
        etud.DateNaiss = self.dateEdit_DNaiss.date()
        etud.Programme = self.comboBox_programme.currentText()
        cas.taille = self.CB_taille.currentText()
        cas.localisation = self.CB_localisation.currentText()
        cas.Num_casier = self.line_num_c.text().lower()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_etudiant = verifier_etudiant_liste(etud.NumEtud)
        verifier_casier = verifier_lst_casier(cas.Num_casier)
        # Si le numéro d'étudiant est valide mais existe déjà dans la liste des étudiants (on ne peut donc pas l'ajouter)
        if verifier_etudiant is False:
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            self.lineEdit_numero.clear()
            self.label_erreur_Etu_Inexistant.setVisible(True)
        if verifier_casier is False:
            self.line_num_c.clear()
            self.MS_e_num_c3.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if etud.NomEtud == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant et afficher un message d'erreur
        if etud.NumEtud == "":
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setVisible(True)
        # Si la date de naissance est invalide, afficher un message d'erreur
        if etud.DateNaiss == "":
            self.label_erreur_date.setVisible(True)
        if cas.Num_casier == "":
            self.line_num_c.clear()
            self.MS_e_num_c1.setVisible(True)
        # Si les informations entrées sont valides et l'étudiant n'existe pas dans la liste des étudiants
        if etud.NomEtud != "" and etud.NumEtud != "" and etud.DateNaiss != "" and cas.Num_casier != "" \
                and verifier_etudiant is True and verifier_casier is True:
            for elt in ls_Etudiants:
                # Chercher dans la liste des étudiants un étudiant ayant le numéro d'étudiant entré
                if elt.NumEtud == self.lineEdit_numero.text():
                            # Apporter les modifications aux attributs Nom_Etud, Programme et Date_Naiss
                            elt.NomEtud = self.lineEdit_nom.text().capitalize()
                            elt.Programme = self.comboBox_programme.currentText()
                            elt.DateNaiss = self.dateEdit_DNaiss.date()
                            elt.casier.Num_casier = self.line_num_c.text()
                            elt.casier.taille = self.CB_taille.currentText()
                            elt.casier.localisation = self.CB_localisation.currentText()
            # Effacer le textBowser
            self.textBrowser_afficher.clear()
            # Après modifications, réfficher tous les étudiants de la liste dans le textBrowser
            for elt in ls_Etudiants:
                self.textBrowser_afficher.append(elt.__str__())
            # Réinitialiser les lineEdits du numéro et du nom et le dateEdit
            self.lineEdit_numero.clear()
            self.lineEdit_nom.clear()
            self.dateEdit_DNaiss.setDate(QDate(2000, 1, 1))
            self.line_num_c.clear()

    @pyqtSlot()
    # Bouton Supprimer
    def on_pushButton_supprimer_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Supprimer
        """
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Eudiant
        etud = Etudiant()
        cas = Casier()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        etud.NomEtud = self.lineEdit_nom.text().capitalize()
        etud.NumEtud = self.lineEdit_numero.text()
        etud.DateNaiss = self.dateEdit_DNaiss.date()
        etud.Programme = self.comboBox_programme.currentText()
        cas.taille = self.CB_taille.currentText()
        cas.localisation = self.CB_localisation.currentText()
        cas.Num_casier = self.line_num_c.text().lower()
        # Booleen qui nous informe si le numéro d'étudiant existe ou pas dans la liste des étudiants
        verifier_etudiant = verifier_etudiant_liste(etud.NumEtud)
        verifier_casier = verifier_lst_casier(cas.Num_casier)
        # Si le nom, le numéro et la date de naissance sont valides et l'étudiant existe dans la liste des étudiants:
        if etud.NomEtud != "" and etud.NumEtud != "" and etud.DateNaiss != "" and cas.Num_casier != "" \
                and verifier_casier is True and verifier_etudiant is True:
            trouve = False
            for elt in ls_Etudiants:
                # # Chercher dans la liste des étudiants un étudiant ayant les informations entrées
                date = self.dateEdit_DNaiss.date() # change format de date pour comparer
                if elt.NumEtud == self.lineEdit_numero.text() and elt.NomEtud == self.lineEdit_nom.text() \
                        and elt.DateNaiss == f"{date.year()}, {date.month()}, {date.day()}" \
                        and elt.Programme == self.comboBox_programme.currentText() \
                        and elt.casier.Num_casier == self.line_num_c.text() \
                        and elt.casier.taille == self.CB_taille.currentText() \
                        and elt.casier.localisation == self.CB_localisation.currentText():
                    # Supprimer l'étudiant de la liste des étudiants
                    trouve = True
                    ls_Etudiants.remove(elt)
                    break
            # Si l'étudiant n'existe pas dans la liste afficher un message d'erreur dans le label_erreur_Etu_Inexistant
            if not trouve:
                self.label_erreur_Etu_Inexistant.setVisible(True)
            else:
                # Réafficher dans le textBrowser la nouvelle liste qui ne contient pas l'étudiant supprimé
                self.textBrowser_afficher.clear()
                for elt in ls_Etudiants:
                    self.textBrowser_afficher.append(elt.__str__())
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_numero.clear()
                self.lineEdit_nom.clear()
                self.dateEdit_DNaiss.setDate(QDate(2000,1,1))
                self.line_num_c.clear()
                # Si le numéro d'étudiant est valide mais existe déjà dans la liste (on ne peut donc pas l'ajouter)
        if verifier_etudiant is False:
            # Effacer le lineEdit du numéro étudiant et afficher le message d'erreur
            self.lineEdit_numero.clear()
            self.label_erreur_Etu_Inexistant.setVisible(True)
        if verifier_casier is False:
            self.line_num_c.clear()
            self.MS_e_num_c3.setVisible(True)
        # si le nom est invalide, afficher un message d'erreur
        if etud.NomEtud == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if etud.NumEtud == "":
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setVisible(True)
            # Si la date de naissance est invalide, afficher un message d'erreur
        if etud.DateNaiss == "":
            self.label_erreur_date.setVisible(True)

    @pyqtSlot()
    # Bouton Sauvegarder
    def on_pushButton_sauvegarder_clicked(self):
        """
        Gestionnaire d'évènement pour le bouton Sauvegarder
        """
        chaine = ""
        for elt in ls_Etudiants:
            chaine += elt.__str__()
        try:
            with open("." + "/" + "listeEtudiants"+"/"+"ListeEtudiants.txt", "w") as fichier:
                try :
                    fichier.write(chaine)

                except :
                    self.label_erreur_fichier.setText("<font color=\"#ff0000\">Erreur d'écriture dans le fichier</font>r")
        except :
            self.label_erreur_fichier.setText("<font color=\"#ff0000\">Erreur d'ouverture de fichier</font>")

    @pyqtSlot()
    def on_pushButton_serealiser_clicked(self):
        # Cacher les labels qui affichent les différentes erreurs
        cacher_labels_erreur(self)
        # Instancier un objet Eudiant
        etud = Etudiant()
        # Entrée de donnée pour les attributs de l'objet Etudiant
        etud.NomEtud = self.lineEdit_nom.text().capitalize()
        etud.NumEtud = self.lineEdit_numero.text()
        etud.DateNaiss = self.dateEdit_DNaiss.date()
        etud.Programme = self.comboBox_programme.currentText()
        # Si le nom, le numéro et la date de naissance sont valides :
        if etud.NomEtud != "" and etud.NumEtud != "" and etud.DateNaiss != "":
            # Séréaliser cet objet
            result = etud.serialiser("." + "/" + "Serealiser" + "/" + etud.NomEtud + "_" + etud.NumEtud + ".json")
            # Si la séréalisation a marché
            if result == 0:
                # Réinitialiser les lineEdit et le dateEdit
                self.lineEdit_numero.clear()
                self.lineEdit_nom.clear()
                self.dateEdit_DNaiss.setDate(QDate(2000, 1, 1))
                self.label_erreur_fichier.setText("")
            # sinon afficher des messages d'erreur
            elif result == 1:
                # Afficher le message d'erreur d'écriture dans le fichier
                self.label_erreur_fichier.setText("<font color=\"#ff0000\">Erreur d'écriture dans le fichier</font>")
            else:
                # Afficher le message d'erreur d'ouverture du fichier
                self.label_erreur_fichier.setText("<font color=\"#ff0000\">Erreur d'ouverture du fichier</font>")
        # si le nom est invalide, afficher un message d'erreur
        if etud.NomEtud == "":
            self.lineEdit_nom.clear()
            self.label_erreur_nom.setVisible(True)
        # Si le numéro d'étudiant est invalide, effacer le lineEdit du numéro étudiant  et afficher un message d'erreur
        if etud.NumEtud == "":
            self.lineEdit_numero.clear()
            self.label_erreur_numero.setVisible(True)
            # Si la date de naissance est invalide, afficher un message d'erreur
        if etud.DateNaiss == "":
            self.label_erreur_date.setVisible(True)

    # Bouton Afficher listview
    @pyqtSlot()
    def on_pushButton_afficher_listview_clicked(self):
        # Instancier une boite de dialogue FenetreListview
        dialog = Fenetrelistview() # nomde la classe du pop up
        # Préparer la listview
        model = QStandardItemModel()
        dialog.listView_etudiants.setModel(model)
        for e in ls_Etudiants:
            item = QStandardItem(e.NumEtud+" * "+e.NomEtud + " * " + e.Programme )
            model.appendRow(item)
        #Afficher la boite de dialogue
        dialog.show()
        reply = dialog.exec_()

#################################
###### PROGRAMME PRINCIPAL ######
#################################

# Créer le main qui lance la fenêtre de Qt

def main():
    """
    Méthode main : point d'entré du programme.
    Exécution de l'applicatin avec l'interface graphique.
    reply = Dialog.exec_()
    """
    # Instancier une application et une fenetre principale
    app = QtWidgets.QApplication(sys.argv)
    form = fenetrePrincipale()
    # Afficher la fenêtre principale
    form.show()
    # Lancer l'application
    app.exec()

if __name__ == "__main__":
    main()