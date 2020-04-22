# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)

import json
import requests
data = json.load(open('passQT.json', 'r'))
info = json.load(open('studentsQT.json', 'r'))
moves={"Americana":0,"Kimura":0,"Armbar":0,"Triangle":0}

class Ui_Stats_Page(object):
    def __init__(self, user):
        self.user= user
    def setupUi(self, Stats_Page):
        Stats_Page.setObjectName("Stats_Page")
        Stats_Page.resize(581, 733)
        self.centralwidget = QtWidgets.QWidget(Stats_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.banner = QtWidgets.QLabel(self.centralwidget)
        self.banner.setGeometry(QtCore.QRect(0, 0, 581, 131))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("banner.jpg"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.Statslabel = QtWidgets.QLabel(self.centralwidget)
        self.Statslabel.setGeometry(QtCore.QRect(60, 150, 451, 300))
        self.Statslabel.setScaledContents(True)
        self.Statslabel.setWordWrap(True)
        self.Statslabel.setObjectName("Statslabel")
        self.moveEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.moveEdit.setGeometry(QtCore.QRect(290, 440, 131, 31))
        self.moveEdit.setText("")
        self.moveEdit.setObjectName("moveEdit")
        self.repEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.repEdit.setGeometry(QtCore.QRect(290, 490, 131, 31))
        self.repEdit.setText("")
        self.repEdit.setObjectName("repEdit")
        self.moveLabel = QtWidgets.QLabel(self.centralwidget)
        self.moveLabel.setGeometry(QtCore.QRect(130, 440, 131, 31))
        self.moveLabel.setObjectName("moveLabel")
        self.repLabel = QtWidgets.QLabel(self.centralwidget)
        self.repLabel.setGeometry(QtCore.QRect(130, 490, 131, 31))
        self.repLabel.setObjectName("repLabel")
        self.addStats_Button = QtWidgets.QPushButton(self.centralwidget)
        self.addStats_Button.setGeometry(QtCore.QRect(180, 550, 171, 41))
        self.addStats_Button.setObjectName("addStats_Button")
        Stats_Page.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Stats_Page)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        Stats_Page.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Stats_Page)
        self.statusbar.setObjectName("statusbar")
        Stats_Page.setStatusBar(self.statusbar)

        self.addStats_Button.clicked.connect(self.add_move)

        self.retranslateUi(Stats_Page)
        QtCore.QMetaObject.connectSlotsByName(Stats_Page)

    def print_stats(self):
        stats =""
        for move in info[self.user].keys():
            rep = info[self.user][move]
            stats += (move + ": "+ str(rep) + "\n")
        return stats


    def add_move(self):
        move = self.moveEdit.text().capitalize()
        rep = int(self.repEdit.text())
        if move in info[self.user].keys():
            info[self.user][move]+= rep
        else:
            info[self.user][move]=rep

        json.dump(info, open('studentsQT.json', 'w'))
        final =self.print_stats()
        self.Statslabel.setText(final)

        
              


    def retranslateUi(self, Stats_Page):

        _translate = QtCore.QCoreApplication.translate
        final =self.print_stats()
        Stats_Page.setWindowTitle(_translate("Stats_Page", "My Stats"))
        self.Statslabel.setText(_translate("Stats_Page", final))
        self.moveEdit.setPlaceholderText(_translate("Stats_Page", "Enter Move"))
        self.repEdit.setPlaceholderText(_translate("Stats_Page", "Enter Reps"))
        self.moveLabel.setText(_translate("Stats_Page", "Move:"))
        self.repLabel.setText(_translate("Stats_Page", "Reps:"))
        self.addStats_Button.setText(_translate("Stats_Page", "Add to Stats"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Stats_Page = QtWidgets.QMainWindow()
    ui = Ui_Stats_Page()
    ui.setupUi(Stats_Page)
    Stats_Page.show()
    sys.exit(app.exec_())
