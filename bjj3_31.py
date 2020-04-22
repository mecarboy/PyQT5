# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bjj3-31.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
import json
import requests
from secondWindow import Ui_SecondWindow
from loginpage import Ui_LoginPage

data = json.load(open('passQT.json', 'r'))
info = json.load(open('studentsQT.json', 'r'))
moves={"Americana":0,"Kimura":0,"Armbar":0,"Triangle":0}

class Ui_MainWindow(object):
    def openWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.user =user
        self.ui2 = Ui_SecondWindow(self.user)
        self.ui2.setupUi(self.window)
        self.window.show()

    def create_login(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_LoginPage()
        self.ui2.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(581, 733)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.banner = QtWidgets.QLabel(self.centralwidget)
        self.banner.setGeometry(QtCore.QRect(0, 0, 581, 131))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("banner.jpg"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.username = QtWidgets.QLabel(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(130, 180, 291, 51))
        self.username.setObjectName("username")
        self.password = QtWidgets.QLabel(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(130, 240, 291, 51))
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setGeometry(QtCore.QRect(50, 330, 141, 41))
        self.login.setObjectName("login")
        self.new_user = QtWidgets.QPushButton(self.centralwidget)
        self.new_user.setGeometry(QtCore.QRect(390, 330, 141, 41))
        self.new_user.setObjectName("new_user")
        self.cancel = QtWidgets.QPushButton(self.centralwidget)
        self.cancel.setGeometry(QtCore.QRect(220, 330, 141, 41))
        self.cancel.setObjectName("cancel")
        self.username_entered = QtWidgets.QLineEdit(self.centralwidget)
        self.username_entered.setGeometry(QtCore.QRect(200, 190, 211, 31))
        self.username_entered.setText("")
        self.username_entered.setObjectName("username_entered")
        self.password_entered = QtWidgets.QLineEdit(self.centralwidget)
        self.password_entered.setGeometry(QtCore.QRect(200, 250, 211, 31))
        self.password_entered.setText("")
        self.password_entered.setObjectName("password_entered")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.login.clicked.connect(self.check_password)
        self.cancel.clicked.connect(self.cancel_login)
        self.new_user.clicked.connect(self.create_login)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def check_password(self):
        msg = QMessageBox()
        global user
        user = self.username_entered.text()
        password = self.password_entered.text()
        if user in data.keys() and data[user]==password:
            MainWindow.hide()
            self.openWindow()

             
        else:
            msg.setText("Incorrect Password")
            msg.exec_()

    def cancel_login(self):
        app.quit()

    def login_page(self):
        self.create_login()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username.setText(_translate("MainWindow", "Username"))
        self.password.setText(_translate("MainWindow", "Password"))
        self.login.setText(_translate("MainWindow", "Login"))
        self.new_user.setText(_translate("MainWindow", "Create New User"))
        self.cancel.setText(_translate("MainWindow", "Cancel"))
        self.username_entered.setPlaceholderText(_translate("MainWindow", "Enter Username"))
        self.password_entered.setPlaceholderText(_translate("MainWindow", "Enter Password"))

   


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

