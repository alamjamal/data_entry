from mysql.connector import connect, Error

# try:
# 	with connect(
# 		host="remotemysql.com",
# 		user="W4OzzEsjRw",
# 		password="c7fK7ePJlR",
# 		database="W4OzzEsjRw",
# 	) as connection:
# 		print(connection)
# except Error as e:
# 	print(e)

connection=connect(
		host="remotemysql.com",
		user="W4OzzEsjRw",
		password="c7fK7ePJlR",
		database="W4OzzEsjRw"
	)

mycursor = connection.cursor()

sql = "INSERT INTO register ( auth_code, fname, lname, email) VALUES ( %s,%s, %s,%s)"
val = ("675tgbhj",'alam','jamal','alam@gmail.com')
mycursor.execute(sql, val)

connection.commit()

print(mycursor.rowcount, "record inserted.")