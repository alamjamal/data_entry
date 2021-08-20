import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox

from PyQt5.uic import  loadUiType

from PyQt5.QtGui import QIcon

from mysql.connector import connect, Error

import os

from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)


ui,_=loadUiType('Register.ui')

class MyForm(QMainWindow, ui):
	def __init__(self):
		QMainWindow.__init__(self)
		# super(MyForm, self).__init__(parent)
		self.setupUi(self)

		self.setWindowIcon(QIcon(resource_path('icon.ico')))
		self.pushButton.clicked.connect(self.generateKey)
		self.pushButton_1.clicked.connect(self.SubmitForm)

	  

	def generateKey(self):
		import random
		import string
		letters_and_digits = string.ascii_letters + string.digits 
		result_str = ''.join((random.choice(letters_and_digits) for i in range(12)))

		self.lineEdit.setText(result_str)
		print("Random alphanumeric String is:", result_str)

	def SubmitForm(self):

		auth_code=self.lineEdit.text()
		fname=self.lineEdit_2.text()
		lname=self.lineEdit_3.text()
		email=self.lineEdit_4.text()
		mobile_number=self.lineEdit_5.text()

		import re
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		res=bool(re.match(regex, email))

		if(auth_code=="" or fname=="" or lname=="" or email=="" or mobile_number==""):
			self.ShowMessageBox('Error !!!!!', 'All Fields are Compulsory.. ')
			return
		if res is False:
			self.ShowMessageBox('Error !!!!!', 'Invalid Email Address.. ')
			return
		if not mobile_number.isdigit() or not len(mobile_number)==10:
			self.ShowMessageBox('Error !!!!!', 'Invalid Mobile Number.. ')
			return
		try:
			connection=connect(
			host="plumitnetwork.com",
			user="plum_user",
			password="y(l.%=Ud1vYm",
			database="db_plum")
			mycursor = connection.cursor()
			sql="SELECT * from register WHERE email=%s"
			adr=(email,)
			mycursor.execute(sql,adr)
			found=mycursor.fetchone()
			
			# mycursor.close()
			# connection.commit()
			# print(found[4])
			if found:
				self.ShowMessageBox('Error !!!!!', 'Already Email Address.. ')
				return
			else:
				sql = "INSERT INTO register ( auth_code, fname, lname, email, mobile_number) VALUES ( %s,%s, %s,%s,%s)"
				val = (auth_code,fname,lname,email, mobile_number)
				mycursor.execute(sql, val)
				connection.commit()
				self.ShowMessageBox('Registration', 'User Generated Successfully')
				self.lineEdit.setText("")
				self.lineEdit_2.setText("")
				self.lineEdit_3.setText("")
				self.lineEdit_4.setText("")
				self.lineEdit_5.setText("")
				print(mycursor.rowcount, "record inserted.")
		except Error as e:
			print(e)

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

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	form = MyForm()
	form.show()
	app.exec_()



