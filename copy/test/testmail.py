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