# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'secondWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json
import requests
from stats_page import Ui_Stats_Page

data = json.load(open('passQT.json', 'r'))
info = json.load(open('studentsQT.json', 'r'))
moves={"Americana":0,"Kimura":0,"Armbar":0,"Triangle":0}

class Ui_SecondWindow(object):
    def __init__(self, user):
        self.user= user

    def openStats(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_Stats_Page(self.user)
        self.ui2.setupUi(self.window)
        self.window.show()


    def setupUi(self, SecondWindow):
        SecondWindow.setObjectName("SecondWindow")
        SecondWindow.resize(581, 733)
        self.centralwidget = QtWidgets.QWidget(SecondWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.banner = QtWidgets.QLabel(self.centralwidget)
        self.banner.setGeometry(QtCore.QRect(0, 0, 581, 131))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("banner.jpg"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.stats = QtWidgets.QPushButton(self.centralwidget)
        self.stats.setGeometry(QtCore.QRect(170, 220, 231, 71))
        self.stats.setObjectName("stats")
        self.workout = QtWidgets.QPushButton(self.centralwidget)
        self.workout.setGeometry(QtCore.QRect(170, 320, 231, 71))
        self.workout.setObjectName("workout")
        self.badges = QtWidgets.QPushButton(self.centralwidget)
        self.badges.setGeometry(QtCore.QRect(170, 420, 231, 71))
        self.badges.setObjectName("badges")
        SecondWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SecondWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        SecondWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SecondWindow)
        self.statusbar.setObjectName("statusbar")
        SecondWindow.setStatusBar(self.statusbar)

        self.stats.clicked.connect(self.openStats)

        self.retranslateUi(SecondWindow)
        QtCore.QMetaObject.connectSlotsByName(SecondWindow)



    def retranslateUi(self, SecondWindow):
        _translate = QtCore.QCoreApplication.translate
        SecondWindow.setWindowTitle(_translate("SecondWindow", "MainWindow"))
        self.stats.setText(_translate("SecondWindow", "Stats"))
        self.workout.setText(_translate("SecondWindow", "Today\'s Workout"))
        self.badges.setText(_translate("SecondWindow", "Badges"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SecondWindow = QtWidgets.QMainWindow()
    ui = Ui_SecondWindow()
    ui.setupUi(SecondWindow)
    SecondWindow.show()
    sys.exit(app.exec_())
