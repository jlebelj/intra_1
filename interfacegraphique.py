# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfacegraphique.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(964, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_ajouter = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_ajouter.setGeometry(QtCore.QRect(30, 620, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_ajouter.setFont(font)
        self.pushButton_ajouter.setObjectName("pushButton_ajouter")
        self.label_numero = QtWidgets.QLabel(self.centralwidget)
        self.label_numero.setGeometry(QtCore.QRect(20, 5, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_numero.setFont(font)
        self.label_numero.setObjectName("label_numero")
        self.lineEdit_numero = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_numero.setGeometry(QtCore.QRect(20, 50, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_numero.setFont(font)
        self.lineEdit_numero.setObjectName("lineEdit_numero")
        self.textBrowser_afficher = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_afficher.setGeometry(QtCore.QRect(210, 560, 571, 171))
        self.textBrowser_afficher.setObjectName("textBrowser_afficher")
        self.lineEdit_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_nom.setGeometry(QtCore.QRect(30, 400, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.lineEdit_nom.setFont(font)
        self.lineEdit_nom.setObjectName("lineEdit_nom")
        self.label_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_nom.setGeometry(QtCore.QRect(30, 360, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_nom.setFont(font)
        self.label_nom.setObjectName("label_nom")
        self.label_erreur_numero = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_numero.setEnabled(True)
        self.label_erreur_numero.setGeometry(QtCore.QRect(20, 150, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_numero.setFont(font)
        self.label_erreur_numero.setObjectName("label_erreur_numero")
        self.pushButton_supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_supprimer.setGeometry(QtCore.QRect(790, 620, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_supprimer.setFont(font)
        self.pushButton_supprimer.setObjectName("pushButton_supprimer")
        self.pushButton_modifier = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_modifier.setGeometry(QtCore.QRect(30, 500, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_modifier.setFont(font)
        self.pushButton_modifier.setObjectName("pushButton_modifier")
        self.label_programme = QtWidgets.QLabel(self.centralwidget)
        self.label_programme.setGeometry(QtCore.QRect(490, 410, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_programme.setFont(font)
        self.label_programme.setObjectName("label_programme")
        self.comboBox_programme = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_programme.setGeometry(QtCore.QRect(490, 460, 291, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_programme.setFont(font)
        self.comboBox_programme.setObjectName("comboBox_programme")
        self.comboBox_programme.addItem("")
        self.comboBox_programme.addItem("")
        self.comboBox_programme.addItem("")
        self.pushButton_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sauvegarder.setGeometry(QtCore.QRect(30, 680, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_sauvegarder.setFont(font)
        self.pushButton_sauvegarder.setObjectName("pushButton_sauvegarder")
        self.pushButton_afficher_listview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_afficher_listview.setGeometry(QtCore.QRect(790, 680, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_afficher_listview.setFont(font)
        self.pushButton_afficher_listview.setObjectName("pushButton_afficher_listview")
        self.dateEdit_DNaiss = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_DNaiss.setGeometry(QtCore.QRect(20, 240, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateEdit_DNaiss.setFont(font)
        self.dateEdit_DNaiss.setObjectName("dateEdit_DNaiss")
        self.label_date_naiss = QtWidgets.QLabel(self.centralwidget)
        self.label_date_naiss.setGeometry(QtCore.QRect(20, 200, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_date_naiss.setFont(font)
        self.label_date_naiss.setObjectName("label_date_naiss")
        self.pushButton_serealiser = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_serealiser.setGeometry(QtCore.QRect(30, 560, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_serealiser.setFont(font)
        self.pushButton_serealiser.setObjectName("pushButton_serealiser")
        self.label_erreur_nom = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_nom.setEnabled(True)
        self.label_erreur_nom.setGeometry(QtCore.QRect(30, 450, 441, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_nom.setFont(font)
        self.label_erreur_nom.setObjectName("label_erreur_nom")
        self.label_erreur_date = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_date.setEnabled(True)
        self.label_erreur_date.setGeometry(QtCore.QRect(20, 290, 471, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_erreur_date.setFont(font)
        self.label_erreur_date.setObjectName("label_erreur_date")
        self.label_erreur_Etu_Existe = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_Etu_Existe.setGeometry(QtCore.QRect(20, 100, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_Etu_Existe.setFont(font)
        self.label_erreur_Etu_Existe.setObjectName("label_erreur_Etu_Existe")
        self.label_erreur_Etu_Inexistant = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_Etu_Inexistant.setGeometry(QtCore.QRect(20, 130, 421, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_Etu_Inexistant.setFont(font)
        self.label_erreur_Etu_Inexistant.setObjectName("label_erreur_Etu_Inexistant")
        self.label_erreur_fichier = QtWidgets.QLabel(self.centralwidget)
        self.label_erreur_fichier.setGeometry(QtCore.QRect(360, 520, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_erreur_fichier.setFont(font)
        self.label_erreur_fichier.setAutoFillBackground(True)
        self.label_erreur_fichier.setTextFormat(QtCore.Qt.RichText)
        self.label_erreur_fichier.setScaledContents(False)
        self.label_erreur_fichier.setWordWrap(False)
        self.label_erreur_fichier.setObjectName("label_erreur_fichier")
        self.BT_casier = QtWidgets.QPushButton(self.centralwidget)
        self.BT_casier.setGeometry(QtCore.QRect(790, 560, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BT_casier.setFont(font)
        self.BT_casier.setObjectName("BT_casier")
        self.label_num_c = QtWidgets.QLabel(self.centralwidget)
        self.label_num_c.setGeometry(QtCore.QRect(490, 10, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_num_c.setFont(font)
        self.label_num_c.setObjectName("label_num_c")
        self.label_taille = QtWidgets.QLabel(self.centralwidget)
        self.label_taille.setGeometry(QtCore.QRect(490, 300, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_taille.setFont(font)
        self.label_taille.setObjectName("label_taille")
        self.CB_localisation = QtWidgets.QComboBox(self.centralwidget)
        self.CB_localisation.setGeometry(QtCore.QRect(490, 240, 291, 51))
        self.CB_localisation.setObjectName("CB_localisation")
        self.CB_localisation.addItem("")
        self.CB_localisation.addItem("")
        self.CB_localisation.addItem("")
        self.MS_e_num_c1 = QtWidgets.QLabel(self.centralwidget)
        self.MS_e_num_c1.setEnabled(True)
        self.MS_e_num_c1.setGeometry(QtCore.QRect(490, 110, 451, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_c1.setFont(font)
        self.MS_e_num_c1.setObjectName("MS_e_num_c1")
        self.MS_e_num_c2 = QtWidgets.QLabel(self.centralwidget)
        self.MS_e_num_c2.setEnabled(True)
        self.MS_e_num_c2.setGeometry(QtCore.QRect(490, 140, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_c2.setFont(font)
        self.MS_e_num_c2.setObjectName("MS_e_num_c2")
        self.line_num_c = QtWidgets.QLineEdit(self.centralwidget)
        self.line_num_c.setGeometry(QtCore.QRect(490, 50, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(True)
        self.line_num_c.setFont(font)
        self.line_num_c.setObjectName("line_num_c")
        self.label_casier = QtWidgets.QLabel(self.centralwidget)
        self.label_casier.setGeometry(QtCore.QRect(490, 190, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_casier.setFont(font)
        self.label_casier.setObjectName("label_casier")
        self.CB_taille = QtWidgets.QComboBox(self.centralwidget)
        self.CB_taille.setGeometry(QtCore.QRect(490, 350, 291, 51))
        self.CB_taille.setObjectName("CB_taille")
        self.CB_taille.addItem("")
        self.CB_taille.addItem("")
        self.CB_taille.addItem("")
        self.MS_e_num_c3 = QtWidgets.QLabel(self.centralwidget)
        self.MS_e_num_c3.setEnabled(True)
        self.MS_e_num_c3.setGeometry(QtCore.QRect(490, 170, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.MS_e_num_c3.setFont(font)
        self.MS_e_num_c3.setObjectName("MS_e_num_c3")
        self.BT_cour = QtWidgets.QPushButton(self.centralwidget)
        self.BT_cour.setGeometry(QtCore.QRect(790, 500, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.BT_cour.setFont(font)
        self.BT_cour.setObjectName("BT_cour")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 964, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.pushButton_ajouter, self.lineEdit_numero)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ajouter.setText(_translate("MainWindow", "Ajouter"))
        self.label_numero.setText(_translate("MainWindow", "Numéro d\'étudiant"))
        self.label_nom.setText(_translate("MainWindow", "Nom de l\'étudiant"))
        self.label_erreur_numero.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\"> Numéro d\'étudiant invalide. Entrez une valeur numérique.</span></p></body></html>"))
        self.pushButton_supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.pushButton_modifier.setText(_translate("MainWindow", "Modifier"))
        self.label_programme.setText(_translate("MainWindow", "Programme"))
        self.comboBox_programme.setItemText(0, _translate("MainWindow", "Technique de l\'informatique"))
        self.comboBox_programme.setItemText(1, _translate("MainWindow", "Sciences infirmières"))
        self.comboBox_programme.setItemText(2, _translate("MainWindow", "Administration"))
        self.pushButton_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.pushButton_afficher_listview.setText(_translate("MainWindow", " ListView"))
        self.label_date_naiss.setText(_translate("MainWindow", "Date de naissance"))
        self.pushButton_serealiser.setText(_translate("MainWindow", "Sérialiser"))
        self.label_erreur_nom.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Nom d\'étudiant invalide. Entrez une valeur alphabétique.</span></p></body></html>"))
        self.label_erreur_date.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Date de naissance invalide. L\'âge doit être supérieur à 18 ans.</span></p></body></html>"))
        self.label_erreur_Etu_Existe.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant existe déjà. Entrez un nouvel étudiant.</span></p></body></html>"))
        self.label_erreur_Etu_Inexistant.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">L\'étudiant n\'existe pas.</span></p></body></html>"))
        self.label_erreur_fichier.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.BT_casier.setText(_translate("MainWindow", "ajouter casier"))
        self.label_num_c.setText(_translate("MainWindow", "Numero du casier"))
        self.label_taille.setText(_translate("MainWindow", "Taille du casier"))
        self.CB_localisation.setItemText(0, _translate("MainWindow", "A"))
        self.CB_localisation.setItemText(1, _translate("MainWindow", "B"))
        self.CB_localisation.setItemText(2, _translate("MainWindow", "C"))
        self.MS_e_num_c1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Le numero doit commencer par une lettre suivi de 4 chiffres.</span></p></body></html>"))
        self.MS_e_num_c2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Ce casier n\'est pas disponible.</span></p></body></html>"))
        self.label_casier.setText(_translate("MainWindow", "localisation casier"))
        self.CB_taille.setItemText(0, _translate("MainWindow", "Petit"))
        self.CB_taille.setItemText(1, _translate("MainWindow", "Moyen"))
        self.CB_taille.setItemText(2, _translate("MainWindow", "Grand"))
        self.MS_e_num_c3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#ff0000;\">Le numero de casier est inexistant.</span></p></body></html>"))
        self.BT_cour.setText(_translate("MainWindow", "cour"))
