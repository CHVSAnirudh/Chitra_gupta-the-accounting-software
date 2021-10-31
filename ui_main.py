from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient, QStandardItem)
from PySide2.QtCharts import QtCharts
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import *
import files_rc
import mysql.connector
from datetime import datetime
from datetime import date
from datetime import timedelta
from viewdonations import Ui_Forma
import sys
from add_donor_confirmation import *
from ok_popup import *
from reportlab.pdfgen.canvas import Canvas
from datetime import datetime, timedelta
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import BaseDocTemplate, Frame, Paragraph, PageBreak, \
    PageTemplate, Spacer, FrameBreak, NextPageTemplate, Image
from reportlab.lib.pagesizes import letter,A4
from reportlab.lib.units import inch, cm
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER,TA_LEFT,TA_RIGHT
import webbrowser

class Ui_MainWindow(object):
    def get_donar_donations(self):
        self.stackedWidget.setCurrentIndex(22)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        phn = self.lineEdit.text()
        mycursor.execute("select * from all_donations a where a.id_donor=(select donor_id from all_donors where phone={})".format(phn))
        myresult = mycursor.fetchall()
        c=0
        if len(myresult)!=0:
            c = len(myresult[0])
        r = len(myresult)
        self.tableWidget13 = QTableWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget13.setSizePolicy(sizePolicy)
        self.tableWidget13.setMinimumSize(QSize(0, 0))
        self.tableWidget13.setRowCount(r)
        self.tableWidget13.setColumnCount(c+1)
        self.tableWidget13.setObjectName("tableWidget13")
        self.tableWidget13.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
        self.tableWidget13.setRowCount(0)
        index = 0
        columns = ["id_donation", "donation_in_name","phone","email"," date_of_donation","donation_date","Ocassion","remarks"]
        self.tableWidget.setHorizontalHeaderLabels(columns)
        #rb = [QRadioButton() for x in range(r)]
        #for i in range(r):
        #    self.tableWidget.setCellWidget(index, i+1,rb[i] )
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         self.tableWidget13.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           #item_checked = QTableWidgetItem()
           #item_checked.setCheckState(Qt.Unchecked)
           #item_checked.setFlags(Qt.ItemIsUserCheckable |Qt.ItemIsEnabled)
                    #item_checked.setCheckable(True)
           #self.tableWidget13.setItem(row_number,0, item_checked) 
           self.tableWidget13.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        if self.verticalLayout_221212.count() !=0: 
            self.verticalLayout_221212.itemAt(0).widget().deleteLater()
        self.verticalLayout_221212.addWidget(self.tableWidget13)
    def get_exp_pdf(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        fdate = self.dateEdit102.date()
        fdate = fdate.toPython()
        fdate = fdate.strftime('%Y-%m-%d')
        tdate = self.dateEdit_102.date()
        tdate = tdate.toPython()
        tdate = tdate.strftime('%Y-%m-%d')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT voucherdate,voucherid,type,towards,amount FROM  pettycashbook where voucherdate between '{0}' and '{1}'".format(fdate,tdate))
        data = mycursor.fetchall()
        mycursor.execute("select code_name from type_expenditure")
        schemes = mycursor.fetchall()
        schemes = [x[0] for x in schemes]
        print(schemes)
        #print(data)
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Folder')
        print(folderpath)
        fileName = str(folderpath) + '/' + str(fdate) + ' to ' + str(tdate) + '_expenditure.pdf'
        tid = str(fdate) + ' to ' + str(tdate) + ' Full Expenditure report\n'
        canvas = Canvas(fileName, pagesize=landscape(letter))
        doc = BaseDocTemplate(fileName)
        contents =[]
        width,height = A4

        left_header_frame = Frame(
            0.2*inch, 
            height-1.2*inch, 
            2*inch, 
            1*inch
            )

        right_header_frame = Frame(
            2.2*inch, 
            height-1.2*inch, 
            width-2.5*inch, 
            1*inch,id='normal'
            )

        frame_table= Frame(
            0.2*inch, 
            0.7*inch, 
            (width-0.6*inch)+0.17*inch, 
            height-2*inch,
            leftPadding = 0, 
            topPadding=0, 
            showBoundary = 1,
            id='col'
            )

        laterpages = PageTemplate(id='laterpages',frames=[left_header_frame, right_header_frame,frame_table],)

        styleSheet = getSampleStyleSheet()
        style_title = styleSheet['Heading1']
        style_title.fontSize = 20 
        style_title.fontName = 'Helvetica-Bold'
        style_title.alignment=TA_CENTER

        style_data = styleSheet['Normal']
        style_data.fontSize = 16 
        style_data.fontName = 'Helvetica'
        style_data.alignment=TA_CENTER

        style_date = styleSheet['Normal']
        style_date.fontSize = 14
        style_date.fontName = 'Helvetica'
        style_date.alignment=TA_CENTER

        canvas.setTitle(tid)


        title_background = colors.fidblue
        data_actividades = [('Date','Voucher Number','Expeniture','Particulars','amount')]
        i = 0
        table_group= []
        count = 0
        size = len(data)
        for i in range(len(data)):
            data_actividades.append(data[i])
            i+=1
            table_actividades = Table(data_actividades, rowHeights=30, repeatRows=1)
            tblStyle = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), title_background),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            rowNumb = len(data_actividades)
            for row in range(1, rowNumb):
                if row % 2 == 0:
                    table_background = colors.lightblue
                else:
                    table_background = colors.aliceblue

                tblStyle.add('BACKGROUND', (0, row), (-1, row), table_background)

            table_actividades.setStyle(tblStyle)

            if ((count >= 20) or (i== size) ):
                count = 0
                table_group.append(table_actividades)
                data_actividades = [('Date','Voucher Number','Expeniture','Particulars','amount')]
            width = 150
            height = 150
            count += 1
            if i > size:

                break

        contents.append(NextPageTemplate('laterpages'))

        for table in table_group:
            contents.append(FrameBreak())
            contents.append(Paragraph(tid, style_title))
            contents.append(FrameBreak()) 
            contents.append(table)
            contents.append(FrameBreak())

        for z in range(1,len(schemes)+1):
            mycursor.execute("SELECT voucherdate,voucherid,type,towards,amount FROM pettycashbook where voucherdate between '{0}' and '{1}' and type = '{2}'".format(fdate,tdate,str(schemes[z-1])))
            print(str(schemes[z-1]))
            data = mycursor.fetchall()
            print(data)
            count = 0
            table_group.clear()
            i = 0
            size = len(data)
            for i in range(len(data)):
                data_actividades.append(data[i])
                i+=1
                table_actividades = Table(data_actividades, rowHeights=30, repeatRows=1)
                tblStyle = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), title_background),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ])

                rowNumb = len(data_actividades)
                for row in range(1, rowNumb):
                    if row % 2 == 0:
                        table_background = colors.lightblue
                    else:
                        table_background = colors.aliceblue

                    tblStyle.add('BACKGROUND', (0, row), (-1, row), table_background)

                table_actividades.setStyle(tblStyle)

                if ((count >= 20) or (i== size) ):
                    count = 0
                    table_group.append(table_actividades)
                    data_actividades = [('Date','Voucher Number','Expeniture','Particulars','amount')]
                width = 150
                height = 150
                count += 1
                if i > size:

                    break
            
            tid = str(fdate) + ' to ' + str(tdate) + ' {}\n'.format(schemes[z-1])

            contents.append(NextPageTemplate('laterpages'))
            for table in table_group:
                contents.append(FrameBreak())
                contents.append(Paragraph(tid, style_title))
                contents.append(FrameBreak()) 
                contents.append(table)
                contents.append(FrameBreak())


        doc.addPageTemplates([laterpages,])
        doc.build(contents)
    def mailing_list(self):
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Folder')
        print(folderpath)
        fileName = str(folderpath) + '/' + 'mailing list.pdf'
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select f_name,l_name,address,phone,email from all_donors a natural join all_donations b where a.donor_id=b.id_donor and curdate() > remind_date and reminded =0 ")
        l = mycursor.fetchall()
        # importing modules
        from reportlab.pdfgen import canvas
        from reportlab.pdfbase.ttfonts import TTFont
        from reportlab.pdfbase import pdfmetrics
        from reportlab.lib import colors
        
        # initializing variables with values
        documentTitle = 'mailing list'
        title = 'Karunya Sindhu Orphanage'
        subTitle = 'Mailing list'
        textLines = [
        ]
        
        # creating a pdf object
        pdf = canvas.Canvas(fileName)
        
        # setting the title of the document
        pdf.setTitle(documentTitle)
        
        # registering a external font in python

        
        # creating the title by setting it's font
        # and putting it on the canvas
        #pdf.setFont('abc', 36)
        pdf.drawCentredString(300, 770, title)
        
        # creating the subtitle by setting it's font,
        # colour and putting it on the canvas
        pdf.setFillColorRGB(0, 0, 255)
        pdf.setFont("Courier-Bold", 24)
        pdf.drawCentredString(290, 720, subTitle)
        
        # drawing a line
        pdf.line(30, 710, 550, 710)
        
        # creating a multiline text using
        # textline and for loop
        text = pdf.beginText(40, 680)
        text.setFont("Courier", 18)
        text.setFillColor(colors.black)
        for x in l:
            textLines.append("To,")
            for z in x:
                textLines.append(str(z))
            textLines.append("\n\n")
            for line in textLines:
                text.textLine(line)
            textLines.clear()
            pdf.line(30, 710, 550, 710)

        pdf.drawText(text)
        
        # drawing a image at the
        # specified (x.y) position
        #pdf.drawInlineImage(image, 130, 400)
        
        # saving the pdf
        pdf.save()
        webbrowser.open_new_tab(fileName)

    def add_banks_in_donation(self):
        c = self.comboBox_2.currentIndex()
        font7 = QFont()
        font7.setFamily("Segoe UI")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        print("func activated")
        if c!=0:
            if self.gridLayout_3.count()>=25:
                pass
            else:
                self.comboBox_44 = QComboBox(self.new_donation)
                self.comboBox_44.setMaximumSize(QSize(16777215, 40))
                self.comboBox_44.setObjectName("comboBox_192")
                self.comboBox_44.setFont(font7)
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="anirudh123",
                database="chitra_gupta"
                )
                mycursor = mydb.cursor()
                mycursor.execute("select * from banks")
                myresult = mycursor.fetchall()
                i=0
                for x in myresult:
                    self.comboBox_44.addItem("")
                    self.comboBox_44.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
                    i+=1
                #self.gridLayout_194.addWidget(self.comboBox_192, 3, 1, 1, 2)
                self.gridLayout_3.addWidget(self.comboBox_44, 5, 5, 1, 1)
        else:
            print("cash")
            if self.gridLayout_3.count()>=25:
                item = self.gridLayout_3.takeAt(24)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
    def generate_donation_pdf(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        fromd = self.dateEdit9.date()
        fromd = fromd.toPython()
        ffromd = fromd.strftime('%Y-%m-%d')
        tod = self.dateEdit_92.date()
        tod = tod.toPython()
        ftod = tod.strftime('%Y-%m-%d')
        mycursor = mydb.cursor()
        mycursor.execute("SELECT master_registration_number,date_of_donation,donation_in_name,amount,schemes.name FROM all_donations LEFT JOIN schemes ON all_donations.category = schemes.idschemes where date_of_donation between '{0}' and '{1}' order by master_registration_number".format(ffromd,ftod))
        data = mycursor.fetchall()
        mycursor.execute("select * from schemes")
        schemes = mycursor.fetchall()
        schemes = [x[1] for x in schemes]
        print(schemes)
        print(data)
        folderpath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Folder')
        print(folderpath)
        fileName = str(folderpath) + '/' + str(fromd) + ' to ' + str(tod) + '_donation.pdf'
        tid = str(fromd) + ' to ' + str(tod) + ' Full donation report\n'
        canvas = Canvas(fileName, pagesize=landscape(letter))
        doc = BaseDocTemplate(fileName)
        contents =[]
        width,height = A4

        left_header_frame = Frame(
            0.2*inch, 
            height-1.2*inch, 
            2*inch, 
            1*inch
            )

        right_header_frame = Frame(
            2.2*inch, 
            height-1.2*inch, 
            width-2.5*inch, 
            1*inch,id='normal'
            )

        frame_table= Frame(
            0.2*inch, 
            0.7*inch, 
            (width-0.6*inch)+0.17*inch, 
            height-2*inch,
            leftPadding = 0, 
            topPadding=0, 
            showBoundary = 1,
            id='col'
            )

        laterpages = PageTemplate(id='laterpages',frames=[left_header_frame, right_header_frame,frame_table],)

        styleSheet = getSampleStyleSheet()
        style_title = styleSheet['Heading1']
        style_title.fontSize = 20 
        style_title.fontName = 'Helvetica-Bold'
        style_title.alignment=TA_CENTER

        style_data = styleSheet['Normal']
        style_data.fontSize = 16 
        style_data.fontName = 'Helvetica'
        style_data.alignment=TA_CENTER

        style_date = styleSheet['Normal']
        style_date.fontSize = 14
        style_date.fontName = 'Helvetica'
        style_date.alignment=TA_CENTER

        canvas.setTitle(tid)


        title_background = colors.fidblue

        data_actividades = [('Master registration number','date','name','amount','category')]

        i = 0
        table_group= []
        count = 0
        size = len(data)
        for i in range(len(data)):
            data_actividades.append(data[i])
            i+=1
            table_actividades = Table(data_actividades, rowHeights=30, repeatRows=1)
            tblStyle = TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), title_background),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ])

            rowNumb = len(data_actividades)
            for row in range(1, rowNumb):
                if row % 2 == 0:
                    table_background = colors.lightblue
                else:
                    table_background = colors.aliceblue

                tblStyle.add('BACKGROUND', (0, row), (-1, row), table_background)

            table_actividades.setStyle(tblStyle)

            if ((count >= 20) or (i== size) ):
                count = 0
                table_group.append(table_actividades)
                data_actividades = [('Master registration number','date','name','amount','category')]
            width = 150
            height = 150
            count += 1
            if i > size:

                break

        contents.append(NextPageTemplate('laterpages'))

        for table in table_group:
            contents.append(FrameBreak())
            contents.append(Paragraph(tid, style_title))
            contents.append(FrameBreak()) 
            contents.append(table)
            contents.append(FrameBreak())
        
        for z in range(1,len(schemes)+1):
            mycursor.execute("SELECT master_registration_number,date_of_donation,donation_in_name,amount from all_donations where date_of_donation between '{0}' and '{1}' and category = {2} order by master_registration_number ".format(ffromd,ftod,z))
            data = mycursor.fetchall()
            count = 0
            table_group.clear()
            i = 0
            size = len(data)
            for i in range(len(data)):
                data_actividades.append(data[i])
                i+=1
                table_actividades = Table(data_actividades, rowHeights=30, repeatRows=1)
                tblStyle = TableStyle([
                    ('BACKGROUND', (0, 0), (-1, 0), title_background),
                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                    ('ALIGN', (1, 0), (1, -1), 'CENTER'),
                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                ])

                rowNumb = len(data_actividades)
                for row in range(1, rowNumb):
                    if row % 2 == 0:
                        table_background = colors.lightblue
                    else:
                        table_background = colors.aliceblue

                    tblStyle.add('BACKGROUND', (0, row), (-1, row), table_background)

                table_actividades.setStyle(tblStyle)

                if ((count >= 20) or (i== size) ):
                    count = 0
                    table_group.append(table_actividades)
                    data_actividades = [('Master registration number','date','name','amount','category')]
                width = 150
                height = 150
                count += 1
                if i > size:

                    break
            print()
            tid = str(fromd) + ' to ' + str(tod) + ' {}\n'.format(schemes[z-1])

            contents.append(NextPageTemplate('laterpages'))
            for table in table_group:
                contents.append(FrameBreak())
                contents.append(Paragraph(tid, style_title))
                contents.append(FrameBreak()) 
                contents.append(table)
                contents.append(FrameBreak())


        doc.addPageTemplates([laterpages,])
        doc.build(contents)

    def add_manual_transaction(self):
        amount = self.lineEdit_192.text()
        bank = self.comboBox_192.currentText()
        description = self.textEdit19.toPlainText()
        date = self.dateEdit19.date()
        date = date.toPython()
        date = date.strftime('%Y-%m-%d')
        withdrawal = 0
        deposit = 0
        if self.radioButton_192.isChecked():
            withdrawal =1
        elif self.radioButton_193.isChecked():
            deposit = 1
        print(amount,bank,description,date,withdrawal,deposit)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select balance from bank_statement where bank_name = '{0}'".format(bank))
        r = mycursor.fetchall()
        if len(r)!=0:
            balance = r[-1][0]
        else:
            balance = 0
        if withdrawal ==0 and deposit == 0:
            msg = "Please select the transaction type."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        elif not amount.isnumeric() or len(description)==0 or len(amount)==0:
            msg = "Enter all the details properly"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        if withdrawal == 1:
            sql = "INSERT INTO bank_statement (bank_name,date,description,withdrawal,balance) VALUES (%s,%s,%s,%s,%s)"
            val = (bank,date,description,amount,int(balance)-int(amount))
            mycursor.execute(sql, val)
            mydb.commit()
            msg = "Database updated successfully. The amount has been withdrawn."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec() 
            self.stackedWidget.setCurrentIndex(15)
        elif deposit==1:
            sql = "INSERT INTO bank_statement (bank_name,date,description,deposits,balance) VALUES (%s,%s,%s,%s,%s)"
            val = (bank,date,description,amount,int(balance)+int(amount))
            mycursor.execute(sql, val)
            mydb.commit()
            msg = "Database updated successfully. The amount has been deposited."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec() 
            self.stackedWidget.setCurrentIndex(15)

    def manual_trasaction_page(self):
        self.stackedWidget.setCurrentIndex(20)
    def add_exp_cat(self):
        a = self.lineEdit_182.text()
        b = self.lineEdit_183.text()
        c = b+" " + a
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO type_expenditure (code,code_name) VALUES (%s,%s)"
        val = (b,c)
        mycursor.execute(sql, val)
        mydb.commit()
        msg = "Database successfully updated."
        self.dialog = QDialog()
        self.ui = Ui_OK()
        self.ui.setupUi(self.dialog,msg)
        self.dialog.exec()
        self.stackedWidget.setCurrentIndex(0)
    def add_exp_cat_page(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall()
        ltype = myresult[0][1]
        if ltype == "master":
            self.stackedWidget.setCurrentIndex(19)
        else:
            msg = "You dont have permission to add expenditure category"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
    def addYears(self,date, years):
        result = date + timedelta(366 * years)
        if years > 0:
            while result.year - date.year > years or date.month < result.month or date.day < result.day:
                result += timedelta(-1)
        elif years < 0:
            while result.year - date.year < years or date.month > result.month or date.day > result.day:
                result += timedelta(1)
        #print "input: %s output: %s" % (date, result)
        return result
    def donation_edit(self):
        a = self.tableWidget12.currentRow()
        print(a)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from all_donations where checked = 0 ")
        myresult = mycursor.fetchall()
        info = myresult[a]
        #donation_in_name = self.lineEdit_212.text()
        #master_registration = self.lineEdit_214.text()
        #payment_mode = str(self.comboBox_2.currentText())
        #payment_description =  self.textEdit211.toPlainText()
        #occasion = str(self.comboBox_3.currentText())
        #remarks = self.textEdit_212.toPlainText()
        #category = str(self.comboBox_4.currentText())
        #student = str(self.comboBox_5.currentText())
        #book_number = self.lineEdit_215.text()
        #phone = self.lineEdit_213.text()
        #date_of_donation = self.dateTimeEdit.dateTime()
        #date_of_donation = date_of_donation.toPython()
        #formatted_dod = date_of_donation.strftime('%Y-%m-%d %H:%M:%S')
        #donation_date = self.dateEdit2.date()
        #amount = self.lineEdit_2115.text()
        #print(donation_date)
        #donation_date = donation_date.toPython()
        #formatted_dd = donation_date.strftime('%Y-%m-%d')
        #today = donation_date
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
                )

        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from schemes")
        myresult = mycursor.fetchall()
        for x in myresult:
            self.comboBox_4.addItem(str(x[1]))
        self.lineEdit_212.setText(QCoreApplication.translate("MainWindow", info[4]))
        self.lineEdit_214.setText(QCoreApplication.translate("MainWindow", str(info[5])))
        self.lineEdit_215.setText(QCoreApplication.translate("MainWindow", str(info[6])))
        self.textEdit_212.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.textEdit211.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"></p></body></html>"))
        self.textEdit211.insertHtml(info[8])
        #self.textEdit_212.clear()
        #self.textEdit211.insertPlainText(QCoreApplication.translate("MainWindow", info[8]))
        #self.textEdit_212.insertPlainText(QCoreApplication.translate("MainWindow", info[10]))
        self.textEdit_212.insertHtml(info[10])
        self.lineEdit_2115.setText(QCoreApplication.translate("MainWindow", str(info[13])))

        #a = a.toPython()
        self.dateTimeEdit.setDate(info[2])
        self.dateEdit2.setDate(info[3])
        #self.dateEdit_53.setDate(myresult[0][9])
        self.comboBox_2.setCurrentText(info[7])
        self.comboBox_3.setCurrentText(info[9])
        self.comboBox_4.setCurrentIndex(int(info[11]) - 1)
        self.comboBox_5.setCurrentIndex(int(info[12]))

        mycursor.execute("SELECT * FROM chitra_gupta.all_donors where donor_id = {0}".format(info[1]))
        myresult = mycursor.fetchall()
        #self.lineEdit_217.setText(QCoreApplication.translate("MainWindow", myresult[0][2]))
        self.lineEdit_216.setText(QCoreApplication.translate("MainWindow", myresult[0][1]))
        self.lineEdit_213.setText(QCoreApplication.translate("MainWindow", myresult[0][4]))
        self.stackedWidget.setCurrentIndex(4)

    def donation_confirm(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall()
        mid = myresult[0][0]
        mycursor = mydb.cursor()
        mycursor.execute("select * from all_donations where checked = 0")
        result = mycursor.fetchall()
        mycursor.execute("update all_donations set checked = 1, master_id = '{0}'  where checked = 0".format(mid))
        mydb.commit()
        for x in result:
            mycursor.execute("select * from main_cashbook ORDER BY transaction_id DESC LIMIT 1")
            myresult = mycursor.fetchall()
            if len(myresult)==0:
                if x[-1] == "":    
                    sql = "INSERT INTO main_cashbook (date,name,master_registration_number,reciept_number,category,debit,balance) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    val = (x[2],x[4], x[5], x[6],x[11],int(x[13]),int(x[13]))
                    mycursor.execute(sql, val)
                    mydb.commit()
                else:
                    sql = "INSERT INTO main_cashbook (date,name,master_registration_number,reciept_number,category,debit,balance,deposited) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (x[2],x[4], x[5], x[6],x[11],int(x[13]),int(x[13]),1)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    bank = x[-1]
                    name = "Deposition of donations with master registration numbers "
                    name += str(x[5])
                    mycursor.execute("select balance from bank_statement where bank_name = '{0}'".format(bank))
                    r = mycursor.fetchall()
                    if len(r)!=0:
                        balance = r[-1][0]
                    else:
                        balance =0
                    sql = "INSERT INTO bank_statement (bank_name,date,description,deposits,balance) VALUES (%s,%s,%s,%s,%s)"
                    val = (bank,x[2],name,int(x[13]),int(balance)+int(x[13]))
                    mycursor.execute(sql, val)
                    mydb.commit()

            else:
                if x[-1] == "":
                    balance = myresult[0][8]
                    sql = "INSERT INTO main_cashbook (date,name,master_registration_number,reciept_number,category,debit,balance) VALUES (%s,%s,%s,%s,%s,%s,%s)"
                    val = (x[2],x[4], x[5], x[6],x[11],int(x[13]),int(balance)+int(x[13]))
                    mycursor.execute(sql, val)
                    mydb.commit()
                else:
                    balance = myresult[0][8]
                    sql = "INSERT INTO main_cashbook (date,name,master_registration_number,reciept_number,category,debit,balance,deposited) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
                    val = (x[2],x[4], x[5], x[6],x[11],int(x[13]),int(balance)+int(x[13]),1)
                    mycursor.execute(sql, val)
                    mydb.commit()
                    bank = x[-1]
                    name = "Deposition of donations with master registration numbers "
                    name += str(x[5])
                    mycursor.execute("select balance from bank_statement where bank_name = '{0}'".format(bank))
                    r = mycursor.fetchall()
                    if len(r)!=0:
                        balance = r[-1][0]
                    else:
                        balance =0
                    sql = "INSERT INTO bank_statement (bank_name,date,description,deposits,balance) VALUES (%s,%s,%s,%s,%s)"
                    val = (bank,x[2],name,int(x[13]),int(balance)+int(x[13]))
                    mycursor.execute(sql, val)
                    mydb.commit()
                   

        msg = "Updated successfully"
        self.dialog = QDialog()
        self.ui = Ui_OK()
        self.ui.setupUi(self.dialog,msg)
        self.dialog.exec()
        self.tableWidget12.clearContents()
        self.stackedWidget.setCurrentIndex(0)
    def add_bank_account(self):
        bank = self.lineEdit16.text()
        name = self.lineEdit_162.text()
        description = self.textEdit16.toPlainText()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        sql = "INSERT INTO banks (bank_name,bank_details,description) VALUES (%s, %s,%s)"
        val = (name, bank,description)
        mycursor.execute(sql, val)
        mydb.commit()
        msg = "Database updated successfully. Bank has been added in your accounts."
        self.dialog = QDialog()
        self.ui = Ui_OK()
        self.ui.setupUi(self.dialog,msg)
        self.dialog.exec() 
        self.stackedWidget.setCurrentIndex(15)
    def add_bank(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall()
        ltype = myresult[0][1]
        if ltype == "master":
            self.stackedWidget.setCurrentIndex(18)
        else:
            msg = "Else you dont have permission to add bank account"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec() 
    def withdraw_from_bank(self):
        date = self.dateEdit17.date()
        date = date.toPython()
        date = date.strftime('%Y-%m-%d')
        bank = self.comboBox17.currentText()
        amount = self.lineEdit17.text()
        description = self.textEdit17.toPlainText()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select balance from bank_statement where bank_name = '{0}'".format(bank))
        r = mycursor.fetchall()
        if len(r)!=0:
            balance = r[-1][0]
        else:
            balance = 0
        if int(balance)<int(amount):
            msg = "Sorry you cant withdraw since the selected bank doesnot have enough balance."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec() 
        elif len(description)==0:
            msg = "Description is to be filled."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec() 
        else:
            exptype = "Withdrawal from bank"
            mycursor.execute("select balance from petty_cashbook")
            result = mycursor.fetchall()
            if len(result)!=0:
                pbalance = result[-1][0]
            else:
                pbalance = 0
            sql = "INSERT INTO petty_cashbook (date,reciept_number,category,debit,balance) VALUES (%s, %s,%s,%s,%s)"
            val = (date,description,exptype,amount,int(pbalance)+int(amount))
            mycursor.execute(sql, val)
            sql = "INSERT INTO bank_statement (bank_name,date,description,withdrawal,balance) VALUES (%s,%s,%s,%s,%s)"
            val = (bank,date,description,amount,int(balance)-int(amount))
            mycursor.execute(sql, val)
            mydb.commit()
            msg = "Database updated successfully. The amount has been withdrawn."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec() 
            self.stackedWidget.setCurrentIndex(8)
    def pettywithdraw(self):
        self.stackedWidget.setCurrentIndex(17)
    def maindeposit(self):
        c = self.tableWidget6.columnCount()
        r = self.tableWidget6.rowCount()
        amount = 0
        mrnl = []
        temp = []
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        for i in range(r):
            print(i)
            if self.tableWidget6.item(i, 0).checkState() == Qt.Checked:
                temp.append(self.tableWidget6.itemAt(i, 0))
                print("yes")
                mrn = self.tableWidget6.item(i, 4)
                mrnl.append(int(mrn.text()))
                dep = self.tableWidget6.item(i, 7)
                amount+=int(dep.text())
                #print(mrn, dep)
                print(mrn.text(), dep.text())
                mycursor.execute("update main_cashbook set deposited = 1  where master_registration_number = {0}".format(int(mrn.text())))
        name = "Deposition of donations with master registration numbers "
        for x in mrnl:
            name+=str(x)
            name+=", "
        now = datetime.now()
        fnow = now.strftime('%Y-%m-%d %H:%M:%S')
        print(name)
        
        mycursor.execute("select * from main_cashbook ORDER BY transaction_id DESC LIMIT 1")
        myresult = mycursor.fetchall()
        balance = myresult[0][8]
        
        dep =1
        sql = "INSERT INTO main_cashbook (date,name,credit,balance,deposited) VALUES (%s,%s,%s,%s,%s)"
        val = (fnow,name,amount,int(balance)-amount,dep)
        mycursor.execute(sql, val)
        mydb.commit()
        bank = self.comboBox_666.currentText()
        print(bank)
        mycursor.execute("select balance from bank_statement where bank_name = '{0}'".format(bank))
        r = mycursor.fetchall()
        if len(r)!=0:
            balance = r[-1][0]
        else:
            balance =0
        sql = "INSERT INTO bank_statement (bank_name,date,description,deposits,balance) VALUES (%s,%s,%s,%s,%s)"
        val = (bank,fnow,name,amount,int(balance)+amount)
        mycursor.execute(sql, val)
        mydb.commit()
        msg = "Successfully deposited into bank"
        self.dialog = QDialog()
        self.ui = Ui_OK()
        self.ui.setupUi(self.dialog,msg)
        self.dialog.exec()   
        self.stackedWidget.setCurrentIndex(0)  
    
    def cashbookselection(self):
        book = self.comboBox6.currentText()
        if book == "Main Cashbook":
            #while self.horizontalLayout_611.count():
            #    item = self.horizontalLayout_611.takeAt(0)
            #    widget = item.widget()
            #    if widget is not None:
            #        widget.deleteLater()
            self.buttoncash = QRadioButton("only undeposited entries", self.cashbook)
            self.horizontalLayout_69.addWidget(self.buttoncash)
        elif book == "Petty Cashbook":
            if self.horizontalLayout_69.count()==7:
                item = self.horizontalLayout_69.takeAt(6)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
            while self.horizontalLayout_611.count():
                item = self.horizontalLayout_611.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
    def get_cashbook_details(self):
        fdate = self.dateEdit.date()
        fdate = fdate.toPython()
        fdate = fdate.strftime('%Y-%m-%d')
        tdate = self.dateEdit_62.date()
        tdate = tdate.toPython()
        tdate = tdate.strftime('%Y-%m-%d')
        book = self.comboBox6.currentText()
        
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        if book == "Main Cashbook":
            status =0
            if self.buttoncash.isChecked():
                status =1
            if status == 1:
                self.comboBox_666 = QComboBox(self.cashbook)
                self.comboBox_666.setObjectName("comboBox_666")
                mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="anirudh123",
                database="chitra_gupta"
                )
                print(mydb)
                mycursor = mydb.cursor()
                mycursor.execute("select * from banks")
                myresult = mycursor.fetchall()
                i=0
                for x in myresult:
                    self.comboBox_666.addItem("")
                    self.comboBox_666.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
                    i+=1
                if self.horizontalLayout_611.count()==2:
                    pass
                else:
                    self.horizontalLayout_611.addWidget(self.comboBox_666)
                    self.pushButton_62 = QPushButton(self.cashbook)
                    self.pushButton_62.setObjectName("pushButton_62")
                    self.pushButton_62.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
                    self.pushButton_62.clicked.connect(self.maindeposit)
                    self.horizontalLayout_611.addWidget(self.pushButton_62)
                    self.pushButton_62.setText(QCoreApplication.translate("MainWindow", "Deposit"))
                print(fdate,tdate)
                self.label_64.setText(QCoreApplication.translate("MainWindow", "Main cashbook:"))
                mycursor.execute("select * from main_cashbook where date between '{0}' and '{1}' and deposited = 0".format(tdate,fdate))
                myresult = mycursor.fetchall()
                print(myresult)
                c=0
                if len(myresult)!=0:
                    c = len(myresult[0])
                r = len(myresult)
                self.tableWidget6.setRowCount(r)
                self.tableWidget6.setColumnCount(c)
                self.tableWidget6.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
                self.tableWidget6.setRowCount(0)
                index = 0
                columns = ["Status","transaction_id", "Date","Name","Master Registration Number","Reciept Number","Category","Debit","Credit","Balance"]
                self.tableWidget6.setHorizontalHeaderLabels(columns)
            #rb = [QRadioButton() for x in range(r)]
            #for i in range(r):
        #    self.tableWidget.setCellWidget(index, i+1,rb[i] )
                for row_number, row_data in enumerate(myresult):
            #print(row_number)
                    self.tableWidget6.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                    #print(column_number)
                        item_checked = QTableWidgetItem()
                        item_checked.setCheckState(Qt.Unchecked)
                        item_checked.setFlags(Qt.ItemIsUserCheckable |Qt.ItemIsEnabled)
                    #item_checked.setCheckable(True)
                        self.tableWidget6.setItem(row_number,0, item_checked)
                        self.tableWidget6.setItem(row_number, column_number+1, QTableWidgetItem(str(data)))
            elif status==0:
                print(fdate,tdate)
                self.label_64.setText(QCoreApplication.translate("MainWindow", "Main cashbook:"))
                mycursor.execute("select * from main_cashbook where date between '{0}' and '{1}'".format(tdate,fdate))
                myresult = mycursor.fetchall()
                print(myresult)
                c=0
                if len(myresult)!=0:
                    c = len(myresult[0])
                r = len(myresult)
                self.tableWidget6.setRowCount(r)
                self.tableWidget6.setColumnCount(c)
                self.tableWidget6.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
                self.tableWidget6.setRowCount(0)
                index = 0
                columns = ["transaction_id", "Date","Name","Master Registration Number","Reciept Number","Category","Debit","Credit","Balance"]
                self.tableWidget6.setHorizontalHeaderLabels(columns)
            #rb = [QRadioButton() for x in range(r)]
            #for i in range(r):
        #    self.tableWidget.setCellWidget(index, i+1,rb[i] )
                for row_number, row_data in enumerate(myresult):
            #print(row_number)
                    self.tableWidget6.insertRow(row_number)
                    for column_number, data in enumerate(row_data):
                    #print(column_number)
                        #item_checked = QTableWidgetItem()
                        #item_checked.setCheckState(Qt.Checked)
                    #item_checked.setCheckable(True)
                        #self.tableWidget6.setItem(column_number,0, item_checked)
                        self.tableWidget6.setItem(row_number, column_number, QTableWidgetItem(str(data)))

        if book == "Petty Cashbook":
            if self.horizontalLayout_611.count()==1:
                pass
            else:
                self.pushButton_63 = QPushButton(self.cashbook)
                self.pushButton_63.setObjectName("pushButton_62")
                self.pushButton_63.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
                self.pushButton_63.clicked.connect(self.pettywithdraw)
                self.pushButton_63.setText(QCoreApplication.translate("MainWindow", "WithDraw"))
                self.horizontalLayout_611.addWidget(self.pushButton_63)
            self.label_64.setText(QCoreApplication.translate("MainWindow", "Petty cashbook:"))
            print(fdate,tdate)
            #self.label_64.setText(QCoreApplication.translate("MainWindow", "Main cashbook:"))
            mycursor.execute("select * from petty_cashbook where date between '{0}' and '{1}'".format(tdate,fdate))
            myresult = mycursor.fetchall()
            print(myresult)
            c=0
            if len(myresult)!=0:
                c = len(myresult[0])
            r = len(myresult)
            self.tableWidget6.setRowCount(r)
            self.tableWidget6.setColumnCount(c)
            self.tableWidget6.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
            self.tableWidget6.setRowCount(0)
            index = 0
            columns = ["transaction_id", "Date","Towards","Voucher Number","Category","Debit","Credit","Balance"]
            self.tableWidget6.setHorizontalHeaderLabels(columns)
            #rb = [QRadioButton() for x in range(r)]
            #for i in range(r):
        #    self.tableWidget.setCellWidget(index, i+1,rb[i] )
            for row_number, row_data in enumerate(myresult):
            #print(row_number)
                self.tableWidget6.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    #print(column_number)
                    self.tableWidget6.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    
    def add__scheme(self):
        a = self.lineEdit15.text()
        b = self.lineEdit_152.text()
        c = self.lineEdit_153.text()
        d = self.lineEdit_156.text()
        print(a,b,c)

        if not b.isnumeric() or not c.isnumeric() or not d.isnumeric() or len(a)==0 or len(b)==0 or len(c)==0 or len(d==0):
            msg = "Check your entries"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()     
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
            )
            mycursor = mydb.cursor()
            sql = "INSERT schemes (idschemes,name,validity,remainder) VALUES (%s, %s,%s,%s)"
            val = (d,a,b,c)
            mycursor.execute(sql,val)
            mydb.commit()
            msg = "Database updated!!!"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()   

    def add_category(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall()
        ltype = myresult[0][1]
        if ltype == "master":
            self.stackedWidget.setCurrentIndex(16)
        else:
            msg = "You dont have permissions to add scheme"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()

    
    def get_statement(self):
        fdate = self.dateEdit14.date()
        fdate = fdate.toPython()
        fdate = fdate.strftime('%Y-%m-%d')
        tdate = self.dateEdit_142.date()
        tdate = tdate.toPython()
        tdate = tdate.strftime('%Y-%m-%d')
        bank = self.comboBox14.currentText()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from bank_statement where bank_name = '{0}' and date between '{1}' and '{2}'".format(bank,fdate,tdate))
        myresult = mycursor.fetchall()
        print(myresult)

        c=0
        if len(myresult)!=0:
            c = len(myresult[0])
        r = len(myresult)
        self.tableWidget14.setRowCount(r)
        self.tableWidget14.setColumnCount(c)
        self.tableWidget14.setObjectName("tableWidget")
        self.tableWidget14.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
        self.tableWidget14.setRowCount(0)
        index = 0
        columns = ["transaction_id", "bank_name","date","description"," withdrawals","deposits","Balance"]
        self.tableWidget14.setHorizontalHeaderLabels(columns)
        #rb = [QRadioButton() for x in range(r)]
        #for i in range(r):
        #    self.tableWidget.setCellWidget(index, i+1,rb[i] )
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         self.tableWidget14.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           self.tableWidget14.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    def bankacc(self):
        now = datetime.now()
        self.dateEdit14.setDate(now)
        self.dateEdit_142.setDate(now)
        self.stackedWidget.setCurrentIndex(15)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        
    def edit_exp_details(self):
        vouchnum= self.lineEdit_56.text()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from type_expenditure")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            self.comboBox_52.addItem("")
            self.comboBox_52.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
            i+=1
        
        mycursor.execute("select * from pettycashbook where voucherid = {0}".format(vouchnum))
        myresult = mycursor.fetchall()
        print(myresult) 
        #vouchnum= self.lineEdit_56.text()
        #towards= self.lineEdit_55.text()
        #amount = self.lineEdit_53.text()
        #name = self.lineEdit_52.text()
        #vdate = self.dateEdit5.date()
        #vdate = vdate.toPython()
        #vdate = vdate.strftime('%Y-%m-%d')
        #cdated= self.dateEdit_52.date()
        
        #cdated = cdated.toPython()
        #cdated = cdated.strftime('%Y-%m-%d')
        #cdrawn= self.dateEdit_53.date()
        #cdrawn = cdrawn.toPython()
        #cdrawn = cdrawn.strftime('%Y-%m-%d')
        #type_exp = str(self.comboBox_52.currentText())
        #verification= self.radioButton_52.isChecked()
        self.lineEdit_54.setText(QCoreApplication.translate("MainWindow", myresult[0][6]))
        self.lineEdit_55.setText(QCoreApplication.translate("MainWindow", myresult[0][8]))
        self.lineEdit_53.setText(QCoreApplication.translate("MainWindow", str(myresult[0][4])))
        self.lineEdit_52.setText(QCoreApplication.translate("MainWindow", myresult[0][2]))
        a = myresult[0][3]
        #a = a.toPython()
        self.dateEdit5.setDate(a)
        self.dateEdit_52.setDate(myresult[0][7])
        self.dateEdit_53.setDate(myresult[0][9])
        self.comboBox_52.setCurrentText(myresult[0][5])


    def exp_edit(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("")
        mydb.commit()
        self.pushButton_53 = QPushButton(self.deb_voucher)
        self.pushButton_53.setObjectName("pushButton_53")
        self.pushButton_53.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")     
        #self.pushButton_52.clicked.connect(self.add_expenditure)
        self.gridLayout_53.addWidget(self.pushButton_53, 2, 3, 1, 1)
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", "Get details"))
        self.pushButton_53.clicked.connect(self.edit_exp_details)
        self.stackedWidget.setCurrentIndex(6)
        #self.verticalLayout_510.addWidget(self.pushButton_52)
        #self.stackedWidget.setCurrentIndex(0)
        
    def reminded(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        r = self.tableWidget12.rowCount()
        amount = 0
        temp = []
        for i in range(r):
            print(i)
            if self.tableWidget12.item(i, 0).checkState() == Qt.Checked:
                temp = self.tableWidget12.item(i, 1)
                id_d = int(temp.text())
                mycursor.execute("update all_donations set reminded = 1 where id_donations = {0}".format(id_d))
                mydb.commit()
                mycursor.execute("select f_name,l_name,donation_date from all_donors a natural join   all_donations b where a.donor_id=b.id_donor and b.id_donations = {}".format(id_d))
                l = mycursor.fetchall()
                self.tableWidget12.removeRow(i)
                import webbrowser
                folderpath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Folder')
                print(folderpath)
                fileName = str(folderpath) + '/' + '{}.html'.format(str(id_d))
                f = open(fileName,'w',encoding='utf-8')
                name = l[0][0]+l[0][1]
                date = str(datetime.now())
                prevdate= str(l[0][2])               
                message = f"""<html>

                <head>
                <meta http-equiv=Content-Type content="text/html; charset=utf-8">
                <meta name=Generator content="Microsoft Word 15 (filtered)">
                <style>
                <!--
                /* Font Definitions */
                @font-face
                    {{font-family:SimSun;
                    panose-1:2 1 6 0 3 1 1 1 1 1;}}
                @font-face
                    {{font-family:Gautami;
                    panose-1:2 0 5 0 0 0 0 0 0 0;}}
                @font-face
                    {{font-family:"Cambria Math";
                    panose-1:2 4 5 3 5 4 6 3 2 4;}}
                @font-face
                    {{font-family:Calibri;
                    panose-1:2 15 5 2 2 2 4 3 2 4;}}
                @font-face
                    {{font-family:"Arial Unicode MS";
                    panose-1:2 11 6 4 2 2 2 2 2 4;}}
                @font-face
                    {{font-family:Peddana;}}
                @font-face
                    {{font-family:"\@SimSun";
                    panose-1:2 1 6 0 3 1 1 1 1 1;}}
                @font-face
                    {{font-family:"\@Arial Unicode MS";
                    panose-1:2 11 6 4 2 2 2 2 2 4;}}
                /* Style Definitions */
                p.MsoNormal, li.MsoNormal, div.MsoNormal
                    {{margin-top:0in;
                    margin-right:0in;
                    margin-bottom:10.0pt;
                    margin-left:0in;
                    line-height:115%;
                    font-size:11.0pt;
                    font-family:"Calibri",sans-serif;}}
                .MsoChpDefault
                    {{font-family:"Calibri",sans-serif;}}
                .MsoPapDefault
                    {{margin-bottom:10.0pt;
                    line-height:115%;}}
                @page WordSection1
                    {{size:8.5in 11.0in;
                    margin:.9in 1.0in 1.0in .6in;}}
                div.WordSection1
                    {{page:WordSection1;}}
                -->
                </style>

                </head>

                <body lang=EN-US style='word-wrap:break-word'>

                <div class=WordSection1>

                <p class=MsoNormal><span lang=TE style='font-size:12.0pt;line-height:115%;
                font-family:Peddana'>సేవ </span><span style='font-size:12.0pt;line-height:115%;
                font-family:Peddana'>                                                                                                 <span
                lang=TE>సంస్కారము   </span>                                                                                                           </span></p>

                <div style='border:none;border-bottom:solid windowtext 1.0pt;padding:0in 0in 1.0pt 0in'>

                <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
                line-height:normal;border:none;padding:0in'><span lang=TE style='font-size:
                16.0pt;font-family:Peddana'>కరుణశ్రీ సేవ సమితి</span></p>

                <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
                line-height:normal;border:none;padding:0in'><span lang=TE style='font-size:
                12.0pt;font-family:Peddana'>రిజిస్టర్డ్ నం : </span><span style='font-size:
                12.0pt;font-family:Peddana'>7451/1999</span></p>

                <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
                line-height:normal;border:none;padding:0in'><span lang=TE style='font-size:
                12.0pt;font-family:Peddana'>కారుణ్య సింధు (అరక్షిత బాలుర ఆశ్రమము )</span></p>

                <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
                line-height:normal;border:none;padding:0in'><span lang=TE style='font-size:
                12.0pt;font-family:Peddana'>విశ్వహిందూ పరిషత్ సేవ ప్రకల్పము</span></p>

                <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
                line-height:normal;border:none;padding:0in'><span style='font-size:12.0pt;
                font-family:Peddana'>17-1-474, <span lang=TE>కృష్ణానగర్ కాలనీ</span>, <span
                lang=TE>సైదాబాద్</span>, <span lang=TE>హైదరాబాద్ -</span>500 059, <span
                lang=TE>దూరవాణి: </span>040-24073204, 9000889785</span></p>

                </div>

                <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span lang=TE
                style='font-size:12.0pt;font-family:Peddana'>ఆచార్య కడారి సత్యమూర్తి </span><span
                style='font-size:12.0pt;font-family:Peddana'>                        <span
                lang=TE>పుప్పాల వెంకటేశ్వర రావు  </span>            <span lang=TE>రాజాపేట
                సత్యనారాయణ </span></span></p>

                <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
                style='font-size:12.0pt;font-family:Peddana'>         <span lang=TE>అధ్యక్షులు &emsp; &emsp; &emsp;&emsp;     
                </span>                                     <span lang=TE> కార్యదర్శి  &nbsp; &emsp; &emsp; &emsp;   &emsp; &emsp; &emsp;</span>                         <span
                lang=TE>    కోశాధికారి &emsp; &emsp;</span></span></p>

                <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
                style='font-size:14.0pt;font-family:Peddana'>     9849320610 &nbsp; &emsp;                             
                7386247393   &emsp; &emsp; &emsp;&emsp; &emsp;                      8555800196 &emsp; &emsp;&emsp;</span></p>

                <p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
                margin-left:4.0in;text-indent:.5in'><span lang=TE style='font-size:12.0pt;
                line-height:115%;font-family:Peddana'>తేదీ:</span><span style='font-size:12.0pt;
                line-height:115%;font-family:Peddana'>{date}</span></p>

                <p class=MsoNormal><span lang=TE style='font-size:12.0pt;line-height:115%;
                font-family:Peddana'> శ్రీమతి / శ్రీ </span><span style='font-size:12.0pt;
                line-height:115%;font-family:Peddana'>M /S
                {name}     <span lang=TE>గారికి  సప్రేమ
                నమస్కారములు</span>.<span lang=TE>    </span></span></p>

                <p class=MsoNormal><span lang=TE style='font-size:12.0pt;line-height:115%;
                font-family:Peddana'>మీరు సహృదయముతో మా ఆశ్రమ బాలల సంరక్షణార్థం మీ ఆత్మీయుల జన్మదిన/స్మృతిదిన
                జ్ఞాపకార్థం గత సంవత్సరము తేదీ  </span><span style='font-size:12.0pt;line-height:
                115%;font-family:Peddana'>{prevdate}<span lang=TE> నాడు అన్నదాన కార్యక్రమము
                ఏర్పాటు చేసినారు. ధన్యవాదములు</span>, <span lang=TE>ఈ సంవత్సరము కూడా మీ తరపున
                అన్నదానము చేయుటకు సమ్మతి తెలియచేయగలరని ప్రార్థిస్తున్నాము. </span></span></p>

                <p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
                margin-left:1.0in;text-indent:.5in;line-height:normal'><span lang=TE
                style='font-size:12.0pt;font-family:Peddana'>ఒక రోజు భోజనము  రూ. 2,000/-</span></p>

                <p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
                margin-left:1.0in;text-indent:.5in;line-height:normal'><span lang=TE
                style='font-size:12.0pt;font-family:Peddana'>శాశ్వత అన్నదాన నిధి  రూ. 10,000/-</span></p>

                <p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
                margin-left:.5in;text-indent:.5in;line-height:normal'><span lang=TE
                style='font-size:12.0pt;font-family:Peddana'>( సంవత్సరములో మీరు ఎంచుకున్న ఒక్క
                రోజు 10 సంవత్సరాల వరకు )</span></p>

                <p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
                margin-left:1.0in;text-indent:.5in;line-height:normal'><span lang=TE
                style='font-size:12.0pt;font-family:Peddana'> విద్యార్ధి సంరక్షణ  నిధి  రూ. 25</span><span
                style='font-size:12.0pt;font-family:Peddana'>,<span lang=TE>000/-</span></span></p>

                <p class=MsoNormal style='margin-top:0in;margin-right:0in;margin-bottom:0in;
                margin-left:1.0in;text-indent:.5in;line-height:normal'><span lang=TE
                style='font-size:12.0pt;font-family:Peddana'>చెక్కులు /డి.డి.లు &quot; </span><span
                style='font-size:12.0pt;font-family:Peddana'>Karunasri Seva Samithi <span
                lang=TE> &quot; పేరున వ్రాయవలెను... </span></span></p>

                <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
                style='font-size:12.0pt;font-family:Peddana'>&nbsp;</span></p>

                <p class=MsoNormal style='margin-bottom:0in;line-height:normal'><span
                style='font-size:12.0pt;font-family:Peddana'>                                                    
                <span lang=TE>ధన్యవాదములతో.</span></span></p>

                <p class=MsoNormal><span style='font-size:12.0pt;line-height:115%;font-family:
                Peddana'>                                                                                                                                    <span
                lang=TE>ఇట్లు</span></span></p>

                <p class=MsoNormal><span style='font-size:12.0pt;line-height:115%;font-family:
                Peddana'>                                                                                                       <span
                lang=TE>కరుణశ్రీ సేవ సమితి</span></span></p>

                <p class=MsoNormal><span style='font-size:12.0pt;line-height:115%;font-family:
                Peddana'>&nbsp;</span></p>

                <p class=MsoNormal><span lang=TE style='font-size:12.0pt;line-height:115%;
                font-family:"Arial Unicode MS",sans-serif'>&nbsp;</span></p>

                </div>

                </body>

                </html>"""
                f.write(message)
                f.close()
                #formatted = jinja2.Template(message).render(products=helloworld)
                webbrowser.open_new_tab(fileName)
        self.stackedWidget.setCurrentIndex(0)

    def donation_remainder_button(self):
        self.stackedWidget.setCurrentIndex(12)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select id_donations, donation_in_name,phone,email, date_of_donation,donation_date,Ocassion,remarks from all_donations ado, all_donors ad where curdate() > remind_date and reminded =0 and ado.id_donor = ad.donor_id")
        myresult = mycursor.fetchall()
        c=0
        if len(myresult)!=0:
            c = len(myresult[0])
        r = len(myresult)
        self.tableWidget12 = QTableWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget12.setSizePolicy(sizePolicy)
        self.tableWidget12.setMinimumSize(QSize(0, 0))
        self.tableWidget12.setRowCount(r)
        self.tableWidget12.setColumnCount(c+1)
        self.tableWidget12.setObjectName("tableWidget12")
        self.tableWidget12.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
        self.tableWidget12.setRowCount(0)
        index = 0
        columns = ["id_donation", "donation_in_name","phone","email"," date_of_donation","donation_date","Ocassion","remarks"]
        self.tableWidget.setHorizontalHeaderLabels(columns)
        #rb = [QRadioButton() for x in range(r)]
        #for i in range(r):
        #    self.tableWidget.setCellWidget(index, i+1,rb[i] )
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         self.tableWidget12.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           item_checked = QTableWidgetItem()
           item_checked.setCheckState(Qt.Unchecked)
           item_checked.setFlags(Qt.ItemIsUserCheckable |Qt.ItemIsEnabled)
                    #item_checked.setCheckable(True)
           self.tableWidget12.setItem(row_number,0, item_checked) 
           self.tableWidget12.setItem(row_number, column_number+1, QTableWidgetItem(str(data)))
        if self.verticalLayout_121212.count() !=0: 
            self.verticalLayout_121212.itemAt(0).widget().deleteLater()
        self.verticalLayout_121212.addWidget(self.tableWidget12)
    
    def exp_confirm(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall()
        mid = myresult[0][0]
        mycursor = mydb.cursor()
        mycursor.execute("select * from pettycashbook where checked = 0")
        result = mycursor.fetchall()
        l = len(result)
        mycursor.execute("update pettycashbook set checked = 1, masterid = '{0}'  where checked = 0".format(mid))
        mydb.commit()
        for x in result:
            mycursor.execute("select * from petty_cashbook ORDER BY transaction_id DESC LIMIT 1")
            myresult = mycursor.fetchall()
            if len(myresult) == 0:
                balance = 0
            else:
                balance = myresult[0][7]
            sql = "INSERT INTO petty_cashbook (date,name,reciept_number,category,credit,balance) VALUES (%s, %s,%s,%s,%s,%s)"
            val = (x[3],x[8],x[1],x[5],int(x[4]),int(balance)-int(x[4]))
            mycursor.execute(sql, val)
            mydb.commit()
        msg = "Updated successfully"
        self.dialog = QDialog()
        self.ui = Ui_OK()
        self.ui.setupUi(self.dialog,msg)
        self.dialog.exec()
        self.tableWidget11.clearContents()
        self.stackedWidget.setCurrentIndex(0)

    
    def exp_analysisbutton(self):
        fdate = self.dateEdit102.date()
        fdate = fdate.toPython()
        fdate = fdate.strftime('%Y-%m-%d')
        tdate = self.dateEdit_102.date()
        tdate = tdate.toPython()
        tdate = tdate.strftime('%Y-%m-%d')
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from type_expenditure as t,pettycashbook as c where t.code_name = c.type and c.voucherdate between '{0}' and '{1}' ".format(fdate,tdate))
        myresult = mycursor.fetchall()
        val = [0 for x in range(10)]
        for x in myresult:
            for i in range(10):
                if x[0]>=i*10 and x[0]<(i+1)*10:
                    val[i]+=x[6]
                    #print(x[6])
        piedata = []
        x=val
        for i in range(10):
            if x[i]!=0:
                if i==1:
                    piedata.append(("salaries",x[i]))
                elif i==2:
                    piedata.append(("mess expences",x[i]))
                elif i==3:
                    piedata.append(("administration expences",x[i]))
                elif i==4:
                    piedata.append(("educational expences",x[i]))
                elif i==5:
                    piedata.append(("medical/building expences",x[i]))
                elif i==9:
                    piedata.append(("general expences",x[i]))
                else:
                    piedata.append(("new category",x[i]))
                
        series = QtCharts.QPieSeries()
        for x in piedata:
            series.append(x[0],int(x[1]))
        series.setLabelsVisible(True)
        #series.setLabelsPosition(bottom)
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("Donations from various Schemes")
        #chart.legend().setAlignment(Qt.AlignBottom)
        chartview = QtCharts.QChartView(chart)
        chartview.setBackgroundBrush(QColor("darkgray"))
        #chartview.setRenderHint(QPainter.Antialiasing)
        if self.horizontalLayout_1014.count() !=0: 
            self.horizontalLayout_1014.itemAt(0).widget().deleteLater()
        self.horizontalLayout_1014.addWidget(chartview)
        t = sum(val)
        self.lcdNumber10.display(t)
        #print(val)
    def get_exp_butn(self):
        fdate = self.dateEdit102.date()
        fdate = fdate.toPython()
        fdate = fdate.strftime('%Y-%m-%d')
        tdate = self.dateEdit_102.date()
        tdate = tdate.toPython()
        tdate = tdate.strftime('%Y-%m-%d')
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from pettycashbook where voucherdate between '{0}' and '{1}' ".format(fdate,tdate))
        myresult = mycursor.fetchall()
        c = len(myresult[0])
        r = len(myresult)
        self.tableWidget = QTableWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setRowCount(r)
        self.tableWidget.setColumnCount(c)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        
        self.tableWidget.setRowCount(0)
        total = 0
        for x in myresult:
            total+=x[4]
        self.lcdNumber10.display(total)
        columns = ["database id","vocher id","paid to","voucher date","amount","type of expenditure","payment mode","date on check","towards","drawn on","master id","checked"]
        self.tableWidget.setHorizontalHeaderLabels(columns)
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         self.tableWidget.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        if self.horizontalLayout_1014.count() !=0: 
            self.horizontalLayout_1014.itemAt(0).widget().deleteLater()
        self.horizontalLayout_1014.addWidget(self.tableWidget)
        
    def add_expenditure(self):
        masterid= self.lineEdit_57.text() 
        vouchnum= self.lineEdit_56.text()
        mode = self.lineEdit_54.text()
        towards= self.lineEdit_55.text()
        amount = self.lineEdit_53.text()
        name = self.lineEdit_52.text()
        vdate = self.dateEdit5.date()
        vdate = vdate.toPython()
        vdate = vdate.strftime('%Y-%m-%d')
        cdated= self.dateEdit_52.date()
        cdated = cdated.toPython()
        cdated = cdated.strftime('%Y-%m-%d')
        cdrawn= self.dateEdit_53.date()
        cdrawn = cdrawn.toPython()
        cdrawn = cdrawn.strftime('%Y-%m-%d')
        type_exp = str(self.comboBox_52.currentText())
        verification= self.radioButton_52.isChecked()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from log ORDER BY loginid DESC LIMIT 1")
        myresult = mycursor.fetchall() 
        ltype = myresult[0][1]
        mid = myresult[0][0]
        mycursor = mydb.cursor()
        if ltype == 'master':
            t=1
        mycursor.execute("select voucherid from pettycashbook where voucherid = '{0}'".format(vouchnum))
        r = mycursor.fetchall()
        if len(r)==0:
            insert = 1
        else:
            insert = 0 
        if len(vouchnum)==0 or len(name)==0 or len(towards)==0:
            msg = "All the fields are mandatory."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        elif verification and ltype == 'master':
            if insert == 1:
                sql = "INSERT INTO pettycashbook (voucherid,paidto, voucherdate,amount,type,payment_mode,check_dated,towards,drawn_on,masterid,checked) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                t=1
                val = (vouchnum,name,vdate,amount,type_exp,mode,cdated,towards,cdrawn,myresult[0][0],t)
                mycursor.execute(sql, val)
                mydb.commit()
                
                msg = "Database updated successfully."
                self.dialog = QDialog()
                self.ui = Ui_OK()
                self.ui.setupUi(self.dialog,msg)
                self.dialog.exec()
            else:
                mycursor.execute("update pettycashbook set voucherid = '{0}',paidto = {1}, voucherdate = '{2}',amount = '{3}',type,payment_mode = {4},check_dated = '{5}',towards = {6},drawn_on = '{7}' where voucherid = '{8}'".format(vouchnum,name,vdate,amount,type_exp,mode,cdated,towards,cdrawn,vouchnum))
                mydb.commit()
                msg = "Database updated successfully."
                self.dialog = QDialog()
                self.ui = Ui_OK()
                self.ui.setupUi(self.dialog,msg)
                self.dialog.exec()
        elif verification and ltype == 'normal':
            msg = "Normal user do not have permission to verify the expenditure. pls uncheck the master button"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        else:
            if insert == 1:
                sql = "INSERT INTO pettycashbook (voucherid,paidto, voucherdate,amount,type,payment_mode,check_dated,towards,drawn_on) VALUES (%s, %s,%s,%s,%s,%s,%s,%s,%s)"
                val = (vouchnum,name,vdate,amount,type_exp,mode,cdated,towards,cdrawn)
                mycursor.execute(sql, val)
                mydb.commit()
                msg = "Database updated successfully."
                self.dialog = QDialog()
                self.ui = Ui_OK()
                self.ui.setupUi(self.dialog,msg)
                self.dialog.exec()
            else:
                mycursor.execute("update pettycashbook set voucherid = '{0}',paidto = '{1}', voucherdate = '{2}',amount = {3},type='{4}',payment_mode = '{5}',check_dated = '{6}',towards = '{7}',drawn_on = '{8}' where voucherid = {9}".format(vouchnum,name,vdate,amount,type_exp,mode,cdated,towards,cdrawn,vouchnum))
                mydb.commit()
                msg = "Database updated successfully."
                self.dialog = QDialog()
                self.ui = Ui_OK()
                self.ui.setupUi(self.dialog,msg)
                self.dialog.exec()
                
    def update_details_button(self):
        sid = self.lineEdit7.text()
        annual_fee = self.lineEdit_75.text()
        studying = self.lineEdit_78.text()
        fee_paid = self.lineEdit_76.text()
        adhar_no = self.lineEdit_77.text()
        school_addr = self.textEdit7.toPlainText()
        school_name = self.lineEdit_74.text()
        academicyear = self.lineEdit_79.text()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        if len(adhar_no)!=12 or not adhar_no.isnumeric():
            msg = "Check your adhar number"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        else:
            sql = "update student set school_name = '{1}', school_address = '{2}',studying = '{3}',academic_year = '{4}',annualfeel = {5},feepaid = {6},adharnumber = {7} where ashramam_id = {0}".format(sid,school_name, school_addr,studying,academicyear,annual_fee,fee_paid,adhar_no)
            #val = (school_name, school_addr,studying,academicyear,annual_fee,fee_paid,adhar_no)
            mycursor.execute(sql)
            mydb.commit()
            msg = "Database updated Successfully."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            self.stackedWidget.setCurrentIndex(0)
        
        
    
    def get_stud_details(self):
        sid = self.lineEdit7.text()
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute( "select * from student where ashramam_id = {0}".format(sid))
        myresult = mycursor.fetchall()
        if len(myresult)==0:
            msg = "No student found with the given id. please check!!!"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        else:
            self.lineEdit_72.setText(QCoreApplication.translate("MainWindow", myresult[0][2]))
            self.lineEdit_73.setText(QCoreApplication.translate("MainWindow", myresult[0][3]))
            print(myresult)
        
    def exp_analysis_func(self):
        self.stackedWidget.setCurrentIndex(11)
    
    def alldonations(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        fromd = self.dateEdit9.date()
        fromd = fromd.toPython()
        ffromd = fromd.strftime('%Y-%m-%d')
        tod = self.dateEdit_92.date()
        tod = tod.toPython()
        ftod = tod.strftime('%Y-%m-%d')
        mycursor = mydb.cursor()
        mycursor.execute( "select * from donations where date_of_donation between '{0}' and '{1}'".format(ffromd,ftod))
        myresult = mycursor.fetchall()
        c = len(myresult[0])
        r = len(myresult)
        self.tableWidget = QTableWidget()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        columns = ["donation id","donor id","date of donation","donation date","donation in name","master registration number","reciept number","payment mode","payment description","ocassion","remarks","category","student id","amount"]
        self.tableWidget.setRowCount(r)
        self.tableWidget.setColumnCount(c)
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        #self.verticalLayout.addWidget(self.tableWidget)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         self.tableWidget.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        t =0
        for x in myresult:
            t+=x[13]
        
        if self.verticalLayout_991.count() !=0: 
            self.verticalLayout_991.itemAt(0).widget().deleteLater()
        self.verticalLayout_991.addWidget(self.tableWidget)
        self.lcdNumber9.display(t)
        
        #print(myresult)
        #app = QApplication(sys.argv)
        #Form = QWidget()
        #self.dialog = QDialog()
        #self.ui =  Ui_Forma()
        #self.ui.setupUi(Form,myresult)
        #Form.show()
        #sys.exit(app.exec_())

    def donation_analysis(self):
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        fromd = self.dateEdit9.date()
        fromd = fromd.toPython()
        ffromd = fromd.strftime('%Y-%m-%d')
        tod = self.dateEdit_92.date()
        tod = tod.toPython()
        ftod = tod.strftime('%Y-%m-%d')
        mycursor = mydb.cursor()
        mycursor.execute("select category, sum(amount) from all_donations where date_of_donation between '{0}' and '{1}' group by category".format(ffromd,ftod))
        myresult = mycursor.fetchall()
        mycursor.execute("select * from schemes")
        cat = mycursor.fetchall()
        series = QtCharts.QPieSeries()
        tsum=0
        for x in myresult:
            series.append(cat[x[0]-1][1],x[1])
            tsum+=x[1]
        self.lcdNumber9.display(tsum)
        series.setLabelsVisible(True)
        #series.setLabelsPosition(bottom)
        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)
        chart.setTitle("Donations from various Schemes")
        #chart.legend().setAlignment(Qt.AlignBottom)
        chartview = QtCharts.QChartView(chart)
        chartview.setBackgroundBrush(QColor("darkgray"))
        #chartview.setRenderHint(QPainter.Antialiasing)
        if self.verticalLayout_991.count() !=0: 
            self.verticalLayout_991.itemAt(0).widget().deleteLater()
        self.verticalLayout_991.addWidget(chartview)
        

        #self.widget9.addWidget(chartview)
    def new_user_func(self):
        fname = self.lineEdit8.text()
        passw = self.lineEdit_84.text()
        username = self.lineEdit_83.text()
        designation = self.lineEdit_85.text()
        rpassw = self.lineEdit_86.text()
        lname = self.lineEdit_82.text()
        reset_pass = self.lineEdit_87.text()
        
        g = ''
        if self.radioButton8.isChecked():
            g = 'normal'
        else:
            g= 'master'
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from login where username = '{0}'".format(username))
        myresult = mycursor.fetchall()
        if(passw!=rpassw):
            msg = "Both Passwords doesnt match. please check!!!"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        elif(len(fname)==0 or len(passw)==0 or len(username)==0 or len(designation)==0 or len(rpassw)==0 or len(lname)==0):
            msg = "All fields are mandatory..."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        elif(len(myresult)!=0):
            msg = "Username already exsits. pls chooce another one."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        else:
            mycursor = mydb.cursor()
            sql = "INSERT INTO login (username, password,login_type,fname,lname,designation,reset_pass) VALUES (%s, %s,%s,%s,%s,%s,%s)"
            val = (username, passw,g,fname,lname,designation,reset_pass)
            mycursor.execute(sql, val)
            mydb.commit()
            msg = "Database updated succesfully. New account has been created."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            self.stackedWidget.setCurrentIndex(0)
    def dreports(self):
        self.stackedWidget.setCurrentIndex(10)
    
    def update_stud_butn(self):
        print("update stud working")
        self.stackedWidget.setCurrentIndex(8)
    
    def update_stud_details(self):
        self.stackedWidget.setCurrentIndex(7)
    def deb_voucher(self):
        print("working new_student")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from type_expenditure")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            self.comboBox_52.addItem("")
            self.comboBox_52.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
            i+=1
        now = datetime.now()
        self.dateEdit5.setDate(now)
        self.dateEdit_52.setDate(now)
        self.dateEdit_53.setDate(now)
        self.stackedWidget.setCurrentIndex(6)
        #self.
    
    def open_new_student(self):
        print("working new_student")
        self.stackedWidget.setCurrentIndex(5)
    
    def new_donor_button(self):
        print("working new_donor_button")
        self.stackedWidget.setCurrentIndex(3)
    
    def new_donation_button(self):
        print("working new_donation_button")
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
                )

        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from schemes")
        myresult = mycursor.fetchall()
        for x in myresult:
            self.comboBox_4.addItem(str(x[1]))
        mycursor.execute("select * from all_donations ORDER BY id_donations DESC LIMIT 1")
        result = mycursor.fetchall()
        reg = str(result[0][5]+1)
        print(result)
        self.lineEdit_214.setText(reg)
        self.stackedWidget.setCurrentIndex(4)
    
    def new_donor_save(self):
        print("working new_donor_save")
        fname = self.lineEdit_2.text()
        lname = self.lineEdit_3.text()
        phone_num = self.lineEdit_4.text()
        adhar_id = self.lineEdit_5.text()
        address = self.textEdit_au.toPlainText()
        email = self.lineEdit_13.text()
        #govt_id_type = str(self.comboBox_12.currentText())
        pan_id =  self.lineEdit_0.text()
        if(len(phone_num)!=10 or not phone_num.isnumeric()):
            msg = "Wrong Phone number. Please check and enter the phone number properly"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            #self.dialog.exec()
            self.lineEdit_4.setStyleSheet('''
    QLineEdit {
        border: 2px solid rgb(63, 63, 63);
        color: rgb(255, 255, 255);
        background-color: rgb(255, 0, 0);
    }
''')
        elif(len(adhar_id) != 12 and adhar_id != 'NA' ):
            msg = "Wrong Adhaar Id. Please check and enter the Adhaar Id properly"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
              #  self.dialog.exec()
            self.lineEdit_5.setStyleSheet('''
    QLineEdit {
        border: 2px solid rgb(63, 63, 63);
        color: rgb(255, 255, 255);
        background-color: rgb(255, 0, 0);
    }
''')
            
        elif(len(pan_id) != 12 and pan_id != 'NA'):
            msg = "Wrong Pan Id. Please check and enter the Pan Id properly"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            self.lineEdit_0.setStyleSheet('''
    QLineEdit {
        border: 2px solid rgb(63, 63, 63);
        color: rgb(255, 255, 255);
        background-color: rgb(255, 0, 0);
    }
''')
        elif('@' not in email and email != 'NA'):
            self.lineEdit_13.setStyleSheet('''
    QLineEdit {
        border: 2px solid rgb(63, 63, 63);
        color: rgb(255, 255, 255);
        background-color: rgb(255, 0, 0);
    }
''')
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
                )

            print(mydb)
            mycursor = mydb.cursor()
            sql = "INSERT INTO all_donors (f_name, l_name,address,phone,email,adhar_id,pan_id) VALUES (%s, %s,%s,%s,%s,%s,%s)"
            val = (fname, lname,address,phone_num,email,adhar_id,pan_id)
            mycursor.execute(sql, val)
            mydb.commit()

            print(mycursor.rowcount, "record inserted.")
            msg = "Database updated Successfully"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            self.stackedWidget.setCurrentIndex(0)

    def new_donation_save(self):
        donation_in_name = self.lineEdit_212.text()
        master_registration = self.lineEdit_214.text()
        payment_mode = str(self.comboBox_2.currentText())
        payment_description =  self.textEdit211.toPlainText()
        occasion = str(self.comboBox_3.currentText())
        remarks = self.textEdit_212.toPlainText()
        category = str(self.comboBox_4.currentText())
        student = str(self.comboBox_5.currentText())
        book_number = self.lineEdit_215.text()
        phone = self.lineEdit_213.text()
        date_of_donation = self.dateTimeEdit.dateTime()
        date_of_donation = date_of_donation.toPython()
        formatted_dod = date_of_donation.strftime('%Y-%m-%d %H:%M:%S')
        donation_date = self.dateEdit2.date()
        amount = self.lineEdit_2115.text()
        bank_deposit = ''
        if payment_mode == "Direct remittance to bank" or payment_mode == "Cheque":
            bank_deposit = str(self.comboBox_44.currentText())
        
        print(donation_date)
        donation_date = donation_date.toPython()
        formatted_dd = donation_date.strftime('%Y-%m-%d')
        today = donation_date
        print(phone,donation_in_name,master_registration,payment_mode,payment_description,occasion)
        print(remarks,category,student,book_number,date_of_donation,donation_date,bank_deposit)
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
                )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from schemes")
        sch = mycursor.fetchall()
        for x in sch:
            if category == x[1]:
                end = today + timedelta(days=x[2])
        formatted_end = end.strftime('%Y-%m-%d')
        mycursor.execute("select * from all_donors where phone = {0}".format(phone))
        myresult = mycursor.fetchall()
        print(myresult)
        if len(myresult)!=0:
            donor_id = myresult[0][0]
        else:
            msg = "Donor is not available in database please add the new donor"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        mycursor.execute("select * from schemes where name = '{0}'".format(category))
        cat = mycursor.fetchall()
        catid = cat[0][0]
        if len(donation_in_name)==0 or len(master_registration)==0 or len(payment_mode)==0 or len(payment_description)==0 or len(occasion)==0 or len(remarks)==0 or len(category)==0 or len(book_number)==0 or not amount.isnumeric():
            msg = "All feilds are to be filled. Students feild only if applicable"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        elif len(myresult)==0:
            msg = "Pls add the donor in the databse before making the donation"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        else:
            mycursor = mydb.cursor()
            if(student==''):
                student=0
            mycursor.execute("select * from all_donations where master_registration_number = {0}".format(master_registration))
            update = mycursor.fetchall()
            l = len(update)
            if l==0:
                sql = "INSERT INTO all_donations (id_donor, date_of_donation,donation_date,donation_in_name,master_registration_number,reciept_number,payment_mode,payment_description,Ocassion,remarks,category,id_student,amount,remind_date,date_show,bank_deposit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                val = (int(donor_id),formatted_dod,formatted_dd,donation_in_name, master_registration, book_number,payment_mode,payment_description, occasion,remarks,int(catid),student,int(amount),formatted_end,formatted_dd,bank_deposit)
                mycursor.execute(sql, val)
                mydb.commit()
                mycursor.execute("update all_donors set number_of_times_donated = number_of_times_donated+1 where donor_id = {0}".format(donor_id))
                mydb.commit()
            elif l>0:
                sql = "Update all_donations set id_donor = {0}, date_of_donation = '{1}',donation_date = '{2}',donation_in_name = '{3}',reciept_number = {5},payment_mode = '{6}',payment_description = '{7}',Ocassion = '{8}',remarks ='{9}',category = {10},id_student = {11},amount = '{12}',remind_date = '{13}',date_show = '{14}',bank_deposit = '{15}' where master_registration_number = {4}".format(int(donor_id),formatted_dod,formatted_dd,donation_in_name, master_registration, book_number,payment_mode,payment_description, occasion,remarks,int(catid),student,int(amount),formatted_end,formatted_dd,bank_deposit)
                #val = (int(donor_id),formatted_dod,formatted_dd,donation_in_name, master_registration, book_number,payment_mode,payment_description, occasion,remarks,int(catid),student,int(amount),formatted_end)
                mycursor.execute(sql)
                mydb.commit()
            msg = "Database updated Successfully and donation has been saved"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            import webbrowser
            folderpath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Folder')
            print(folderpath)
            fileName = str(folderpath) + '/' + '{}.html'.format(str(master_registration))
            f = open(fileName,'w',encoding='utf-8')
            #import jinja2
            marker = str(date_of_donation)
            name = donation_in_name
            amount = amount
            if payment_mode == 'Cheque': 
                chenum = payment_description
                chedate = str(date_of_donation)
                chers = amount
            else:
                chers = amount
                chenum = ''
                chedate = ''
            reciptnum = master_registration

            message = f"""<html>

            <head>
            <meta http-equiv=Content-Type content="text/html; charset=utf-8">

            <meta name=Generator content="Microsoft Word 15 (filtered)">
            <style>
            <!--
            /* Font Definitions */
            @font-face
                {{font-family:SimSun;
                panose-1:2 1 6 0 3 1 1 1 1 1;}}
            @font-face
                {{font-family:Gautami;
                panose-1:2 0 5 0 0 0 0 0 0 0;}}
            @font-face
                {{font-family:"Cambria Math";
                panose-1:2 4 5 3 5 4 6 3 2 4;}}
            @font-face
                {{font-family:Peddana;}}
            @font-face
                {{font-family:"\@SimSun";
                panose-1:2 1 6 0 3 1 1 1 1 1;}}
            /* Style Definitions */
            p.MsoNormal, li.MsoNormal, div.MsoNormal
                {{margin-top:0in;
                margin-right:0in;
                margin-bottom:10.0pt;
                margin-left:0in;
                line-height:115%;
                font-size:11.0pt;
                font-family:"Calibri",sans-serif;}}
            .MsoChpDefault
                {{font-family:"Calibri",sans-serif;}}
            .MsoPapDefault
                {{margin-bottom:10.0pt;
                line-height:115%;}}
            @page WordSection1
                {{size:8.5in 11.0in;
                margin:1.0in 1.0in 1.0in 1.0in;}}
            div.WordSection1
                {{page:WordSection1;}}
            -->
            </style>

            </head>

            <body lang=EN-US style='word-wrap:break-word'>

            <div class=WordSection1>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'>సేవ</span><span
            style='font-family:Peddana'>                                                                                                                  
            <span lang=TE> సంస్కారము   </span></span></p>

            <div style='border:none;border-bottom:solid windowtext 1.0pt;padding:0in 0in 1.0pt 0in'>

            <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
            line-height:normal;border:none;padding:0in'><span lang=TE style='font-size:
            26.0pt;font-family:Peddana'>కరుణశ్రీ సేవ సమితి</span></p>

            <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
            line-height:normal;border:none;padding:0in'><span lang=TE style='font-family:
            Peddana'>రిజిస్టర్డ్ నం : </span><span style='font-family:Peddana'>7451/1999</span></p>

            <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
            line-height:normal;border:none;padding:0in'><span lang=TE style='font-family:
            Peddana'>కారుణ్య సింధు (అరక్షిత బాలుర ఆశ్రమము )</span></p>

            <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
            line-height:normal;border:none;padding:0in'><span lang=TE style='font-family:
            Peddana'>విశ్వహిందూ పరిషత్ సేవ ప్రకల్పము</span></p>

            <p class=MsoNormal align=center style='margin-bottom:0in;text-align:center;
            line-height:normal;border:none;padding:0in'><span style='font-family:Peddana'>17-1-474,
            <span lang=TE>కృష్ణానగర్ కాలనీ</span>, <span lang=TE>సైదాబాద్</span>, <span
            lang=TE>హైదరాబాద్ -</span>500 059, <span lang=TE>చరవాణి: </span>040-24073204,
            9000889785</span></p>

            </div>

            <p class=MsoNormal style='margin-bottom:0in'><span lang=TE style='font-family:
            Peddana'>ఆచార్య కడారి సత్యమూర్తి </span><span style='font-family:Peddana'>                              <span
            lang=TE>పుప్పాల వెంకటేశ్వర రావు  </span>              <span lang=TE>రాజాపేట
            సత్యనారాయణ </span></span></p>

            <p class=MsoNormal style='margin-bottom:0in'><span style='font-family:Peddana'>        
            <span lang=TE>అధ్యక్షులు      </span>                                        <span
            lang=TE> కార్యదర్శి     </span>                           <span lang=TE>    కోశాధికారి 
            </span></span></p>

            <p class=MsoNormal style='margin-left:4.0in;text-indent:.5in'><span lang=TE
            style='font-family:Peddana'>తేదీ:</span><span style='font-family:Peddana'> {marker} </span></p>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'> శ్రీమతి / శ్రీ </span><span
            style='font-family:Peddana'>M /S {name}  
            <span lang=TE>గారికి  సప్రేమ నమస్కారములు</span>.<span lang=TE>    </span></span></p>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'>మీరు సహృదయముతో మా
            ఆశ్రమ బాలల సంరక్షణార్థం చెల్లించిన విరాళము రూ.</span><span style='font-family:
            Peddana'> {amount} <span lang=TE> </span></span></p>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'>చెక్కు  నెంబర్ </span><span
            style='font-family:Peddana'> {chenum} <span lang=TE> తేదీ</span> {chedate} .<span
            lang=TE>    నగద</span>. <span lang=TE>  రూ </span> {chers} </span></p>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'>స్వీకరించబడినది.
            అందులకు మా హృదయకపూర్వక కృతజ్ఞతాభివందనాలు</span><span style='font-family:Peddana'>,
            <span lang=TE>మీకు</span>,<span lang=TE>మీ కుటుంబ సభ్యులకు సంపూర్ణ
            ఆయురారోగ్యాలను</span>, <span lang=TE>సకల సుఖసంతోషాలను ప్రసాదించాలని</span>, <span
            lang=TE>మీ అభీష్టాలను నెరవేర్చాలని</span>, <span lang=TE>కార్యవర్గ సభ్యులము</span>,
            <span lang=TE>ఆశ్రమ బాలురు పరమేశ్వరుని ప్రార్థిస్తున్నాము. </span></span></p>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'> మీరు చెల్లించిన
            విరాళములకై మా సంస్థ యొక్క రశీదు నెంబర్</span><span style='font-family:Peddana'> {reciptnum} <span
            lang=TE> తేదీ </span> {chedate} <span
            lang=TE> రూ</span> {amount}.<span lang=TE>
            పంపుచున్నాము. </span></span></p>

            <p class=MsoNormal><span lang=TE style='font-family:Peddana'>ఈ బాలలకు మీ
            ప్రేమను ఆశీస్సులను అందజేస్తూ మున్ముందు కూడా ఈ సంస్థకు చేయూత ఇవ్వగలరని
            కోరుతున్నాము. </span></p>

            <p class=MsoNormal align=right style='text-align:right'><span style='font-family:
            Peddana'>&nbsp;</span></p>

            <p class=MsoNormal align=right style='text-align:right'><span lang=TE
            style='font-family:Peddana'>ఇట్లు</span></p>

            </div>

            </body>

            </html>"""
            f.write(message)
            f.close()
            mycursor.execute("select * from all_donors where donor_id = (select id_donor from all_donations where master_registration_number = {})".format(master_registration))
            ans = mycursor.fetchall()
            #formatted = jinja2.Template(message).render(products=helloworld)
            webbrowser.open_new_tab(fileName)
            import webbrowser
            import inflect
            folderpath = QtWidgets.QFileDialog.getExistingDirectory(None,'Select Folder')
            print(folderpath)
            fileName = str(folderpath) + '/' + 'reciept {}.html'.format(str(master_registration))
            f = open(fileName,'w',encoding='utf-8')
            date='31-10-21'
            receipt_no=20
            name = ans[0][1] + ans[0][2]
            mobile_no= phone
            pan_no=ans[0][7]
            aadhar_no=ans[0][6]
            address=ans[0][3]
            mail_id=ans[0][5]
            p = inflect.engine()
            
            amount_in_words = p.number_to_words(amount) 
            cheque_no = payment_description 
            drawn_bank= bank_deposit
            towards= remarks

            message = f"""<html>
            <head>

            <style type="text/css">
            <!--
            body {{ font-family: Arial; font-size: 22.1px }}
            .pos {{ position: absolute; z-index: 0; left: 0px; top: 0px }}
            -->
            </style>
            </head>
            <body>
            <nobr><nowrap>
            <div class="pos" id="_0:0" style="top:0">
            <img name="_1100:850" src="page_001.jpeg" height="1100" width="850" border="0" usemap="#Map"></div>
            <div class="pos" id="_78:210" style="top:210;left:78">
            <span id="_16.3" style=" font-family:Arial; font-size:16.3px; color:#000000">
            SEVA</span>
            </div>
            <div class="pos" id="_209:205" style="top:205;left:209">
            <span id="_32.0" style=" font-family:Arial; font-size:32.0px; color:#000000">
            KARUNASRI SEVA SAMITHI</span>
            </div>
            <div class="pos" id="_678:201" style="top:201;left:678">
            <span id="_16.3" style=" font-family:Arial; font-size:16.3px; color:#000000">
            SAMSKAR</span>
            </div>
            <div class="pos" id="_197:251" style="top:251;left:197">
            <span id="_13.6" style=" font-family:Arial; font-size:13.6px; color:#000000">
            H.No. 17-1-474, Krishna Nagar Colony, Saidabad, Hyderabad - 500 059</span>
            </div>
            <div class="pos" id="_144:287" style="top:287;left:144">
            <span id="_13.6" style=" font-family:Arial; font-size:13.6px; color:#000000">
            Soceity Regd. No.7451/1999, PAN No. AAATK6724F, Phone: 040-24073204, 9000889785</span>
            </div>
            <div class="pos" id="_149:304" style="top:304;left:149">
            <span id="_13.6" style=" font-family:Arial; font-size:13.6px; color:#000000">
            Email.ID: karunasri1999@gmail.com, Website:https://karunasri.org & www.karunasri.org</span>
            </div>
            <div class="pos" id="_390:332" style="top:332;left:390">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            <U>R</U><U>E</U><U>C</U><U>E</U><U>I</U><U>P</U><U>T</U></span>
            </div>
            <div class="pos" id="_71:351" style="top:351;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Receipt No:{receipt_no}</span>
            </div>
            <div class="pos" id="_579:351" style="top:351;left:579">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Date:{date}</span>
            </div>
            <div class="pos" id="_71:378" style="top:378;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Received with thanks from sri/Smt/M/s.{name}</span>
            </div>
            <div class="pos" id="_71:406" style="top:406;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Mobile{mobile_no} </span>
            </div>
            <div class="pos" id="_319:406" style="top:406;left:319">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            PAN No:{pan_no}                           &ensp;&ensp;&ensp;        Aadhar:{aadhar_no}</span>
            </div>
            <div class="pos" id="_71:433" style="top:433;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Address:{address}</span>
            </div>
            <div class="pos" id="_71:461" style="top:461;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            <U> </U> <U>E</U> mail Id: {mail_id}       A sum of Rs:{amount}                  </span>
            </div>
            <div class="pos" id="_71:497" style="top:497;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Rupees in words:{amount_in_words}                         </span>
            </div>
            <div class="pos" id="_71:534" style="top:534;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            by Cash/Cheque No:{cheque_no}              </span>
            </div>
            <div class="pos" id="_71:570" style="top:570;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            drawn on: {drawn_bank}   Bank, </span>
            </div>
            <div class="pos" id="_71:607" style="top:607;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Towards:  {towards}</span>
            </div>
            <div class="pos" id="_71:671" style="top:671;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            1). Corpus Funds:</span>
            </div>
            <div class="pos" id="_224:675" style="top:675;left:224">
            <span id="_12.2" style="font-weight:bold; font-family:Times New Roman; font-size:12.2px; color:#000000">
            Income Tax exemption under Section 80G IT ACT 1961 received vide director of Income Tax (Exemption) </span>
            </div>
            <div class="pos" id="_242:690" style="top:690;left:242">
            <span id="_12.2" style="font-weight:bold; font-family:Times New Roman; font-size:12.2px; color:#000000">
            Ltr.LF.No.DI(E)HYD/806/90/(05)07-08 dated 29-10-2007 & CBDT Circular No.7 dated 27-10-2010.</span>
            </div>
            <div class="pos" id="_71:699" style="top:699;left:71">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            2). Others :</span>
            </div>
            <div class="pos" id="_392:705" style="top:705;left:392">
            <span id="_12.2" style="font-weight:bold; font-family:Times New Roman; font-size:12.2px; color:#000000">
            and as amended by the Finance ACT 2020.</span>
            </div>
            <div class="pos" id="_87:795" style="top:795;left:87">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Signature of Donor</span>
            </div>
            <div class="pos" id="_386:795" style="top:795;left:386">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Receipient</span>
            </div>
            <div class="pos" id="_603:795" style="top:795;left:603">
            <span id="_16.3" style=" font-family:Times New Roman; font-size:16.3px; color:#000000">
            Treasurer/General Secretary</span>
            </div>
            </nowrap></nobr>
            </body>
            </html>"""
            f.write(message)
            f.close()
            webbrowser.open_new_tab(fileName)
            self.stackedWidget.setCurrentIndex(0)
            
    def get_donar_details(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
                )

        print(mydb)
        mycursor = mydb.cursor()
        phone = self.lineEdit.text()
        mycursor.execute("SELECT * FROM chitra_gupta.all_donors where phone = {0}".format(phone))
        myresult = mycursor.fetchall()
        print(myresult)
        if len(myresult)==0:
            msg = "The Donor is not available in the database. Please add the donor details"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            self.stackedWidget.setCurrentIndex(3)
        else:
            self.stackedWidget.setCurrentIndex(4)
            #self.lineEdit_217.setText(QCoreApplication.translate("MainWindow", myresult[0][2]))
            self.lineEdit_216.setText(QCoreApplication.translate("MainWindow", myresult[0][1]))
            self.lineEdit_213.setText(QCoreApplication.translate("MainWindow", myresult[0][4]))
            mycursor = mydb.cursor()
            mycursor.execute("select * from schemes")
            myresult = mycursor.fetchall()
            for x in myresult:
                self.comboBox_4.addItem(str(x[1]))
            mycursor.execute("select * from all_donations ORDER BY id_donations DESC LIMIT 1")
            result = mycursor.fetchall()
            reg = str(result[0][5]+1)
            print(result)
            self.lineEdit_214.setText(reg)
            
        
            
    def new_stud_add(self):
        fname = self.lineEdit_42.text()
        lname = self.lineEdit_43.text()
        student_id = self.lineEdit_46.text()
        student_details = self.textEdit4.toPlainText()
        dob = self.dateEdit4.date()
        dob = dob.toPython()
        formatted_dob = dob.strftime('%Y-%m-%d')
        if len(fname)==0 or len(lname)==0 or len(student_id)==0 or not student_id.isnumeric():
            msg = "All feilds are to be filled. Re-Check and enter the details correctly"
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="anirudh123",
            database="chitra_gupta"
                )

            print(mydb)
            mycursor = mydb.cursor()
            sql = "INSERT INTO student (ashramam_id,fname, lname,dob,student_details) VALUES (%s, %s,%s,%s,%s)"
            val = (student_id,fname, lname,formatted_dob,student_details)
            mycursor.execute(sql, val)
            msg = "Database updated Successfully."
            self.dialog = QDialog()
            self.ui = Ui_OK()
            self.ui.setupUi(self.dialog,msg)
            self.dialog.exec()
            self.stackedWidget.setCurrentIndex(0)
            mydb.commit()


    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1000, 720)
        MainWindow.setMinimumSize(QSize(1000, 720))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(0, 0, 0, 0))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(66, 73, 90, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(55, 61, 75, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(22, 24, 30, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(29, 32, 40, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        brush6 = QBrush(QColor(210, 210, 210, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush7 = QBrush(QColor(0, 0, 0, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush7)
        brush8 = QBrush(QColor(85, 170, 255, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.Link, brush8)
        brush9 = QBrush(QColor(255, 0, 127, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush10 = QBrush(QColor(44, 49, 60, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        brush11 = QBrush(QColor(210, 210, 210, 128))
        brush11.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush11)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.Link, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        brush12 = QBrush(QColor(210, 210, 210, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush7)
        brush13 = QBrush(QColor(51, 153, 255, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Link, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.LinkVisited, brush9)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        brush14 = QBrush(QColor(210, 210, 210, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setStyleSheet(u"/* LINE EDIT */\n"
"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"	border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
""
                        "	border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"	border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63"
                        ", 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius"
                        ": 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb("
                        "85, 170, 255);	\n"
"	background-color: rgb(27, 29, 35);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:verti"
                        "cal {\n"
"    background-color: rgb(85, 170, 255);\n"
"	border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"	border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 65))
        self.frame_top.setMaximumSize(QSize(16777215, 65))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle_menu = QPushButton(self.frame_toggle)
        self.btn_toggle_menu.setObjectName(u"btn_toggle_menu")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet(u"QPushButton {\n"
"	background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"	border: none;\n"
"	background-color: rgb(27, 29, 35);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")

        self.verticalLayout_3.addWidget(self.btn_toggle_menu)


        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_top_right = QFrame(self.frame_top)
        self.frame_top_right.setObjectName(u"frame_top_right")
        self.frame_top_right.setStyleSheet(u"background: transparent;")
        self.frame_top_right.setFrameShape(QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_top_right)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_top_right)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet(u"background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy1)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.frame_icon_top_bar = QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setObjectName(u"frame_icon_top_bar")
        self.frame_icon_top_bar.setMaximumSize(QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet(u"background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/favicon.jpg);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.frame_icon_top_bar)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
        self.btn_minimize.setMinimumSize(QSize(40, 0))
        self.btn_minimize.setMaximumSize(QSize(40, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
        self.btn_maximize_restore.setMinimumSize(QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMinimumSize(QSize(40, 0))
        self.btn_close.setMaximumSize(QSize(40, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)

        self.frame_top_info = QFrame(self.frame_top_right)
        self.frame_top_info.setObjectName(u"frame_top_info")
        self.frame_top_info.setMaximumSize(QSize(16777215, 65))
        self.frame_top_info.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_top_info)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(10, 0, 10, 0)
        self.label_top_info_1 = QLabel(self.frame_top_info)
        self.label_top_info_1.setObjectName(u"label_top_info_1")
        self.label_top_info_1.setMaximumSize(QSize(16777215, 15))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.label_top_info_1.setFont(font2)
        self.label_top_info_1.setStyleSheet(u"color: rgb(98, 103, 111); ")

        self.horizontalLayout_8.addWidget(self.label_top_info_1)

        self.label_top_info_2 = QLabel(self.frame_top_info)
        self.label_top_info_2.setObjectName(u"label_top_info_2")
        self.label_top_info_2.setMinimumSize(QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QSize(250, 20))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setWeight(75)
        self.label_top_info_2.setFont(font3)
        self.label_top_info_2.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.label_top_info_2)


        self.verticalLayout_2.addWidget(self.frame_top_info)


        self.horizontalLayout_3.addWidget(self.frame_top_right)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus, 0, Qt.AlignTop)

        self.frame_extra_menus = QFrame(self.frame_left_menu)
        self.frame_extra_menus.setObjectName(u"frame_extra_menus")
        sizePolicy3.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy3)
        self.frame_extra_menus.setFrameShape(QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QFrame.Raised)
        self.layout_menu_bottom = QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName(u"layout_menu_bottom")
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.label_user_icon = QLabel(self.frame_extra_menus)
        self.label_user_icon.setObjectName(u"label_user_icon")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.label_user_icon.sizePolicy().hasHeightForWidth())
        self.label_user_icon.setSizePolicy(sizePolicy4)
        self.label_user_icon.setMinimumSize(QSize(60, 60))
        self.label_user_icon.setMaximumSize(QSize(60, 60))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_user_icon.setFont(font4)
        self.label_user_icon.setStyleSheet(u"QLabel {\n"
"	border-radius: 30px;\n"
"	background-color: rgb(44, 49, 60);\n"
"	border: 5px solid rgb(39, 44, 54);\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"}")
        self.label_user_icon.setAlignment(Qt.AlignCenter)

        self.layout_menu_bottom.addWidget(self.label_user_icon, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.frame_extra_menus, 0, Qt.AlignBottom)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        
       
        
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.scrollArea = QScrollArea(self.page_home)
        self.scrollArea.setFrameShadow(QFrame.Sunken)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QRect(-472, 0, 1730, 2318))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents)
        self.frame_2.setMinimumSize(QSize(0, 2300))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label0 = QLabel(self.frame_2)
        self.label0.setMinimumSize(QSize(150, 150))
        self.label0.setMaximumSize(QSize(200, 200))
        self.label0.setText("")
        self.label0.setPixmap(QPixmap(":/16x16/icons/16x16/diya.jpg"))
        self.label0.setScaledContents(True)
        self.label0.setObjectName("label0")
        self.gridLayout.addWidget(self.label0, 1, 1, 1, 1)
        self.label_06 = QLabel(self.frame_2)
        self.label_06.setObjectName("label_06")
        self.gridLayout.addWidget(self.label_06, 2, 1, 1, 4)
        self.label_04 = QLabel(self.frame_2)
        self.label_04.setObjectName("label_04")
        self.gridLayout.addWidget(self.label_04, 0, 4, 1, 1)
        self.label_05 = QLabel(self.frame_2)
        self.label_05.setObjectName("label_05")
        self.gridLayout.addWidget(self.label_05, 0, 1, 1, 1)
        self.label_03 = QLabel(self.frame_2)
        self.label_03.setMinimumSize(QSize(150, 150))
        self.label_03.setMaximumSize(QSize(250, 200))
        self.label_03.setText("")
        self.label_03.setPixmap(QPixmap(":/16x16/icons/16x16/10741493-removebg-preview.png"))
        self.label_03.setScaledContents(True)
        self.label_03.setObjectName("label_03")
        self.gridLayout.addWidget(self.label_03, 1, 3, 1, 1)
        self.verticalLayout_8.addLayout(self.gridLayout)
        self.label_07 = QLabel(self.frame_2)
        self.label_07.setObjectName("label_07")
        self.verticalLayout_8.addWidget(self.label_07)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_02 = QLabel(self.frame_2)
        self.label_02.setObjectName("label_02")
        self.horizontalLayout_9.addWidget(self.label_02)
        self.label_08 = QLabel(self.frame_2)
        self.label_08.setObjectName("label_08")
        self.horizontalLayout_9.addWidget(self.label_08)
        self.verticalLayout_8.addLayout(self.horizontalLayout_9)
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setOpenExternalLinks(True)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_010 = QLabel(self.frame_2)
        self.label_010.setObjectName("label_010")
        self.verticalLayout_8.addWidget(self.label_010)
        self.label_011 = QLabel(self.frame_2)
        self.label_011.setMaximumSize(QSize(16777215, 50))
        self.label_011.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_011.setObjectName("label_011")
        self.verticalLayout_8.addWidget(self.label_011)
        self.label_012 = QLabel(self.frame_2)
        self.label_012.setObjectName("label_012")
        self.verticalLayout_8.addWidget(self.label_012)
        self.label_013 = QLabel(self.frame_2)
        self.label_013.setMaximumSize(QSize(16777215, 30))
        self.label_013.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_013.setObjectName("label_013")
        self.verticalLayout_8.addWidget(self.label_013)
        self.label_014 = QLabel(self.frame_2)
        self.label_014.setObjectName("label_014")
        self.verticalLayout_8.addWidget(self.label_014)
        self.label_015 = QLabel(self.frame_2)
        self.label_015.setMaximumSize(QSize(16777215, 50))
        self.label_015.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.label_015.setObjectName("label_015")
        self.verticalLayout_8.addWidget(self.label_015)
        self.label_016 = QLabel(self.frame_2)
        self.label_016.setObjectName("label_016")
        self.verticalLayout_8.addWidget(self.label_016)
        self.verticalLayout_11.addLayout(self.verticalLayout_8)
        self.verticalLayout_7.addWidget(self.frame_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_10.addWidget(self.scrollArea)
        self.stackedWidget.addWidget(self.page_home)
        self.stackedWidget.addWidget(self.page_home)
        
        self.new_donor = QWidget()
        self.new_donor.setObjectName("new_donor")
        self.verticalLayout_10 = QVBoxLayout(self.new_donor)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QLineEdit(self.new_donor)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_3.addWidget(self.lineEdit_2, 5, 2, 1, 1)
        self.label_5 = QLabel(self.new_donor)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 8, 0, 1, 1)
        self.label_3 = QLabel(self.new_donor)
        font7 = QFont()
        font7.setFamily("Segoe UI")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.label_3.setFont(font7)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_4 = QLabel(self.new_donor)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.lineEdit_3 = QLineEdit(self.new_donor)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout_3.addWidget(self.lineEdit_3, 5, 3, 1, 1)
        self.textEdit_au = QTextEdit(self.new_donor)
        self.textEdit_au.setMaximumSize(QSize(16777215, 300))
        self.textEdit_au.setObjectName("textEdit_au")
        self.gridLayout_3.addWidget(self.textEdit_au, 6, 2, 1, 2)
        self.lineEdit_4 = QLineEdit(self.new_donor)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout_3.addWidget(self.lineEdit_4, 7, 2, 1, 1)
        self.label_2 = QLabel(self.new_donor)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 5, 0, 1, 1)
        #self.comboBox_12 = QComboBox(self.new_donor)
        #self.comboBox_12.setObjectName("comboBox_12")
        #self.comboBox_12.addItem("")
        #self.comboBox_12.addItem("")
        #self.gridLayout_3.addWidget(self.comboBox_12, 8, 2, 1, 1)
        self.lineEdit_5 = QLineEdit(self.new_donor)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 8, 2, 1, 1)
        self.label_16 = QLabel(self.new_donor)
        self.label_16.setEnabled(True)
        #sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        #sizePolicy.setHorizontalStretch(0)
        #sizePolicy.setVerticalStretch(0)
        #sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        
        #self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        #self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet("")
        self.label_16.setScaledContents(True)
        #self.label_16.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_16.setIndent(0)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 2, 1, 2)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        
        self.stackedWidget.addWidget(self.new_donor)
        
        self.expenditure_opening = QWidget()
        self.expenditure_opening.setObjectName("expenditure_opening")
        self.verticalLayout_10 = QVBoxLayout(self.expenditure_opening)
        self.verticalLayout_10.setObjectName("verticalLayout_3110")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_3112")
        self.label31 = QLabel(self.expenditure_opening)
        self.label31.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(19)
        font.setBold(True)
        font.setWeight(75)
        self.label31.setFont(font)
        self.label31.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label31.setObjectName("label31")
        self.verticalLayout_12.addWidget(self.label31)
        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.commandLinkButton_312 = QCommandLinkButton(self.expenditure_opening)
        self.commandLinkButton_312.setObjectName("commandLinkButton_312")
        self.commandLinkButton_312.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(50, 53, 65);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        #self.commandLinkButton_312.clicked.connect(self.new_donation_button)
        self.commandLinkButton_312.setFont(font1)
        self.commandLinkButton_312.clicked.connect(self.update_stud_butn)
        icon312 = QIcon()
        icon312.addFile(u":/16x16/icons/16x16/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_312.setIcon(icon312)
        self.gridLayout_3.addWidget(self.commandLinkButton_312, 0, 0, 1, 1)

        self.commandLinkButton_315 = QCommandLinkButton(self.expenditure_opening)
        self.commandLinkButton_315.setObjectName("commandLinkButton_315")
        self.commandLinkButton_315.setFont(font1)
        self.commandLinkButton_315.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(50, 53, 65);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        #self.commandLinkButton_312.clicked.connect(self.new_donation_button)
        self.commandLinkButton_315.clicked.connect(self.bankacc)
        icon315 = QIcon()
        icon315.addFile(u":/16x16/icons/16x16/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_315.setIcon(icon315)
        self.gridLayout_3.addWidget(self.commandLinkButton_315, 0, 3, 1, 1)
        self.label_314 = QLabel(self.expenditure_opening)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_314.setFont(font)
        self.label_314.setObjectName("label_314")
        self.gridLayout_3.addWidget(self.label_314, 4, 0, 1, 1)
        self.lcdNumber_313 = QLCDNumber(self.expenditure_opening)
        self.lcdNumber_313.setObjectName("lcdNumber_313")
        self.gridLayout_3.addWidget(self.lcdNumber_313, 4, 1, 1, 1)
        self.commandLinkButton_313 = QCommandLinkButton(self.expenditure_opening)
        self.commandLinkButton_313.setObjectName("commandLinkButton_313")
        self.commandLinkButton_313.setFont(font1)
        self.commandLinkButton_313.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(50, 53, 65);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")

        self.commandLinkButton_313.clicked.connect(self.exp_analysis_func)
        icon313 = QIcon()
        icon313.addFile(u":/16x16/icons/16x16/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_313.setIcon(icon313)
        self.gridLayout_3.addWidget(self.commandLinkButton_313, 0, 2, 1, 1)
        self.lcdNumber_312 = QLCDNumber(self.expenditure_opening)
        self.lcdNumber_312.setObjectName("lcdNumber_312")
        self.gridLayout_3.addWidget(self.lcdNumber_312, 3, 1, 1, 1)
        self.commandLinkButton_314 = QCommandLinkButton(self.expenditure_opening)
        self.commandLinkButton_314.setObjectName("commandLinkButton_314")
        self.commandLinkButton_314.setFont(font1)
        self.commandLinkButton_314.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(50, 53, 65);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        #self.commandLinkButton_312.clicked.connect(self.new_donation_button)
        icon314 = QIcon()
        icon314.addFile(u":/16x16/icons/16x16/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_314.setIcon(icon314)
        self.commandLinkButton_314.clicked.connect(self.deb_voucher)
        self.gridLayout_3.addWidget(self.commandLinkButton_314, 0, 1, 1, 1)
        self.commandLinkButton_316 = QCommandLinkButton(self.expenditure_opening)
        self.commandLinkButton_316.setObjectName("commandLinkButton_314")
        self.commandLinkButton_316.setFont(font1)
        self.commandLinkButton_316.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(50, 53, 65);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        #self.commandLinkButton_312.clicked.connect(self.new_donation_button)
        icon316 = QIcon()
        icon316.addFile(u":/16x16/icons/16x16/cil-credit-card.png", QSize(), QIcon.Normal, QIcon.Off)
        self.commandLinkButton_316.setIcon(icon316)
        self.commandLinkButton_316.clicked.connect(self.add_exp_cat_page)
        self.gridLayout_3.addWidget(self.commandLinkButton_316, 0, 4, 1, 1)


        self.lcdNumber = QLCDNumber(self.expenditure_opening)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout_3.addWidget(self.lcdNumber, 2, 1, 1, 1)
        self.label_313 = QLabel(self.expenditure_opening)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_313.setFont(font)
        self.label_313.setObjectName("label_313")
        self.gridLayout_3.addWidget(self.label_313, 3, 0, 1, 1)
        self.label_312 = QLabel(self.expenditure_opening)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_312.setFont(font)
        self.label_312.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_312, 2, 0, 1, 1)
        self.label_315 = QLabel(self.expenditure_opening)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_315.setFont(font)
        self.label_315.setAlignment(Qt.AlignCenter)
        self.label_315.setObjectName("label_315")
        self.gridLayout_3.addWidget(self.label_315, 1, 0, 1, 3)
        self.verticalLayout_12.addLayout(self.gridLayout_3)
        self.verticalLayout_10.addLayout(self.verticalLayout_12)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        now = datetime.now()
        now = now.strftime('%Y-%m-%d')
        mycursor.execute("select * from pettycashbook where voucherdate = '{0}' ".format(now))
        myresult = mycursor.fetchall()
        te=0
        for x in myresult:
            te+=x[4]
        self.lcdNumber.display(te)
        today = date.today()
        yesterday = today - timedelta(days = 1)
        mycursor.execute("select * from pettycashbook where voucherdate = '{0}' ".format(yesterday))
        myresult = mycursor.fetchall()
        te=0
        for x in myresult:
            te+=x[4]
        self.lcdNumber_312.display(te)

        #day = datetime.strptime(now, '%d/%b/%Y')
        today = date.today()
        start = today - timedelta(days=today.weekday())
        
        end = start + timedelta(days=6)
        mycursor.execute("select * from pettycashbook where voucherdate between '{0}' and '{1}' ".format(start,end))
        myresult = mycursor.fetchall()
        te=0
        for x in myresult:
            te+=x[4]
        self.lcdNumber_313.display(te)

        self.stackedWidget.addWidget(self.expenditure_opening)


        self.add_user = QWidget()
        self.add_user.setObjectName(u"add_user")
        self.verticalLayout_10 = QVBoxLayout(self.add_user)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_2 = QLineEdit(self.add_user)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setFont(font7)
        self.gridLayout_3.setHorizontalSpacing(50)
        self.gridLayout_3.setVerticalSpacing(50)
        self.gridLayout_3.addWidget(self.lineEdit_2, 5, 2, 1, 1)
        self.label_5 = QLabel(self.add_user)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font7)
        self.gridLayout_3.addWidget(self.label_5, 9, 0, 1, 1)
        self.label_3 = QLabel(self.add_user)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font7)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 6, 0, 1, 1)
        self.label_4 = QLabel(self.add_user)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font7)
        self.gridLayout_3.addWidget(self.label_4, 7, 0, 1, 1)
        self.lineEdit_3 = QLineEdit(self.add_user)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_3, 5, 3, 1, 1)

        self.label_14 = QLabel(self.add_user)
        self.label_14.setObjectName("label_4")
        self.label_14.setFont(font7)
        self.gridLayout_3.addWidget(self.label_14, 8, 0, 1, 1)
        self.lineEdit_13 = QLineEdit(self.add_user)
        self.lineEdit_13.setObjectName("lineEdit_3")
        self.lineEdit_13.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_13, 8, 2, 1, 1)

        self.textEdit_au = QTextEdit(self.add_user)
        self.textEdit_au.setMaximumSize(QSize(16777215, 200))
        self.textEdit_au.setObjectName("textEdit_au")
        self.textEdit_au.setFont(font7)
        self.gridLayout_3.addWidget(self.textEdit_au, 6, 2, 1, 1)
        self.lineEdit_4 = QLineEdit(self.add_user)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_4, 7, 2, 1, 1)
        self.label_2 = QLabel(self.add_user)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font7)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 5, 0, 1, 1)
        #self.comboBox_12 = QComboBox(self.add_user)
        #self.comboBox_12.setObjectName("comboBox_12")
        #self.comboBox_12.addItem("")
        #self.comboBox_12.addItem("")
        #self.gridLayout_3.addWidget(self.comboBox_12, 9, 2, 1, 1)
        self.label_0 = QLabel(self.add_user)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_0.setFont(font7)
        self.label_0.setObjectName("label_0")
        self.gridLayout_3.addWidget(self.label_0, 10, 0, 1, 1)
        self.lineEdit_0 = QLineEdit(self.add_user)
        self.lineEdit_0.setObjectName("lineEdit_0")
        self.lineEdit_0.setMinimumSize(QSize(0,30))
        self.lineEdit_0.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_0, 10, 2, 1, 1)
        self.lineEdit_5 = QLineEdit(self.add_user)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout_3.addWidget(self.lineEdit_5, 9, 2, 1, 1)
        self.lineEdit_5.setFont(font7)
        self.label_16 = QLabel(self.add_user)
        self.label_16.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred,QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy)
        self.label_16.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(85)
        self.label_16.setFont(font)
        #self.label_16.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_16.setAutoFillBackground(False)
        self.label_16.setStyleSheet("")
        self.label_16.setScaledContents(True)
        self.label_16.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_16.setIndent(0)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 1, 2, 1, 2)
        self.verticalLayout_10.addLayout(self.gridLayout_3)
        self.pushButton_2 = QPushButton(self.page_home)
        self.pushButton_2.setObjectName("pushButton_2")
        font7 = QFont()
        font7.setFamily("Segoe UI")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.pushButton_2.setFont(font7)
        self.pushButton_2.clicked.connect(self.new_donor_save)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.verticalLayout_10.addWidget(self.pushButton_2)
        
        self.stackedWidget.addWidget(self.add_user)

       
        
        self.new_donation = QWidget()
        self.new_donation.setObjectName("new_donation")
        self.verticalLayout_10 = QVBoxLayout(self.new_donation)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label2 = QLabel(self.new_donation)
        self.label2.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label2.setFont(font)
        self.label2.setAlignment(Qt.AlignCenter|Qt.AlignTop)
        #self.label.setAlignment(Qt.AlignTop)
        self.label2.setObjectName("label2")
        self.verticalLayout_10.addWidget(self.label2)
        font7 = QFont()
        font7.setFamily("Segoe UI")
        font7.setPointSize(14)
        font7.setBold(True)
        font7.setWeight(75)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(50)
        self.gridLayout_3.setVerticalSpacing(40)
        self.lineEdit_215 = QLineEdit(self.new_donation)
        self.lineEdit_215.setObjectName("lineEdit_215")
        self.lineEdit_215.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_215, 3, 3, 1, 1)
        self.textEdit211 = QTextEdit(self.new_donation)
        self.textEdit211.setMaximumSize(QSize(16777215, 150))
        self.textEdit211.setObjectName("textEdit211")
        self.textEdit211.setFont(font7)
        self.gridLayout_3.addWidget(self.textEdit211, 5, 2, 1, 1)
        self.label_214 = QLabel(self.new_donation)
        self.label_214.setObjectName("label_214")
        self.label_214.setFont(font7)
        self.gridLayout_3.addWidget(self.label_214, 0, 0, 1, 1)
        self.label_217 = QLabel(self.new_donation)
        self.label_217.setObjectName("label_217")
        self.label_217.setFont(font7)
        self.gridLayout_3.addWidget(self.label_217, 3, 0, 1, 1)
        self.label_212 = QLabel(self.new_donation)
        self.label_212.setObjectName("label_212")
        self.label_212.setFont(font7)
        self.gridLayout_3.addWidget(self.label_212, 1, 0, 1, 1)
        self.lineEdit_212 = QLineEdit(self.new_donation)
        self.lineEdit_212.setObjectName("lineEdit_212")
        self.lineEdit_212.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_212, 1, 1, 1, 1)
        #self.lineEdit_217 = QLineEdit(self.new_donation)
        #self.lineEdit_217.setObjectName("lineEdit_217")
        #self.lineEdit_217.setFont(font7)
        #self.gridLayout_3.addWidget(self.lineEdit_217, 0, 2, 1, 1)
        self.label_213 = QLabel(self.new_donation)
        self.label_213.setObjectName("label_213")
        self.label_213.setFont(font7)
        self.gridLayout_3.addWidget(self.label_213, 2, 0, 1, 1)
        self.lineEdit_214 = QLineEdit(self.new_donation)
        self.lineEdit_214.setObjectName("lineEdit_214")
        self.lineEdit_214.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_214, 3, 1, 1, 1)
        self.lineEdit_216 = QLineEdit(self.new_donation)
        self.lineEdit_216.setObjectName("lineEdit_216")
        self.lineEdit_216.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_216, 0, 1, 1, 1)
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_215 = QLabel(self.new_donation)
        self.label_215.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_215.setObjectName("label_215")
        self.label_215.setFont(font7)
        self.horizontalLayout_13.addWidget(self.label_215)
        self.dateEdit2 = QDateEdit(self.new_donation)
        self.dateEdit2.setMinimumSize(QSize(100, 40))
        self.dateEdit2.setObjectName("dateEdit2")
        now = datetime.now()
        self.dateEdit2.setDate(now)
        #self.dateEdit.currentDateTime()
        self.horizontalLayout_13.addWidget(self.dateEdit2)
        self.gridLayout_3.addLayout(self.horizontalLayout_13, 2, 2, 1, 2)
        self.dateTimeEdit = QDateEdit(self.new_donation)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.dateTimeEdit.setDate(now)
        #self.dateTimeEdit.setTime(now)
        self.dateTimeEdit.setMinimumSize(QSize(100, 40))
        self.gridLayout_3.addWidget(self.dateTimeEdit, 2, 1, 1, 1)
        self.label_218 = QLabel(self.new_donation)
        self.label_218.setObjectName("label_218")
        self.label_218.setFont(font7)
        self.gridLayout_3.addWidget(self.label_218, 3, 2, 1, 1)
        self.label_216 = QLabel(self.new_donation)
        self.label_216.setObjectName("label_216")
        self.label_216.setFont(font7)
        self.gridLayout_3.addWidget(self.label_216, 5, 0, 1, 1)
        self.comboBox_2 = QComboBox(self.new_donation)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setFont(font7)
        self.gridLayout_3.addWidget(self.comboBox_2, 5, 1, 1, 1)
        self.label_219 = QLabel(self.new_donation)
        self.label_219.setObjectName("label_219")
        self.label_219.setFont(font7)
        self.gridLayout_3.addWidget(self.label_219, 6, 0, 1, 1)
        self.comboBox_3 = QComboBox(self.new_donation)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setFont(font7)
        self.comboBox_2.currentIndexChanged.connect(self.add_banks_in_donation)
        self.gridLayout_3.addWidget(self.comboBox_3, 6, 1, 1, 1)
        self.textEdit_212 = QTextEdit(self.new_donation)
        self.textEdit_212.setMaximumSize(QSize(16777215, 150))
        self.textEdit_212.setObjectName("textEdit_212")
        self.textEdit_212.setFont(font7)
        self.gridLayout_3.addWidget(self.textEdit_212, 6, 2, 1, 1)
        self.lineEdit_2115 = QLineEdit(self.new_donation)
        self.lineEdit_2115.setObjectName("lineEdit_2115")
        self.lineEdit_2115.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_2115, 5, 3, 1, 1)
        self.label_2110 = QLabel(self.new_donation)
        self.label_2110.setObjectName("label_2110")
        self.label_2110.setFont(font7)
        self.gridLayout_3.addWidget(self.label_2110, 7, 0, 1, 1)
        self.comboBox_4 = QComboBox(self.new_donation)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.setFont(font7)
        self.gridLayout_3.addWidget(self.comboBox_4, 7, 1, 1, 1)
        self.label_2111 = QLabel(self.new_donation)
        self.label_2111.setObjectName("label_2111")
        self.label_2111.setFont(font7)
        self.gridLayout_3.addWidget(self.label_2111, 7, 2, 1, 1)
        self.comboBox_5 = QComboBox(self.new_donation)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setFont(font7)
        self.gridLayout_3.addWidget(self.comboBox_5, 7, 3, 1, 1)
        self.label_2112 = QLabel(self.new_donation)
        self.label_2112.setObjectName("label_2112")
        self.label_2112.setFont(font7)
        #self.label_2112.setAlignment(Qt.AlignCenter)
        self.gridLayout_3.addWidget(self.label_2112, 1, 2, 1, 1)
        self.lineEdit_213 = QLineEdit(self.new_donation)
        self.lineEdit_213.setObjectName("lineEdit_213")
        self.lineEdit_213.setMinimumSize(QSize(150, 0))
        self.lineEdit_213.setFont(font7)
        self.gridLayout_3.addWidget(self.lineEdit_213, 1, 3, 1, 1)
        self.verticalLayout_12.addLayout(self.gridLayout_3)
        self.verticalLayout_10.addLayout(self.verticalLayout_12)
        self.pushButton_212 = QPushButton(self.new_donation)
        self.pushButton_212.setObjectName("pushButton_212")
        self.pushButton_212.setFont(font7)
        self.pushButton_212.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.verticalLayout_10.addWidget(self.pushButton_212)
        self.pushButton_212.clicked.connect(self.new_donation_save)
        self.stackedWidget.addWidget(self.new_donation)
        

        self.new_student = QWidget()
        self.new_student.setObjectName("new_student")
        self.verticalLayout_410 = QVBoxLayout(self.new_student)
        self.verticalLayout_410.setObjectName("verticalLayout_410")
        self.label_416 = QLabel(self.new_student)
        self.label_416.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_416.sizePolicy().hasHeightForWidth())
        self.label_416.setSizePolicy(sizePolicy)
        self.label_416.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_416.setFont(font)
        self.label_416.setCursor(QCursor(Qt.ArrowCursor))
        self.label_416.setAutoFillBackground(False)
        self.label_416.setStyleSheet("")
        self.label_416.setScaledContents(True)
        self.label_416.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_416.setIndent(0)
        self.label_416.setObjectName("label_416")
        self.verticalLayout_410.addWidget(self.label_416)
        self.gridLayout_43 = QGridLayout()
        self.gridLayout_43.setObjectName("gridLayout_43")
        self.gridLayout_43.setHorizontalSpacing(50)
        self.gridLayout_43.setVerticalSpacing(40)
        self.dateEdit4 = QDateEdit(self.new_student)
        self.dateEdit4.setObjectName("dateEdit4")
        self.gridLayout_43.addWidget(self.dateEdit4, 13, 2, 1, 1)
        #self.label_47 = QLabel(self.new_student)
        #self.label_47.setObjectName("label_47")
        #self.gridLayout_43.addWidget(self.label_47, 14, 0, 1, 1)
        #self.lineEdit_48 = QLineEdit(self.new_student)
        #self.lineEdit_48.setText("")
        #self.lineEdit_48.setObjectName("lineEdit_48")
        #self.gridLayout_43.addWidget(self.lineEdit_48, 14, 2, 1, 1)
        self.label_43 = QLabel(self.new_student)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setText("")
        self.label_43.setObjectName("label_43")
        self.gridLayout_43.addWidget(self.label_43, 20, 0, 1, 1)
        self.label_42 = QLabel(self.new_student)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.gridLayout_43.addWidget(self.label_42, 12, 0, 1, 1)
        self.lineEdit_43 = QLineEdit(self.new_student)
        self.lineEdit_43.setObjectName("lineEdit_43")
        self.gridLayout_43.addWidget(self.lineEdit_43, 12, 6, 1, 1)
        self.label4 = QLabel(self.new_student)
        self.label4.setObjectName("label4")
        self.gridLayout_43.addWidget(self.label4, 3, 0, 1, 1)
        self.label_45 = QLabel(self.new_student)
        self.label_45.setText("")
        self.label_45.setObjectName("label_45")
        self.gridLayout_43.addWidget(self.label_45, 23, 0, 1, 1)
        self.lineEdit_46 = QLineEdit(self.new_student)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.gridLayout_43.addWidget(self.lineEdit_46, 3, 2, 1, 1)
        self.lineEdit_42 = QLineEdit(self.new_student)
        self.lineEdit_42.setObjectName("lineEdit_42")
        self.gridLayout_43.addWidget(self.lineEdit_42, 12, 2, 1, 1)
        self.label_46 = QLabel(self.new_student)
        self.label_46.setObjectName("label_46")
        self.gridLayout_43.addWidget(self.label_46, 13, 0, 1, 1)
        self.label_44 = QLabel(self.new_student)
        self.label_44.setObjectName("label_44")
        self.gridLayout_43.addWidget(self.label_44, 21, 0, 1, 1)
        self.textEdit4 = QTextEdit(self.new_student)
        self.textEdit4.setMaximumSize(QSize(16777215, 300))
        self.textEdit4.setObjectName("textEdit4")
        self.gridLayout_43.addWidget(self.textEdit4, 16, 2, 1, 1)
        self.pushButton_42 = QPushButton(self.new_student)
        self.pushButton_42.setObjectName("pushButton_42")
        self.pushButton_42.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_42.clicked.connect(self.new_stud_add)
        self.gridLayout_43.addWidget(self.pushButton_42, 21, 2, 1, 1)
        self.label_48 = QLabel(self.new_student)
        self.label_48.setObjectName("label_48")
        self.gridLayout_43.addWidget(self.label_48, 16, 0, 1, 1)
        self.verticalLayout_410.addLayout(self.gridLayout_43)
        self.stackedWidget.addWidget(self.new_student)

        self.deb_voucher = QWidget()
        self.deb_voucher.setObjectName("deb_voucher")
        self.verticalLayout_510 = QVBoxLayout(self.deb_voucher)
        self.verticalLayout_510.setObjectName("verticalLayout_10")
        self.gridLayout_53 = QGridLayout()
        self.gridLayout_53.setObjectName("gridLayout_53")
        self.gridLayout_53.setHorizontalSpacing(30)
        self.gridLayout_53.setVerticalSpacing(40)
        self.lineEdit_57 = QLineEdit(self.deb_voucher)
        self.lineEdit_57.setObjectName("lineEdit_57")
        self.lineEdit_57.setMinimumSize(QSize(0, 30))
        self.gridLayout_53.addWidget(self.lineEdit_57, 10, 1, 1, 1)
        self.lineEdit_54 = QLineEdit(self.deb_voucher)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_54.setMinimumSize(QSize(0, 30))
        self.gridLayout_53.addWidget(self.lineEdit_54, 8, 1, 1, 1)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_55 = QLabel(self.deb_voucher)
        self.label_55.setObjectName("label_55")
        self.label_55.setFont(font)
        self.gridLayout_53.addWidget(self.label_55, 7, 0, 1, 1)
        self.dateEdit5 = QDateEdit(self.deb_voucher)
        self.dateEdit5.setObjectName("dateEdit5")
        #self.dateEdit5.setMinimumSize(QSize(40, 30))
        self.gridLayout_53.addWidget(self.dateEdit5, 3, 3, 1, 1)
        self.label_54 = QLabel(self.deb_voucher)
        self.label_54.setObjectName("label_4")
        self.label_54.setFont(font)
        self.gridLayout_53.addWidget(self.label_54, 8, 0, 1, 1)
        self.lineEdit_56 = QLineEdit(self.deb_voucher)
        self.lineEdit_56.setObjectName("lineEdit_56")
        self.lineEdit_56.setMinimumSize(QSize(0, 30))
        self.gridLayout_53.addWidget(self.lineEdit_56, 2, 1, 1, 1)
        self.lineEdit_52 = QLineEdit(self.deb_voucher)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_52.setMinimumSize(QSize(0, 30))
        self.gridLayout_53.addWidget(self.lineEdit_52, 5, 1, 1, 1)
        self.horizontalLayout_518 = QHBoxLayout()
        self.horizontalLayout_518.setObjectName("horizontalLayout_18")
        self.label = QLabel(self.deb_voucher)
        self.label.setObjectName("label")
        self.horizontalLayout_518.addWidget(self.label)
        self.gridLayout_53.addLayout(self.horizontalLayout_518, 6, 0, 1, 1)
        self.label_516 = QLabel(self.deb_voucher)
        self.label_516.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_516.sizePolicy().hasHeightForWidth())
        self.label_516.setSizePolicy(sizePolicy)
        self.label_516.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_516.setFont(font)
        self.label_516.setCursor(QCursor(Qt.ArrowCursor))
        self.label_516.setAutoFillBackground(False)
        self.label_516.setStyleSheet("")
        self.label_516.setScaledContents(True)
        self.label_516.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_516.setIndent(0)
        self.label_516.setObjectName("label_516")
        self.gridLayout_53.addWidget(self.label_516, 1, 0, 1, 4)
        self.label_52 = QLabel(self.deb_voucher)
        self.label_52.setFont(font)
        self.label_52.setObjectName("label_52")
        self.gridLayout_53.addWidget(self.label_52, 5, 0, 1, 1)
        self.lineEdit_55 = QLineEdit(self.deb_voucher)
        self.lineEdit_55.setObjectName("lineEdit_55")
        self.lineEdit_55.setMinimumSize(QSize(0, 30))
        self.gridLayout_53.addWidget(self.lineEdit_55, 9, 1, 1, 1)
        self.label_56 = QLabel(self.deb_voucher)
        self.label_56.setObjectName("label_56")
        self.label_56.setFont(font)
        self.gridLayout_53.addWidget(self.label_56, 8, 2, 1, 1)
        self.lineEdit_53 = QLineEdit(self.deb_voucher)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_53.setMinimumSize(QSize(0, 30))
        self.gridLayout_53.addWidget(self.lineEdit_53, 6, 1, 1, 1)
        self.label_57 = QLabel(self.deb_voucher)
        self.label_57.setObjectName("label_57")
        self.label_57.setFont(font)
        self.gridLayout_53.addWidget(self.label_57, 9, 0, 1, 1)
        self.dateEdit_52 = QDateEdit(self.deb_voucher)
        self.dateEdit_52.setObjectName("dateEdit_52")
        #self.dateEdit_52.setMinimumSize(QSize(40, 30))
        self.gridLayout_53.addWidget(self.dateEdit_52, 8, 3, 1, 1)
        self.comboBox_52 = QComboBox(self.deb_voucher)
        self.comboBox_52.setObjectName("comboBox_52")
        self.comboBox_52.setMinimumSize(QSize(0, 30))
        self.comboBox_52.setFont(font)
        self.gridLayout_53.addWidget(self.comboBox_52, 7, 1, 1, 1)
        self.radioButton_52 = QRadioButton(self.deb_voucher)
        self.radioButton_52.setObjectName("radioButton_52")
        self.gridLayout_53.addWidget(self.radioButton_52, 10, 2, 1, 1)
        self.label_58 = QLabel(self.deb_voucher)
        self.label_58.setObjectName("label_58")
        self.label_58.setFont(font)
        self.gridLayout_53.addWidget(self.label_58, 2, 0, 1, 1)
        self.label_59 = QLabel(self.deb_voucher)
        self.label_59.setObjectName("label_59")
        self.label_59.setFont(font)
        self.gridLayout_53.addWidget(self.label_59, 10, 0, 1, 1)
        self.label_53 = QLabel(self.deb_voucher)
        self.label_53.setObjectName("label_53")
        self.label_53.setFont(font)
        self.gridLayout_53.addWidget(self.label_53, 3, 2, 1, 1)
        self.label_510 = QLabel(self.deb_voucher)
        self.label_510.setObjectName("label_510")
        self.label_510.setFont(font)
        self.gridLayout_53.addWidget(self.label_510, 9, 2, 1, 1)
        self.dateEdit_53 = QDateEdit(self.deb_voucher)
        self.dateEdit_53.setObjectName("dateEdit_53")
        #self.dateEdit_53.setMinimumSize(QSize(40, 30))
        self.gridLayout_53.addWidget(self.dateEdit_53, 9, 3, 1, 1)
        self.verticalLayout_510.addLayout(self.gridLayout_53)
        self.pushButton_52 = QPushButton(self.deb_voucher)
        self.pushButton_52.setObjectName("pushButton_52")
        self.pushButton_52.setMinimumSize(QSize(0, 30))
        self.pushButton_52.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")     
        self.pushButton_52.clicked.connect(self.add_expenditure)
        self.verticalLayout_510.addWidget(self.pushButton_52)
        self.stackedWidget.addWidget(self.deb_voucher)

        
        self.update_stud = QWidget()
        self.update_stud.setObjectName("update_stud")
        self.verticalLayout_710 = QVBoxLayout(self.update_stud)
        self.verticalLayout_710.setObjectName("verticalLayout_710")
        self.gridLayout_73 = QGridLayout()
        self.gridLayout_73.setObjectName("gridLayout_73")
        self.gridLayout_73.setHorizontalSpacing(30)
        self.gridLayout_73.setVerticalSpacing(40)
        self.label_73 = QLabel(self.update_stud)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_73.setFont(font)
        self.label_73.setObjectName("label_73")
        self.gridLayout_73.addWidget(self.label_73, 7, 0, 1, 1)
        self.label_711 = QLabel(self.update_stud)
        self.label_711.setObjectName("label_711")
        self.gridLayout_73.addWidget(self.label_711, 10, 0, 1, 1)
        self.label_712 = QLabel(self.update_stud)
        self.label_712.setObjectName("label_712")
        self.gridLayout_73.addWidget(self.label_712, 8, 0, 1, 1)
        self.label_79 = QLabel(self.update_stud)
        self.label_79.setObjectName("label_79")
        self.gridLayout_73.addWidget(self.label_79, 2, 0, 1, 1)
        self.lineEdit_77 = QLineEdit(self.update_stud)
        self.lineEdit_77.setObjectName("lineEdit_77")
        self.lineEdit_77.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_77, 10, 1, 1, 1)
        self.textEdit7 = QTextEdit(self.update_stud)
        self.textEdit7.setMaximumSize(QSize(16777215, 300))
        self.textEdit7.setObjectName("textEdit7")
        self.gridLayout_73.addWidget(self.textEdit7, 7, 1, 1, 2)
        self.lineEdit_78 = QLineEdit(self.update_stud)
        self.lineEdit_78.setObjectName("lineEdit_78")
        self.lineEdit_78.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_78, 8, 1, 1, 1)
        self.label_74 = QLabel(self.update_stud)
        self.label_74.setObjectName("label_74")
        self.gridLayout_73.addWidget(self.label_74, 9, 0, 1, 1)
        self.lineEdit_72 = QLineEdit(self.update_stud)
        self.lineEdit_72.setObjectName("lineEdit_72")
        self.lineEdit_72.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_72, 5, 1, 1, 1)
        self.lineEdit_76 = QLineEdit(self.update_stud)
        self.lineEdit_76.setObjectName("lineEdit_76")
        self.lineEdit_76.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_76, 9, 3, 1, 1)
        self.pushButton7 = QPushButton(self.update_stud)
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setMinimumSize(QSize(100, 30))
        self.pushButton7.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton7.clicked.connect(self.get_stud_details)
        self.gridLayout_73.addWidget(self.pushButton7, 2, 2, 1, 1)
        self.label_716 = QLabel(self.update_stud)
        self.label_716.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_716.sizePolicy().hasHeightForWidth())
        self.label_716.setSizePolicy(sizePolicy)
        self.label_716.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_716.setFont(font)
        self.label_716.setCursor(QCursor(Qt.ArrowCursor))
        self.label_716.setAutoFillBackground(False)
        self.label_716.setStyleSheet("")
        self.label_716.setScaledContents(True)
        self.label_716.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_716.setIndent(0)
        self.label_716.setObjectName("label_716")
        self.gridLayout_73.addWidget(self.label_716, 1, 0, 1, 4)
        self.lineEdit_73 = QLineEdit(self.update_stud)
        self.lineEdit_73.setObjectName("lineEdit_73")
        self.lineEdit_73.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_73, 5, 2, 1, 1)
        self.label_75 = QLabel(self.update_stud)
        self.label_75.setObjectName("label_75")
        self.gridLayout_73.addWidget(self.label_75, 6, 0, 1, 1)
        self.lineEdit_75 = QLineEdit(self.update_stud)
        self.lineEdit_75.setObjectName("lineEdit_75")
        self.lineEdit_75.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_75, 9, 1, 1, 1)
        self.label_710 = QLabel(self.update_stud)
        self.label_710.setObjectName("label_710")
        self.gridLayout_73.addWidget(self.label_710, 9, 2, 1, 1)
        self.lineEdit_74 = QLineEdit(self.update_stud)
        self.lineEdit_74.setObjectName("lineEdit_74")
        self.lineEdit_74.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_74, 6, 1, 1, 2)
        self.lineEdit7 = QLineEdit(self.update_stud)
        self.lineEdit7.setObjectName("lineEdit7")
        self.lineEdit7.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit7, 2, 1, 1, 1)
        self.label_72 = QLabel(self.update_stud)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_72.setFont(font)
        self.label_72.setObjectName("label_72")
        self.gridLayout_73.addWidget(self.label_72, 5, 0, 1, 1)
        self.label_713 = QLabel(self.update_stud)
        self.label_713.setObjectName("label_713")
        self.label_713.setFont(font)
        self.gridLayout_73.addWidget(self.label_713, 8, 2, 1, 1)
        self.lineEdit_79 = QLineEdit(self.update_stud)
        self.lineEdit_79.setObjectName("lineEdit_79")
        self.lineEdit_79.setMinimumSize(QSize(100, 30))
        self.gridLayout_73.addWidget(self.lineEdit_79, 8, 3, 1, 1)
        self.pushButton78 = QPushButton(self.update_stud)
        self.pushButton78.setObjectName("pushButton78")
        self.pushButton78.setMinimumSize(QSize(100, 30))
        self.pushButton78.setFont(font)
        self.pushButton78.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton78.clicked.connect(self.update_details_button)
        self.gridLayout_73.addWidget(self.pushButton78, 10, 3, 1, 1)
        self.verticalLayout_710.addLayout(self.gridLayout_73)
        self.stackedWidget.addWidget(self.update_stud)
        
        self.cashbook = QWidget()
        self.cashbook.setObjectName("cashbook")
        self.verticalLayout_66 = QVBoxLayout(self.cashbook)
        self.verticalLayout_66.setObjectName("verticalLayout_66")
        self.frame = QFrame(self.cashbook)
        self.frame.setStyleSheet("border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_615 = QVBoxLayout(self.frame)
        self.verticalLayout_615.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_615.setSpacing(0)
        self.verticalLayout_615.setObjectName("verticalLayout_615")
        self.frame_div_content_61 = QFrame(self.frame)
        self.frame_div_content_61.setMinimumSize(QSize(0, 110))
        self.frame_div_content_61.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_61.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_61.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_61.setFrameShadow(QFrame.Raised)
        self.frame_div_content_61.setObjectName("frame_div_content_61")
        self.verticalLayout_67 = QVBoxLayout(self.frame_div_content_61)
        self.verticalLayout_67.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_67.setSpacing(0)
        self.verticalLayout_67.setObjectName("verticalLayout_67")
        self.frame_title_wid_61 =QFrame(self.frame_div_content_61)
        self.frame_title_wid_61.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_61.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_61.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_61.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_61.setObjectName("frame_title_wid_61")
        self.verticalLayout_68 = QVBoxLayout(self.frame_title_wid_61)
        self.verticalLayout_68.setObjectName("verticalLayout_68")
        self.labelBoxBlenderInstalation6 = QLabel(self.frame_title_wid_61)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation6.setFont(font)
        self.labelBoxBlenderInstalation6.setStyleSheet("")
        self.labelBoxBlenderInstalation6.setAlignment(Qt.AlignCenter)
        self.labelBoxBlenderInstalation6.setObjectName("labelBoxBlenderInstalation6")
        self.verticalLayout_68.addWidget(self.labelBoxBlenderInstalation6)
        self.verticalLayout_67.addWidget(self.frame_title_wid_61)
        self.frame_content_wid_61 = QFrame(self.frame_div_content_61)
        self.frame_content_wid_61.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_61.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_61.setObjectName("frame_content_wid_61")
        self.horizontalLayout_69 = QHBoxLayout(self.frame_content_wid_61)
        self.horizontalLayout_69.setObjectName("horizontalLayout_69")
        self.label_62 = QLabel(self.frame_content_wid_61)
        self.label_62.setObjectName("label_62")
        self.label_62.setFont(font)
        self.horizontalLayout_69.addWidget(self.label_62)
        self.dateEdit_62 = QDateEdit(self.frame_content_wid_61)
        self.dateEdit_62.setObjectName("dateEdit_62")
        self.horizontalLayout_69.addWidget(self.dateEdit_62)
        self.label_63 = QLabel(self.frame_content_wid_61)
        self.label_63.setObjectName("label_63")
        self.label_63.setFont(font)
        self.horizontalLayout_69.addWidget(self.label_63)
        self.dateEdit = QDateEdit(self.frame_content_wid_61)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_69.addWidget(self.dateEdit)
        self.comboBox6 = QComboBox(self.frame_content_wid_61)
        self.comboBox6.setObjectName("comboBox6")
        self.comboBox6.addItem("Petty Cashbook")
        self.comboBox6.addItem("Main Cashbook")
        self.comboBox6.setFont(font)
        self.comboBox6.currentIndexChanged.connect(self.cashbookselection)
        now = datetime.now()
        self.dateEdit_62.setDate(now)
        self.dateEdit_62.setMinimumSize(QSize(0, 30))
        self.dateEdit.setDate(now)
        self.horizontalLayout_69.addWidget(self.comboBox6)
        self.pushButton6 = QPushButton(self.frame_content_wid_61)
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setFont(font)
        self.pushButton6.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton6.setFont(font)
        self.pushButton6.clicked.connect(self.get_cashbook_details)
        self.horizontalLayout_69.addWidget(self.pushButton6)
        self.verticalLayout_67.addWidget(self.frame_content_wid_61)
        self.verticalLayout_615.addWidget(self.frame_div_content_61)
        self.verticalLayout_66.addWidget(self.frame)
        self.frame_63 = QFrame(self.cashbook)
        self.frame_63.setMinimumSize(QSize(0, 100))
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.frame_63.setObjectName("frame_63")
        self.horizontalLayout_612 = QHBoxLayout(self.frame_63)
        self.horizontalLayout_612.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_612.setSpacing(0)
        self.horizontalLayout_612.setObjectName("horizontalLayout_612")
        self.frame_62 = QFrame(self.frame_63)
        self.frame_62.setMinimumSize(QSize(0, 150))
        self.frame_62.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.frame_62.setObjectName("frame_62")
        self.verticalLayout_611 = QVBoxLayout(self.frame_62)
        self.verticalLayout_611.setObjectName("verticalLayout_611")
        self.label_64 = QLabel(self.frame_62)
        self.label_64.setFont(font)
        self.label_64.setObjectName("label_64")
        self.verticalLayout_611.addWidget(self.label_64)
        self.tableWidget6 = QTableWidget(self.frame_62)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget6.sizePolicy().hasHeightForWidth())
        self.tableWidget6.setSizePolicy(sizePolicy)
        self.tableWidget6.setPalette(palette)
        self.tableWidget6.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        self.tableWidget6.setFrameShape(QFrame.NoFrame)
        self.tableWidget6.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget6.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableWidget6.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget6.setAlternatingRowColors(False)
        self.tableWidget6.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget6.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget6.setShowGrid(True)
        self.tableWidget6.setGridStyle(Qt.SolidLine)
        self.tableWidget6.setObjectName("tableWidget6")
        self.tableWidget6.setColumnCount(5)
        self.tableWidget6.setRowCount(2)
        item = QTableWidgetItem()
        self.tableWidget6.setVerticalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget6.setVerticalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableWidget6.setHorizontalHeaderItem(4, item)
        self.tableWidget6.horizontalHeader().setVisible(True)
        self.tableWidget6.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget6.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget6.horizontalHeader().setStretchLastSection(True)
        self.tableWidget6.verticalHeader().setVisible(False)
        self.tableWidget6.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget6.verticalHeader().setHighlightSections(False)
        self.tableWidget6.verticalHeader().setStretchLastSection(True)
        self.verticalLayout_611.addWidget(self.tableWidget6)
        self.gridLayout6 = QGridLayout()
        self.gridLayout6.setObjectName("gridLayout6")
        self.label_68 = QLabel(self.frame_62)
        self.label_68.setObjectName("label_68")
        self.gridLayout6.addWidget(self.label_68, 1, 0, 1, 1)
        self.label_65 = QLabel(self.frame_62)
        self.label_65.setObjectName("label_65")
        self.gridLayout6.addWidget(self.label_65, 0, 0, 1, 1)
        self.lcdNumber = QLCDNumber(self.frame_62)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout6.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.lcdNumber_62 = QLCDNumber(self.frame_62)
        self.lcdNumber_62.setObjectName("lcdNumber_62")
        self.gridLayout6.addWidget(self.lcdNumber_62, 1, 1, 1, 1)
        self.verticalLayout_611.addLayout(self.gridLayout6)
        self.horizontalLayout_611 = QHBoxLayout(self.cashbook)
        self.verticalLayout_611.addLayout(self.horizontalLayout_611)
        self.horizontalLayout_612.addWidget(self.frame_62)
        self.verticalLayout_66.addWidget(self.frame_63)
        self.stackedWidget.addWidget(self.cashbook)

        self.new_user = QWidget()
        self.new_user.setObjectName("new_user")
        self.verticalLayout_810 = QVBoxLayout(self.new_user)
        self.verticalLayout_810.setObjectName("verticalLayout_810")
        self.verticalLayout_88 = QVBoxLayout()
        self.verticalLayout_88.setObjectName("verticalLayout_88")
        self.label_87 = QLabel(self.new_user)
        self.label_87.setMaximumSize(QSize(16777215, 100))
        self.label_87.setMinimumSize(QSize(16777215, 100))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_87.setFont(font)
        self.label_87.setAlignment(Qt.AlignCenter)
        self.label_87.setObjectName("label_87")
        self.verticalLayout_88.addWidget(self.label_87)
        self.gridLayout_83 = QGridLayout()
        self.gridLayout_83.setObjectName("gridLayout_83")
        self.gridLayout_83.setHorizontalSpacing(30)
        self.gridLayout_83.setVerticalSpacing(40)
        self.label_813 = QLabel(self.new_user)
        self.label_813.setObjectName("label_813")
        self.gridLayout_83.addWidget(self.label_813, 1, 4, 1, 1)
        self.horizontalLayout_811 = QHBoxLayout()
        self.horizontalLayout_811.setObjectName("horizontalLayout_811")
        self.radioButton_82 = QRadioButton(self.new_user)
        self.radioButton_82.setObjectName("radioButton_82")
        self.horizontalLayout_811.addWidget(self.radioButton_82)
        self.label_814 = QLabel(self.new_user)
        self.label_814.setObjectName("label_813")
        self.gridLayout_83.addWidget(self.label_814, 4, 4, 1, 1)
        self.lineEdit_87 = QLineEdit(self.new_user)
        self.lineEdit_87.setObjectName("lineEdit_87")
        self.lineEdit_87.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit_87, 4, 5, 1, 1)
        self.radioButton8 = QRadioButton(self.new_user)
        self.radioButton8.setObjectName("radioButton8")
        self.horizontalLayout_811.addWidget(self.radioButton8)
        self.gridLayout_83.addLayout(self.horizontalLayout_811, 3, 5, 1, 1)
        self.label_810 = QLabel(self.new_user)
        self.label_810.setObjectName("label_810")
        self.gridLayout_83.addWidget(self.label_810, 1, 0, 1, 1)
        self.label_812 = QLabel(self.new_user)
        self.label_812.setObjectName("label_812")
        self.gridLayout_83.addWidget(self.label_812, 4, 0, 1, 1)
        self.lineEdit8 = QLineEdit(self.new_user)
        self.lineEdit8.setObjectName("lineEdit8")
        self.lineEdit8.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit8, 0, 2, 1, 1)
        self.label_89 = QLabel(self.new_user)
        self.label_89.setObjectName("label_89")
        self.gridLayout_83.addWidget(self.label_89, 0, 4, 1, 1)
        self.lineEdit_84 = QLineEdit(self.new_user)
        self.lineEdit_84.setObjectName("lineEdit_84")
        self.lineEdit_84.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit_84, 3, 2, 1, 1)
        self.label_88 = QLabel(self.new_user)
        self.label_88.setObjectName("label_88")
        self.gridLayout_83.addWidget(self.label_88, 0, 0, 1, 1)
        self.label_811 = QLabel(self.new_user)
        self.label_811.setObjectName("label_811")
        self.gridLayout_83.addWidget(self.label_811, 3, 0, 1, 1)
        self.lineEdit_83 = QLineEdit(self.new_user)
        self.lineEdit_83.setObjectName("lineEdit_83")
        self.lineEdit_83.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit_83, 1, 2, 1, 1)
        self.lineEdit_86 = QLineEdit(self.new_user)
        self.lineEdit_86.setObjectName("lineEdit_86")
        self.lineEdit_86.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit_86, 4, 2, 1, 1)
        self.lineEdit_85 = QLineEdit(self.new_user)
        self.lineEdit_85.setObjectName("lineEdit_85")
        self.lineEdit_85.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit_85, 1, 5, 1, 1)
        self.lineEdit_82 = QLineEdit(self.new_user)
        self.lineEdit_82.setObjectName("lineEdit_82")
        self.lineEdit_82.setMinimumSize(QSize(0, 30))
        self.gridLayout_83.addWidget(self.lineEdit_82, 0, 5, 1, 1)
        self.pushButton_82 = QPushButton(self.new_user)
        self.pushButton_82.setObjectName("pushButton_82")
        self.pushButton_82.setMinimumSize(QSize(0, 30))
        self.pushButton_82.clicked.connect(self.new_user_func)
        self.pushButton_82.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.gridLayout_83.addWidget(self.pushButton_82, 5, 5, 1, 1)
        self.verticalLayout_88.addLayout(self.gridLayout_83)
        self.verticalLayout_810.addLayout(self.verticalLayout_88)
        self.stackedWidget.addWidget(self.new_user)

        self.d_analysis = QWidget()
        self.d_analysis.setObjectName("d_analysis")
        self.verticalLayout_910 = QVBoxLayout(self.d_analysis)
        self.verticalLayout_910.setObjectName("verticalLayout_910")
        self.verticalLayout_912 = QVBoxLayout()
        self.verticalLayout_912.setObjectName("verticalLayout_912")
        self.label9 = QLabel(self.d_analysis)
        self.label9.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label9.setFont(font)
        self.label9.setAlignment(Qt.AlignCenter)
        self.label9.setObjectName("label9")
        self.verticalLayout_912.addWidget(self.label9)
        self.gridLayout_93 = QGridLayout()
        self.gridLayout_93.setObjectName("gridLayout_93")
        self.gridLayout_93.setHorizontalSpacing(30)
        self.gridLayout_93.setVerticalSpacing(40)
        self.pushButton_92 = QPushButton(self.d_analysis)
        self.pushButton_92.setObjectName("pushButton_92")
        self.pushButton_92.setMinimumSize(QSize(16777215, 30))
        self.pushButton_92.clicked.connect(self.alldonations)
        self.pushButton_92.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.gridLayout_93.addWidget(self.pushButton_92, 1, 1, 1, 1)
        self.dateEdit9 = QDateEdit(self.d_analysis)
        self.dateEdit9.setObjectName("dateEdit9")
        self.dateEdit9.setMinimumSize(QSize(0, 30))
        now = datetime.now()
        self.dateEdit9.setDate(now)
        self.gridLayout_93.addWidget(self.dateEdit9, 0, 1, 1, 1)
        self.dateEdit_92 = QDateEdit(self.d_analysis)
        self.dateEdit_92.setObjectName("dateEdit_92")
        now = datetime.now()
        self.dateEdit_92.setDate(now)
        self.dateEdit_92.setMinimumSize(QSize(0, 30))
        self.gridLayout_93.addWidget(self.dateEdit_92, 0, 3, 1, 1)
        self.label_92 = QLabel(self.d_analysis)
        self.label_92.setObjectName("label_92")
        self.gridLayout_93.addWidget(self.label_92, 0, 0, 1, 1)
        self.label_93 = QLabel(self.d_analysis)
        self.label_93.setObjectName("label_93")
        self.gridLayout_93.addWidget(self.label_93, 0, 2, 1, 1)
        self.pushButton_93 = QPushButton(self.d_analysis)
        self.pushButton_93.setObjectName("pushButton_93")
        self.pushButton_93.clicked.connect(self.donation_analysis)
        self.pushButton_93.setMinimumSize(QSize(16777215, 30))
        self.pushButton_93.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.gridLayout_93.addWidget(self.pushButton_93, 1, 2, 1, 1)
        self.pushButton_94 = QPushButton(self.d_analysis)
        self.pushButton_94.setObjectName("pushButton_93")
        self.pushButton_94.clicked.connect(self.generate_donation_pdf)
        self.pushButton_94.setMinimumSize(QSize(16777215, 30))
        self.pushButton_94.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.gridLayout_93.addWidget(self.pushButton_94, 1, 3, 1, 1)
        self.verticalLayout_912.addLayout(self.gridLayout_93)
        self.verticalLayout_910.addLayout(self.verticalLayout_912)
        self.label_94 = QLabel(self.d_analysis)
        self.label_94.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_94.setFont(font)
        self.label_94.setObjectName("label_94")
        self.verticalLayout_910.addWidget(self.label_94)
        self.widget9 = QWidget(self.d_analysis)
        self.widget9.setMinimumSize(QSize(0, 350))
        self.widget9.setObjectName("widget9")
        self.verticalLayout_991 = QVBoxLayout(self.widget9)
        self.verticalLayout_991.setObjectName("verticalLayout_991")
        self.verticalLayout_910.addWidget(self.widget9)
        self.horizontalLayout_913 = QHBoxLayout()
        self.horizontalLayout_913.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_913.setObjectName("horizontalLayout_13")
        self.label_95 = QLabel(self.d_analysis)
        self.label_95.setMaximumSize(QSize(16777215, 20))
        self.label_95.setObjectName("label_95")
        self.horizontalLayout_913.addWidget(self.label_95)
        self.lcdNumber9 = QLCDNumber(self.d_analysis)
        self.lcdNumber9.setObjectName("lcdNumber9")
        self.horizontalLayout_913.addWidget(self.lcdNumber9)
        self.verticalLayout_910.addLayout(self.horizontalLayout_913)
        self.stackedWidget.addWidget(self.d_analysis)


        self.exp_analysis = QWidget()
        self.exp_analysis.setObjectName("exp_analysis")
        self.verticalLayout_1010 = QVBoxLayout(self.exp_analysis)
        self.verticalLayout_1010.setObjectName("verticalLayout_1010")
        self.verticalLayout_1012 = QVBoxLayout()
        self.verticalLayout_1012.setObjectName("verticalLayout_1012")
        self.label10 = QLabel(self.exp_analysis)
        self.label10.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label10.setFont(font)
        self.label10.setAlignment(Qt.AlignCenter)
        self.label10.setObjectName("label10")
        self.verticalLayout_1012.addWidget(self.label10)
        self.gridLayout_103 = QGridLayout()
        self.gridLayout_103.setObjectName("gridLayout_103")
        self.gridLayout_103.setHorizontalSpacing(30)
        self.gridLayout_103.setVerticalSpacing(40)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_102 = QPushButton(self.exp_analysis)
        self.pushButton_102.setObjectName("pushButton_102")
        self.pushButton_102.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_102.setFont(font)
        self.pushButton_102.clicked.connect(self.get_exp_butn)
        self.gridLayout_103.addWidget(self.pushButton_102, 1, 1, 1, 1)
        self.pushButton_106 = QPushButton(self.exp_analysis)
        self.pushButton_106.setObjectName("pushButton_106")
        self.pushButton_106.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_106.setFont(font)
        self.pushButton_106.clicked.connect(self.get_exp_pdf)
        self.gridLayout_103.addWidget(self.pushButton_106, 1, 3, 1, 1)
        self.dateEdit102 = QDateEdit(self.exp_analysis)
        self.dateEdit102.setObjectName("dateEdit102")
        now = datetime.now()
        self.dateEdit102.setDate(now)
        self.gridLayout_103.addWidget(self.dateEdit102, 0, 1, 1, 1)
        self.dateEdit_102 = QDateEdit(self.exp_analysis)
        self.dateEdit_102.setObjectName("dateEdit_102")
        self.dateEdit_102.setDate(now)
        #self.dateEdit_102.setMinimumSize(QSize(0, 30))
        self.gridLayout_103.addWidget(self.dateEdit_102, 0, 3, 1, 1)
        self.label_102 = QLabel(self.exp_analysis)
        self.label_102.setObjectName("label_102")
        self.label_102.setFont(font)
        self.gridLayout_103.addWidget(self.label_102, 0, 0, 1, 1)
        self.label_103 = QLabel(self.exp_analysis)
        self.label_103.setObjectName("label_103")
        self.label_103.setFont(font)
        self.gridLayout_103.addWidget(self.label_103, 0, 2, 1, 1)
        self.pushButton_103 = QPushButton(self.exp_analysis)
        self.pushButton_103.setObjectName("pushButton_103")
        self.pushButton_103.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_103.setFont(font)
        self.pushButton_103.clicked.connect(self.exp_analysisbutton)
        self.gridLayout_103.addWidget(self.pushButton_103, 1, 2, 1, 1)
        self.verticalLayout_1012.addLayout(self.gridLayout_103)
        self.verticalLayout_1010.addLayout(self.verticalLayout_1012)
        self.label_104 = QLabel(self.exp_analysis)
        self.label_104.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_104.setFont(font)
        self.label_104.setText("")
        self.label_104.setObjectName("label_104")
        self.verticalLayout_1010.addWidget(self.label_104)
        self.widget10 = QWidget(self.exp_analysis)
        self.widget10.setMinimumSize(QSize(0, 350))
        self.widget10.setObjectName("widget10")
        self.horizontalLayout_1014 = QHBoxLayout(self.widget10)
        self.horizontalLayout_1014.setObjectName("horizontalLayout_1014")
        self.verticalLayout_1010.addWidget(self.widget10)
        self.horizontalLayout_1013 = QHBoxLayout()
        self.horizontalLayout_1013.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_1013.setObjectName("horizontalLayout_1013")
        self.label_105 = QLabel(self.exp_analysis)
        self.label_105.setMaximumSize(QSize(16777215, 20))
        self.label_105.setObjectName("label_105")
        self.label_105.setFont(font)
        self.horizontalLayout_1013.addWidget(self.label_105)
        self.lcdNumber10 = QLCDNumber(self.exp_analysis)
        self.lcdNumber10.setObjectName("lcdNumber10")
        self.horizontalLayout_1013.addWidget(self.lcdNumber10)
        self.verticalLayout_1010.addLayout(self.horizontalLayout_1013)
        self.horizontalLayout_1015 = QHBoxLayout()
        self.horizontalLayout_1015.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_1015.setObjectName("horizontalLayout_1015")
        self.pushButton_104 = QPushButton(self.exp_analysis)
        self.pushButton_104.setObjectName("pushButton_104")
        self.pushButton_104.clicked.connect(self.open_new_student)
        self.pushButton_104.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_104.setFont(font)
        self.horizontalLayout_1015.addWidget(self.pushButton_104)
        self.pushButton_105 = QPushButton(self.exp_analysis)
        self.pushButton_105.setObjectName("pushButton_105")
        self.pushButton_105.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_105.setFont(font)
        self.pushButton_105.clicked.connect(self.update_stud_details)
        self.horizontalLayout_1015.addWidget(self.pushButton_105)
        self.verticalLayout_1010.addLayout(self.horizontalLayout_1015)
        self.stackedWidget.addWidget(self.exp_analysis)


        self.donation_remainder = QWidget()
        self.donation_remainder.setObjectName("donation_remainder")
        self.verticalLayout_1210 = QVBoxLayout(self.donation_remainder)
        self.verticalLayout_1210.setObjectName("verticalLayout_1210")
        self.verticalLayout_1212 = QVBoxLayout()
        self.verticalLayout_1212.setObjectName("verticalLayout_1212")
        self.label12 = QLabel(self.donation_remainder)
        self.label12.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label12.setFont(font)
        self.label12.setAlignment(Qt.AlignCenter)
        self.label12.setObjectName("label")
        self.verticalLayout_1212.addWidget(self.label12)
        self.verticalLayout_1210.addLayout(self.verticalLayout_1212)
        self.widget12 = QWidget(self.donation_remainder)
        self.widget12.setMinimumSize(QSize(0, 350))
        self.widget12.setObjectName("widget12")
        self.verticalLayout_121212 = QVBoxLayout(self.widget12)
        self.verticalLayout_121212.setObjectName("verticalLayout_121212")
        self.verticalLayout_1210.addWidget(self.widget12)
        self.horizontalLayout_1213 = QHBoxLayout()
        self.horizontalLayout_1213.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_1213.setObjectName("horizontalLayout_1213")
        self.pushButton_122 = QPushButton(self.donation_remainder)
        self.pushButton_122.setMinimumSize(QSize(0, 40))
        self.pushButton_122.setObjectName("pushButton_122")
        self.pushButton_122.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_122.clicked.connect(self.reminded)
        self.horizontalLayout_1213.addWidget(self.pushButton_122)
        self.pushButton_123 = QPushButton(self.donation_remainder)
        self.pushButton_123.setMinimumSize(QSize(0, 40))
        self.pushButton_123.setObjectName("pushButton_122")
        self.pushButton_123.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_123.clicked.connect(self.mailing_list)
        self.horizontalLayout_1213.addWidget(self.pushButton_123)
        self.verticalLayout_1210.addLayout(self.horizontalLayout_1213)
        self.stackedWidget.addWidget(self.donation_remainder)

        self.exp_confirmation_page = QWidget()
        self.exp_confirmation_page.setObjectName("exp_confirmation_page")
        self.verticalLayout_116 = QVBoxLayout(self.exp_confirmation_page)
        self.verticalLayout_116.setObjectName("verticalLayout_116")
        self.frame = QFrame(self.exp_confirmation_page)
        self.frame.setStyleSheet("border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_1115 = QVBoxLayout(self.frame)
        self.verticalLayout_1115.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1115.setSpacing(0)
        self.verticalLayout_1115.setObjectName("verticalLayout_1115")
        self.frame_div_content_111 = QFrame(self.frame)
        self.frame_div_content_111.setMinimumSize(QSize(0, 110))
        self.frame_div_content_111.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_111.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_111.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_111.setFrameShadow(QFrame.Raised)
        self.frame_div_content_111.setObjectName("frame_div_content_111")
        self.verticalLayout_117 = QVBoxLayout(self.frame_div_content_111)
        self.verticalLayout_117.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_117.setSpacing(0)
        self.verticalLayout_117.setObjectName("verticalLayout_117")
        self.frame_title_wid_111 = QFrame(self.frame_div_content_111)
        self.frame_title_wid_111.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_111.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_111.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_111.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_111.setObjectName("frame_title_wid_111")
        self.verticalLayout_118 = QVBoxLayout(self.frame_title_wid_111)
        self.verticalLayout_118.setObjectName("verticalLayout_118")
        self.labelBoxBlenderInstalation11 = QLabel(self.frame_title_wid_111)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation11.setFont(font)
        self.labelBoxBlenderInstalation11.setStyleSheet("")
        self.labelBoxBlenderInstalation11.setAlignment(Qt.AlignCenter)
        self.labelBoxBlenderInstalation11.setObjectName("labelBoxBlenderInstalation11")
        self.verticalLayout_118.addWidget(self.labelBoxBlenderInstalation11)
        self.verticalLayout_117.addWidget(self.frame_title_wid_111)
        self.frame_content_wid_111 = QFrame(self.frame_div_content_111)
        self.frame_content_wid_111.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_111.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_111.setObjectName("frame_content_wid_111")
        self.horizontalLayout_119 = QHBoxLayout(self.frame_content_wid_111)
        self.horizontalLayout_119.setObjectName("horizontalLayout_119")
        self.verticalLayout_117.addWidget(self.frame_content_wid_111)
        self.verticalLayout_1115.addWidget(self.frame_div_content_111)
        self.verticalLayout_116.addWidget(self.frame)
        self.frame_112 = QFrame(self.exp_confirmation_page)
        self.frame_112.setMinimumSize(QSize(0, 150))
        self.frame_112.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_112.setFrameShape(QFrame.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Raised)
        self.frame_112.setObjectName("frame_112")
        self.verticalLayout_1111 = QVBoxLayout(self.frame_112)
        self.verticalLayout_1111.setObjectName("verticalLayout_1111")
        self.tableWidget11 = QTableWidget(self.frame_112)
        self.tableWidget11.setObjectName("tableWidget11")
        self.tableWidget11.setColumnCount(0)
        self.tableWidget11.setRowCount(0)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from pettycashbook where checked = 0 ")
        myresult = mycursor.fetchall()
        c= 0
        if(len(myresult)!=0):         
            c = len(myresult[0])
        r = len(myresult)
        print(r)
        self.tableWidget11.setColumnCount(c)
        self.tableWidget11.setRowCount(r)
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         #self.tableWidget11.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           #item_checked = QTableWidgetItem()
           #item_checked.setCheckState(Qt.Unchecked)
           #item_checked.setFlags(Qt.ItemIsUserCheckable |Qt.ItemIsEnabled)
                    #item_checked.setCheckable(True)
           #self.tableWidget11.setItem(row_number,0, item_checked)
           self.tableWidget11.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.tableWidget11.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        columns = ["database id","vocher id","paid to","voucher date","amount","type of expenditure","payment mode","date on check","towards","drawn on","master id","checked"]
        self.tableWidget11.setHorizontalHeaderLabels(columns)
        self.verticalLayout_1111.addWidget(self.tableWidget11)
        self.frame_113 = QFrame(self.frame_112)
        self.frame_113.setMinimumSize(QSize(0, 150))
        self.frame_113.setFrameShape(QFrame.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Raised)
        self.frame_113.setObjectName("frame_113")
        self.horizontalLayout_1112 = QHBoxLayout(self.frame_113)
        self.horizontalLayout_1112.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1112.setSpacing(0)
        self.horizontalLayout_1112.setObjectName("horizontalLayout_1112")
        self.pushButton_114 = QPushButton(self.frame_113)
        self.pushButton_114.setObjectName("pushButton_114")
        self.pushButton_114.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_114.clicked.connect(self.exp_edit)
        self.horizontalLayout_1112.addWidget(self.pushButton_114)
        self.pushButton_112 = QPushButton(self.frame_113)
        self.pushButton_112.setText("")
        self.pushButton_112.setObjectName("pushButton_112")
        self.pushButton_112.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_112.clicked.connect(self.exp_confirm)
        self.horizontalLayout_1112.addWidget(self.pushButton_112)
        self.verticalLayout_1111.addWidget(self.frame_113)
        self.verticalLayout_116.addWidget(self.frame_112)
        self.stackedWidget.addWidget(self.exp_confirmation_page)

        self.donation_confirmation_page = QWidget()
        self.donation_confirmation_page.setObjectName("donation_confirmation_page")
        self.verticalLayout_126 = QVBoxLayout(self.donation_confirmation_page)
        self.verticalLayout_126.setObjectName("verticalLayout_126")
        self.frame12 = QFrame(self.donation_confirmation_page)
        self.frame12.setStyleSheet("border-radius: 5px;")
        self.frame12.setFrameShape(QFrame.StyledPanel)
        self.frame12.setFrameShadow(QFrame.Raised)
        self.frame12.setObjectName("frame12")
        self.verticalLayout_1215 = QVBoxLayout(self.frame12)
        self.verticalLayout_1215.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_1215.setSpacing(0)
        self.verticalLayout_1215.setObjectName("verticalLayout_1215")
        self.frame_div_content_121 = QFrame(self.frame12)
        self.frame_div_content_121.setMinimumSize(QSize(0, 110))
        self.frame_div_content_121.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_121.setStyleSheet("background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")
        self.frame_div_content_121.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_121.setFrameShadow(QFrame.Raised)
        self.frame_div_content_121.setObjectName("frame_div_content_121")
        self.verticalLayout_127 = QVBoxLayout(self.frame_div_content_121)
        self.verticalLayout_127.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_127.setSpacing(0)
        self.verticalLayout_127.setObjectName("verticalLayout_127")
        self.frame_title_wid_121 = QFrame(self.frame_div_content_121)
        self.frame_title_wid_121.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_121.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_title_wid_121.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_121.setFrameShadow(QFrame.Raised)
        self.frame_title_wid_121.setObjectName("frame_title_wid_121")
        self.verticalLayout_128 = QVBoxLayout(self.frame_title_wid_121)
        self.verticalLayout_128.setObjectName("verticalLayout_118")
        self.labelBoxBlenderInstalation12 = QLabel(self.frame_title_wid_121)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.labelBoxBlenderInstalation12.setFont(font)
        self.labelBoxBlenderInstalation12.setStyleSheet("")
        self.labelBoxBlenderInstalation12.setAlignment(Qt.AlignCenter)
        self.labelBoxBlenderInstalation12.setObjectName("labelBoxBlenderInstalation12")
        self.verticalLayout_128.addWidget(self.labelBoxBlenderInstalation12)
        self.verticalLayout_127.addWidget(self.frame_title_wid_121)
        self.frame_content_wid_121 = QFrame(self.frame_div_content_121)
        self.frame_content_wid_121.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_121.setFrameShadow(QFrame.Raised)
        self.frame_content_wid_121.setObjectName("frame_content_wid_121")
        self.horizontalLayout_129 = QHBoxLayout(self.frame_content_wid_121)
        self.horizontalLayout_129.setObjectName("horizontalLayout_129")
        self.verticalLayout_127.addWidget(self.frame_content_wid_121)
        self.verticalLayout_1215.addWidget(self.frame_div_content_121)
        self.verticalLayout_126.addWidget(self.frame12)
        self.frame_122 = QFrame(self.donation_confirmation_page)
        self.frame_122.setMinimumSize(QSize(0, 150))
        self.frame_122.setStyleSheet("background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_122.setFrameShape(QFrame.StyledPanel)
        self.frame_122.setFrameShadow(QFrame.Raised)
        self.frame_122.setObjectName("frame_122")
        self.verticalLayout_1211 = QVBoxLayout(self.frame_122)
        self.verticalLayout_1211.setObjectName("verticalLayout_1211")
        self.tableWidget12 = QTableWidget(self.frame_122)
        self.tableWidget12.setObjectName("tableWidget12")
        self.tableWidget12.setColumnCount(0)
        self.tableWidget12.setRowCount(0)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from all_donations where checked = 0 ")
        myresult = mycursor.fetchall()
        c= 0
        if(len(myresult)!=0):         
            c = len(myresult[0])
        r = len(myresult)
        self.tableWidget12.setColumnCount(c)
        self.tableWidget12.setRowCount(r)
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         #self.tableWidget12.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           self.tableWidget12.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        self.tableWidget12.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")
        columns = ["database id","vocher id","paid to","voucher date","amount","type of expenditure","payment mode","date on check","towards","drawn on","master id","checked"]
        self.tableWidget12.setHorizontalHeaderLabels(columns)
        self.verticalLayout_1211.addWidget(self.tableWidget12)
        self.frame_123 = QFrame(self.frame_122)
        self.frame_123.setMinimumSize(QSize(0, 150))
        self.frame_123.setFrameShape(QFrame.StyledPanel)
        self.frame_123.setFrameShadow(QFrame.Raised)
        self.frame_123.setObjectName("frame_123")
        self.horizontalLayout_1212 = QHBoxLayout(self.frame_123)
        self.horizontalLayout_1212.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_1212.setSpacing(0)
        self.horizontalLayout_1212.setObjectName("horizontalLayout_1212")
        self.pushButton_134 = QPushButton(self.frame_123)
        self.pushButton_134.setObjectName("pushButton_134")
        self.pushButton_134.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_134.clicked.connect(self.donation_edit)
        self.horizontalLayout_1212.addWidget(self.pushButton_134)
        self.pushButton_132 = QPushButton(self.frame_123)
        self.pushButton_132.setText("")
        self.pushButton_132.setObjectName("pushButton_132")
        self.pushButton_132.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_132.clicked.connect(self.donation_confirm)
        self.horizontalLayout_1212.addWidget(self.pushButton_132)
        self.verticalLayout_1211.addWidget(self.frame_123)
        self.verticalLayout_126.addWidget(self.frame_122)
        self.stackedWidget.addWidget(self.donation_confirmation_page)


        self.bank_statement = QWidget()
        self.bank_statement.setObjectName("bank_statement")
        self.verticalLayout_1410 = QVBoxLayout(self.bank_statement)
        self.verticalLayout_1410.setObjectName("verticalLayout_1410")
        self.verticalLayout_146 = QVBoxLayout()
        self.verticalLayout_146.setObjectName("verticalLayout_146")
        self.label14 = QLabel(self.bank_statement)
        self.label14.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label14.setFont(font)
        self.label14.setAlignment(Qt.AlignCenter)
        self.label14.setObjectName("label14")
        self.verticalLayout_146.addWidget(self.label14)
        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName("horizontalLayout_149")
        self.label_142 = QLabel(self.bank_statement)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_142.setFont(font)
        self.label_142.setObjectName("label_142")
        self.horizontalLayout_149.addWidget(self.label_142)
        self.dateEdit14 = QDateEdit(self.bank_statement)
        self.dateEdit14.setObjectName("dateEdit14")
        self.dateEdit14.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_149.addWidget(self.dateEdit14)
        self.label_143 =QLabel(self.bank_statement)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_143.setFont(font)
        self.label_143.setObjectName("label_143")
        self.horizontalLayout_149.addWidget(self.label_143)
        self.dateEdit_142 =QDateEdit(self.bank_statement)
        self.dateEdit_142.setObjectName("dateEdit_142")
        self.dateEdit_142.setMinimumSize(QSize(0, 30))
        self.horizontalLayout_149.addWidget(self.dateEdit_142)
        self.verticalLayout_146.addLayout(self.horizontalLayout_149)
        self.verticalLayout_1410.addLayout(self.verticalLayout_146)
        self.horizontalLayout_1412 = QHBoxLayout()
        self.horizontalLayout_1412.setObjectName("horizontalLayout_1412")
        self.label_144 = QLabel(self.bank_statement)
        self.label_144.setObjectName("label_144")
        self.label_144.setFont(font)
        self.horizontalLayout_1412.addWidget(self.label_144)
        self.comboBox14 = QComboBox(self.bank_statement)
        self.comboBox14.setObjectName("comboBox14")
        self.comboBox14.setFont(font)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from banks")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            self.comboBox14.addItem("")
            self.comboBox14.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
            i+=1
        self.horizontalLayout_1412.addWidget(self.comboBox14)
        self.verticalLayout_1410.addLayout(self.horizontalLayout_1412)
        self.pushButton14 = QPushButton(self.bank_statement)
        self.pushButton14.setObjectName("pushButton14")
        self.pushButton14.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton14.setFont(font)
        self.pushButton14.clicked.connect(self.get_statement)
        self.verticalLayout_1410.addWidget(self.pushButton14)
        self.tableWidget14 = QTableWidget(self.bank_statement)
        self.tableWidget14.setObjectName("tableWidget14")
        self.tableWidget14.setColumnCount(0)
        self.tableWidget14.setRowCount(0)
        self.pushButton141 = QPushButton(self.bank_statement)
        self.pushButton141.setObjectName("pushButton141")
        self.pushButton141.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton141.setFont(font)
        self.pushButton141.clicked.connect(self.add_bank)
        self.verticalLayout_1410.addWidget(self.tableWidget14)
        self.verticalLayout_1410.addWidget(self.pushButton141)
        self.pushButton142 = QPushButton(self.bank_statement)
        self.pushButton142.setObjectName("pushButton142")
        self.pushButton142.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton142.setFont(font)
        self.pushButton142.clicked.connect(self.manual_trasaction_page)
        self.verticalLayout_1410.addWidget(self.pushButton142)
        self.stackedWidget.addWidget(self.bank_statement)

        self.add_scheme = QWidget()
        self.add_scheme.setObjectName("add_scheme")
        self.verticalLayout_1510 = QVBoxLayout(self.add_scheme)
        self.verticalLayout_1510.setObjectName("verticalLayout_1510")
        self.verticalLayout_156 = QVBoxLayout()
        self.verticalLayout_156.setObjectName("verticalLayout_156")
        self.label15 = QLabel(self.add_scheme)
        self.label15.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label15.setFont(font)
        self.label15.setAlignment(Qt.AlignCenter)
        self.label15.setObjectName("label15")
        self.verticalLayout_156.addWidget(self.label15)
        self.gridLayout15 = QGridLayout()
        self.gridLayout15.setObjectName("gridLayout15")
        self.gridLayout15.setHorizontalSpacing(30)
        self.gridLayout15.setVerticalSpacing(40)
        self.lineEdit_153 = QLineEdit(self.add_scheme)
        self.lineEdit_153.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lineEdit_153.setFont(font)
        self.lineEdit_153.setObjectName("lineEdit_153")
        self.gridLayout15.addWidget(self.lineEdit_153, 3, 1, 1, 1)
        self.label_152 = QLabel(self.add_scheme)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_152.setFont(font)
        self.label_152.setObjectName("label_152")
        self.gridLayout15.addWidget(self.label_152, 1, 0, 1, 1)
        self.label_156 = QLabel(self.add_scheme)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_156.setFont(font)
        self.label_156.setObjectName("label_156")
        self.gridLayout15.addWidget(self.label_156, 0, 0, 1, 1)
        self.lineEdit15 =QLineEdit(self.add_scheme)
        self.lineEdit15.setMinimumSize(QSize(0, 30))
        self.lineEdit15.setObjectName("lineEdit15")
        self.gridLayout15.addWidget(self.lineEdit15, 1, 1, 1, 1)
        self.lineEdit_152 = QLineEdit(self.add_scheme)
        self.lineEdit_152.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lineEdit_152.setFont(font)
        self.lineEdit_152.setObjectName("lineEdit_152")
        self.gridLayout15.addWidget(self.lineEdit_152, 2, 1, 1, 1)
        self.lineEdit_156 = QLineEdit(self.add_scheme)
        self.lineEdit_156.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lineEdit_156.setFont(font)
        self.lineEdit_156.setObjectName("lineEdit_152")
        self.gridLayout15.addWidget(self.lineEdit_156, 0, 1, 1, 1)
        self.label_153 = QLabel(self.add_scheme)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_153.setFont(font)
        self.label_153.setObjectName("label_153")
        self.gridLayout15.addWidget(self.label_153, 2, 0, 1, 1)
        self.label_154 = QLabel(self.add_scheme)
        font =QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_154.setFont(font)
        self.label_154.setObjectName("label_154")
        self.gridLayout15.addWidget(self.label_154, 3, 0, 1, 1)
        self.pushButton15 = QPushButton(self.add_scheme)
        self.pushButton15.setMinimumSize(QSize(0, 30))
        self.pushButton15.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton15.clicked.connect(self.add__scheme)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.pushButton15.setFont(font)
        self.pushButton15.setObjectName("pushButton15")
        self.gridLayout15.addWidget(self.pushButton15, 4, 1, 1, 1)
        self.verticalLayout_156.addLayout(self.gridLayout15)
        self.verticalLayout_1510.addLayout(self.verticalLayout_156)
        self.stackedWidget.addWidget(self.add_scheme)

        self.withdraw = QWidget()
        self.withdraw.setObjectName("withdraw")
        self.verticalLayout_1710 = QVBoxLayout(self.withdraw)
        self.verticalLayout_1710.setObjectName("verticalLayout_1710")
        self.verticalLayout_176 = QVBoxLayout()
        self.verticalLayout_176.setObjectName("verticalLayout_176")
        self.label17 = QLabel(self.withdraw)
        self.label17.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label17.setFont(font)
        self.label17.setAlignment(Qt.AlignCenter)
        self.label17.setObjectName("label17")
        self.verticalLayout_176.addWidget(self.label17)
        self.gridLayout17 = QGridLayout()
        self.gridLayout17.setObjectName("gridLayout17")
        self.gridLayout17.setHorizontalSpacing(30)
        self.gridLayout17.setVerticalSpacing(40)
        self.label_172 = QLabel(self.withdraw)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_172.setFont(font)
        self.label_172.setObjectName("label_172")
        self.gridLayout17.addWidget(self.label_172, 0, 0, 1, 1)
        self.comboBox17 = QComboBox(self.withdraw)
        self.comboBox17.setMinimumSize(QSize(0, 30))
        self.comboBox17.setObjectName("comboBox17")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        mycursor = mydb.cursor()
        mycursor.execute("select * from banks")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            self.comboBox17.addItem("")
            self.comboBox17.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
            i+=1
        self.gridLayout17.addWidget(self.comboBox17, 1, 1, 1, 1)
        self.label_173 = QLabel(self.withdraw)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_173.setFont(font)
        self.label_173.setObjectName("label_173")
        self.gridLayout17.addWidget(self.label_173, 2, 0, 1, 1)
        self.lineEdit17 = QLineEdit(self.withdraw)
        self.lineEdit17.setMinimumSize(QSize(0, 30))
        self.lineEdit17.setObjectName("lineEdit17")
        self.gridLayout17.addWidget(self.lineEdit17, 2, 1, 1, 1)
        self.label_174 = QLabel(self.withdraw)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_174.setFont(font)
        self.label_174.setObjectName("label_174")
        self.gridLayout17.addWidget(self.label_174, 1, 0, 1, 1)
        self.dateEdit17 = QDateEdit(self.withdraw)
        self.dateEdit17.setMinimumSize(QSize(0, 30))
        now = datetime.now()
        self.dateEdit17.setDate(now)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.dateEdit17.setFont(font)
        self.dateEdit17.setObjectName("dateEdit17")
        self.gridLayout17.addWidget(self.dateEdit17, 0, 1, 1, 1)
        self.label_175 = QLabel(self.withdraw)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_175.setFont(font)
        self.label_175.setObjectName("label_175")
        self.gridLayout17.addWidget(self.label_175, 3, 0, 1, 1)
        self.textEdit17 = QTextEdit(self.withdraw)
        self.textEdit17.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.textEdit17.setFont(font)
        self.textEdit17.setObjectName("textEdit17")
        self.gridLayout17.addWidget(self.textEdit17, 3, 1, 1, 1)
        self.verticalLayout_176.addLayout(self.gridLayout17)
        self.verticalLayout_1710.addLayout(self.verticalLayout_176)
        self.pushButton17 =QPushButton(self.withdraw)
        self.pushButton17.setMinimumSize(QSize(0, 30))
        self.pushButton17.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton17.setFont(font)
        self.pushButton17.setObjectName("pushButton17")
        self.pushButton17.clicked.connect(self.withdraw_from_bank)
        self.verticalLayout_1710.addWidget(self.pushButton17)
        self.stackedWidget.addWidget(self.withdraw)

        self.add_bank_acc = QWidget()
        self.add_bank_acc.setObjectName("add_bank_acc")
        self.verticalLayout_1610 = QVBoxLayout(self.add_bank_acc)
        self.verticalLayout_1610.setObjectName("verticalLayout_1610")
        self.verticalLayout_166 = QVBoxLayout()
        self.verticalLayout_166.setObjectName("verticalLayout_166")
        self.label116 = QLabel(self.add_bank_acc)
        self.label116.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label116.setFont(font)
        self.label116.setAlignment(Qt.AlignCenter)
        self.label116.setObjectName("label116")
        self.verticalLayout_166.addWidget(self.label116)
        self.gridLayout16 = QGridLayout()
        self.gridLayout16.setObjectName("gridLayout")
        self.label_163 = QLabel(self.add_bank_acc)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_163.setFont(font)
        self.label_163.setObjectName("label_163")
        self.gridLayout16.addWidget(self.label_163, 2, 0, 1, 1)
        self.label_162 = QLabel(self.add_bank_acc)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_162.setFont(font)
        self.label_162.setObjectName("label_162")
        self.gridLayout16.addWidget(self.label_162, 1, 0, 1, 1)
        self.lineEdit16 = QLineEdit(self.add_bank_acc)
        self.lineEdit16.setMinimumSize(QSize(0, 30))
        self.lineEdit16.setObjectName("lineEdit16")
        self.gridLayout16.addWidget(self.lineEdit16, 1, 1, 1, 1)
        self.textEdit16 = QTextEdit(self.add_bank_acc)
        self.textEdit16.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.textEdit16.setFont(font)
        self.textEdit16.setObjectName("textEdit16")
        self.gridLayout16.addWidget(self.textEdit16, 2, 1, 1, 1)
        self.label16 = QLabel(self.add_bank_acc)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label16.setFont(font)
        self.label16.setObjectName("label16")
        self.gridLayout16.addWidget(self.label16, 0, 0, 1, 1)
        self.lineEdit_162 = QLineEdit(self.add_bank_acc)
        self.lineEdit_162.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.lineEdit_162.setFont(font)
        self.lineEdit_162.setObjectName("lineEdit_162")
        self.gridLayout16.addWidget(self.lineEdit_162, 0, 1, 1, 1)
        self.verticalLayout_166.addLayout(self.gridLayout16)
        self.verticalLayout_1610.addLayout(self.verticalLayout_166)
        self.pushButton16 = QPushButton(self.add_bank_acc)
        self.pushButton16.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton16.setFont(font)
        self.pushButton16.setObjectName("pushButton16")
        self.pushButton16.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton16.clicked.connect(self.add_bank_account)
        self.verticalLayout_1610.addWidget(self.pushButton16)
        self.stackedWidget.addWidget(self.add_bank_acc)

        self.add_category_page = QWidget()
        self.add_category_page.setObjectName("add_category_page")
        self.verticalLayout_1810 = QVBoxLayout(self.add_category_page)
        self.verticalLayout_1810.setObjectName("verticalLayout_1810")
        self.gridLayout_183 = QGridLayout()
        self.gridLayout_183.setObjectName("gridLayout_183")
        self.label_182 = QLabel(self.add_category_page)
        self.label_182.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_182.setFont(font)
        self.label_182.setObjectName("label_182")
        self.gridLayout_183.addWidget(self.label_182, 1, 0, 1, 1)
        self.label_183 = QLabel(self.add_category_page)
        self.label_183.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_183.setFont(font)
        self.label_183.setObjectName("label_183")
        self.gridLayout_183.addWidget(self.label_183, 2, 0, 1, 1)
        self.lineEdit_183 = QLineEdit(self.add_category_page)
        self.lineEdit_183.setMaximumSize(QSize(16777215, 60))
        self.lineEdit_183.setObjectName("lineEdit_183")
        self.gridLayout_183.addWidget(self.lineEdit_183, 2, 1, 1, 2)
        self.lineEdit_182 = QLineEdit(self.add_category_page)
        self.lineEdit_182.setMaximumSize((QSize(16777215, 50)))
        self.lineEdit_182.setObjectName("lineEdit_182")
        self.gridLayout_183.addWidget(self.lineEdit_182, 1, 2, 1, 1)
        self.label = QLabel(self.add_category_page)
        self.label.setMaximumSize(QSize(16777215, 70))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        #self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setObjectName("label")
        self.gridLayout_183.addWidget(self.label, 0, 0, 1, 3)
        self.pushButton_182 = QPushButton(self.add_category_page)
        self.pushButton_182.setMaximumSize((QSize(16777215, 50)))
        self.pushButton_182.setObjectName("pushButton_182")
        self.pushButton_182.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_182.clicked.connect(self.add_exp_cat)
        self.gridLayout_183.addWidget(self.pushButton_182, 3, 0, 1, 3)
        self.verticalLayout_1810.addLayout(self.gridLayout_183)
        self.stackedWidget.addWidget(self.add_category_page)


        self.manual_transaction = QWidget()
        self.manual_transaction.setObjectName("manual_transaction")
        self.verticalLayout_1910 = QVBoxLayout(self.manual_transaction)
        self.verticalLayout_1910.setObjectName("verticalLayout_1910")
        self.gridLayout_194 = QGridLayout()
        self.gridLayout_194.setObjectName("gridLayout_194")
        self.gridLayout_194.setHorizontalSpacing(30)
        self.gridLayout_194.setVerticalSpacing(40)
        self.horizontalLayout_1910 = QHBoxLayout()
        self.horizontalLayout_1910.setObjectName("horizontalLayout_1910")
        self.radioButton_192 = QRadioButton(self.manual_transaction)
        self.radioButton_192.setObjectName("radioButton_192")
        self.horizontalLayout_1910.addWidget(self.radioButton_192)
        self.gridLayout_194.addLayout(self.horizontalLayout_1910, 6, 2, 1, 1)
        self.lineEdit_192 = QLineEdit(self.manual_transaction)
        self.lineEdit_192.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_192.setObjectName("lineEdit_192")
        self.gridLayout_194.addWidget(self.lineEdit_192, 4, 1, 1, 2)
        self.comboBox_192 = QComboBox(self.manual_transaction)
        self.comboBox_192.setMaximumSize(QSize(16777215, 40))
        self.comboBox_192.setObjectName("comboBox_192")
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        mycursor = mydb.cursor()
        mycursor.execute("select * from banks")
        myresult = mycursor.fetchall()
        i=0
        for x in myresult:
            self.comboBox_192.addItem("")
            self.comboBox_192.setItemText(i, QCoreApplication.translate("MainWindow", x[1]))
            i+=1
        self.gridLayout_194.addWidget(self.comboBox_192, 3, 1, 1, 2)
        self.label_192 = QLabel(self.manual_transaction)
        self.label_192.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_192.setFont(font)
        self.label_192.setObjectName("label_192")
        self.gridLayout_194.addWidget(self.label_192, 1, 0, 1, 1)
        self.label_195 = QLabel(self.manual_transaction)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_195.setFont(font)
        self.label_195.setObjectName("label_195")
        self.gridLayout_194.addWidget(self.label_195, 5, 0, 1, 1)
        self.textEdit19 = QTextEdit(self.manual_transaction)
        self.textEdit19.setMaximumSize(QSize(16777215, 170))
        self.textEdit19.setObjectName("textEdit19")
        self.gridLayout_194.addWidget(self.textEdit19, 5, 1, 1, 2)
        self.label_194 = QLabel(self.manual_transaction)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_194.setFont(font)
        self.label_194.setObjectName("label_194")
        self.gridLayout_194.addWidget(self.label_194, 4, 0, 1, 1)
        self.dateEdit19 = QDateEdit(self.manual_transaction)
        self.dateEdit19.setMaximumSize(QSize(16777215, 40))
        self.dateEdit19.setObjectName("dateEdit19")
        now = datetime.now()
        self.dateEdit19.setDate(now)
        self.gridLayout_194.addWidget(self.dateEdit19, 1, 1, 1, 2)
        self.label19 = QLabel(self.manual_transaction)
        self.label19.setMaximumSize(QSize(16777215, 80))
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label19.setFont(font)
        self.label19.setObjectName("label19")
        self.label19.setAlignment(Qt.AlignCenter)
        self.gridLayout_194.addWidget(self.label19, 0, 0, 1, 3)
        self.radioButton_193 = QRadioButton(self.manual_transaction)
        self.radioButton_193.setObjectName("radioButton_193")
        self.horizontalLayout_1910.addWidget(self.radioButton_193)
        self.label_193 = QLabel(self.manual_transaction)
        self.label_193.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_193.setFont(font)
        self.label_193.setObjectName("label_193")
        self.gridLayout_194.addWidget(self.label_193, 3, 0, 1, 1)
        self.pushButton_192 = QPushButton(self.manual_transaction)
        self.pushButton_192.setObjectName("pushButton_192")
        self.pushButton_192.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        self.pushButton_192.clicked.connect(self.add_manual_transaction)
        self.gridLayout_194.addWidget(self.pushButton_192, 7, 0, 1, 3)
        self.verticalLayout_1910.addLayout(self.gridLayout_194)
        self.stackedWidget.addWidget(self.manual_transaction)

        self.page_widgets = QWidget()
        self.page_widgets.setObjectName(u"page_widgets")
        self.verticalLayout_6 = QVBoxLayout(self.page_widgets)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.page_widgets)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-radius: 5px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.frame)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setStyleSheet(u"background-color: rgb(41, 45, 56);\n"
"border-radius: 5px;\n"
"")     
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setStyleSheet(u"background-color: rgb(39, 44, 54);")
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_7.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_content_wid_1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.gridLayout.setContentsMargins(-1, -1, -1, 0)
        self.lineEdit = QLineEdit(self.frame_content_wid_1)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 40))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"QLineEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(27, 29, 35);\n"
