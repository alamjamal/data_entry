import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.uic import  loadUiType
from PyQt5.QtGui import QIcon

ui,_=loadUiType('mail.ui')

import os
from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

import sqlite3
db=sqlite3.connect(resource_path("data.db"))
cursor=db.cursor()

class SendForm(QMainWindow, ui):
	def __init__(self,user_id):
		QMainWindow.__init__(self)
		# super(RegisterForm, self).__init__(parent)
		self.user_id=user_id
		self.setupUi(self)
		self.setFixedSize(710,535)
		self.setWindowIcon(QIcon('icon.ico'))
		self.toaddr = "alamjamal88@gmail.com"
		self.lineEdit_3.setText(self.toaddr)
		self.pushButton.clicked.connect(self.exportModule)


	def exportModule(self):
		import pandas as pd
		import numpy as np
		df=pd.read_sql_query("SELECT * from data where user_id=?",db, params=(self.user_id, ))
		df.replace('', 'Not Mentioned', inplace=True)
		a=df.shape[0]
		b=df.shape[1]
		# print(b)
		desktop=os.getlogin()
		# writer = pd.ExcelWriter('FormData.xlsx', engine='xlsxwriter')
		# df.to_excel(writer, sheet_name='Sheet1',index=False)
		try:
			with pd.ExcelWriter('FormData.xlsx',engine='xlsxwriter') as writer:
				df.to_excel(writer,sheet_name='Sheet1',index=False)
				workbook  = writer.book
				worksheet = writer.sheets['Sheet1']
				for col in range(50):
					worksheet.set_column(col, col, 20)
				worksheet.set_column(5, 5, 50)
				yellow_format= workbook.add_format({'bg_color':'yellow'})
				white_format= workbook.add_format({'bg_color':'white'})
				red_format = workbook.add_format({'bg_color':'red'})
				green_format = workbook.add_format({'bg_color':'green'})

				worksheet.conditional_format(1, 5, a, 5, {'type':   'blanks',
													   'format': yellow_format})

				worksheet.conditional_format(1,1,a,b, {'type': 'text',
													  'criteria': 'containing',
													   'value':     'Not Mentioned',
													   'format': red_format})
				worksheet.conditional_format(1, 8, a, 8, {'type': 'text',
													  'criteria': 'begins with',
													   'value':     'http://www.',
													   'format': white_format})
				worksheet.conditional_format(1, 8, a, 8, {'type': 'no_blanks',
													   'format': yellow_format})
				print("no save")
				# writer.save()
				# writer.close()
		except xlsxwriter.exceptions.FileCreateError as e:
			print(e)
			self.ShowMessageBox('Close File', 'Please Close Your File Before Saving')
		self.sendEmail()
		

	def sendEmail(self):
		# self.label_2.setText("Mail Successfully Sent")
		from socket import gaierror
		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
		from email.mime.base import MIMEBase
		from email import encoders
		fromaddr = self.lineEdit.text()
		password=self.lineEdit_2.text()

		if fromaddr=="" or fromaddr=="":
			self.ShowMessageBox('Error!!', "Password can't be blank")

		else:
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = self.toaddr
			msg['Subject'] = self.lineEdit_4.text()
			body = self.textEdit.toPlainText()
			msg.attach(MIMEText(body, 'plain'))
			filename = "FormData.xlsx"

			try:
				with open(filename, 'rb') as attachment:
		    		# part = MIMEApplication(attachment.read(), Name=basename(filename))
					# attachment = open(filename, "rb")
					
					part = MIMEBase('application', 'octet-stream')
					part.set_payload((attachment).read())
					encoders.encode_base64(part)
					part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
					msg.attach(part)
			
				with smtplib.SMTP("smtp.gmail.com", 587) as server:
					# server = smtplib.SMTP('smtp.gmail.com', 587)
					server.starttls()
					server.login(fromaddr, password)
					text = msg.as_string()
					server.sendmail(fromaddr, self.toaddr, text)
					server.quit()
					self.ShowMessageBox2('Delivery Report', 'Mail successfuly sent to {}'.format(self.toaddr))
					print("success")
					os.remove("FormData.xlsx")
					cursor.execute("UPDATE USER SET isSubmitted=True WHERE user_id=?",(self.user_id,))
					print(cursor.rowcount)
					db.commit();
					self.close()

			except (smtplib.SMTPAuthenticationError,TypeError) as e:
				self.ShowMessageBox('Error: INCORRECT EMAIL OR PASSWORD', 'YOU MUST HAVE GMAIL ADDRESS TO SUBMIT THE PROJECT \n \n OR \n \n INVALID EMAIL ADDRESS OR PASSWORD')
				print(e)
			except gaierror as e:
				self.ShowMessageBox('No Internet', 'Your Internet is not Connected')


	def ShowMessageBox(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QMessageBox.Critical)
		msgBox.setWindowIcon(QIcon("icon.ico"))
		msgBox.setWindowTitle(title)
		msgBox.setText(messege)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()

	def ShowMessageBox2(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QtWidgets.QMessageBox.Information)
		msgBox.setWindowTitle(title)
		msgBox.setText(messege)
		msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
		msgBox.exec_()

if __name__ == "__main__":
	import sys
	app = QApplication(sys.argv)
	form = SendForm(4)
	form.show()
	app.exec_()