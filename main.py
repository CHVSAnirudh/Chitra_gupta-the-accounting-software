import sys
import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
# GUI FILE
from app_modules import *
from login import *
from intro import *
import os
import mysql.connector

class MainWindow(QMainWindow):
    ltype = ''
    uname = ''
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        ## PRINT ==> SYSTEM
        Form = QtWidgets.QDialog()
        ui = Ui_login()
        ui.setupUi(Form)
        Form.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)
        Form.exec() 
        print('System: ' + platform.system())
        print('Version: ' +platform.release())
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database = "chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall()
        ltype = myresult[0][1]

        ########################################################################
        ## START - WINDOW ATTRIBUTES
        ########################################################################

        ## REMOVE ==> STANDARD TITLE BAR
        UIFunctions.removeTitleBar(True)
        ## ==> END ##

        ## SET ==> WINDOW TITLE
        self.setWindowTitle('Main Window - Python Base')
        UIFunctions.labelTitle(self, 'CHITRA GUPTA - The accounting software')
        UIFunctions.labelDescription(self, '')
        ## ==> END ##

        ## WINDOW SIZE ==> DEFAULT SIZE
        startSize = QSize(1150, 760)
        self.resize(startSize)
        self.setMinimumSize(startSize)
        # UIFunctions.enableMaximumSize(self, 500, 720)
        ## ==> END ##

        ## ==> CREATE MENUS
        ########################################################################

        ## ==> TOGGLE MENU SIZE
        self.ui.btn_toggle_menu.clicked.connect(lambda: UIFunctions.toggleMenu(self, 220, True))
        ## ==> END ##

        ## ==> ADD CUSTOM MENUS
        self.ui.stackedWidget.setMinimumWidth(20)
        UIFunctions.addNewMenu(self, "HOME", "btn_home", "url(:/16x16/icons/16x16/cil-home.png)", True)
        UIFunctions.addNewMenu(self, "DONATIONS", "btn_widgets", "url(:/16x16/icons/16x16/cil-window-restore.png)", True)
        UIFunctions.addNewMenu(self, "EXPENDITURE", "expenditure", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        if(ltype=='master'):
            UIFunctions.addNewMenu(self, "New User", "new_user", "url(:/16x16/icons/16x16/cil-user-follow.png)", True)
            UIFunctions.addNewMenu(self, "Expenditure Confirmation", "expenditure_confirm", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
            UIFunctions.addNewMenu(self, "Donation Confirmation", "Donation_confirm", "url(:/16x16/icons/16x16/cil-equalizer.png)", True)
        ## ==> END ##

        # START MENU => SELECTION
        UIFunctions.selectStandardMenu(self, "btn_home")
        ## ==> END ##

        ## ==> START PAGE
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
        ## ==> END ##

        ## USER ICON ==> SHOW HIDE
        str = myresult[0][3][0] + myresult[0][4][0] 
        UIFunctions.userIcon(self, str.upper(), "", True)
        ## ==> END ##

        ## ==> MOVE WINDOW / MAXIMIZE / RESTORE
        ########################################################################
        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if UIFunctions.returStatus() == 1:
                UIFunctions.maximize_restore(self)

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        # WIDGET TO MOVE
        self.ui.frame_label_top_btns.mouseMoveEvent = moveWindow
        ## ==> END ##

        ## ==> LOAD DEFINITIONS
        ########################################################################
        UIFunctions.uiDefinitions(self)
        ## ==> END ##

        ########################################################################
        ## END - WINDOW ATTRIBUTES
        ############################## ---/--/--- ##############################




        ########################################################################
        #                                                                      #
        ## START -------------- WIDGETS FUNCTIONS/PARAMETERS ---------------- ##
        #                                                                      #
        ## ==> USER CODES BELLOW                                              ##
        ########################################################################



        ## ==> QTableWidget RARAMETERS
        ########################################################################
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        ## ==> END ##



        ########################################################################
        #                                                                      #
        ## END --------------- WIDGETS FUNCTIONS/PARAMETERS ----------------- ##
        #                                                                      #
        ############################## ---/--/--- ##############################


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        
        ## ==> END ##

    ########################################################################
    ## MENUS ==> DYNAMIC MENUS FUNCTIONS
    ########################################################################
    def Button(self):
        # GET BT CLICKED
        btnWidget = self.sender()

        # PAGE HOME
        if btnWidget.objectName() == "btn_home":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            UIFunctions.resetStyle(self, "btn_home")
            UIFunctions.labelPage(self, "Home")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        # PAGE WIDGETS
        if btnWidget.objectName() == "btn_widgets":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_widgets)
            UIFunctions.resetStyle(self, "btn_widgets")
            UIFunctions.labelPage(self, "DONATIONS")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        if btnWidget.objectName() == "expenditure":
            self.ui.stackedWidget.setCurrentWidget(self.ui.expenditure_opening)
            UIFunctions.resetStyle(self, "expenditure")
            UIFunctions.labelPage(self, "EXPENDITURE")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        if btnWidget.objectName() == "new_user":
            self.ui.stackedWidget.setCurrentWidget(self.ui.new_user)
            UIFunctions.resetStyle(self, "new_user")
            UIFunctions.labelPage(self, "NEW USER")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))

        if btnWidget.objectName() == "expenditure_confirm":
            self.ui.stackedWidget.setCurrentWidget(self.ui.exp_confirmation_page)
            UIFunctions.resetStyle(self, "exp_confirmation_page")
            UIFunctions.labelPage(self, "confirma")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        if btnWidget.objectName() == "Donation_confirm":
            self.ui.stackedWidget.setCurrentWidget(self.ui.donation_confirmation_page)
            UIFunctions.resetStyle(self, "donation_confirmation_page")
            UIFunctions.labelPage(self, "donation_confirmation_page")
            btnWidget.setStyleSheet(UIFunctions.selectMenu(btnWidget.styleSheet()))
        
        
        
    ## ==> END ##

    ########################################################################
    ## START ==> APP EVENTS
    ########################################################################

    ## EVENT ==> MOUSE DOUBLE CLICK
    ########################################################################
    def eventFilter(self, watched, event):
        if watched == self.le and event.type() == QtCore.QEvent.MouseButtonDblClick:
            print("pos: ", event.pos())
    ## ==> END ##

    ## EVENT ==> MOUSE CLICK
    ########################################################################
    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()
        if event.buttons() == Qt.LeftButton:
            print('Mouse click: LEFT CLICK')
        if event.buttons() == Qt.RightButton:
            print('Mouse click: RIGHT CLICK')
        if event.buttons() == Qt.MidButton:
            print('Mouse click: MIDDLE BUTTON')
    ## ==> END ##

    ## EVENT ==> KEY PRESSED
    ########################################################################
    def keyPressEvent(self, event):
        print('Key: ' + str(event.key()) + ' | Text Press: ' + str(event.text()))
    ## ==> END ##

    ## EVENT ==> RESIZE EVENT
    ########################################################################
    def resizeEvent(self, event):
        self.resizeFunction()
        return super(MainWindow, self).resizeEvent(event)

    def resizeFunction(self):
        print('Height: ' + str(self.height()) + ' | Width: ' + str(self.width()))
    ## ==> END ##

    ########################################################################
    ## END ==> APP EVENTS
    ############################## ---/--/--- ##############################

if __name__ == "__main__":
#sys.exit(app.exec_())
    app = QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeui.ttf')
    QtGui.QFontDatabase.addApplicationFont('fonts/segoeuib.ttf')
    window = MainWindow()
    sys.exit(app.exec_())
    
    