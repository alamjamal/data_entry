import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox,QPushButton

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Hello World')
        button1 = QPushButton()
        button1.setText("Show dialog!")
        button1.move(50,50)
        button1.clicked.connect(self.showDialog)
        self.show()

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
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())