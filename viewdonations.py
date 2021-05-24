
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import *
 
class Ui_Forma(object):
    def setupUi(self, Form,result):
        Form.setObjectName("Form")
        Form.resize(482, 451)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QTableWidget(Form)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setRowCount(8)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.verticalLayout.addWidget(self.tableWidget)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(result):
         #print(row_number)
         self.tableWidget.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        run()
       
        
        #we have connected clicked signal of button with the selec_data method
        self.verticalLayout.addWidget(self.tableWidget)
 
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        
        
    #this is the method for selecting data
    
    def retranslateUi(self, Form):
        _translate = QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
 