"	padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame_content_wid_1)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(150, 40))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(14)
        font8.setBold(True)
        self.pushButton.setFont(font8)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon3)
        self.gridLayout.addWidget(self.pushButton, 0, 1, 1, 1)
        self.pushButton.clicked.connect(self.get_donar_details)
        self.pushButton2 = QPushButton(self.frame_content_wid_1)
        self.pushButton2.setObjectName(u"pushButton2")
        self.pushButton2.setMinimumSize(QSize(150, 40))
        font8 = QFont()
        font8.setFamily(u"Segoe UI")
        font8.setPointSize(14)
        font8.setBold(True)
        self.pushButton2.setFont(font8)
        self.pushButton2.setStyleSheet(u"QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/16x16/icons/16x16/cil-chevron-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton2.setIcon(icon3)
        self.gridLayout.addWidget(self.pushButton2, 0, 2, 1, 1)
        self.pushButton2.clicked.connect(self.get_donar_donations)

        self.labelVersion_3 = QLabel(self.frame_content_wid_1)
        self.labelVersion_3.setObjectName(u"labelVersion_3")
        self.labelVersion_3.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_3.setLineWidth(1)
        self.labelVersion_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.labelVersion_3, 1, 0, 1, 2)


        self.horizontalLayout_9.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame_content_wid_1)


        self.verticalLayout_15.addWidget(self.frame_div_content_1)


        self.verticalLayout_6.addWidget(self.frame)

        self.frame_2 = QFrame(self.page_widgets)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 100))
        self.frame_2.setStyleSheet(u"background-color: rgb(39, 44, 54);\n"
"border-radius: 5px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        #self.checkBox = QCheckBox(self.frame_2)
        #self.checkBox.setObjectName(u"checkBox")
        #self.checkBox.setAutoFillBackground(False)
        #self.checkBox.setStyleSheet(u"")

        #self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)

        #self.radioButton = QRadioButton(self.frame_2)
        #self.radioButton.setObjectName(u"radioButton")
        #self.radioButton.setStyleSheet(u"")

        #self.gridLayout_2.addWidget(self.radioButton, 0, 1, 1, 1)

        #self.verticalSlider = QSlider(self.frame_2)
        #self.verticalSlider.setObjectName(u"verticalSlider")
        #self.verticalSlider.setStyleSheet(u"")
        #self.verticalSlider.setOrientation(Qt.Vertical)

        #self.gridLayout_2.addWidget(self.verticalSlider, 0, 2, 3, 1)

        #self.verticalScrollBar = QScrollBar(self.frame_2)
        #self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        #self.verticalScrollBar.setStyleSheet(u" QScrollBar:vertical {\n"
#"	border: none;\n"
#"    background: rgb(52, 59, 72);\n"
#"    width: 14px;\n"
#"    margin: 21px 0 21px 0;\n"
#"	border-radius: 0px;\n"
#" }")
        #self.verticalScrollBar.setOrientation(Qt.Vertical)

        #self.gridLayout_2.addWidget(self.verticalScrollBar, 0, 4, 3, 1)

        #self.scrollArea = QScrollArea(self.frame_2)
        #self.scrollArea.setObjectName(u"scrollArea")
        #self.scrollArea.setStyleSheet(u"QScrollArea {\n"
#"	border: none;\n"
#"	border-radius: 0px;\n"
#"}\n"
#"QScrollBar:horizontal {\n"
#"    border: none;\n"
#"    background: rgb(52, 59, 72);\n"
#"    height: 14px;\n"
#"    margin: 0px 21px 0 21px;\n"
#"	border-radius: 0px;\n"
#"}\n"
#" QScrollBar:vertical {\n"
#"	border: none;\n"
#"    background: rgb(52, 59, 72);\n"
#"    width: 14px;\n"
#"    margin: 21px 0 21px 0;\n"
#"	border-radius: 0px;\n"
#" }\n"
#"")
        #self.scrollArea.setFrameShape(QFrame.NoFrame)
        #self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        #self.scrollArea.setWidgetResizable(True)
        #self.scrollAreaWidgetContents = QWidget()
        #self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        #self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 274, 218))
        #self.horizontalLayout_11 = QHBoxLayout(self.scrollAreaWidgetContents)
        #self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        #self.plainTextEdit = QPlainTextEdit(self.scrollAreaWidgetContents)
        #self.plainTextEdit.setObjectName(u"plainTextEdit")
        #self.plainTextEdit.setMinimumSize(QSize(200, 200))
        #self.plainTextEdit.setStyleSheet(u"QPlainTextEdit {\n"
#"	background-color: rgb(27, 29, 35);\n"
#"	border-radius: 5px;\n"
#"	padding: 10px;\n"
#"}\n"
#"QPlainTextEdit:hover {\n"
#"	border: 2px solid rgb(64, 71, 88);\n"
#"}\n"
#"QPlainTextEdit:focus {\n"
#"	border: 2px solid rgb(91, 101, 124);\n"
#"}")

        #self.horizontalLayout_11.addWidget(self.plainTextEdit)

        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        #self.gridLayout_2.addWidget(self.scrollArea, 0, 5, 3, 1)

        #self.comboBox = QComboBox(self.frame_2)
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.addItem("")
        #self.comboBox.setObjectName(u"comboBox")
        #self.comboBox.setFont(font8)
        #self.comboBox.setAutoFillBackground(False)
        #self.comboBox.setStyleSheet(u"QComboBox{\n"
#"	background-color: rgb(27, 29, 35);\n"
#"	border-radius: 5px;\n"
#"	border: 2px solid rgb(27, 29, 35);\n"
#"	padding: 5px;\n"
#"	padding-left: 10px;\n"
#"}\n"
#"QComboBox:hover{\n"
#"	border: 2px solid rgb(64, 71, 88);\n"
#"}\n"
#"QComboBox QAbstractItemView {\n"
#"	color: rgb(85, 170, 255);	\n"
#"	background-color: rgb(27, 29, 35);\n"
#"	padding: 10px;\n"
#"	selection-background-color: rgb(39, 44, 54);\n"
#"}")
       # self.comboBox.setIconSize(QSize(16, 16))
       # self.comboBox.setFrame(True)

        #self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 2)

        #self.horizontalScrollBar = QScrollBar(self.frame_2)
        #self.horizontalScrollBar.setObjectName(u"horizontalScrollBar")
        #sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        #sizePolicy5.setHorizontalStretch(0)
        #sizePolicy5.setVerticalStretch(0)
        #sizePolicy5.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        #self.horizontalScrollBar.setSizePolicy(sizePolicy5)
        #self.horizontalScrollBar.setStyleSheet(u"QScrollBar:horizontal {\n"
#"    border: none;\n"
#"    background: rgb(52, 59, 72);\n"
#"    height: 14px;\n"
#"    margin: 0px 21px 0 21px;\n"
#"	border-radius: 0px;\n"
#"}\n"
#"")
 #       self.horizontalScrollBar.setOrientation(Qt.Horizontal)

  #      self.gridLayout_2.addWidget(self.horizontalScrollBar, 1, 3, 1, 1)

        font1 = QFont()
        font1.setFamily("Segoe UI")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.new_donation_btn = QCommandLinkButton(self.frame_2)
        self.new_donation_btn.setObjectName(u"new_donation_btn")
        self.new_donation_btn.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        self.new_donation_btn.setFont(font1)
        self.new_donation_btn.clicked.connect(self.new_donation_button)
        icon4 = QIcon()
        icon4.addFile(u":/16x16/icons/16x16/cil-envelope-letter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_donation_btn.setIcon(icon4)

        self.gridLayout_2.addWidget(self.new_donation_btn, 1, 3, 1, 1)

        self.new_donor = QCommandLinkButton(self.frame_2)
        self.new_donor.setObjectName(u"new_donor")
        self.new_donor.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_donor.setIcon(icon5)
        self.new_donor.setFont(font1)
        self.new_donor.clicked.connect(self.new_donor_button)
        self.gridLayout_2.addWidget(self.new_donor, 1, 1, 1, 1)

        self.remainders = QCommandLinkButton(self.frame_2)
        self.remainders.setObjectName(u"remainders")
        self.remainders.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/16x16/icons/16x16/cil-user-follow.png", QSize(), QIcon.Normal, QIcon.Off)
        self.remainders.setIcon(icon5)
        self.remainders.setFont(font1)
        self.remainders.clicked.connect(self.donation_remainder_button)
        self.gridLayout_2.addWidget(self.remainders, 1, 4, 1, 1)

        self.reports = QCommandLinkButton(self.frame_2)
        self.reports.setObjectName(u"reports")
        self.reports.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        self.reports.clicked.connect(self.dreports)
        self.reports.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reports.setIcon(icon6)

        self.gridLayout_2.addWidget(self.reports, 1, 6, 1, 1)

        self.adds = QCommandLinkButton(self.frame_2)
        self.adds.setObjectName(u"adds")
        self.adds.setStyleSheet(u"QCommandLinkButton {	\n"
"	color: rgb(85, 170, 255);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pressed {	\n"
"	color: rgb(210, 210, 210);\n"
"	background-color: rgb(52, 58, 71);\n"
"}")
        self.adds.clicked.connect(self.add_category)
        self.adds.setFont(font1)
        icon6 = QIcon()
        icon6.addFile(u":/16x16/icons/16x16/cil-chart-line.png", QSize(), QIcon.Normal, QIcon.Off)
        self.adds.setIcon(icon6)
        self.adds.setText(QCoreApplication.translate("MainWindow", u"Add Scheme/Category", None))
        self.gridLayout_2.addWidget(self.adds, 1, 8, 1, 1)
            

       # self.horizontalSlider = QSlider(self.frame_2)
       # self.horizontalSlider.setObjectName(u"horizontalSlider")
       # self.horizontalSlider.setStyleSheet(u"")
       # self.horizontalSlider.setOrientation(Qt.Horizontal)

        #self.gridLayout_2.addWidget(self.horizontalSlider, 2, 0, 1, 2)


        self.verticalLayout_11.addLayout(self.gridLayout_2)


        self.verticalLayout_6.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.page_widgets)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 150))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        
        self.labeltable = QLabel(self.frame_3)
        self.labeltable.setObjectName(u"labeltable")
        self.labeltable.setFont(font)
        self.labeltable.setStyleSheet(u"")
        
        #self.horizontalLayout_12.addWidget(self.labelBoxBlenderInstalation)
        self.tableWidget = QTableWidget(self.frame_3)
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="anirudh123",
        database="chitra_gupta"
        )
        print(mydb)
        now = datetime.now()
        now = now.strftime('%Y-%m-%d')
        mycursor = mydb.cursor()
        mycursor.execute("select * from  donations where id_donations in (select id_donations from all_donations where date_show = '{0}')".format(now))
        myresult = mycursor.fetchall()
        print(myresult)
        self.tableWidget.setObjectName(u"tableWidget")
        c=0
        if len(myresult)!=0:
            c = len(myresult[0])
        r = len(myresult)
        self.tableWidget = QTableWidget()
        #sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #sizePolicy.setHorizontalStretch(100)
        #sizePolicy.setVerticalStretch(100)
        #sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        #self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QSize(0, 0))
        self.tableWidget.setRowCount(r)
        self.tableWidget.setColumnCount(c)
        self.tableWidget.setObjectName("tableWidget")
        columns = ["donation id","donor id","date of donation","donation date","donation in name","master registration number","reciept number","payment mode","payment description","ocassion","remarks","category","student id","amount","remind_date","reminded"]   
        self.tableWidget.setHorizontalHeaderLabels(columns)
        self.tableWidget.setRowCount(0)
        for row_number, row_data in enumerate(myresult):
         #print(row_number)
         self.tableWidget.insertRow(row_number)
         for column_number, data in enumerate(row_data):
                    #print(column_number)
           self.tableWidget.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(39, 44, 54, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush15)
        brush16 = QBrush(QColor(210, 210, 210, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush16)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush15)
        brush17 = QBrush(QColor(210, 210, 210, 128))
        brush17.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush17)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush18 = QBrush(QColor(210, 210, 210, 128))
        brush18.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush18)
