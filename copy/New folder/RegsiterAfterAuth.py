import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import  loadUiType


import sqlite3
db=sqlite3.connect("data.db")
cursor=db.cursor()

from mysql.connector import connect, Error
connection=connect(
		host="remotemysql.com",
		user="W4OzzEsjRw",
		password="c7fK7ePJlR",
		database="W4OzzEsjRw")

mycursor = connection.cursor()


ui,_=loadUiType('RegisterAfterAuth.ui')

class MyRegisterForm(QMainWindow, ui):
	def __init__(self, id, fname, lname,email):
		QMainWindow.__init__(self)
		# super(MyForm, self).__init__(parent)
		self.id=id
		self.fname=fname
		self.lname=lname
		self.email=email
		self.setupUi(self)
		self.setWindowIcon(QIcon('icon.ico'))
		print(self.email)
		self.pushButton_1.clicked.connect(self.SubmitData)


	def SubmitData(self):
		pass1=self.lineEdit.text()
		pass2=self.lineEdit_3.text()
		if pass1 != pass2:
			self.ShowMessageBox('Password Warning', 'Your Password Did Not Match')
		else:
			cursor.execute("INSERT INTO USER ( FNAME, LNAME, EMAIL , PASSWORD , CREATED_AT,EXPIRE_AT) VALUES(?,?,?,?,DATETIME('NOW','localtime'),DATETIME('NOW','20 DAY','localtime'))",(self.fname,self.lname,self.email,pass1))
			db.commit();
			print("succesfully insert data")
			sql = "UPDATE  register SET isRegisterd = %s WHERE register_id=%s "			
			val = (True, self.id)
			try:
				print("UP deleted")
				mycursor.execute(sql, val)
				connection.commit()
				print("updated")
			except Error as e:
				print(e)
				connection.rollback()
			finally:
				print("CLOSE")
				connection.close()
				mycursor.close()

			self.ShowMessageBox('Registration Successful', 'Your Registration is Successful')
			from main import Login
			self.close()
			self.login=Login()
			self.login.show()

	
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
	window = MyRegisterForm('1','alam','jamal','alam@gmail.com')
	window.show()
	app.exec_()



