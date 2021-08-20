import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.uic import  loadUiType
from mysql.connector import connect, Error
from PyQt5.QtCore import QDate,Qt
from socket import gaierror

ui,_=loadUiType('RegisterAuth.ui')

class MyAuthForm(QMainWindow, ui):
	def __init__(self):
		QMainWindow.__init__(self)
		# super(MyForm, self).__init__(parent)
		self.setupUi(self)
		self.setWindowIcon(QIcon('icon.ico'))
		self.pushButton.clicked.connect(self.AuthenticateKey)

	def AuthenticateKey(self):
		try:
			connection=connect(
					host="remotemysql.com",
					user="W4OzzEsjRw",
					password="c7fK7ePJlR",
					database="W4OzzEsjRw")
			mycursor = connection.cursor()
			auth_code=self.lineEdit.text()
			sql="SELECT * from register WHERE auth_code=%s and isRegisterd=0 and project_number<=6"
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
				self.ShowMessageBox('Auth Code Invalid', 'Your Auth Code Is Not valid or Already Registerd')
		except Error as e:
			print(e)
			self.ShowMessageBox('Connection Error', 'No Internet Connection Found')

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



