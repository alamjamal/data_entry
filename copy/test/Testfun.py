from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt, QTimer
class Employee:
	
	b="class variable"
	def __init__(self, id, name):  
		self.id = id  
		self.name = name

		self.a=10
		self.fun1()
		self.fun2()
		self.display()

	def fun1(self): #is function me a ko change kr skte hain
		# global a
		createdDate=QDate(2021,1,1)
		postDate=createdDate.addDays(60)
		print(postDate)
		currentDate = QDate.currentDate()
		remainDay=currentDate.daysTo(postDate)
		print(remainDay)
		count=6

		if remainDay==40 or remainDay==20 or remainDay==0:
			createdDate=QDate.currentDate().addDays(20)
			remainDay-=1
			count-=1


		print(count)
		print(createdDate)


		b=self.a+5
		print(b)
		a=self.a
		print(a)
		c=a+30
		if a==10:
			c=50

	def fun2(self):
		print(self.a)
		# print(self.c)
		# self.c=10

	def display(self):
		print(Employee.b)  
		# print(self.c)


Employee(1, "jamal")
