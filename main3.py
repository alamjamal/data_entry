
from PyQt5.QtWidgets import QDialog, QApplication,QMainWindow,QLabel,QWidget,QMessageBox,QTableWidgetItem
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtGui import QIcon
from PyQt5.uic import  loadUiType
import sys
# from xlsxwriter import *
# import xlsxwriter

import os
from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

import sqlite3
db=sqlite3.connect(resource_path("data.db"))
cursor=db.cursor()

ui,_=loadUiType(resource_path('main3.ui'))

class MainApp(QMainWindow, ui):
	def __init__(self,user_id):
		QMainWindow.__init__(self)
		self.user_id=user_id
		print("user id {} ".format(self.user_id))
		self.setupUi(self)
		self.setWindowIcon(QIcon(resource_path('icon.ico')))
		self.pushButton_2.clicked.connect(self.exportModule)
		# self.combo.activated[str].connect(self.onChanged)

		result=cursor.execute("SELECT * from data where user_id=?",(self.user_id,))
		self.table_2.setRowCount(0)
		for row_number, row_data in enumerate(result):
			self.table_2.insertRow(row_number)
			for column_number, data in enumerate(row_data):
				self.table_2.setItem(row_number, column_number,QTableWidgetItem(str(data)))

	# def onChanged(self,text):
		# self.user_id=int(text.split(" ")[1])
		# print(self.user_id)
		# result=cursor.execute("with result as (SELECT * , DENSE_RANK () OVER (ORDER BY user_id) as LRank FROM data) select * from result where lrank=?",[self.user_id,])
		# print(result.fetchall())

		# self.table_2.setRowCount(0)
		# for row_number, row_data in enumerate(result):
		# 	# print(row_number, row_data)
		# 	self.table_2.insertRow(row_number)
		# 	for column_number, data in enumerate(row_data):
		# 		# print(column_number, data)
		# 		self.table_2.setItem(row_number, column_number,QTableWidgetItem(str(data)))

	def exportModule(self):
		import pandas as pd
		# import numpy as np
		print(self.user_id)
		# df=pd.read_sql_query("with result as (SELECT * , DENSE_RANK () OVER (ORDER BY user_id) as LRank FROM data) select * from result where lrank=?",db, params=(self.user_id, ))
		df=pd.read_sql_query("select * from data where user_id=?",db, params=(self.user_id,))
		html = df.to_html(index=False)
		desktop=os.getlogin()
		try:
			with open(f'C:\\Users\\{desktop}\\Desktop\\Project{self.user_id}.html','w') as f:
				f.write(html)
				f.close()
				self.ShowMessageBox('Form Saved', 'You Project Successfully Exported To Your Desktop')
		except OSError as e:
			print(e)
			self.ShowMessageBox('Close File', 'Some OS Error')
		

	def ShowMessageBox(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(messege)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()


def main():
	app=QApplication(sys.argv)
	window=MainApp(5)
	window.show()
	app.exec_()

if __name__ == '__main__':
	main()


	