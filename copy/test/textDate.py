from PyQt5.QtCore import QDate, QTime, QDateTime, Qt
# curDate = QDate.currentDate()

# print(now)
# print(now.toString(Qt.ISODate))

now="2021-1-18"
year,month,day=now.split('-')
print(type(year))

acDate = QDate(int(year),int(month),int(day)) #current date
postDate=acDate.addDays(20) #after 60 day

curDate=QDate(2021,2,6)
remainDay=curDate.daysTo(postDate) #remain day

if (remainDay==0 or remainDay==2 or remainDay==4):
	print("zero or two")
print(acDate)
print(postDate)
print(remainDay)








# self.postDate=self.createdDate.addDays(20)
        # self.currentDate = QDate.currentDate()
        # self.remainDay=self.currentDate.daysTo(self.postDate)
        # print(self.remainDay)