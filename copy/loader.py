import os
from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets


class DatabaseWorker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()

    @QtCore.pyqtSlot(object)
    def writeToDatabase(self, value):
        self.started.emit()
        for i in range(value):
            QtCore.QThread.msleep(10)
            print(i)
        self.finished.emit()


class Windows_GUI(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # ...
        self.m_database_worker = DatabaseWorker()
        self.m_database_worker.moveToThread(thread)
        self.m_database_worker.started.connect(self.start_animation)

        button.clicked.connect(self.on_clicked)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        value = 1000
        wrapper = partial(self.m_database_worker.writeToDatabase, value)
        QtCore.QTimer.singleShot(0, wrapper)