from email import message
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5 import uic, QtGui
import log_in
import sys

class MainWindow(QMainWindow, log_in.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.closeButton.clicked.connect(self.closeFunc)
        self.show()

    def closeFunc(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.question)
        msg.setWindowTitle("Close Message")
        msg.setText("Do you really want to exit?")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        msg.exec_()

        self.close()



def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    app.exec_()

if __name__=="__main__":
    main()