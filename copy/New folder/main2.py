import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QDialog, QApplication,QFileDialog,QMainWindow,QLabel,QLineEdit,QWidget,QMessageBox
from PyQt5.QtGui import QPixmap,QIcon
from PyQt5.uic import  loadUiType
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer

import os
from os import path
def resource_path(relative_path):
    base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

import sqlite3
db=sqlite3.connect(resource_path("data.db"))
cursor=db.cursor()
# print(user_id)

ui,_=loadUiType(resource_path('main2.ui'))

class MainApp(QMainWindow, ui):

    def __init__(self,count,user_id,date,dateto,no_of_forms,fileDone,email):
        # super(QMainWindow, self).__init__(parent)
        QMainWindow.__init__(self)
        self.email=email
        self.no_of_forms=no_of_forms
        self.fileDone=fileDone
        self.count=count
        self.user_id=user_id
        self.date=date.split(" ")
        self.createdDate = QDate.fromString(self.date[0], "yyyy-M-d")
        self.dateto=dateto.split(" ")
        self.postDate = QDate.fromString(self.dateto[0], "yyyy-M-d")
        
        # print("createdDate {}".format(self.createdDate))
        # print("createdDate Convert {}".format(self.createdDate.toString(Qt.ISODate)))
        self.setupUi(self)
        self.setFixedSize(1028,700)
        self.setWindowIcon(QIcon('icon.ico'))

        # self.DictValue={"isTrue":False}

        self.current=0
        self.found=None
        r=cursor.execute("SELECT * FROM DATA WHERE USER_ID=?",[self.user_id])
        self.found=r.fetchall()

        self.onOpenMainWindow()
        
        # self.setWindowState(Qt.WindowMaximized)

        #----------Left group button enable Disable ------------#
        self.pushButton_group1.clicked.connect(self.enableGroup1)
        self.pushButton_group2.clicked.connect(self.enableGroup2)
        self.pushButton_group3.clicked.connect(self.enableGroup3)

        self.scrollArea.setEnabled(True)
        self.scrollArea_2.setEnabled(False)
        self.scrollArea_3.setEnabled(False)
        self.pushButton_group1.setEnabled(False)

        self.pushButton_close.clicked.connect(self.close)
        self.pushButton_new.clicked.connect(self.newFormButton)
        self.filename=""
        self.btn1.clicked.connect(self.getImage)
        self.pushButton_next.clicked.connect(self.nextFormValue)
        self.pushButton_prev.clicked.connect(self.prevFormValue)
        # self.disableButton()

        self.btn1_2.clicked.connect(self.saveData)
        self.pushButton_3.clicked.connect(self.submitData)

        
        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)
        self.startTimer()

        self.pushButton_9.clicked.connect(self.setValueB1)
        self.pushButton_10.clicked.connect(self.setValueI1)
        self.pushButton_11.clicked.connect(self.setValueU1)
        self.pushButton_12.clicked.connect(self.setValueR1)

        self.pushButton_13.clicked.connect(self.setValueB2)
        self.pushButton_14.clicked.connect(self.setValueI2)
        self.pushButton_15.clicked.connect(self.setValueU2)
        self.pushButton_16.clicked.connect(self.setValueR2)

        self.pushButton_17.clicked.connect(self.setValueB3)
        self.pushButton_18.clicked.connect(self.setValueI3)
        self.pushButton_19.clicked.connect(self.setValueU3)
        self.pushButton_20.clicked.connect(self.setValueR3)

        self.pushButton_21.clicked.connect(self.setValueB4)
        self.pushButton_22.clicked.connect(self.setValueI4)
        self.pushButton_23.clicked.connect(self.setValueU4)
        self.pushButton_24.clicked.connect(self.setValueR4)

        self.pushButton_25.clicked.connect(self.setValueB5)
        self.pushButton_26.clicked.connect(self.setValueI5)
        self.pushButton_27.clicked.connect(self.setValueU5)
        self.pushButton_28.clicked.connect(self.setValueR5)

        self.pushButton_29.clicked.connect(self.setValueB6)
        self.pushButton_30.clicked.connect(self.setValueI6)
        self.pushButton_31.clicked.connect(self.setValueU6)
        self.pushButton_32.clicked.connect(self.setValueR6)

        self.pushButton_33.clicked.connect(self.setValueB7)
        self.pushButton_34.clicked.connect(self.setValueI7)
        self.pushButton_35.clicked.connect(self.setValueU7)
        self.pushButton_36.clicked.connect(self.setValueR7)

        self.pushButton_37.clicked.connect(self.setValueB9)
        self.pushButton_38.clicked.connect(self.setValueI9)
        self.pushButton_39.clicked.connect(self.setValueU9)
        self.pushButton_40.clicked.connect(self.setValueR9)

        self.pushButton_41.clicked.connect(self.setValueB10)
        self.pushButton_42.clicked.connect(self.setValueI10)
        self.pushButton_43.clicked.connect(self.setValueU10)
        self.pushButton_44.clicked.connect(self.setValueR10)

        self.pushButton_45.clicked.connect(self.setValueB11)
        self.pushButton_46.clicked.connect(self.setValueI11)
        self.pushButton_47.clicked.connect(self.setValueU11)
        self.pushButton_48.clicked.connect(self.setValueR11)

        self.pushButton_65.clicked.connect(self.setValueB15)
        self.pushButton_66.clicked.connect(self.setValueI15)
        self.pushButton_67.clicked.connect(self.setValueU15)
        self.pushButton_68.clicked.connect(self.setValueR15)

        self.pushButton_49.clicked.connect(self.setValueB12)
        self.pushButton_50.clicked.connect(self.setValueI12)
        self.pushButton_51.clicked.connect(self.setValueU12)
        self.pushButton_52.clicked.connect(self.setValueR12)

        self.pushButton_57.clicked.connect(self.setValueB13)
        self.pushButton_58.clicked.connect(self.setValueI13)
        self.pushButton_59.clicked.connect(self.setValueU13)
        self.pushButton_60.clicked.connect(self.setValueR13)

        self.pushButton_53.clicked.connect(self.setValueB8)
        self.pushButton_54.clicked.connect(self.setValueI8)
        self.pushButton_55.clicked.connect(self.setValueU8)
        self.pushButton_56.clicked.connect(self.setValueR8)

        self.pushButton_61.clicked.connect(self.setValueB14)
        self.pushButton_62.clicked.connect(self.setValueI14)
        self.pushButton_63.clicked.connect(self.setValueU14)
        self.pushButton_64.clicked.connect(self.setValueR14)

        self.pushButton_69.clicked.connect(self.setValueB16)
        self.pushButton_70.clicked.connect(self.setValueI16)
        self.pushButton_71.clicked.connect(self.setValueU16)
        self.pushButton_72.clicked.connect(self.setValueR16)

        self.pushButton_73.clicked.connect(self.setValueB17)
        self.pushButton_74.clicked.connect(self.setValueI17)
        self.pushButton_75.clicked.connect(self.setValueU17)
        self.pushButton_76.clicked.connect(self.setValueR17)

        self.pushButton_77.clicked.connect(self.setValueB18)
        self.pushButton_78.clicked.connect(self.setValueI18)
        self.pushButton_79.clicked.connect(self.setValueU18)
        self.pushButton_80.clicked.connect(self.setValueR18)

        self.pushButton_85.clicked.connect(self.setValueB19)
        self.pushButton_86.clicked.connect(self.setValueI19)
        self.pushButton_87.clicked.connect(self.setValueU19)
        self.pushButton_88.clicked.connect(self.setValueR19)

        self.pushButton_89.clicked.connect(self.setValueB20)
        self.pushButton_90.clicked.connect(self.setValueI20)
        self.pushButton_91.clicked.connect(self.setValueU20)
        self.pushButton_92.clicked.connect(self.setValueR20)

        self.pushButton_93.clicked.connect(self.setValueB21)
        self.pushButton_94.clicked.connect(self.setValueI21)
        self.pushButton_95.clicked.connect(self.setValueU21)
        self.pushButton_96.clicked.connect(self.setValueR21)

        self.pushButton_97.clicked.connect(self.setValueB22)
        self.pushButton_98.clicked.connect(self.setValueI22)
        self.pushButton_99.clicked.connect(self.setValueU22)
        self.pushButton_100.clicked.connect(self.setValueR22)

        self.pushButton_101.clicked.connect(self.setValueB23)
        self.pushButton_102.clicked.connect(self.setValueI23)
        self.pushButton_103.clicked.connect(self.setValueU23)
        self.pushButton_104.clicked.connect(self.setValueR23)

        self.pushButton_105.clicked.connect(self.setValueB24)
        self.pushButton_106.clicked.connect(self.setValueI24)
        self.pushButton_107.clicked.connect(self.setValueU24)
        self.pushButton_108.clicked.connect(self.setValueR24)

        self.pushButton_109.clicked.connect(self.setValueB25)
        self.pushButton_110.clicked.connect(self.setValueI25)
        self.pushButton_111.clicked.connect(self.setValueU25)
        self.pushButton_112.clicked.connect(self.setValueR25)

        self.pushButton_113.clicked.connect(self.setValueB26)
        self.pushButton_114.clicked.connect(self.setValueI26)
        self.pushButton_115.clicked.connect(self.setValueU26)
        self.pushButton_116.clicked.connect(self.setValueR26)

        self.pushButton_117.clicked.connect(self.setValueB27)
        self.pushButton_118.clicked.connect(self.setValueI27)
        self.pushButton_119.clicked.connect(self.setValueU27)
        self.pushButton_120.clicked.connect(self.setValueR27)

        self.pushButton_121.clicked.connect(self.setValueB30)
        self.pushButton_122.clicked.connect(self.setValueI30)
        self.pushButton_123.clicked.connect(self.setValueU30)
        self.pushButton_124.clicked.connect(self.setValueR30)

        self.pushButton_125.clicked.connect(self.setValueB28)
        self.pushButton_126.clicked.connect(self.setValueI28)
        self.pushButton_127.clicked.connect(self.setValueU28)
        self.pushButton_128.clicked.connect(self.setValueR28)

        self.pushButton_129.clicked.connect(self.setValueB29)
        self.pushButton_130.clicked.connect(self.setValueI29)
        self.pushButton_131.clicked.connect(self.setValueU29)
        self.pushButton_132.clicked.connect(self.setValueR29)

        self.btn1_3.clicked.connect(self.viewSubmitData)


    def viewSubmitData(self):
        from main3 import MainApp       
        self.window3=MainApp(self.user_id)
        self.window3.show()

    def onOpenMainWindow(self):
        if (self.no_of_forms == self.fileDone):
            self.btn1_2.setEnabled(False)
            self.pushButton_3.setEnabled(True)
        else:
            self.btn1_2.setEnabled(True)
            self.pushButton_3.setEnabled(False)
        
    def nextFormValue(self):
        if self.current >= len(self.found):
            print('Next Not possible ')
        else:
            print(self.found[self.current][0])
            self.lineEdit_3.setText(self.found[self.current][2])
            self.lineEdit_4.setText(self.found[self.current][3])
            self.lineEdit_5.setText(self.found[self.current][4])
            self.textEdit.setPlainText(self.found[self.current][5])
            self.lineEdit_6.setText(self.found[self.current][6])
            self.lineEdit_7.setText(self.found[self.current][7])
            self.lineEdit_8.setText(self.found[self.current][8])
            self.lineEdit_9.setText(self.found[self.current][9])
            self.lineEdit_10.setText(self.found[self.current][10])
            self.lineEdit_11.setText(self.found[self.current][11])
            self.lineEdit_15.setText(self.found[self.current][12])
            self.lineEdit_12.setText(self.found[self.current][13])
            self.lineEdit_13.setText(self.found[self.current][14])
            self.textEdit_2.setPlainText(self.found[self.current][15])
            self.lineEdit_14.setText(self.found[self.current][16])
            self.lineEdit_16.setText(self.found[self.current][17])
            self.lineEdit_17.setText(self.found[self.current][18])
            self.lineEdit_18.setText(self.found[self.current][19])
            self.lineEdit_19.setText(self.found[self.current][20])
            self.lineEdit_20.setText(self.found[self.current][21])
            self.lineEdit_21.setText(self.found[self.current][22])
            self.lineEdit_22.setText(self.found[self.current][23])
            self.lineEdit_23.setText(self.found[self.current][24])
            self.textEdit_3.setPlainText(self.found[self.current][25])
            self.lineEdit_25.setText(self.found[self.current][26])
            self.lineEdit_26.setText(self.found[self.current][27])
            self.lineEdit_27.setText(self.found[self.current][28])
            self.lineEdit_30.setText(self.found[self.current][29])
            self.lineEdit_28.setText(self.found[self.current][30])
            self.lineEdit_29.setText(self.found[self.current][31])
            self.current += 1
            

    def prevFormValue(self):
        if self.current <=1 :
            print('Prev Not Possible ')
        else:
            self.current -= 1
            # print(self.found[self.current][0])
            self.lineEdit_3.setText(self.found[self.current-1][2])
            self.lineEdit_4.setText(self.found[self.current-1][3])
            self.lineEdit_5.setText(self.found[self.current-1][4])
            self.textEdit.setPlainText(self.found[self.current-1][5])
            self.lineEdit_6.setText(self.found[self.current-1][6])
            self.lineEdit_7.setText(self.found[self.current-1][7])
            self.lineEdit_8.setText(self.found[self.current-1][8])
            self.lineEdit_9.setText(self.found[self.current-1][9])
            self.lineEdit_10.setText(self.found[self.current-1][10])
            self.lineEdit_11.setText(self.found[self.current-1][11])
            self.lineEdit_15.setText(self.found[self.current-1][12])
            self.lineEdit_12.setText(self.found[self.current-1][13])
            self.lineEdit_13.setText(self.found[self.current-1][14])
            self.textEdit_2.setPlainText(self.found[self.current-1][15])
            self.lineEdit_14.setText(self.found[self.current-1][16])
            self.lineEdit_16.setText(self.found[self.current-1][17])
            self.lineEdit_17.setText(self.found[self.current-1][18])
            self.lineEdit_18.setText(self.found[self.current-1][19])
            self.lineEdit_19.setText(self.found[self.current-1][20])
            self.lineEdit_20.setText(self.found[self.current-1][21])
            self.lineEdit_21.setText(self.found[self.current-1][22])
            self.lineEdit_22.setText(self.found[self.current-1][23])
            self.lineEdit_23.setText(self.found[self.current-1][24])
            self.textEdit_3.setPlainText(self.found[self.current-1][25])
            self.lineEdit_25.setText(self.found[self.current-1][26])
            self.lineEdit_26.setText(self.found[self.current-1][27])
            self.lineEdit_27.setText(self.found[self.current-1][28])
            self.lineEdit_30.setText(self.found[self.current-1][29])
            self.lineEdit_28.setText(self.found[self.current-1][30])
            self.lineEdit_29.setText(self.found[self.current-1][31])
            

    def enableGroup1(self):
        self.scrollArea.setEnabled(True)
        self.scrollArea_2.setEnabled(False)
        self.scrollArea_3.setEnabled(False)
        self.pushButton_group1.setEnabled(False)
        self.pushButton_group2.setEnabled(True)
        self.pushButton_group3.setEnabled(True)
    def enableGroup2(self):
        self.scrollArea.setEnabled(False)
        self.scrollArea_2.setEnabled(True)
        self.scrollArea_3.setEnabled(False)
        self.pushButton_group1.setEnabled(True)
        self.pushButton_group2.setEnabled(False)
        self.pushButton_group3.setEnabled(True)
    def enableGroup3(self):
        self.scrollArea.setEnabled(False)
        self.scrollArea_2.setEnabled(False)
        self.scrollArea_3.setEnabled(True)
        self.pushButton_group1.setEnabled(True)
        self.pushButton_group2.setEnabled(True)
        self.pushButton_group3.setEnabled(False)



    #------------ timeDisplay -----------#
    def showTime(self):
        global timeDisplay
        time=QDateTime.currentDateTime()
        self.timeDisplay=time.toString('dd-MM-yyyy hh:mm:ss')
        self.statusBar().showMessage("Current Date {} - {}".format(self.timeDisplay,self.postDate.toString(Qt.ISODate)))

    def startTimer(self):
        self.timer.start(1000)

    def endTimer(self):
        self.timer.stop()


    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',os.getcwd(), "Image files (*.jpg *.gif *.jpeg)")
        imagePath=fname[0]
        self.filename = imagePath.split("/")[-1]
        print(self.filename)
        pixmap = QPixmap(imagePath)
        print("pixmap {} ".format(pixmap))
        print("self.imagePath {}".format(imagePath))
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setPixmap(pixmap)
        
        # pixmap2 = pixmap.scaled(720, 640, QtCore.Qt.KeepAspectRatio)
        # pixmap5 = pixmap.scaled(720, 640)
        # self.label.setPixmap(QPixmap(pixmap))
        # self.resize(pixmap.width(), pixmap.height())


    def setValueB1(self,text):
        text=self.lineEdit_3.text()
        if "<B>" in text:
            self.lineEdit_3.setText(text.replace('<B>',''))
        else:
            self.lineEdit_3.setText("<B>"+text)

    def setValueI1(self):
        text=self.lineEdit_3.text()
        if "<i>" in text:
            self.lineEdit_3.setText(text.replace('<i>',''))
        else:
            self.lineEdit_3.setText("<i>"+text)

    def setValueU1(self):
        text=self.lineEdit_3.text()
        if "<U>" in text:
            self.lineEdit_3.setText(text.replace('<U>',''))
        else:
            self.lineEdit_3.setText("<U>"+text)

    def setValueR1(self):
        text=self.lineEdit_3.text()
        if "<R>" in text:
            self.lineEdit_3.setText(text.replace('<R>',''))
        else:
            self.lineEdit_3.setText("<R>"+text)




    def setValueB2(self,text):
        text=self.lineEdit_4.text()
        if "<B>" in text:
            self.lineEdit_4.setText(text.replace('<B>',''))
        else:
            self.lineEdit_4.setText("<B>"+text)

    def setValueI2(self):
        text=self.lineEdit_4.text()
        if "<i>" in text:
            self.lineEdit_4.setText(text.replace('<i>',''))
        else:
            self.lineEdit_4.setText("<i>"+text)

    def setValueU2(self):
        text=self.lineEdit_4.text()
        if "<U>" in text:
            self.lineEdit_4.setText(text.replace('<U>',''))
        else:
            self.lineEdit_4.setText("<U>"+text)

    def setValueR2(self):
        text=self.lineEdit_4.text()
        if "<R>" in text:
            self.lineEdit_4.setText(text.replace('<R>',''))
        else:
            self.lineEdit_4.setText("<R>"+text)



    def setValueB3(self,text):
        text=self.lineEdit_5.text()
        if "<B>" in text:
            self.lineEdit_5.setText(text.replace('<B>',''))
        else:
            self.lineEdit_5.setText("<B>"+text)

    def setValueI3(self):
        text=self.lineEdit_5.text()
        if "<i>" in text:
            self.lineEdit_5.setText(text.replace('<i>',''))
        else:
            self.lineEdit_5.setText("<i>"+text)

    def setValueU3(self):
        text=self.lineEdit_5.text()
        if "<U>" in text:
            self.lineEdit_5.setText(text.replace('<U>',''))
        else:
            self.lineEdit_5.setText("<U>"+text)

    def setValueR3(self):
        text=self.lineEdit_5.text()
        if "<R>" in text:
            self.lineEdit_5.setText(text.replace('<R>',''))
        else:
            self.lineEdit_5.setText("<R>"+text)



    def setValueB4(self,text):
        text=self.textEdit.toPlainText()
        if "<B>" in text:
            self.textEdit.setPlainText(text.replace('<B>',''))
        else:
            self.textEdit.setPlainText("<B>"+text)
    def setValueI4(self):
        text=self.textEdit.toPlainText()
        if "<i>" in text:
            self.textEdit.setPlainText(text.replace('<i>',''))
        else:
            self.textEdit.setPlainText("<i>"+text)
    def setValueU4(self):
        text=self.textEdit.toPlainText()
        if "<U>" in text:
            self.textEdit.setPlainText(text.replace('<U>',''))
        else:
            self.textEdit.setPlainText("<U>"+text)

    def setValueR4(self):
        text=self.textEdit.toPlainText()
        if "<R>" in text:
            self.textEdit.setPlainText(text.replace('<R>',''))
        else:
            self.textEdit.setPlainText("<R>"+text)


    def setValueB5(self,text):
        text=self.lineEdit_6.text()
        if "<B>" in text:
            self.lineEdit_6.setText(text.replace('<B>',''))
        else:
            self.lineEdit_6.setText("<B>"+text)

    def setValueI5(self):
        text=self.lineEdit_6.text()
        if "<i>" in text:
            self.lineEdit_6.setText(text.replace('<i>',''))
        else:
            self.lineEdit_6.setText("<i>"+text)

    def setValueU5(self):
        text=self.lineEdit_6.text()
        if "<U>" in text:
            self.lineEdit_6.setText(text.replace('<U>',''))
        else:
            self.lineEdit_6.setText("<U>"+text)

    def setValueR5(self):
        text=self.lineEdit_6.text()
        if "<R>" in text:
            self.lineEdit_6.setText(text.replace('<R>',''))
        else:
            self.lineEdit_6.setText("<R>"+text)


    def setValueB6(self,text):
        text=self.lineEdit_7.text()
        if "<B>" in text:
            self.lineEdit_7.setText(text.replace('<B>',''))
        else:
            self.lineEdit_7.setText("<B>"+text)

    def setValueI6(self):
        text=self.lineEdit_7.text()
        if "<i>" in text:
            self.lineEdit_7.setText(text.replace('<i>',''))
        else:
            self.lineEdit_7.setText("<i>"+text)

    def setValueU6(self):
        text=self.lineEdit_7.text()
        if "<U>" in text:
            self.lineEdit_7.setText(text.replace('<U>',''))
        else:
            self.lineEdit_7.setText("<U>"+text)

    def setValueR6(self):
        text=self.lineEdit_7.text()
        if "<R>" in text:
            self.lineEdit_7.setText(text.replace('<R>',''))
        else:
            self.lineEdit_7.setText("<R>"+text)


    def setValueB7(self,text):
        text=self.lineEdit_8.text()
        if "<B>" in text:
            self.lineEdit_8.setText(text.replace('<B>',''))
        else:
            self.lineEdit_8.setText("<B>"+text)

    def setValueI7(self):
        text=self.lineEdit_8.text()
        if "<i>" in text:
            self.lineEdit_8.setText(text.replace('<i>',''))
        else:
            self.lineEdit_8.setText("<i>"+text)

    def setValueU7(self):
        text=self.lineEdit_8.text()
        if "<U>" in text:
            self.lineEdit_8.setText(text.replace('<U>',''))
        else:
            self.lineEdit_8.setText("<U>"+text)

    def setValueR7(self):
        text=self.lineEdit_8.text()
        if "<R>" in text:
            self.lineEdit_8.setText(text.replace('<R>',''))
        else:
            self.lineEdit_8.setText("<R>"+text)

    

    def setValueB9(self,text):
        text=self.lineEdit_9.text()
        if "<B>" in text:
            self.lineEdit_9.setText(text.replace('<B>',''))
        else:
            self.lineEdit_9.setText("<B>"+text)

    def setValueI9(self):
        text=self.lineEdit_9.text()
        if "<i>" in text:
            self.lineEdit_9.setText(text.replace('<i>',''))
        else:
            self.lineEdit_9.setText("<i>"+text)

    def setValueU9(self):
        text=self.lineEdit_9.text()
        if "<U>" in text:
            self.lineEdit_9.setText(text.replace('<U>',''))
        else:
            self.lineEdit_9.setText("<U>"+text)

    def setValueR9(self):
        text=self.lineEdit_9.text()
        if "<R>" in text:
            self.lineEdit_9.setText(text.replace('<R>',''))
        else:
            self.lineEdit_9.setText("<R>"+text)


    def setValueB10(self,text):
        text=self.lineEdit_10.text()
        if "<B>" in text:
            self.lineEdit_10.setText(text.replace('<B>',''))
        else:
            self.lineEdit_10.setText("<B>"+text)

    def setValueI10(self):
        text=self.lineEdit_10.text()
        if "<i>" in text:
            self.lineEdit_10.setText(text.replace('<i>',''))
        else:
            self.lineEdit_10.setText("<i>"+text)

    def setValueU10(self):
        text=self.lineEdit_10.text()
        if "<U>" in text:
            self.lineEdit_10.setText(text.replace('<U>',''))
        else:
            self.lineEdit_10.setText("<U>"+text)

    def setValueR10(self):
        text=self.lineEdit_10.text()
        if "<R>" in text:
            self.lineEdit_10.setText(text.replace('<R>',''))
        else:
            self.lineEdit_10.setText("<R>"+text)


    def setValueB11(self,text):
        text=self.lineEdit_11.text()
        if "<B>" in text:
            self.lineEdit_11.setText(text.replace('<B>',''))
        else:
            self.lineEdit_11.setText("<B>"+text)

    def setValueI11(self):
        text=self.lineEdit_11.text()
        if "<i>" in text:
            self.lineEdit_11.setText(text.replace('<i>',''))
        else:
            self.lineEdit_11.setText("<i>"+text)

    def setValueU11(self):
        text=self.lineEdit_11.text()
        if "<U>" in text:
            self.lineEdit_11.setText(text.replace('<U>',''))
        else:
            self.lineEdit_11.setText("<U>"+text)

    def setValueR11(self):
        text=self.lineEdit_11.text()
        if "<R>" in text:
            self.lineEdit_11.setText(text.replace('<R>',''))
        else:
            self.lineEdit_11.setText("<R>"+text)


    def setValueB15(self,text):
        text=self.lineEdit_15.text()
        if "<B>" in text:
            self.lineEdit_15.setText(text.replace('<B>',''))
        else:
            self.lineEdit_15.setText("<B>"+text)
    def setValueI15(self):
        text=self.lineEdit_15.text()
        if "<i>" in text:
            self.lineEdit_15.setText(text.replace('<i>',''))
        else:
            self.lineEdit_15.setText("<i>"+text)
    def setValueU15(self):
        text=self.lineEdit_15.text()
        if "<U>" in text:
            self.lineEdit_15.setText(text.replace('<U>',''))
        else:
            self.lineEdit_15.setText("<U>"+text)
    def setValueR15(self):
        text=self.lineEdit_15.text()
        if "<R>" in text:
            self.lineEdit_15.setText(text.replace('<R>',''))
        else:
            self.lineEdit_15.setText("<R>"+text)


    def setValueB12(self,text):
        text=self.lineEdit_12.text()
        if "<B>" in text:
            self.lineEdit_12.setText(text.replace('<B>',''))
        else:
            self.lineEdit_12.setText("<B>"+text)
    def setValueI12(self):
        text=self.lineEdit_12.text()
        if "<i>" in text:
            self.lineEdit_12.setText(text.replace('<i>',''))
        else:
            self.lineEdit_12.setText("<i>"+text)
    def setValueU12(self):
        text=self.lineEdit_12.text()
        if "<U>" in text:
            self.lineEdit_12.setText(text.replace('<U>',''))
        else:
            self.lineEdit_12.setText("<U>"+text)
    def setValueR12(self):
        text=self.lineEdit_12.text()
        if "<R>" in text:
            self.lineEdit_12.setText(text.replace('<R>',''))
        else:
            self.lineEdit_12.setText("<R>"+text)


    def setValueB13(self,text):
        text=self.lineEdit_13.text()
        if "<B>" in text:
            self.lineEdit_13.setText(text.replace('<B>',''))
        else:
            self.lineEdit_13.setText("<B>"+text)
    def setValueI13(self):
        text=self.lineEdit_13.text()
        if "<i>" in text:
            self.lineEdit_13.setText(text.replace('<i>',''))
        else:
            self.lineEdit_13.setText("<i>"+text)
    def setValueU13(self):
        text=self.lineEdit_13.text()
        if "<U>" in text:
            self.lineEdit_13.setText(text.replace('<U>',''))
        else:
            self.lineEdit_13.setText("<U>"+text)
    def setValueR13(self):
        text=self.lineEdit_13.text()
        if "<R>" in text:
            self.lineEdit_13.setText(text.replace('<R>',''))
        else:
            self.lineEdit_13.setText("<R>"+text)


    def setValueB8(self,text):
        text=self.textEdit_2.toPlainText()
        if "<B>" in text:
            self.textEdit_2.setPlainText(text.replace('<B>',''))
        else:
            self.textEdit_2.setPlainText("<B>"+text)
    def setValueI8(self):
        text=self.textEdit_2.toPlainText()
        if "<i>" in text:
            self.textEdit_2.setPlainText(text.replace('<i>',''))
        else:
            self.textEdit_2.setPlainText("<i>"+text)
    def setValueU8(self):
        text=self.textEdit_2.toPlainText()
        if "<U>" in text:
            self.textEdit_2.setPlainText(text.replace('<U>',''))
        else:
            self.textEdit_2.setPlainText("<U>"+text)

    def setValueR8(self):
        text=self.textEdit_2.toPlainText()
        if "<R>" in text:
            self.textEdit_2.setPlainText(text.replace('<R>',''))
        else:
            self.textEdit_2.setPlainText("<R>"+text)


    def setValueB14(self,text):
        text=self.lineEdit_14.text()
        if "<B>" in text:
            self.lineEdit_14.setText(text.replace('<B>',''))
        else:
            self.lineEdit_14.setText("<B>"+text)
    def setValueI14(self):
        text=self.lineEdit_14.text()
        if "<i>" in text:
            self.lineEdit_14.setText(text.replace('<i>',''))
        else:
            self.lineEdit_14.setText("<i>"+text)
    def setValueU14(self):
        text=self.lineEdit_14.text()
        if "<U>" in text:
            self.lineEdit_14.setText(text.replace('<U>',''))
        else:
            self.lineEdit_14.setText("<U>"+text)
    def setValueR14(self):
        text=self.lineEdit_14.text()
        if "<R>" in text:
            self.lineEdit_14.setText(text.replace('<R>',''))
        else:
            self.lineEdit_14.setText("<R>"+text)


    def setValueB16(self,text):
        text=self.lineEdit_16.text()
        if "<B>" in text:
            self.lineEdit_16.setText(text.replace('<B>',''))
        else:
            self.lineEdit_16.setText("<B>"+text)
    def setValueI16(self):
        text=self.lineEdit_16.text()
        if "<i>" in text:
            self.lineEdit_16.setText(text.replace('<i>',''))
        else:
            self.lineEdit_16.setText("<i>"+text)
    def setValueU16(self):
        text=self.lineEdit_16.text()
        if "<U>" in text:
            self.lineEdit_16.setText(text.replace('<U>',''))
        else:
            self.lineEdit_16.setText("<U>"+text)
    def setValueR16(self):
        text=self.lineEdit_16.text()
        if "<R>" in text:
            self.lineEdit_16.setText(text.replace('<R>',''))
        else:
            self.lineEdit_16.setText("<R>"+text)


    def setValueB17(self,text):
        text=self.lineEdit_17.text()
        if "<B>" in text:
            self.lineEdit_17.setText(text.replace('<B>',''))
        else:
            self.lineEdit_17.setText("<B>"+text)
    def setValueI17(self):
        text=self.lineEdit_17.text()
        if "<i>" in text:
            self.lineEdit_17.setText(text.replace('<i>',''))
        else:
            self.lineEdit_17.setText("<i>"+text)
    def setValueU17(self):
        text=self.lineEdit_17.text()
        if "<U>" in text:
            self.lineEdit_17.setText(text.replace('<U>',''))
        else:
            self.lineEdit_17.setText("<U>"+text)
    def setValueR17(self):
        text=self.lineEdit_17.text()
        if "<R>" in text:
            self.lineEdit_17.setText(text.replace('<R>',''))
        else:
            self.lineEdit_17.setText("<R>"+text)

    def setValueB18(self,text):
        text=self.lineEdit_18.text()
        if "<B>" in text:
            self.lineEdit_18.setText(text.replace('<B>',''))
        else:
            self.lineEdit_18.setText("<B>"+text)
    def setValueI18(self):
        text=self.lineEdit_18.text()
        if "<i>" in text:
            self.lineEdit_18.setText(text.replace('<i>',''))
        else:
            self.lineEdit_18.setText("<i>"+text)
    def setValueU18(self):
        text=self.lineEdit_18.text()
        if "<U>" in text:
            self.lineEdit_18.setText(text.replace('<U>',''))
        else:
            self.lineEdit_18.setText("<U>"+text)
    def setValueR18(self):
        text=self.lineEdit_18.text()
        if "<R>" in text:
            self.lineEdit_18.setText(text.replace('<R>',''))
        else:
            self.lineEdit_18.setText("<R>"+text)

    def setValueB19(self,text):
        text=self.lineEdit_19.text()
        if "<B>" in text:
            self.lineEdit_19.setText(text.replace('<B>',''))
        else:
            self.lineEdit_19.setText("<B>"+text)
    def setValueI19(self):
        text=self.lineEdit_19.text()
        if "<i>" in text:
            self.lineEdit_19.setText(text.replace('<i>',''))
        else:
            self.lineEdit_19.setText("<i>"+text)
    def setValueU19(self):
        text=self.lineEdit_19.text()
        if "<U>" in text:
            self.lineEdit_19.setText(text.replace('<U>',''))
        else:
            self.lineEdit_19.setText("<U>"+text)
    def setValueR19(self):
        text=self.lineEdit_19.text()
        if "<R>" in text:
            self.lineEdit_19.setText(text.replace('<R>',''))
        else:
            self.lineEdit_19.setText("<R>"+text)

    def setValueB20(self,text):
        text=self.lineEdit_20.text()
        if "<B>" in text:
            self.lineEdit_20.setText(text.replace('<B>',''))
        else:
            self.lineEdit_20.setText("<B>"+text)
    def setValueI20(self):
        text=self.lineEdit_20.text()
        if "<i>" in text:
            self.lineEdit_20.setText(text.replace('<i>',''))
        else:
            self.lineEdit_20.setText("<i>"+text)
    def setValueU20(self):
        text=self.lineEdit_20.text()
        if "<U>" in text:
            self.lineEdit_20.setText(text.replace('<U>',''))
        else:
            self.lineEdit_20.setText("<U>"+text)
    def setValueR20(self):
        text=self.lineEdit_20.text()
        if "<R>" in text:
            self.lineEdit_20.setText(text.replace('<R>',''))
        else:
            self.lineEdit_20.setText("<R>"+text)

    def setValueB21(self,text):
        text=self.lineEdit_21.text()
        if "<B>" in text:
            self.lineEdit_21.setText(text.replace('<B>',''))
        else:
            self.lineEdit_21.setText("<B>"+text)
    def setValueI21(self):
        text=self.lineEdit_21.text()
        if "<i>" in text:
            self.lineEdit_21.setText(text.replace('<i>',''))
        else:
            self.lineEdit_21.setText("<i>"+text)
    def setValueU21(self):
        text=self.lineEdit_21.text()
        if "<U>" in text:
            self.lineEdit_21.setText(text.replace('<U>',''))
        else:
            self.lineEdit_21.setText("<U>"+text)
    def setValueR21(self):
        text=self.lineEdit_21.text()
        if "<R>" in text:
            self.lineEdit_21.setText(text.replace('<R>',''))
        else:
            self.lineEdit_21.setText("<R>"+text)

    def setValueB22(self,text):
        text=self.lineEdit_22.text()
        if "<B>" in text:
            self.lineEdit_22.setText(text.replace('<B>',''))
        else:
            self.lineEdit_22.setText("<B>"+text)
    def setValueI22(self):
        text=self.lineEdit_22.text()
        if "<i>" in text:
            self.lineEdit_22.setText(text.replace('<i>',''))
        else:
            self.lineEdit_22.setText("<i>"+text)
    def setValueU22(self):
        text=self.lineEdit_22.text()
        if "<U>" in text:
            self.lineEdit_22.setText(text.replace('<U>',''))
        else:
            self.lineEdit_22.setText("<U>"+text)
    def setValueR22(self):
        text=self.lineEdit_22.text()
        if "<R>" in text:
            self.lineEdit_22.setText(text.replace('<R>',''))
        else:
            self.lineEdit_22.setText("<R>"+text)


    def setValueB23(self,text):
        text=self.lineEdit_23.text()
        if "<B>" in text:
            self.lineEdit_23.setText(text.replace('<B>',''))
        else:
            self.lineEdit_23.setText("<B>"+text)
    def setValueI23(self):
        text=self.lineEdit_23.text()
        if "<i>" in text:
            self.lineEdit_23.setText(text.replace('<i>',''))
        else:
            self.lineEdit_23.setText("<i>"+text)
    def setValueU23(self):
        text=self.lineEdit_23.text()
        if "<U>" in text:
            self.lineEdit_23.setText(text.replace('<U>',''))
        else:
            self.lineEdit_23.setText("<U>"+text)
    def setValueR23(self):
        text=self.lineEdit_23.text()
        if "<R>" in text:
            self.lineEdit_23.setText(text.replace('<R>',''))
        else:
            self.lineEdit_23.setText("<R>"+text)



    def setValueB24(self,text):
        text=self.textEdit_3.toPlainText()
        if "<B>" in text:
            self.textEdit_3.setPlainText(text.replace('<B>',''))
        else:
            self.textEdit_3.setPlainText("<B>"+text)
    def setValueI24(self):
        text=self.textEdit_3.toPlainText()
        if "<i>" in text:
            self.textEdit_3.setPlainText(text.replace('<i>',''))
        else:
            self.textEdit_3.setPlainText("<i>"+text)
    def setValueU24(self):
        text=self.textEdit_3.toPlainText()
        if "<U>" in text:
            self.textEdit_3.setPlainText(text.replace('<U>',''))
        else:
            self.textEdit_3.setPlainText("<U>"+text)

    def setValueR24(self):
        text=self.textEdit_3.toPlainText()
        if "<R>" in text:
            self.textEdit_3.setPlainText(text.replace('<R>',''))
        else:
            self.textEdit_3.setPlainText("<R>"+text)  


    def setValueB25(self,text):
        text=self.lineEdit_25.text()
        if "<B>" in text:
            self.lineEdit_25.setText(text.replace('<B>',''))
        else:
            self.lineEdit_25.setText("<B>"+text)
    def setValueI25(self):
        text=self.lineEdit_25.text()
        if "<i>" in text:
            self.lineEdit_25.setText(text.replace('<i>',''))
        else:
            self.lineEdit_25.setText("<i>"+text)
    def setValueU25(self):
        text=self.lineEdit_25.text()
        if "<U>" in text:
            self.lineEdit_25.setText(text.replace('<U>',''))
        else:
            self.lineEdit_25.setText("<U>"+text)
    def setValueR25(self):
        text=self.lineEdit_25.text()
        if "<R>" in text:
            self.lineEdit_25.setText(text.replace('<R>',''))
        else:
            self.lineEdit_25.setText("<R>"+text)



    def setValueB26(self,text):
        text=self.lineEdit_26.text()
        if "<B>" in text:
            self.lineEdit_26.setText(text.replace('<B>',''))
        else:
            self.lineEdit_26.setText("<B>"+text)
    def setValueI26(self):
        text=self.lineEdit_26.text()
        if "<i>" in text:
            self.lineEdit_26.setText(text.replace('<i>',''))
        else:
            self.lineEdit_26.setText("<i>"+text)
    def setValueU26(self):
        text=self.lineEdit_26.text()
        if "<U>" in text:
            self.lineEdit_26.setText(text.replace('<U>',''))
        else:
            self.lineEdit_26.setText("<U>"+text)
    def setValueR26(self):
        text=self.lineEdit_26.text()
        if "<R>" in text:
            self.lineEdit_26.setText(text.replace('<R>',''))
        else:
            self.lineEdit_26.setText("<R>"+text)


    def setValueB27(self,text):
        text=self.lineEdit_27.text()
        if "<B>" in text:
            self.lineEdit_27.setText(text.replace('<B>',''))
        else:
            self.lineEdit_27.setText("<B>"+text)
    def setValueI27(self):
        text=self.lineEdit_27.text()
        if "<i>" in text:
            self.lineEdit_27.setText(text.replace('<i>',''))
        else:
            self.lineEdit_27.setText("<i>"+text)
    def setValueU27(self):
        text=self.lineEdit_27.text()
        if "<U>" in text:
            self.lineEdit_27.setText(text.replace('<U>',''))
        else:
            self.lineEdit_27.setText("<U>"+text)
    def setValueR27(self):
        text=self.lineEdit_27.text()
        if "<R>" in text:
            self.lineEdit_27.setText(text.replace('<R>',''))
        else:
            self.lineEdit_27.setText("<R>"+text)



    def setValueB30(self,text):
        text=self.lineEdit_30.text()
        if "<B>" in text:
            self.lineEdit_30.setText(text.replace('<B>',''))
        else:
            self.lineEdit_30.setText("<B>"+text)
    def setValueI30(self):
        text=self.lineEdit_30.text()
        if "<i>" in text:
            self.lineEdit_30.setText(text.replace('<i>',''))
        else:
            self.lineEdit_30.setText("<i>"+text)
    def setValueU30(self):
        text=self.lineEdit_30.text()
        if "<U>" in text:
            self.lineEdit_30.setText(text.replace('<U>',''))
        else:
            self.lineEdit_30.setText("<U>"+text)
    def setValueR30(self):
        text=self.lineEdit_30.text()
        if "<R>" in text:
            self.lineEdit_30.setText(text.replace('<R>',''))
        else:
            self.lineEdit_30.setText("<R>"+text)

    def setValueB28(self,text):
        text=self.lineEdit_28.text()
        if "<B>" in text:
            self.lineEdit_28.setText(text.replace('<B>',''))
        else:
            self.lineEdit_28.setText("<B>"+text)
    def setValueI28(self):
        text=self.lineEdit_28.text()
        if "<i>" in text:
            self.lineEdit_28.setText(text.replace('<i>',''))
        else:
            self.lineEdit_28.setText("<i>"+text)
    def setValueU28(self):
        text=self.lineEdit_28.text()
        if "<U>" in text:
            self.lineEdit_28.setText(text.replace('<U>',''))
        else:
            self.lineEdit_28.setText("<U>"+text)
    def setValueR28(self):
        text=self.lineEdit_28.text()
        if "<R>" in text:
            self.lineEdit_28.setText(text.replace('<R>',''))
        else:
            self.lineEdit_28.setText("<R>"+text)


    def setValueB29(self,text):
        text=self.lineEdit_29.text()
        if "<B>" in text:
            self.lineEdit_29.setText(text.replace('<B>',''))
        else:
            self.lineEdit_29.setText("<B>"+text)
    def setValueI29(self):
        text=self.lineEdit_29.text()
        if "<i>" in text:
            self.lineEdit_29.setText(text.replace('<i>',''))
        else:
            self.lineEdit_29.setText("<i>"+text)
    def setValueU29(self):
        text=self.lineEdit_29.text()
        if "<U>" in text:
            self.lineEdit_29.setText(text.replace('<U>',''))
        else:
            self.lineEdit_29.setText("<U>"+text)
    def setValueR29(self):
        text=self.lineEdit_29.text()
        if "<R>" in text:
            self.lineEdit_29.setText(text.replace('<R>',''))
        else:
            self.lineEdit_29.setText("<R>"+text)

    def saveData(self):
        # fileName=self.filename
        # print("save data file name = {} ".format(fileName))
        formNo=self.lineEdit_3.text()
        if "<B>" in formNo:
            formNo=formNo+'<B>'
        companyCode=self.lineEdit_4.text()
        companyName=self.lineEdit_5.text()
        if "<R>" in companyName:
            companyName=companyName+'<R>'
        companyAddress=self.textEdit.toPlainText()
        zipCode=self.lineEdit_6.text()
        fax=self.lineEdit_7.text()
        website=self.lineEdit_8.text()
        email=self.lineEdit_9.text()
        contactNo=self.lineEdit_10.text()
        state=self.lineEdit_11.text()
        country=self.lineEdit_15.text()
        if "<R><i>" in country:
            country=country+'<i><R>'
        headquarter=self.lineEdit_12.text()
        if '<i><U>' in headquarter:
            headquarter=headquarter+'<U><i>'
        noOfEmployees=self.lineEdit_13.text()
        industry=self.textEdit_2.toPlainText()
        if "<B><U>" in industry:
            industry=industry+'<U><B>'
        brandAmbassador=self.lineEdit_14.text()
        if "<B>" in brandAmbassador:
            brandAmbassador=brandAmbassador+'<B>'
        mediaPartner=self.lineEdit_16.text()
        socialMedia=self.lineEdit_17.text()
        frenchisePartner=self.lineEdit_18.text()
        investor=self.lineEdit_19.text()
        advertisingMedia=self.lineEdit_20.text()
        product=self.lineEdit_21.text()
        services=self.lineEdit_22.text()
        manager=self.lineEdit_23.text()
        if "<B>" in manager:
            manager=manager+'<B>'
        subclassification=self.textEdit_3.toPlainText()
        if "<i><U>" in subclassification:
            subclassification=subclassification+'<U><i>'
        registrationDate=self.lineEdit_25.text()
        yearlyRevenue=self.lineEdit_26.text()
        landmark=self.lineEdit_27.text()
        accAudit=self.lineEdit_30.text()
        currency=self.lineEdit_28.text()
        yearlyExpense=self.lineEdit_29.text()

        self.fileDone+=1
        if self.count==0:
            self.ShowMessageBox('Attempt Left', 'You Dont Have Any Attempt Left')
        elif self.filename=="":
            self.ShowMessageBox('Upload Form', 'Please Upload Form And Try Again')
        else:
            cursor.execute("INSERT INTO DATA (fileName,formNo, companyCode, companyName, companyAddress, zipCode, fax, website, email, contactNo, state, country, headquarter, noOfEmployees, industry, brandAmbassador, mediaPartner, socialMedia, frenchisePartner, investor, advertisingMedia, product, services, manager, subclassification, registrationDate, yearlyRevenue, landmark, accAudit, currency, yearlyExpense,user_id) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(self.filename,formNo, companyCode, companyName, companyAddress, zipCode, fax, website, email, contactNo, state, country, headquarter, noOfEmployees, industry, brandAmbassador, mediaPartner, socialMedia, frenchisePartner, investor, advertisingMedia, product, services, manager, subclassification, registrationDate, yearlyRevenue, landmark, accAudit, currency, yearlyExpense,self.user_id))
            cursor.execute("UPDATE  USER  SET fileDone= ? WHERE USER_ID= ?",(self.fileDone,self.user_id ))
            db.commit();
            # self.label_2.setText("data inserted successfully")
            self.label.setPixmap(QPixmap(""))
            self.filename=""
            self.lineEdit_3.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit_5.setText("")
            self.textEdit.setPlainText("")
            self.lineEdit_6.setText("")
            self.lineEdit_7.setText("")
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_10.setText("")
            self.lineEdit_11.setText("")
            self.lineEdit_15.setText("")
            self.lineEdit_12.setText("")
            self.lineEdit_13.setText("")
            self.textEdit_2.setPlainText("")
            self.lineEdit_14.setText("")
            self.lineEdit_16.setText("")
            self.lineEdit_17.setText("")
            self.lineEdit_18.setText("")
            self.lineEdit_19.setText("")
            self.lineEdit_20.setText("")
            self.lineEdit_21.setText("")
            self.lineEdit_22.setText("")
            self.lineEdit_23.setText("")
            self.textEdit_3.setPlainText("")
            self.lineEdit_25.setText("")
            self.lineEdit_26.setText("")
            self.lineEdit_27.setText("")
            self.lineEdit_30.setText("")
            self.lineEdit_28.setText("")
            self.lineEdit_29.setText("")
            self.current=0
            r=cursor.execute("SELECT * FROM DATA WHERE USER_ID=?",[self.user_id])
            self.found=r.fetchall()
            self.lineEdit_2.setText(str(self.fileDone))
            val=int(self.fileDone/self.no_of_forms*100)
            self.progressBar.setValue(val)

            if (self.no_of_forms == self.fileDone):
                self.btn1_2.setEnabled(False)
                self.pushButton_3.setEnabled(True)
            else:
                self.btn1_2.setEnabled(True)
                self.pushButton_3.setEnabled(False)
                

            print("data inserted successfully")
            self.ShowMessageBox('Form Saved', 'Form Saved Successfully')

    def submitData(self):
        msgBox = QMessageBox()
        self.setWindowIcon(QIcon('icon.ico'))
        msgBox.setText("Have Your Project Complited?? \n \n After Sumbission of your project you will not able to work with this project \n \n Are You Sure?? ")
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setWindowTitle("Worning!!")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        # msgBox.buttonClicked.connect(msgButtonClick)
        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            a=cursor.execute("SELECT isSubmitted FROM USER WHERE USER_ID=?",(self.user_id,))
            f=a.fetchone()[0]
            if(f==False):
                print('OK clicked')
                from sendFile import SendForm
                self.send_form=SendForm(self.user_id)
                self.send_form.show()
            else:
                self.ShowMessageBox('Already Submitted', 'You Have Already Submitted The Form')



    def newFormButton(self):
        self.label.setPixmap(QPixmap(""))
        self.filename=""
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.textEdit.setPlainText("")
        self.lineEdit_6.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.lineEdit_15.setText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.textEdit_2.setPlainText("")
        self.lineEdit_14.setText("")
        self.lineEdit_16.setText("")
        self.lineEdit_17.setText("")
        self.lineEdit_18.setText("")
        self.lineEdit_19.setText("")
        self.lineEdit_20.setText("")
        self.lineEdit_21.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_23.setText("")
        self.textEdit_3.setPlainText("")
        self.lineEdit_25.setText("")
        self.lineEdit_26.setText("")
        self.lineEdit_27.setText("")
        self.lineEdit_30.setText("")
        self.lineEdit_28.setText("")
        self.lineEdit_29.setText("")


    def ShowMessageBox(self,title, messege):
        msgBox=QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle(title)
        msgBox.setText(messege)
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec_()
        
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Control:
            self.ShowMessageBox('Key Blocked', 'Control Key is Blocked')
            


def main():
    app=QApplication(sys.argv)
    window=MainApp(6, 9 , '2021-02-15 23:02:02', '2021-03-07 23:02:02', 2 , 0, 'dsfh@fd.com')
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()