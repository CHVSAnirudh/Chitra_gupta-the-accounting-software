# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ok_popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_OK(object):
    def setupUi(self, Dialog,msg):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 350)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setGeometry(QRect(-1, -1, 421, 311))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit = QTextEdit(self.verticalLayoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        #self.pushButton = QPushButton("OK",self.verticalLayoutWidget)
        #self.pushButton.setObjectName("pushButton")
        #self.verticalLayout.addWidget(self.pushButton)
        #self.pushButton.clicked.connect(self.collapse(Dialog))
        self.retranslateUi(Dialog,msg)
        QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog,msg):
        _translate = QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Confirmation"))
        self.textEdit.setPlainText(_translate("%s",msg))
    #def collapse(self,Dialog):
     #   Dialog.reject()

