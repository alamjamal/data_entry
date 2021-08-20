import sqlite3
from xlsxwriter import *
import pandas as pd
import numpy as np


db=sqlite3.connect("data.db")
cursor=db.cursor()
# df=pd.read_sql_query("SELECT * FROM data",db)
# df.replace('', np.nan, inplace=True)
# print(df.isnull().sum())

		

data=cursor.execute("SELECT * from data")
wb=Workbook('data_excel.xlsx')
sheet=wb.add_worksheet()
sheet.write(0,0,'id')
sheet.write(0,1,'formName')
sheet.write(0,2,'formNo')
sheet.write(0,3,'companyCode')
sheet.write(0,4,'companyName')
sheet.write(0,5,'companyAddress')
sheet.write(0,6,'zipCode')
sheet.write(0,7,'fax')
sheet.write(0,8,'website')
sheet.write(0,9,'email')
sheet.write(0,10,'contactNo')
sheet.write(0,11,'state')
sheet.write(0,12,'country')
sheet.write(0,13,'headquarter')
sheet.write(0,14,'noOfEmployees')
sheet.write(0,15,'industry')
sheet.write(0,16,'brandAmbassador')
sheet.write(0,17,'mediaPartner')
sheet.write(0,18,'socialMedia')
sheet.write(0,19,'frenchisePartner')
sheet.write(0,20,'investor')
sheet.write(0,21,'advertisingMedia')
sheet.write(0,22,'product')
sheet.write(0,23,'services')
sheet.write(0,24,'manager')
sheet.write(0,25,'subclassification')
sheet.write(0,26,'registrationDate')
sheet.write(0,27,'yearlyRevenue')
sheet.write(0,28,'landmark')
sheet.write(0,29,'accAudit')
sheet.write(0,30,'currency')
sheet.write(0,31,'yearlyExpense')

		
row_number=1
for row in data:
	print("row upper", row)
	column_number=0
	for item in row:
		print("row", row)
		print("item", item)
		sheet.write(row_number,column_number, str(item))
		column_number +=1
	row_number +=1

wb.close()
