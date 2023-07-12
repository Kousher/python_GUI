from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QWidget, QMessageBox
from PyQt5.uic import loadUi
import sys
from send_email import send_email


class EmailSender(QMainWindow):
    def __init__(self):
        super(EmailSender, self).__init__()
        loadUi("email_sender.ui", self)

        self.pushButton.clicked.connect(self.send_email)

    def send_email(self):
        if self.lineEdit.text():
            send_email(recipient=self.lineEdit.text(),
                       email=self.textEdit.toPlainText())
        else:
            message = QMessageBox()
            message.setIcon(QMessageBox.Critical)
            message.setText("Invalid recipient")
            message.setWindowTitle("Error!")
            message.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmailSender()
    window.show()
    app.exec_()
