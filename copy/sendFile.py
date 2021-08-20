import sys
from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import  QMainWindow,QLabel,QPushButton,QApplication,QMessageBox
from PyQt5.uic import  loadUiType
from PyQt5.QtGui import QIcon
from socket import gaierror
from mysql.connector import connect, Error
from mysql.connector.cursor import MySQLCursor
import re


import os
from os import path
def resource_path(relative_path):
	base_path=getattr(sys, '_MEIPASS',os.path.dirname(os.path.abspath(__file__)))
	return os.path.join(base_path, relative_path)

import sqlite3
db=sqlite3.connect(resource_path("data.db"))
cursor=db.cursor()

# dataentriesservices@gmail.com

ui,_=loadUiType(resource_path('mail.ui'))

class SendForm(QMainWindow, ui):
	def __init__(self,user_id, user_name,email):
		QMainWindow.__init__(self)
		# super(RegisterForm, self).__init__(parent)
		self.email=email
		self.user_id=user_id
		self.user_name=user_name
		self.setupUi(self)
		self.setFixedSize(710,535)
		self.setWindowIcon(QIcon(resource_path('icon.ico')))
		# result = self.onOpen()
		# self.toaddr = result[0]
		# self.pdf_password = result[1]
		self.toaddr='uerscanada1@gmail.com'
		self.pdf_password='mujeeb'
		self.lineEdit.setText(self.email)
		self.lineEdit_5.setText(self.user_name+'.zip')
		self.pushButton.clicked.connect(self.sendEmail)

	# def onOpen(self):
	# 	try:
	# 		connection=connect(
	# 				host="remotemysql.com",
	# 				user="W4OzzEsjRw",
	# 				password="c7fK7ePJlR",
	# 				database="W4OzzEsjRw")
	# 		mycursor = connection.cursor()
	# 		sql ="""SELECT email from admin_email_boss order by id DESC LIMIT 0, 1"""
	# 		mycursor.execute(sql)
	# 		res1 = mycursor.fetchone()[0]
	# 		sql ="""SELECT pdf_password from admin_pdf_boss order by id DESC"""
	# 		mycursor.execute(sql)
	# 		res2 = mycursor.fetchone()[0]
	# 		connection.close()
	# 		mycursor.close()
	# 		return [res1,res2]

	# 	except Error as e:
	# 		print(e)
	# 		self.ShowMessageBox('Connection Error', 'Database Error or No Internet')
	# 	except (AttributeError, ModuleNotFoundError, ImportError) as e:
	# 		self.ShowMessageBox('Connection Error', 'Please Connect To The Internet')

	def exportModule(self):
		import pandas as pd
		import numpy as np
		print(self.user_id)
		df=pd.read_sql_query("SELECT * from data where user_id=?",db, params=(self.user_id, ))
		df['formNo']=df['formNo'].apply(lambda x : x+' *' if bool(re.match(r"^(<B>)[\w]+(<B>)$", x))==False else x )
		df['companyCode']=df['companyCode'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['companyName']=df['companyName'].apply(lambda x : x+' *' if bool(re.match(r"^(<R>)[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*(<R>)$", x))==False else x )
		df['companyAddress']=df['companyAddress'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([.]+ )*([,]+ )*( [-]+)*( [a-zA-Z0-9]+([.]+ )*([,]+ )*( [-]+)*)*$", x))==False else x )
		df['zipCode']=df['zipCode'].apply(lambda x : x+' *' if bool(re.match(r"[\d]{4,6}$", x))==False else x )
		df['fax']=df['fax'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9+]+([,]+ )*( [-]+)*( [a-zA-Z0-9+]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['website']=df['website'].apply(lambda x : x+' *' if bool(re.match(r"^(<I><U>)(http|https):\/\/+[www]+\.[\w]+\.[a-z]+$",x))==False else x )
		df['email']=df['email'].apply(lambda x : x+' *' if bool(re.match(r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,6}$", x))==False else x )
		df['contactNo']=df['contactNo'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9+]+([,]+ )*( [-]+)*( [a-zA-Z0-9+]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['state']=df['state'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['country']=df['country'].apply(lambda x : x+' *' if bool(re.match(r"^(<R><I>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*(<I><R>)$", x))==False else x )
		df['headquarter']=df['headquarter'].apply(lambda x : x+' *' if bool(re.match(r"^(<I><U>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*(<U><I>)$", x))==False else x )
		df['noOfEmployees']=df['noOfEmployees'].apply(lambda x : x+' *' if bool(re.match(r"[0-9,]+$", x))==False else x )
		df['industry']=df['industry'].apply(lambda x : x+' *' if bool(re.match(r"^(<B><U>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*(<U><B>)$", x))==False else x )
		df['brandAmbassador']=df['brandAmbassador'].apply(lambda x : x+' *' if bool(re.match(r"^(<B>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*(<B>)$", x))==False else x )
		df['mediaPartner']=df['mediaPartner'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['socialMedia']=df['socialMedia'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['frenchisePartner']=df['frenchisePartner'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['investor']=df['investor'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['advertisingMedia']=df['advertisingMedia'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['product']=df['product'].apply(lambda x : x+' *' if bool(re.match(r"^(<R><B>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['services']=df['services'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['manager']=df['manager'].apply(lambda x : x+' *' if bool(re.match(r"^(<B>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*(<B>)$", x))==False else x )
		df['subclassification']=df['subclassification'].apply(lambda x : x+' *' if bool(re.match(r"^(<I><U>)[a-zA-Z0-9_]+([,]+ )*( [-]+)*( [a-zA-Z0-9_]+([,]+ )*( [-]+)*)*(<U><I>)$", x))==False else x )
		df['registrationDate']=df['registrationDate'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['yearlyRevenue']=df['yearlyRevenue'].apply(lambda x : x+' *' if bool(re.match(r"[0-9,]+$", x))==False else x )
		df['landmark']=df['landmark'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['accAudit']=df['accAudit'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['currency']=df['currency'].apply(lambda x : x+' *' if bool(re.match(r"^[a-zA-Z0-9]+([,]+ )*( [-]+)*( [a-zA-Z0-9]+([,]+ )*( [-]+)*)*$", x))==False else x )
		df['yearlyExpense']=df['yearlyExpense'].apply(lambda x : x+' *' if bool(re.match(r"[0-9,]+$", x))==False else x )
		print(df)

		# df.replace('', 'Not Mentioned', inplace=True)
		a=df.shape[0]
		b=df.shape[1]
		desktop=os.getlogin()
		try:
			with pd.ExcelWriter(resource_path(self.user_name+'.xlsx'),options={'strings_to_urls': False}, engine='xlsxwriter') as writer:
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


				#starting row , starting column, ending row , ending column 
				worksheet.conditional_format(1,1,a,b, {'type': 'text',
													  'criteria': 'ends with',
													   'value':     '*',
													   'format': yellow_format})

				worksheet.conditional_format(1,2,a,3, {'type':   'duplicate',
													   'format': red_format})

				worksheet.conditional_format(1,1,a,b, {'type': 'text',
													  'criteria': 'containing',
													   'value':     'Not Given',
													   'format': yellow_format})

			import pyminizip
			pyminizip.compress(resource_path(self.user_name+'.xlsx'), None, resource_path(self.user_name+'.zip'), self.pdf_password, 5)
			os.remove(resource_path(self.user_name+'.xlsx'))
		except xlsxwriter.exceptions.FileCreateError as e:
			print(e)
			self.ShowMessageBox('Close File', 'Please Close Your File Before Saving')
		except OSError as e:
			self.ShowMessageBox('Fatal Error', 'Some Os Error')

	def sendEmail(self):
		# self.label_2.setText("Mail Successfully Sent")
		import smtplib
		from email.mime.multipart import MIMEMultipart
		from email.mime.text import MIMEText
		from email.mime.base import MIMEBase
		from email import encoders
		fromaddr = self.lineEdit.text()
		password=self.lineEdit_2.text()

		if fromaddr=="" or password=="" :
			self.ShowMessageBox('Error!!', "Password / Email can't be blank")
			return
		regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
		res=bool(re.match(regex, str(self.toaddr)))
		if res is False or str(self.toaddr)=="":
			self.ShowMessageBox('Error', 'Invalid Admin Email or No Internet')
			return
		try:
			msg = MIMEMultipart()
			msg['From'] = fromaddr
			msg['To'] = self.toaddr
			print(self.toaddr)
			msg['Subject'] = self.lineEdit_4.text()
			body = self.textEdit.toPlainText()
			msg.attach(MIMEText(body, 'plain'))
			self.exportModule()
			filename = self.user_name+'.zip'
			with open(resource_path(filename), 'rb') as attachment:
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
				self.ShowMessageBox2('Delivery Report', 'Mail successfuly sent')
				print("success")
				os.remove(resource_path(self.user_name+'.zip'))
				cursor.execute("UPDATE USER SET isSubmitted=True WHERE user_id=?",(self.user_id,))
				print(cursor.rowcount)
				db.commit()
				connection=connect(
					host="plumitnetwork.com",
					user="plum_user",
					password="y(l.%=Ud1vYm",
					database="db_plum")
				mycursor = connection.cursor()
				sql = "UPDATE  register SET isRegisterd = %s  WHERE email=%s "		
				val = (False, self.email)
				mycursor.execute(sql, val)
				connection.commit()
				print("updated")
				connection.close()
				mycursor.close()
				self.close()

		except (smtplib.SMTPAuthenticationError,TypeError,smtplib.SMTPRecipientsRefused) as e:
			self.ShowMessageBox('Error: INCORRECT EMAIL OR PASSWORD', 'YOU MUST HAVE GMAIL ADDRESS TO SUBMIT THE PROJECT \n \n OR \n \n INVALID EMAIL ADDRESS OR PASSWORD')
			print("Error on Email",e)
			print(fromaddr)
			print(password)
			os.remove(resource_path(self.user_name+'.zip'))
		except gaierror as e:
			self.ShowMessageBox('No Internet', 'Your Internet is not Connected')
			os.remove(resource_path(self.user_name+'.zip'))
		except OSError as e:
			self.ShowMessageBox('Fatal Error', 'Some Os Error')
		except Error as e :
			self.ShowMessageBox('MySql', 'You Have Error in Your SQL Connection')
			os.remove(resource_path(self.user_name+'.zip'))

	def ShowMessageBox(self,title, messege):
		msgBox=QtWidgets.QMessageBox()
		msgBox.setIcon(QMessageBox.Critical)
		msgBox.setWindowIcon(QIcon(resource_path("icon.ico")))
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
	form = SendForm(5,'alam','alamjamal888@gmail.com')
	form.show()
	app.exec_()