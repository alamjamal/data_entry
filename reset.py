import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox,QDesktopWidget
from PyQt5.uic import  loadUiType
import os
from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

import sqlite3
# db=sqlite3.connect("data.db")
# cursor=db.cursor()
ui,_=loadUiType(resource_path('reset.ui'))

class ResetForm(QMainWindow, ui):
	def __init__(self):
		QMainWindow.__init__(self)
		# super(RegisterForm, self).__init__(parent)
		self.setupUi(self)
		self.pushButton.clicked.connect(self.reset_data)
		self.pushButton_2.clicked.connect(self.cancel_data)

	def reset_data(self):
		try:
			connection=sqlite3.connect(resource_path("data.db"))
			cursor=connection.cursor()
			cursor.execute("DELETE FROM DATA")
			cursor.execute("UPDATE USER SET fileDone=0 , isSubmitted=0")
			# cursor.execute("DELETE FROM USER")
			# cursor.execute("UPDATE  USER  SET count = count+1")
			connection.commit()
			self.ShowMessageBox('Project Reset ', 'Your Project is Reset Successfully')
			from DataFillingSoft import Login
			self.login=Login()
			self.login.show()
			self.close()
		except sqlite3.Error as error:
			print("Failed to read data from sqlite table", error)
		finally:
			if (connection):
				connection.close()
				self.close()
				print("sqlite connection is closed")

	def cancel_data(self):
		self.close()


	def ShowMessageBox(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(messege)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()



if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = ResetForm()
	form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
	qtRectangle = form.frameGeometry()
	centerPoint = QDesktopWidget().availableGeometry().center()
	qtRectangle.moveCenter(centerPoint)
	form.move(qtRectangle.topLeft())
	# form.move(0, 0)
	form.show()
	app.exec_()
