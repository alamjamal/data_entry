import sqlite3
db=sqlite3.connect("data.db")
cursor=db.cursor()
# fname="alam"
# lname="jamal"
# email="alam"
# password="jamal"
# cursor.execute("INSERT INTO USER ( FNAME, LNAME, EMAIL , PASSWORD , CREATED_AT) VALUES(?,?,?,?,DATE('NOW'))",(fname,lname,email,password))

cursor.execute("DELETE FROM USER WHERE CREATED_AT <= date('now','-1 DAY')")
db.commit();
print("success")

