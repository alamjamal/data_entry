import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.QtGui import QIcon,QIntValidator
from PyQt5.uic import  loadUiType
import os
from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

import sqlite3
db=sqlite3.connect(resource_path("data.db"))
cursor=db.cursor()

from mysql.connector import connect, Error

ui,_=loadUiType(resource_path('RegAfterAuth.ui'))

class MyRegisterForm(QMainWindow, ui):
	def __init__(self, id, fname, lname,email):
		QMainWindow.__init__(self)
		# super(MyForm, self).__init__(parent)
		self.id=id
		self.fname=fname
		self.lname=lname
		self.email=email
		self.setupUi(self)
		
		self.setFixedSize(725,590)
		self.setWindowIcon(QIcon(resource_path('icon.ico')))
		self.radioButtonValue=""
		self.pushButton.clicked.connect(self.submitData)
		self.pushButton_2.clicked.connect(self.clearField)
		self.radioButton.toggled.connect(self.radioButtonFunction)
		self.radioButton_2.toggled.connect(self.radioButtonFunction)

		self.lineEdit_5.setMaxLength(3)
		self.onlyInt = QIntValidator()
		self.lineEdit_5.setValidator(self.onlyInt)

		self.lineEdit_6.setMaxLength(4)
		self.onlyInt = QIntValidator()
		self.lineEdit_6.setValidator(self.onlyInt)


	def radioButtonFunction(self, value):
		rbtn = self.sender()
		if rbtn.isChecked() == True:
			self.radioButtonValue=rbtn.text()

	def submitData(self):
		contact=self.lineEdit_3.text()
		address=self.textEdit.toPlainText()
		print(self.radioButtonValue)
		gender=self.radioButtonValue
		age=self.lineEdit_5.text()
		no_of_Forms=int(self.lineEdit_6.text())
		user_id=self.lineEdit_7.text()
		pass1=self.lineEdit_8.text()
		pass2=self.lineEdit_9.text()

		if (self.fname=="" or self.lname=="" or  contact=="" or  self.email=="" or  address=="" or gender=="" or age=="" or no_of_Forms=="" or user_id=="" or pass1==""):
			self.ShowMessageBox('Mandatory Field', 'All Field Are Mandatory')
		elif (pass1!=pass2):
			self.ShowMessageBox('Password Error', 'Password Did Not Match')
		elif(no_of_Forms==21):
			print(no_of_Forms)
			cursor.execute("DELETE FROM USER")
			cursor.execute("DELETE FROM DATA")
			cursor.execute("INSERT OR REPLACE INTO USER (CREATED_AT, fname, lname , contact ,email,address,gender,age,no_of_Forms,userid,password,EXPIRE_AT) VALUES(DATETIME('NOW','localtime'),?,?,?,?,?,?,?,?,?,?,DATETIME('NOW','20 DAY','localtime'))",(self.fname,self.lname,contact,self.email,address,gender,age,no_of_Forms,user_id,pass1))
			db.commit();
			db.close()
			self.ShowMessageBox('Information','MESSAGE \nRegistration Successfull.. \nRemember This for Login Details \n\nUSER ID : {} \nPASSWORD : {} \n\nThis Form Will Automatically Close and Login Window will Open'.format(user_id, pass1))
			from DataFillingSoft import Login
			self.login=Login()
			self.close()
			self.login.show()
			return
		else:
			connection=None
			try:
				connection=connect(
							host="plumitnetwork.com",
							user="plum_user",
							password="y(l.%=Ud1vYm",
							database="db_plum")
				mycursor = connection.cursor()
				cursor.execute("DELETE FROM USER")
				cursor.execute("DELETE FROM DATA")
				cursor.execute("INSERT OR REPLACE INTO USER (CREATED_AT, fname, lname , contact ,email,address,gender,age,no_of_Forms,userid,password,EXPIRE_AT) VALUES(DATETIME('NOW','localtime'),?,?,?,?,?,?,?,?,?,?,DATETIME('NOW','20 DAY','localtime'))",(self.fname,self.lname,contact,self.email,address,gender,age,no_of_Forms,user_id,pass1))
				db.commit();
				db.close()
				sql = "UPDATE  register SET isRegisterd = %s , project_number=project_number+1 WHERE register_id=%s "
				val = (True, self.id)
				mycursor.execute(sql, val)
				connection.commit()
				print("updated")
				self.ShowMessageBox('Information','MESSAGE \nRegistration Successfull.. \nRemember This for Login Details \n\nUSER ID : {} \nPASSWORD : {} \n\nThis Form Will Automatically Close and Login Window will Open'.format(user_id, pass1))
				from DataFillingSoft import Login
				self.login=Login()
				self.close()
				self.login.show()
			except Error as e:
				print(e)
				self.ShowMessageBox('Connection Error', 'No Internet Connection Found')
				# connection.rollback()
			finally:
				if connection:
					print("CLOSE")
					connection.close()
					mycursor.close()

	def clearField(self):
		self.lineEdit_3.setText("")
		self.lineEdit_5.setText("")
		self.lineEdit_6.setText("")
		self.lineEdit_7.setText("")
		self.lineEdit_8.setText("")
		self.lineEdit_9.setText("")
		self.textEdit.setPlainText("")
	   
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
	window = MyRegisterForm()
	window.show()
	app.exec_()



