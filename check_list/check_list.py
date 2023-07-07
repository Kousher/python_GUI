import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget
from PyQt5.uic import loadUi
import sys


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        loadUi("check_list.ui", self)
        new_list = ["kousher", "Sad", "Rajib", "Nazmul"]
        for val in new_list:
            item = QListWidgetItem(val)
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            self.listWidget.addItem(item)
        self.pushButton.clicked.connect(self.toggle_all)

    def toggle_all(self):
        for i in range(self.listWidget.count()):
            item = self.listWidget.item(i)
            if item.checkState() == QtCore.Qt.Checked:
                item.setCheckState(QtCore.Qt.Unchecked)
            else:
                item.setCheckState(QtCore.Qt.Checked)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()
