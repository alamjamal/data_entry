import pandas as pd
import numpy as np
import sqlite3
def sendMail():
	import smtplib
	from email.mime.multipart import MIMEMultipart
	from email.mime.text import MIMEText
	from email.mime.base import MIMEBase
	from email import encoders
	fromaddr = "alamjamal888@gmail.com"
	toaddr = "alamjamal88@gmail.com"
	msg = MIMEMultipart()
	msg['From'] = fromaddr
	msg['To'] = toaddr
	msg['Subject'] = "SUBJECT OF THE EMAIL"
	body = "TEXT YOU WANT TO SEND"
	msg.attach(MIMEText(body, 'plain'))
	filename = "pandas_conditional.xlsx"
	attachment = open(filename, "rb")
	part = MIMEBase('application', 'octet-stream')
	part.set_payload((attachment).read())
	encoders.encode_base64(part)
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
	msg.attach(part)
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.starttls()
	server.login(fromaddr, "ummebilli88")
	text = msg.as_string()
	server.sendmail(fromaddr, toaddr, text)
	server.quit()
	print("success")

db=sqlite3.connect("data.db")
cursor=db.cursor()

df=pd.read_sql_query("SELECT * from data where user_id=0",db)
df.replace('', 'Not Mentioned', inplace=True)
print(df)
a=df.shape[0]
b=df.shape[1]
print(b)
writer = pd.ExcelWriter('pandas_conditional.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='Sheet1',index=False)
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

# worksheet.conditional_format(1,1,a,b, {'type': 'text',
  #                                     'criteria': 'containing',
  #                                      'value':     "'",
  #                                      'format': red_format})
# worksheet.conditional_format(1,1,a,b, {'type': 'text',
  #                                     'criteria': 'containing',
  #                                      'value':     '?',
  #                                      'format': red_format})
# worksheet.conditional_format(1,1,a,b, {'type': 'text',
  #                                     'criteria': 'containing',
  #                                      'value':     '""',
  #                                      'format': red_format})


worksheet.conditional_format(1, 8, a, 8, {'type': 'text',
                                      'criteria': 'begins with',
                                       'value':     'http://www.',
                                       'format': white_format})

worksheet.conditional_format(1, 8, a, 8, {'type': 'no_blanks',
                                       'format': yellow_format})

writer.save()
sendMail()