#endif
        
        self.tableWidget.setStyleSheet("QTableWidget {    \n"
"    background-color: rgb(39, 44, 54);\n"
"    padding: 10px;\n"
"    border-radius: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item{\n"
"    border-color: rgb(44, 49, 60);\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"    gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"    background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"    Background-color: rgb(39, 44, 54);\n"
"    max-width: 30px;\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::horizontalHeader {    \n"
"    background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 3px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(44, 49, 60);\n"
"}\n"
"")     
        #self.tableWidget.setFrameShape(QFrame.NoFrame)
        #self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        #self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        #self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.tableWidget.setAlternatingRowColors(False)
        #self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        #self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        #self.tableWidget.setShowGrid(True)
        #self.tableWidget.setGridStyle(Qt.SolidLine)
        #self.tableWidget.setSortingEnabled(False)
        #self.tableWidget.horizontalHeader().setVisible(True)
        #self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        #self.tableWidget.horizontalHeader().setDefaultSectionSize(300)
        #self.tableWidget.horizontalHeader().setStretchLastSection(True)
        #self.tableWidget.verticalHeader().setVisible(False)
        #self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        #self.tableWidget.verticalHeader().setHighlightSections(False)
        #self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.horizontalLayout_12.addWidget(self.tableWidget)
        today = datetime.now()
        yesterday = today - timedelta(days = 1)
        mycursor.execute("select * from schemes")
        sch = mycursor.fetchall()
        #for x in sch:
        #    if category == x[1]:
        #        end = today + timedelta(days=x[2])
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')
        mycursor.execute("select * from all_donations where date_show = '{0}'".format(formatted_yesterday))
        alldonations = mycursor.fetchall()
        for y in alldonations:
            for x in sch:
                if y[11] == x[0]:
                    valid = self.addYears(y[3],x[3])
                    nexty = self.addYears(y[18],1)
                    validc = valid.strftime('%y-%m-%d')
                    nextyc = nexty.strftime('%y-%m-%d')
                    print(valid,nexty)
                    if nextyc<validc:
                        print("inn")
                        mycursor.execute("update all_donations set date_show = '{0}' where id_donations = {1}".format(nexty,y[0]))
                        mydb.commit()
        self.labelVersion_4 = QLabel(self.page_widgets)
        self.labelVersion_4.setObjectName(u"labelVersion_3")
        #self.labelVersion_4.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        font.setItalic(True)
        font.setBold(True)
        font.setWeight(75)
        self.labelVersion_4.setFont(font)
        self.verticalLayout_6.addWidget(self.labelVersion_4)
        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.page_widgets)



        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)

        self.donor_donations = QWidget()
        self.donor_donations.setObjectName("donor_donations")
        self.verticalLayout_2210 = QVBoxLayout(self.donor_donations)
        self.verticalLayout_2210.setObjectName("verticalLayout_2210")
        self.verticalLayout_2212 = QVBoxLayout()
        self.verticalLayout_2212.setObjectName("verticalLayout_2212")
        self.label22 = QLabel(self.donor_donations)
        self.label22.setMaximumSize(QSize(16777215, 30))
        font = QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label22.setFont(font)
        self.label22.setAlignment(Qt.AlignCenter)
        self.label22.setObjectName("label22")
        self.label22.setText(QCoreApplication.translate("MainWindow", "All Donations"))
        self.verticalLayout_2212.addWidget(self.label22)
        self.verticalLayout_2210.addLayout(self.verticalLayout_2212)
        self.widget22 = QWidget(self.donor_donations)
        self.widget22.setMinimumSize(QSize(0, 350))
        self.widget22.setObjectName("widget12")
        self.verticalLayout_221212 = QVBoxLayout(self.widget22)
        self.verticalLayout_221212.setObjectName("verticalLayout_221212")
        self.verticalLayout_2210.addWidget(self.widget22)
        self.horizontalLayout_2213 = QHBoxLayout()
        self.horizontalLayout_2213.setSizeConstraint(QLayout.SetMinimumSize)
        self.horizontalLayout_2213.setObjectName("horizontalLayout_2213")
        self.verticalLayout_2210.addLayout(self.horizontalLayout_2213)
        self.stackedWidget.addWidget(self.donor_donations)
    
        self.credits = QWidget()
        self.credits.setObjectName("credits")
        self.verticalLayout_10 = QVBoxLayout(self.credits)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.textEditcredits = QTextEdit(self.credits)
        self.textEditcredits.setObjectName("textEditcredits")
        self.verticalLayout_6.addWidget(self.textEditcredits)
        self.verticalLayout_10.addLayout(self.verticalLayout_6)
        self.stackedWidget.addWidget(self.credits)
        
        

        self.frame_grip = QFrame(self.frame_content_right)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(0, 25))
        self.frame_grip.setMaximumSize(QSize(16777215, 25))
        self.frame_grip.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_grip)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 2, 0)
        self.frame_label_bottom = QFrame(self.frame_grip)
        self.frame_label_bottom.setObjectName(u"frame_label_bottom")
        self.frame_label_bottom.setFrameShape(QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_label_bottom)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 0, 10, 0)
        self.label_credits = QLabel(self.frame_label_bottom)
        self.label_credits.setObjectName(u"label_credits")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(98, 103, 111);")

        self.horizontalLayout_7.addWidget(self.label_credits)

        self.label_version = QLabel(self.frame_label_bottom)
        self.label_version.setObjectName(u"label_version")
        self.label_version.setMaximumSize(QSize(100, 16777215))
        self.label_version.setFont(font2)
        self.label_version.setStyleSheet(u"color: rgb(98, 103, 111);")
        self.label_version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.label_version)


        self.horizontalLayout_6.addWidget(self.frame_label_bottom)

        self.frame_size_grip = QFrame(self.frame_grip)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMaximumSize(QSize(20, 20))
        self.frame_size_grip.setStyleSheet(u"QSizeGrip {\n"
"	background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
"}")
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_size_grip)


        self.verticalLayout_4.addWidget(self.frame_grip)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.btn_toggle_menu)
     #   QWidget.setTabOrder(self.btn_toggle_menu, self.checkBox)
      #  QWidget.setTabOrder(self.checkBox, self.comboBox)
       # QWidget.setTabOrder(self.comboBox, self.radioButton)
       # QWidget.setTabOrder(self.radioButton, self.horizontalSlider)
       # QWidget.setTabOrder(self.horizontalSlider, self.verticalSlider)
       # QWidget.setTabOrder(self.verticalSlider, self.scrollArea)
      #  QWidget.setTabOrder(self.scrollArea, self.plainTextEdit)
       # QWidget.setTabOrder(self.plainTextEdit, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.new_donation_btn)
        QWidget.setTabOrder(self.tableWidget, self.new_donor)
        QWidget.setTabOrder(self.tableWidget, self.reports)



        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_toggle_menu.setText("")
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"Main Window - Base", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.label_top_info_1.setText(QCoreApplication.translate("MainWindow", u"C:\\Program Files\\Blender Foundation\\Blender 2.82", None))
        self.label_top_info_2.setText(QCoreApplication.translate("MainWindow", u"| HOME", None))
        self.label_user_icon.setText(QCoreApplication.translate("MainWindow", u"WM", None))
        self.labeltable.setText(QCoreApplication.translate("MainWindow", u"All Donations", None))
        

        self.label_06.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#010000;\">KARUNASRI SEVA SAMITHI </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\">KARUNYA SINDHU ASHRAM </span><span style=\" font-size:18pt; font-weight:600; color:#010000;\">&amp;</span><span style=\" font-size:18pt; font-weight:600; color:#ff0000;\"> KARUNYA BHARATHI ASHRAM </span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#010000;\">(Home for Orphan Boys)</span></p><p align=\"center\"><span style=\" font-size:18pt; color:#010000;\">Seva prakalp of V.H.P.</span></p></body></html>"))
        self.label_04.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:600; color:#010000;\">SAMSKAR</span></p></body></html>"))
        self.label_05.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#010000;\">SEVA</span></p></body></html>"))
        self.label_07.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#010000;\">No.17-1-474, Krishna Nagar Colony,Saidabad, Hyderabad-500 059 </span></p></body></html>"))
        self.label_02.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Mob:</span><span style=\" font-size:14pt;\"/><span style=\" font-size:14pt; color:#010000;\">9000889785 </span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">Email:</span><span style=\" font-size:14pt;\"/><span style=\" font-size:14pt; color:#010000;\">karunasri1999@gmail.com </span></p></body></html>"))
        self.label_08.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Landline:</span><span style=\" font-size:16pt;\"/><span style=\" font-size:16pt; color:#010000;\">040-24073204</span></p><p align=\"right\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Registration No.</span><span style=\" font-size:16pt; color:#010000;\">7451/1999</span></p></body></html>"))
        self.label_9.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">websites:</span><a href=\"https://www.karunasri.org\"><span style=\" font-size:16pt; text-decoration: underline; color:#0000ff;\">https://www.karunasri.org</span></a><span style=\" font-size:16pt; font-weight:600; color:#010000;\">/ </span><span style=\" font-size:16pt; font-weight:600; color:#020000;\">www.karunasri.org </span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">PAN No.</span><span style=\" font-size:16pt; font-weight:600; color:#010000;\">AAATK6724F</span></p></body></html>"))
        self.label_010.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#010000;\">Karunasri Seva Samithi established Karunya Sindhu Ashram in the year 1999 to cater services to the students who are Orphan/Semi-Orphan &amp; from BPL families. </span></p><p><span style=\" font-size:14pt; color:#010000;\">It is a Unit of V.H.P. Presently it takes care of all round development of the 50 inmate students providing them food, shelter, schooling, and giving them Samskaras etc., </span></p><p><span style=\" font-size:14pt; color:#010000;\">We have 15 college going students &amp; 35 school going students. Presently we have 1 doing M. A,1 in M.Sc, 2 in B.Tech, 4 in Degree course 3 in Diploma (Polytechnic),. and 4 in Jr.college. </span></p><p><span style=\" font-size:14pt; color:#010000;\">All the School going students are studying in school-Saraswathi Sishu Mandir and the Annual School fees is Rs 5.00 lacs and for college students it is about Rs 3.0 lacs. </span></p><p><span style=\" font-size:14pt; color:#010000;\">Our Second Service Cum Skill development Centre - Karunya Bharathi is under construction at Kurma Basti, Keshavgiri,Chandrayangutta</span></p></body></html>"))
        self.label_011.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">OUR REGULAR ACTIVITES</span></p></body></html>"))
        self.label_012.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; color:#010000;\">• Monthly Homayagnamu (Every first Sunday of the month) </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Library &amp; reading room for students • Tuition classes to students </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Bhagavad Gita classes </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Educational Tours to Students </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Medical camps/Yoga classes </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Computer Training </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Water camps in Summer </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Personality Development classes on every Sunday </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Job oriented Training classes to inmate students </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Participation in Sports &amp; Other Competitions </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Celebrate all important Hindu Festivals and Birth &amp; Death Anniversaries of great personalities of India </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Karunya Sindhu Computer Training Centre </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Mana Samskruthi Tharagathulu </span></p><p><span style=\" font-size:14pt; color:#010000;\">• Karunya Sindhu Coaching Centre </span></p></body></html>"))
        self.label_013.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">SCHEMES FOR DONORS</span></p></body></html>"))
        self.label_014.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#010000;\">(For details contact our office on phone or in person) </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Nitya Annadhana Nidhi</span><span style=\" font-size:14pt; color:#010000;\">- For Birthday, Marriage Day celebrations &amp; Anniversaries </span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">-Rs 2000 per event </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Shaswitha Annadhana Nidhi </span><span style=\" font-size:14pt; color:#010000;\">-These schemes are for those who celebrate occasions like Birth days, marriage days,other important days of joyful occasions on selected day of the year for ten years.</span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">-Rs 10,000/- once </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Smruthi Nidhi</span><span style=\" font-size:14pt; color:#010000;\">–In memory of beloved people who left abode </span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">-Rs 2000/- event or Rs 10000/- once for one selected day of the year for ten years </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Vidyarthi Samraksha Nidhi</span><span style=\" font-size:14pt; color:#010000;\">– To meet the general expenses of orphan students </span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">- Any amount </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Vidyarthi PoshakaNidhi</span><span style=\" font-size:14pt; color:#010000;\"> – To meet yearly expenses of a student </span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">–Rs 25000/- per year </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Vidyarthi Pathashala Rusumu Nidhi</span><span style=\" font-size:14pt; color:#010000;\">-To meet the school/college fees of students. </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Patron</span><span style=\" font-size:14pt; color:#010000;\">–As may be approved by the Executive Committee of the organisation </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">General Donors</span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">–Any amount desired by the Donor </span></p><p><span style=\" font-size:14pt; color:#010000;\">• </span><span style=\" font-size:14pt; font-weight:600; color:#010000;\">Ashraya Datha scheme </span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">–Rs 500000/- &amp; above.</span></p></body></html>"))
        self.label_015.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">DONATIONS IN CASH AND KIND ARE WELCOME </span></p><p><span style=\" font-size:12pt; font-weight:600;\">(Donations are exempted under 80G of the IT Act 1961)</span></p></body></html>"))
        self.label_016.setText(QCoreApplication.translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#010000;\">DONATIONS CAN BE SENT TO OUR BANK DIRECTLY OR PAID AT OUR OFFICE</span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline; color:#010000;\">Bank Details:</span><span style=\" font-size:14pt; color:#010000;\"><br/></span></p><p align=\"center\"><span style=\" font-size:14pt; color:#010000;\">State Bank of India, P&amp;T Colony, Hyderabad-500 060 <br/></span></p><p align=\"center\"><span style=\" font-size:14pt; color:#010000;\">SB Account No. 62153473969 </span></p><p align=\"center\"><span style=\" font-size:14pt; color:#010000;\">IFSC Code: SBIN0020864, MICR Code:500002384 </span></p><p align=\"center\"><span style=\" font-size:14pt;\"><br/></span></p><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#ff0000;\">COME &amp; JOIN US TO ENJOY SERVING THE NEEDY ORPHANS </span></p><p align=\"right\"><span style=\" font-size:14pt;\"><br/></span></p><p align=\"right\"><span style=\" font-size:14pt; color:#ff0000;\">Executive Committee </span></p><p align=\"right\"><span style=\" font-size:14pt; color:#010000;\">Karunasri Seva Samithi</span></p></body></html>"))
        self.textEditcredits.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(255, 255, 255, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; text-decoration: underline; color:#ff0000;\">CHITRAGUPTA -ACCOUNTING SOFTWARE</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;color:#000000;\">(FOR KARUNASRI SEVA SAMITHI)</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:20pt; font-weight:600; text-decoration: underline; color:#ff0000;\">TEAM</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Development Team</span><span style=\" font-size:16pt; color:#ff0000;\">:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">1.  </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri CH V S Anirudh</span><span style=\" font-size:12pt;color:#000000;\">, III BE (IT), Vasavi College of Engineering, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">2. </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri. Kaushal Attaluri,</span><span style=\" font-size:12pt;color:#000000;\"> III BE (IT), Vasavi College of Engineering, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">3. </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri. T K Subramanyam,</span><span style=\" font-size:12pt;color:#000000;\"> III BE (IT), Vasavi College of Engineering, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">4. </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri. J Vinay Shankar,</span><span style=\" font-size:12pt;color:#000000;\"> III BE (IT), Vasavi College of Engineering, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">5. S</span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">ri. K V Sidhartha,</span><span style=\" font-size:12pt;color:#000000;\"> III BE (IT), Vasavi College of Engineering, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">6. </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri. G Sai Jishnu,</span><span style=\" font-size:12pt;color:#000000;\"> IV BTech (CSE), N N R G College of Engineering, Hyderabad.  </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;\"> </span><span style=\" font-size:12pt;color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Support Team:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">1. </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri Edla Krishna</span><span style=\" font-size:12pt;color:#000000;\">, MA: Contents Support, Karunya Sindhu Ashram, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">2. </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">Sri D Sohan</span><span style=\" font-size:12pt;color:#000000;\"> : Artist, Karunya Sindhu Ashram, Hyderabad. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\">Domain Experts &amp; Guides:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; color:#ff0000;\"> </span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">1</span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">. Dr CH N A B Sankar</span><span style=\" font-size:12pt;color:#000000;\">, Scientist \'F\', CAIR, DRDO. </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; font-style:italic;color:#000000;\">Initiation, Conceptualization and Technical Guidance</span><span style=\" font-size:12pt;color:#000000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">2.  </span><span style=\" font-size:12pt; font-weight:600;color:#000000;\">CMA Rajapeta Satyanarayana</span><span style=\" font-size:12pt;color:#000000;\">, M. Com, FCMA </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;color:#000000;\">General Manager (Finance &amp; Accts)-Retd., Lubrizol India Pvt. Ltd. Mumbai </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic;color:#000000;\">Contents Development Guide.</span><span style=\" font-size:12pt;\"> </span></p></body></html>"))
        
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", "First name"))
        self.label_5.setText(QCoreApplication.translate("MainWindow", "Adhaar Id"))
        self.label_0.setText(QCoreApplication.translate("MainWindow", "Pan Id"))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "Address"))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Phone number"))
        self.label_14.setText(QCoreApplication.translate("MainWindow", "Email Id:"))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("MainWindow", "Last name"))
        #self.lineEdit_13.setPlaceholderText(QCoreApplication.translate("MainWindow", "email"))
        self.label_2.setText(QCoreApplication.translate("MainWindow", "Name"))
        #self.comboBox_12.setItemText(0, QCoreApplication.translate("MainWindow", "Adhaar Id"))
        #self.comboBox_12.setItemText(1, QCoreApplication.translate("MainWindow", "Pan Card"))
        self.label_16.setText(QCoreApplication.translate("MainWindow", "New Donor"))
        self.textEdit_au.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { black-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:10px; margin-bottom:10px; margin-left:10px; margin-right:10px; -qt-block-indent:0; text-indent:5px;\"><br /></p></body></html>"))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", "Make New Donation"))

        self.label2.setText(QCoreApplication.translate("MainWindow", "Make New Donation"))
        self.textEdit211.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Reference</span></p></body></html>"))
        self.label_214.setText(QCoreApplication.translate("MainWindow", "Name of Donor"))
        self.label_217.setText(QCoreApplication.translate("MainWindow", "Annadhanam Master registration number"))
        self.label_212.setText(QCoreApplication.translate("MainWindow", "Donation in whose name"))
        self.lineEdit_212.setPlaceholderText(QCoreApplication.translate("MainWindow", "Name"))
        #self.lineEdit_217.setText(QCoreApplication.translate("MainWindow", "Last Name"))
        self.label_213.setText(QCoreApplication.translate("MainWindow", "Date Of Donation"))
        self.lineEdit_216.setPlaceholderText(QCoreApplication.translate("MainWindow", " Name "))
        self.label_215.setText(QCoreApplication.translate("MainWindow", "Date of Arrangement"))
        self.label_218.setText(QCoreApplication.translate("MainWindow", "Book number & receipt number"))
        self.label_216.setText(QCoreApplication.translate("MainWindow", "Mode of Donation"))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", "Cash"))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", "Cheque"))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", "Direct remittance to bank"))
        self.label_219.setText(QCoreApplication.translate("MainWindow", "Ocassion"))
        self.lineEdit_2115.setPlaceholderText(QCoreApplication.translate("MainWindow", "Amount"))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainWindow", "B.D"))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainWindow", "M.D"))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainWindow", "S.D"))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainWindow", "Jayanthi"))
        self.comboBox_3.setItemText(4, QCoreApplication.translate("MainWindow", "Vardanthi"))
        self.comboBox_3.setItemText(5, QCoreApplication.translate("MainWindow", "Others"))
        self.textEdit_212.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Sponsors</p></body></html>"))
        self.label_2110.setText(QCoreApplication.translate("MainWindow", "Category"))
        #self.comboBox_4.setItemText(0, QCoreApplication.translate("MainWindow", "Nitya Annadhana Nidhi"))
        #self.comboBox_4.setItemText(1, QCoreApplication.translate("MainWindow", "Shaswitha Annadhana Nidhi"))
        #self.comboBox_4.setItemText(2, QCoreApplication.translate("MainWindow", "Smruthi Nidhi"))
        #self.comboBox_4.setItemText(3, QCoreApplication.translate("MainWindow", "Vidyarthi Poshaka Nidhi"))
        #self.comboBox_4.setItemText(4, QCoreApplication.translate("MainWindow", "Vidyarthi Patashala Rusumu Nidhi"))
        #self.comboBox_4.setItemText(5, QCoreApplication.translate("MainWindow", "Vidyarthi Samraksha Nidhi"))
        #self.comboBox_4.setItemText(6, QCoreApplication.translate("MainWindow", "Patron"))
        #self.comboBox_4.setItemText(7, QCoreApplication.translate("MainWindow", "General Donors"))
        self.label_2111.setText(QCoreApplication.translate("MainWindow", "Donation for student"))
        self.label_2112.setText(QCoreApplication.translate("MainWindow", "Phone number"))
        self.pushButton_212.setText(QCoreApplication.translate("MainWindow", u"Confirm Donation", None))
        

        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"Donations", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Phone Number", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Get Details", None))
        self.pushButton2.setText(QCoreApplication.translate("MainWindow", u"Get Donor Donations", None))
        self.labelVersion_3.setText(QCoreApplication.translate("MainWindow", u"Enter Phone number for exsisting donor details.", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"All donations made for today", None))
      #  self.checkBox.setText(QCoreApplication.translate("MainWindow", u"CheckBox", None))
       # self.radioButton.setText(QCoreApplication.translate("MainWindow", u"RadioButton", None))
        #self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Test 1", None))
        #self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Test 2", None))
        #self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Test 3", None))
        #self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Test 4", None))
        
        self.new_donation_btn.setText(QCoreApplication.translate("MainWindow", u"New Donation", None))
        self.new_donor.setText(QCoreApplication.translate("MainWindow", u"New Donor", None))
        self.reports.setText(QCoreApplication.translate("MainWindow", u"Analysis", None))
        self.remainders.setText(QCoreApplication.translate("MainWindow", u"Donation Reminders", None))
        
        self.label31.setText(QCoreApplication.translate("MainWindow", "Expenditures"))
        self.commandLinkButton_312.setText(QCoreApplication.translate("MainWindow", u"Cash Book", None))
        self.commandLinkButton_314.setText(QCoreApplication.translate("MainWindow", u"New Expenditure", None))
        self.commandLinkButton_313.setText(QCoreApplication.translate("MainWindow", u"Analysis and Student Details", None))
        self.commandLinkButton_315.setText(QCoreApplication.translate("MainWindow", u"Bank", None))
        self.commandLinkButton_316.setText(QCoreApplication.translate("MainWindow", u"Add expenditure category", None))
        self.label_312.setText(QCoreApplication.translate("MainWindow", "Today\'s Expenditure"))
        self.label_313.setText(QCoreApplication.translate("MainWindow", "Yesterday\'s Expenditure"))
        self.label_314.setText(QCoreApplication.translate("MainWindow", "This Week\'s Expenditure"))
        self.label_315.setText(QCoreApplication.translate("MainWindow", "Basic Statistics"))
        
        #self.label31.setText(QCoreApplication.translate("MainWindow", "Expenditures"))
        #self.commandLinkButton_312.setText((QCoreApplication.translate("MainWindow", "Cash Book"))
        #self.label_314.setText(QCoreApplication.translate("MainWindow", "This Week\'s Expenditure"))
        #self.commandLinkButton_313.setText(QCoreApplication.translate("MainWindow", "Analysis and Student Details"))
        #self.commandLinkButton_314.setText(QCoreApplication.translate("MainWindow", "New Expenditure"))
        #self.label_313.setText(QCoreApplication.translate("MainWindow", "Yesterday\'s Expenditure"))
        #self.label_312.setText(QCoreApplication.translate("MainWindow", "Today\'s Expenditure "))
        #self.label_315.setText(QCoreApplication.translate("MainWindow", "Basic Statistics"))

        self.label_416.setText(QCoreApplication.translate("MainWindow", "New Student"))
        #self.label_47.setText(QCoreApplication.translate("MainWindow", "Studying"))
        self.label_42.setText(QCoreApplication.translate("MainWindow", "Name"))
        self.lineEdit_43.setText(QCoreApplication.translate("MainWindow", "Last name"))
        self.label4.setText(QCoreApplication.translate("MainWindow", "Student id"))
        self.lineEdit_42.setPlaceholderText(QCoreApplication.translate("MainWindow", "First name"))
        self.label_46.setText(QCoreApplication.translate("MainWindow", "Date of birth"))
        self.label_44.setText(QCoreApplication.translate("MainWindow", "Do you want to proceed?"))
        self.textEdit4.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label_48.setText(QCoreApplication.translate("MainWindow", "Student Details"))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", "SAVE"))

        self.lineEdit_57.setPlaceholderText(QCoreApplication.translate("MainWindow", "Enter master id"))
        self.label_55.setText(QCoreApplication.translate("MainWindow", "CODE"))
        self.label_54.setText(QCoreApplication.translate("MainWindow", "In cash/ Cheque No."))
        self.lineEdit_52.setPlaceholderText(QCoreApplication.translate("MainWindow", "Paid To"))
        self.label.setText(QCoreApplication.translate("MainWindow", "Amount "))
        self.label_516.setText(QCoreApplication.translate("MainWindow", "DEBIT VOUCHER"))
        self.label_52.setText(QCoreApplication.translate("MainWindow", "Name"))
        self.label_56.setText(QCoreApplication.translate("MainWindow", "          Dated        "))
        self.lineEdit_53.setPlaceholderText(QCoreApplication.translate("MainWindow", "Amount in Rs"))
        self.label_57.setText(QCoreApplication.translate("MainWindow", "bank, towards"))
        self.radioButton_52.setText(QCoreApplication.translate("MainWindow", "Checked by master"))
        self.label_58.setText(QCoreApplication.translate("MainWindow", "Voucher number"))
        self.label_59.setText(QCoreApplication.translate("MainWindow", "Master id"))
        self.label_53.setText(QCoreApplication.translate("MainWindow", "           Date"))
        self.label_510.setText(QCoreApplication.translate("MainWindow", "       Drawn on"))
        self.pushButton_52.setText(QCoreApplication.translate("MainWindow", "OK"))

        self.label_73.setText(QCoreApplication.translate("MainWindow", "School/College Address"))
        self.label_711.setText(QCoreApplication.translate("MainWindow", "Aadhar no."))
        self.label_712.setText(QCoreApplication.translate("MainWindow", "Studying"))
        self.label_79.setText(QCoreApplication.translate("MainWindow", "student id"))
        self.textEdit7.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))
        self.label_74.setText(QCoreApplication.translate("MainWindow", "Anual Fee"))
        self.lineEdit_72.setPlaceholderText(QCoreApplication.translate("MainWindow", "First name"))
        self.pushButton7.setText(QCoreApplication.translate("MainWindow", "Get details"))
        self.pushButton78.setText(QCoreApplication.translate("MainWindow", "Update details"))
        self.label_716.setText(QCoreApplication.translate("MainWindow", "Update/Get Student Details"))
        self.lineEdit_73.setPlaceholderText(QCoreApplication.translate("MainWindow", "Last name"))
        self.label_75.setText(QCoreApplication.translate("MainWindow", "School/College Name"))
        self.label_710.setText(QCoreApplication.translate("MainWindow", "Fee Paid"))
        self.label_72.setText(QCoreApplication.translate("MainWindow", "Name"))
        self.label_713.setText(QCoreApplication.translate("MainWindow", "Academic Year"))
        self.lineEdit_73.setPlaceholderText(QCoreApplication.translate("MainWindow", "Last name"))


        self.label9.setText(QCoreApplication.translate("MainWindow", "Analysis Of Donations"))
        self.pushButton_92.setText(QCoreApplication.translate("MainWindow", "Get all Donations"))
        self.label_92.setText(QCoreApplication.translate("MainWindow", "From Date"))
        self.label_93.setText(QCoreApplication.translate("MainWindow", "To Date"))
        self.pushButton_93.setText(QCoreApplication.translate("MainWindow", "Get Analysis"))
        self.pushButton_94.setText(QCoreApplication.translate("MainWindow", "Generate PDF"))
        self.label_94.setText(QCoreApplication.translate("MainWindow", "Donations From Various Schemes"))
        self.label_95.setText(QCoreApplication.translate("MainWindow", "Total amount recieved by donations"))
       # self.commandLinkButton.setDescription(QCoreApplication.translate("MainWindow", u"Open External Link", None))
       

        self.labelBoxBlenderInstalation6.setText(QCoreApplication.translate("MainWindow", "CASH BOOK"))
        self.label_62.setText(QCoreApplication.translate("MainWindow", "From date:"))
        self.label_63.setText(QCoreApplication.translate("MainWindow", "          To date:"))
        self.pushButton6.setText(QCoreApplication.translate("MainWindow", "Get results"))
        self.label_64.setText(QCoreApplication.translate("MainWindow", "Petty cashbook:"))
        self.tableWidget6.setSortingEnabled(False)
        item = self.tableWidget6.verticalHeaderItem(0)
        item.setText(QCoreApplication.translate("MainWindow", "New Row"))
        item = self.tableWidget6.verticalHeaderItem(1)
        item.setText(QCoreApplication.translate("MainWindow", "New Row"))
        item = self.tableWidget6.horizontalHeaderItem(0)
        item.setText(QCoreApplication.translate("MainWindow", "Transaction"))
        item = self.tableWidget6.horizontalHeaderItem(1)
        item.setText(QCoreApplication.translate("MainWindow", "Category"))
        item = self.tableWidget6.horizontalHeaderItem(2)
        item.setText(QCoreApplication.translate("MainWindow", "Debit"))
        item = self.tableWidget6.horizontalHeaderItem(3)
        item.setText(QCoreApplication.translate("MainWindow", "Credit"))
        item = self.tableWidget6.horizontalHeaderItem(4)
        item.setText(QCoreApplication.translate("MainWindow", "Balance"))
        self.label_68.setText(QCoreApplication.translate("MainWindow", "Total debitted:"))
        self.label_65.setText(QCoreApplication.translate("MainWindow", "Total creditted:"))
        

        self.label_87.setText(QCoreApplication.translate("MainWindow", "New User"))
        self.label_813.setText(QCoreApplication.translate("MainWindow", "Designation"))
        self.label_814.setText(QCoreApplication.translate("MainWindow", "What is your favourite dish?"))
        self.radioButton_82.setText(QCoreApplication.translate("MainWindow", "Master User"))
        self.radioButton8.setText(QCoreApplication.translate("MainWindow", "Normal User"))
        self.label_810.setText(QCoreApplication.translate("MainWindow", "Username"))
        self.label_812.setText(QCoreApplication.translate("MainWindow", "Confirm Password"))
        self.lineEdit8.setPlaceholderText(QCoreApplication.translate("MainWindow", "First Name"))
        self.label_89.setText(QCoreApplication.translate("MainWindow", "Last Name"))
        self.lineEdit_84.setPlaceholderText(QCoreApplication.translate("MainWindow", "Password"))
        self.label_88.setText(QCoreApplication.translate("MainWindow", "First Name"))
        self.label_811.setText(QCoreApplication.translate("MainWindow", "Password"))
        self.lineEdit_83.setPlaceholderText(QCoreApplication.translate("MainWindow", "Username"))
        self.lineEdit_86.setPlaceholderText(QCoreApplication.translate("MainWindow", "Re-enter Password"))
        self.lineEdit_82.setPlaceholderText(QCoreApplication.translate("MainWindow", "Last Name"))
        self.pushButton_82.setText(QCoreApplication.translate("MainWindow", "Add User"))

        self.label10.setText(QCoreApplication.translate("MainWindow", "Analysis Of Expenditure"))
        self.pushButton_102.setText(QCoreApplication.translate("MainWindow", "Get all Expenditures"))
        self.pushButton_106.setText(QCoreApplication.translate("MainWindow", "Get PDF"))
        self.pushButton_104.setText(QCoreApplication.translate("MainWindow", "Add Student"))
        self.pushButton_105.setText(QCoreApplication.translate("MainWindow", "Update Student Details"))
        self.label_102.setText(QCoreApplication.translate("MainWindow", "From Date"))
        self.label_103.setText(QCoreApplication.translate("MainWindow", "To Date"))
        self.pushButton_103.setText(QCoreApplication.translate("MainWindow", "Get Analysis"))
        self.label_105.setText(QCoreApplication.translate("MainWindow", "Total amount recieved by expenditures"))

        self.labelBoxBlenderInstalation11.setText(QCoreApplication.translate("MainWindow", "EXPENDITURE CONFIRMATION"))
        self.pushButton_114.setText(QCoreApplication.translate("MainWindow", "Edit"))
        self.pushButton_112.setText(QCoreApplication.translate("MainWindow", "Confirm"))

        self.labelBoxBlenderInstalation12.setText(QCoreApplication.translate("MainWindow", "DONATION CONFIRMATION"))
        self.pushButton_134.setText(QCoreApplication.translate("MainWindow", "Edit"))
        self.pushButton_132.setText(QCoreApplication.translate("MainWindow", "Confirm"))

        self.label12.setText(QCoreApplication.translate("MainWindow", "Donation Reminders"))
        
        self.pushButton_122.setText(QCoreApplication.translate("MainWindow", "Reminded"))
        self.pushButton_123.setText(QCoreApplication.translate("MainWindow", "Mailing List"))

        self.label14.setText(QCoreApplication.translate("MainWindow", "Bank Statement "))
        self.label_142.setText(QCoreApplication.translate("MainWindow", "From"))
        self.label_143.setText(QCoreApplication.translate("MainWindow", " To"))
        self.label_144.setText(QCoreApplication.translate("MainWindow", "Choose Bank"))
        self.pushButton14.setText(QCoreApplication.translate("MainWindow", "Get Statement"))
        self.pushButton141.setText(QCoreApplication.translate("MainWindow", "Add Bank Account"))
        self.pushButton142.setText(QCoreApplication.translate("MainWindow", "Add Manual Transaction"))

        self.label15.setText(QCoreApplication.translate("MainWindow", "Add Scheme"))
        self.lineEdit_153.setPlaceholderText(QCoreApplication.translate("MainWindow", "number of days"))
        self.label_152.setText(QCoreApplication.translate("MainWindow", "Scheme Name:"))
        self.lineEdit_152.setPlaceholderText(QCoreApplication.translate("MainWindow", "in years"))
        self.label_153.setText(QCoreApplication.translate("MainWindow", "Validity"))
        self.label_154.setText(QCoreApplication.translate("MainWindow", "Reminder (in days)"))
        self.label_156.setText(QCoreApplication.translate("MainWindow", "Scheme id"))
        self.pushButton15.setText(QCoreApplication.translate("MainWindow", "Add scheme"))

        self.label_182.setText(QCoreApplication.translate("MainWindow", "Category name"))
        self.label_183.setText(QCoreApplication.translate("MainWindow", "Category Code"))
        self.label.setText(QCoreApplication.translate("MainWindow", "                                                    Add Category"))
        self.pushButton_182.setText(QCoreApplication.translate("MainWindow", "Add category"))

        self.radioButton_192.setText(QCoreApplication.translate("MainWindow", "Withdrawal"))
        self.label_192.setText(QCoreApplication.translate("MainWindow", "Date"))
        self.label_195.setText(QCoreApplication.translate("MainWindow", "Discription"))
        self.label_194.setText(QCoreApplication.translate("MainWindow", "Enter Amount"))
        self.label19.setText(QCoreApplication.translate("MainWindow", "                                          Manual Transaction"))
        self.radioButton_193.setText(QCoreApplication.translate("MainWindow", "Deposit/Intrest"))
        self.label_193.setText(QCoreApplication.translate("MainWindow", "Select Bank"))
        self.pushButton_192.setText(QCoreApplication.translate("MainWindow", "Confirm Transaction"))

        self.label17.setText(QCoreApplication.translate("MainWindow", "Withdraw from Bank"))
        self.label_172.setText(QCoreApplication.translate("MainWindow", "Date"))
        self.label_173.setText(QCoreApplication.translate("MainWindow", "Amount"))
        self.label_174.setText(QCoreApplication.translate("MainWindow", "Bank"))
        self.label_175.setText(QCoreApplication.translate("MainWindow", "Description"))
        self.pushButton17.setText(QCoreApplication.translate("MainWindow", "WithDraw"))
        self.textEdit17.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

        self.label116.setText(QCoreApplication.translate("MainWindow", "Add Bank Account"))
        self.label_163.setText(QCoreApplication.translate("MainWindow", "Bank Details"))
        self.label_162.setText(QCoreApplication.translate("MainWindow", "Bank name & Branch"))
        self.label16.setText(QCoreApplication.translate("MainWindow", "Bank name (in application)"))
        self.lineEdit_162.setPlaceholderText(QCoreApplication.translate("MainWindow", "This name would be displayed for further references"))
        self.pushButton16.setText(QCoreApplication.translate("MainWindow", "Add Account"))
        self.textEdit16.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

        self.textEdit19.setHtml(QCoreApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n""body { background-color: rgba(66, 73, 90, 255);}"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"Registered by: Team Chitra Gupta", None))
        self.label_version.setText(QCoreApplication.translate("MainWindow", u"v1.1.0", None))
    # retranslateUi
