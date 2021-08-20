from PyQt5.QtWidgets import (QWidget, QMainWindow, QGridLayout, QPushButton,
                             QApplication, QPlainTextEdit, QLabel)
from PyQt5.QtGui import QTextCursor

class BasicWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initWindow()

        # self.keyPressEvent(event)

    def initWindow(self):
        self.setGeometry(400, 300, 400, 100)

        self.grid = QGridLayout()

        self.label = QLabel('Description Line 1')
        self.grid.addWidget(self.label, 0, 0)

        self.field = QPlainTextEdit()
        self.field.setMaximumHeight(40)

        # self.field.textChanged.connect(self.keyPressEvent)

        #TODO how to disable enter/return key events in this field?
        self.grid.addWidget(self.field, 1, 0)

        self.button = QPushButton('Some Button')
        self.grid.addWidget(self.button)

        self.centralWidget = QWidget()
        self.centralWidget.setLayout(self.grid)
        self.setCentralWidget(self.centralWidget)

    # def some_event(self):
    # 	def keyPressEvent(self, event):
    # 		if event.key() == Qt.Key_Space:
    # 			# self.test_method()
    # 			print("alam")

    def keyPressEvent(self, event):
    	if event.key() == Qt.Key_Space:
    	# self.test_method()
    		print("alam")

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = BasicWindow()
    window.show()
    sys.exit(app.exec_())