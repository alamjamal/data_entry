import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   win = QWidget()
   button1 = QPushButton(win)
   button1.setText("Show dialog!")
   button1.move(50,50)
   button1.clicked.connect(showDialog)
   win.setWindowTitle("Click button")
   win.show()
   sys.exit(app.exec_())
	
def showDialog():
   msgBox = QMessageBox()
   msgBox.setIcon(QMessageBox.Information)
   msgBox.setText("Are You Sure Want To Submit Your Project")
   msgBox.setWindowTitle("Confirmation")
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
   # msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      print('OK clicked')
      msgButtonClick()

def msgButtonClick():
   print("Button clicked is:")

def closeEvent(self, event):
      reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?',
      QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
      if reply == QMessageBox.Yes:
         event.accept()
      else:
         event.ignore()
	
if __name__ == '__main__': 
   window()