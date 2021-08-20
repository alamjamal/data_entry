import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class LineEdit1():
	line=QtWidgets.QLineEdit()
	def keyPressEvent(self, event):
		if event.matches(QtGui.QKeySequence.Copy) or event.matches(QtGui.QKeySequence.Paste):
			return
		super().keyPressEvent(event)


if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)
	w = LineEdit1()
	w2 = LineEdit1()
	w.show()
	w2.show()
	app.exec_()