import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import  loadUiType
from mysql.connector import connect, Error
from PyQt5.QtCore import QDate,Qt
from socket import gaierror

import os
from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)


ui,_=loadUiType(resource_path('RegisterAuth.ui'))

class MyAuthForm(QMainWindow, ui):
	def __init__(self):
		QMainWindow.__init__(self)
		# super(MyForm, self).__init__(parent)
		self.setupUi(self)
		self.setWindowIcon(QIcon(resource_path('icon.ico')))
		self.pushButton.clicked.connect(self.AuthenticateKey)

	def AuthenticateKey(self):
		auth_code=self.lineEdit.text()
		if auth_code == "":
			self.ShowMessageBox('Error!!!', 'Cant be empty')
			return
		try:
			connection=connect(
					host="plumitnetwork.com",
					user="plum_user",
					password="y(l.%=Ud1vYm",
					database="db_plum")
			mycursor = connection.cursor()
			sql="SELECT * from register WHERE auth_code=%s and isRegisterd=0 and project_number<4"
			adr=(auth_code,)
			mycursor.execute(sql,adr)
			found=mycursor.fetchone()
			if found:
				from RegAfterAuth import MyRegisterForm
				self.close()
				now=QDate.currentDate()
				id=found[0]
				fname=found[2]
				lname=found[3]
				email=found[4]
				self.window2=MyRegisterForm(id,fname,lname,email)
				self.window2.show()
				self.window2.lineEdit.setText(now.toString(Qt.ISODate))
				self.window2.lineEdit_1.setText(found[2])
				self.window2.lineEdit_2.setText(found[3])
				self.window2.lineEdit_4.setText(found[4])
			else:
				self.ShowMessageBox('Error!!!', 'Your Auth Code Is Not valid or Already Registerd')
		except Error as e:
			print(e)
			self.ShowMessageBox('Connection Error', 'No Internet Connection Found')

		except (AttributeError, ModuleNotFoundError, ImportError) as e:
			self.ShowMessageBox('Connection Error', 'Please Connect To The Internet')


	def ShowMessageBox(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(messege)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()
		

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	window = MyAuthForm()
	window.show()
	app.exec_()



