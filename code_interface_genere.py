# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_QT.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(788, 517)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l_nom = QtWidgets.QLabel(self.centralwidget)
        self.l_nom.setGeometry(QtCore.QRect(50, 10, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.l_nom.setFont(font)
        self.l_nom.setObjectName("l_nom")
        self.line_nom = QtWidgets.QLineEdit(self.centralwidget)
        self.line_nom.setGeometry(QtCore.QRect(20, 30, 251, 51))
        self.line_nom.setObjectName("line_nom")
        self.BT_ajouter = QtWidgets.QPushButton(self.centralwidget)
        self.BT_ajouter.setGeometry(QtCore.QRect(20, 280, 81, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setBold(True)
        font.setWeight(75)
        self.BT_ajouter.setFont(font)
        self.BT_ajouter.setObjectName("BT_ajouter")
        self.line_num = QtWidgets.QLineEdit(self.centralwidget)
        self.line_num.setGeometry(QtCore.QRect(520, 30, 251, 51))
        self.line_num.setText("")
        self.line_num.setObjectName("line_num")
        self.l_num = QtWidgets.QLabel(self.centralwidget)
        self.l_num.setGeometry(QtCore.QRect(540, 0, 221, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.l_num.setFont(font)
        self.l_num.setObjectName("l_num")
        self.TB_answer = QtWidgets.QTextBrowser(self.centralwidget)
        self.TB_answer.setGeometry(QtCore.QRect(440, 260, 341, 201))
        font = QtGui.QFont()
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.TB_answer.setFont(font)
        self.TB_answer.setObjectName("TB_answer")
        self.MS_erreur_num = QtWidgets.QLabel(self.centralwidget)
        self.MS_erreur_num.setGeometry(QtCore.QRect(490, 90, 291, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.MS_erreur_num.setFont(font)
        self.MS_erreur_num.setText("")
        self.MS_erreur_num.setObjectName("MS_erreur_num")
        self.CB_choix = QtWidgets.QComboBox(self.centralwidget)
        self.CB_choix.setGeometry(QtCore.QRect(310, 30, 181, 41))
        self.CB_choix.setObjectName("CB_choix")
        self.CB_choix.addItem("")
        self.CB_choix.addItem("")
        self.DE_age = QtWidgets.QDateEdit(self.centralwidget)
        self.DE_age.setGeometry(QtCore.QRect(20, 160, 131, 31))
        self.DE_age.setObjectName("DE_age")
        self.BT_supprimer = QtWidgets.QPushButton(self.centralwidget)
        self.BT_supprimer.setGeometry(QtCore.QRect(20, 400, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.BT_supprimer.setFont(font)
        self.BT_supprimer.setObjectName("BT_supprimer")
        self.BT_modifier = QtWidgets.QPushButton(self.centralwidget)
        self.BT_modifier.setGeometry(QtCore.QRect(20, 320, 93, 28))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BT_modifier.setFont(font)
        self.BT_modifier.setObjectName("BT_modifier")
        self.BT_sauvegarder = QtWidgets.QPushButton(self.centralwidget)
        self.BT_sauvegarder.setGeometry(QtCore.QRect(20, 440, 141, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BT_sauvegarder.setFont(font)
        self.BT_sauvegarder.setObjectName("BT_sauvegarder")
        self.BT_voir_liste = QtWidgets.QPushButton(self.centralwidget)
        self.BT_voir_liste.setGeometry(QtCore.QRect(20, 360, 101, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BT_voir_liste.setFont(font)
        self.BT_voir_liste.setObjectName("BT_voir_liste")
        self.MS_erreur_nom = QtWidgets.QLabel(self.centralwidget)
        self.MS_erreur_nom.setGeometry(QtCore.QRect(20, 90, 271, 41))
        self.MS_erreur_nom.setText("")
        self.MS_erreur_nom.setObjectName("MS_erreur_nom")
        self.MS_erreur_age = QtWidgets.QLabel(self.centralwidget)
        self.MS_erreur_age.setGeometry(QtCore.QRect(10, 200, 271, 41))
        self.MS_erreur_age.setText("")
        self.MS_erreur_age.setObjectName("MS_erreur_age")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.l_nom.setText(_translate("MainWindow", "Nom de l`etudiant :"))
        self.BT_ajouter.setText(_translate("MainWindow", "Ajouter"))
        self.l_num.setText(_translate("MainWindow", "Numero de l`etudiant :"))
        self.TB_answer.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CB_choix.setItemText(0, _translate("MainWindow", "Programmation"))
        self.CB_choix.setItemText(1, _translate("MainWindow", "Reseaux"))
        self.BT_supprimer.setText(_translate("MainWindow", "Supprimer"))
        self.BT_modifier.setText(_translate("MainWindow", "Modifier"))
        self.BT_sauvegarder.setText(_translate("MainWindow", "Sauvegarder"))
        self.BT_voir_liste.setText(_translate("MainWindow", "voir liste"))
