import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.QtGui import QIcon,QIntValidator
from PyQt5.uic import  loadUiType


import sqlite3
db=sqlite3.connect("data.db")
cursor=db.cursor()

from mysql.connector import connect, Error

ui,_=loadUiType('RegAfterAuth.ui')

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
		self.setWindowIcon(QIcon('icon.ico'))
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
		no_of_Forms=self.lineEdit_6.text()
		user_id=self.lineEdit_7.text()
		pass1=self.lineEdit_8.text()
		pass2=self.lineEdit_9.text()


		if (self.fname=="" or self.lname=="" or  contact=="" or  self.email=="" or  address=="" or gender=="" or age=="" or no_of_Forms=="" or user_id=="" or pass1==""):
			self.ShowMessageBox('Mandatory Field', 'All Field Are Mandatory')
		elif (pass1!=pass2):
			self.ShowMessageBox('Password Error', 'Password Did Not Match')
		else:
			connection=None
			try:
				connection=connect(
							host="remotemysql.com",
							user="W4OzzEsjRw",
							password="c7fK7ePJlR",
							database="W4OzzEsjRw")
				mycursor = connection.cursor()

				cursor.execute("INSERT INTO USER (CREATED_AT, fname, lname , contact ,email,address,gender,age,no_of_Forms,userid,password,EXPIRE_AT) VALUES(DATETIME('NOW','localtime'),?,?,?,?,?,?,?,?,?,?,DATETIME('NOW','20 DAY','localtime'))",(self.fname,self.lname,contact,self.email,address,gender,age,no_of_Forms,user_id,pass1))
				db.commit();
				db.close()
				sql = "UPDATE  register SET isRegisterd = %s , project_number=project_number+1 WHERE register_id=%s "			
				val = (True, self.id)
				mycursor.execute(sql, val)
				connection.commit()
				print("updated")
				self.ShowMessageBox('Information', 'MESSAGE \n  Registration Successfull.. \n Remember This for Login Details \n   USER ID : {} \n   PASSWORD : {} \n\n This form will automatically close start the software to login '.format(user_id, pass1))
				from main import Login
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
	window = MyRegisterForm('1','alam','jamal','alam@gmail.com')
	window.show()
	app.exec_()



