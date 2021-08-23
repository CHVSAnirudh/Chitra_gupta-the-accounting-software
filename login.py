# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2.QtWidgets import QWidget
import mysql.connector
import sys
import os
from ok_popup import *
import platform
import files_rc
from app_modules import *
from main import *
class Ui_login(object):
    Form = 0
    def login_func(self):
        username = self.lineEdit_3.text()
        password = self.lineEdit_4.text()
        if self.Masterlogin.isChecked():
            login_type = 'master'
        else:
            login_type = 'normal'

        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database = "chitra_gupta"
                )

        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM chitra_gupta.login where username = '{0}'".format(username))
        myresult = mycursor.fetchall()
        if(len(myresult)==0):
            msg = "Account not found"
            dialog = QDialog()
            ui = Ui_OK()
            ui.setupUi(dialog,msg)
            dialog.exec()
        elif myresult[0][2]!=password or myresult[0][3]!=login_type :
            msg = "Invalid credentials or login_type"
            dialog = QDialog()
            ui = Ui_OK()
            ui.setupUi(dialog,msg)
            dialog.exec()
        else:
            mycursor = mydb.cursor()
            sql = "INSERT INTO log (id,type,fname,lname) VALUES (%s, %s,%s,%s)"
            val = (int(myresult[0][0]),myresult[0][3],myresult[0][4],myresult[0][5])
            mycursor.execute(sql, val)
            mydb.commit()
            self.Form.close()
            #QtWidgets.QApplication.quit()
            print(myresult)
    
    def setupUi(self, login):
        self.Form = login
        login.setObjectName("login")
        login.resize(311, 455)
        self.widget = QtWidgets.QWidget(login)
        self.widget.setGeometry(QtCore.QRect(10, 10, 290, 431))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.widget.setFont(font)
        self.widget.setStyleSheet("background-color:rgba(16,30,41,240);\n"
"border-radius:10px;")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 340, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"background-color:rgba(2,65,118,255);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login_func)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(60, 30, 180, 150))
        font = QtGui.QFont()
        font.setPointSize(80)
        font.setBold(False)
        font.setWeight(50)
        #self.label.setFont(font)
        #self.label.setStyleSheet("background-color:rgba(0,0,0,0,);\n"
#"color:rgba(0,125,236,255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/16x16/icons/16x16/chitragupta.jpeg"))
        self.label.setScaledContents(True)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 210, 250, 30))
        self.lineEdit_3.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-botton:7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 260, 250, 30))
        self.lineEdit_4.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(46,82,101,255);\n"
"color:rgb(255,255,255);\n"
"padding-botton:7px;")
        self.lineEdit_4.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.Masterlogin = QtWidgets.QRadioButton(self.widget)
        self.Masterlogin.setGeometry(QtCore.QRect(20, 310, 112, 23))
        self.Masterlogin.setStyleSheet("QRadioButton {\n"
"    background-color:       rgba(0,0,0,0);\n"
"    color:rgba(255,255,255,200)\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgba(0,0,0,0);\n"
"    border:                 2px solid white;\n"
"}")
        self.Masterlogin.setObjectName("Masterlogin")
        self.Masterlogin_2 = QtWidgets.QRadioButton(self.widget)
        self.Masterlogin_2.setGeometry(QtCore.QRect(160, 310, 112, 23))
        self.Masterlogin_2.setChecked(True)
        self.Masterlogin_2.setStyleSheet("QRadioButton {\n"
"    background-color:       rgba(0,0,0,0);\n"
"   color:rgba(255,255,255,200)\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width:                  10px;\n"
"    height:                 10px;\n"
"    border-radius:          7px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color:       red;\n"
"    border:                 2px solid white;\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color:       rgba(0,0,0,0);\n"
"    border:                 2px solid white;\n"
"}")
        self.Masterlogin_2.setObjectName("Masterlogin_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 390, 221, 25))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"background-color:rgba(0,0,0,0);\n"
"color:rgba(255,255,255,200);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(2,65,118,100);\n"
"background-position:calc(100%-10px)center;\n"
"}\n"
"QPushButton#pushButton:hover{\n"
"background-color:rgba(2,65,118,200);\n"
"\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Login"))
        self.pushButton.setText(_translate("login", "Log In"))
        #self.label.setText(_translate("login", "👤"))
        self.lineEdit_3.setPlaceholderText(_translate("login", "User Name"))
        self.lineEdit_4.setPlaceholderText(_translate("login", "Password"))
        self.Masterlogin.setText(_translate("login", "Master login"))
        self.Masterlogin_2.setText(_translate("login", "Normal login"))
        self.pushButton_2.setText(_translate("login", "Forgot User Name or Password"))

#if __name__ == "__main__":
 #   app = QtWidgets.QApplication([])
  #  Form = QtWidgets.QWidget()
   # ui = Ui_login()
    #ui.setupUi(Form)
    #Form.show()
    #sys.exit(app.exec_())

