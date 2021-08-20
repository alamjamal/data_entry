import sys
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QDialog, QApplication,QFileDialog,QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
import sqlite3
import os
from os import path
import icon_rc
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

db=sqlite3.connect(resource_path("data.db"))
cursor=db.cursor()
DURATION_INT = 3

class Login(QDialog):
	def __init__(self):
		super(Login,self).__init__()
		self.setFixedSize(650, 235)
		self.setMaximumSize(710, 250)
		loadUi(resource_path("login.ui"),self)
		self.setWindowIcon(QtGui.QIcon('icon.ico'))
		cursor.execute("DELETE FROM USER WHERE CREATED_AT <= date('now','-5 DAY','localtime'); ")
		db.commit()
		self.loginbutton.clicked.connect(self.loginfunction)
		# self.password.setEchoMode(QtWidgets.QLineEdit.Password)
		self.createaccbutton.clicked.connect(self.gotocreate)
		self.SIGINT=False

	def loginfunction(self):
		email=self.email.text()
		password=self.password.text()
		if (email=="" or password=="" ):
			self.ShowMessageBox('Warning ', 'All Field are Mandatory')
		elif (email=="mujeeb" or password=="mujeeb123" ):
			self.gotocreate()
		else:
			db=sqlite3.connect(resource_path("data.db"))
			cursor=db.cursor()
			result=cursor.execute("SELECT user_id, fname, count, DATETIME(CREATED_AT),DATETIME(EXPIRE_AT) , userid ,  no_of_Forms,fileDone, email from USER WHERE userid=? and password = ?",(email,password))
			found=result.fetchone()
			if found:
				db.close()
				self.close()
				from main2 import MainApp
				self.user_id=found[0]
				self.count=found[2]
				self.date=found[3]
				self.dateto=found[4]
				self.no_of_forms=found[6]
				self.fileDone=found[7]
				self.email=found[8]
				print(self.date)
				self.window2=MainApp(self.count,self.user_id,self.date,self.dateto,self.no_of_forms,self.fileDone, self.email)
				# print(found[5])
				self.window2.show()
				self.window2.label_user.setText(found[1])
				self.window2.lineEdit.setText(str(found[6]))
				self.window2.lineEdit_2.setText(str(found[7]))
				self.window2.lineEdit_24.setText("{} : {}".format(found[5],found[3]))
				val=int(self.fileDone/self.no_of_forms*100)
				self.window2.progressBar.setValue(val)
			else:
				self.ShowMessageBox('Warning ', 'Incorrect Email/Password')

	def ShowMessageBox(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(messege)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()

	def gotocreate(self):
		from RegisterAuth import MyAuthForm
		self.close()
		self.createacc=MyAuthForm()
		self.createacc.show()



from PySide2 import QtCore
from PySide2.QtGui import  QColor,QIcon
from PySide2.QtWidgets import QMainWindow,QGraphicsDropShadowEffect
from ui_loader import Ui_SplashScreen
counter = 0

# SPLASH SCREEN
class SplashScreen(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		self.ui = Ui_SplashScreen()
		self.ui.setupUi(self)
		self.setWindowIcon(QIcon('icon.ico'))
		## UI ==> INTERFACE CODES
		########################################################################

		## REMOVE TITLE BAR
		self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
		self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


		## DROP SHADOW EFFECT
		self.shadow = QGraphicsDropShadowEffect(self)
		self.shadow.setBlurRadius(20)
		self.shadow.setXOffset(0)
		self.shadow.setYOffset(0)
		self.shadow.setColor(QColor(0, 0, 0, 60))
		self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

		## QTIMER ==> START
		self.timer = QtCore.QTimer()
		self.timer.timeout.connect(self.progress)
		# TIMER IN MILLISECONDS
		self.timer.start(35)

		# CHANGE DESCRIPTION

		# Initial Text
		self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

		# Change Texts
		QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
		QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


		## SHOW ==> MAIN WINDOW
		########################################################################
		# self.show()
		## ==> END ##

	## ==> APP FUNCTIONS
	########################################################################
	def progress(self):

		
		
		global counter


		# SET VALUE TO PROGRESS BAR
		self.ui.progressBar.setValue(counter)

		# CLOSE SPLASH SCREE AND OPEN APP
		if counter > 100:
			# STOP TIMER
			self.timer.stop()

			# SHOW MAIN WINDOW
			self.login = Login()
			self.login.show()

			# CLOSE SPLASH SCREEN
			self.close()

		# INCREASE COUNTER
		counter += 1



def main():

	app=QApplication(sys.argv)
	window=SplashScreen()
	window.show()
	app.exec_()


if __name__ == '__main__':
	main()

