from PyQt5.QtWidgets import QMessageBox


def send_email(recipient, email):

    message = QMessageBox()
    message.setIcon(QMessageBox.Information)
    message.setText("Email Sent")
    message.setWindowTitle("ok")
    message.exec_()
