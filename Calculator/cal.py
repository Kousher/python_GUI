from email import message
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
import calculator
import sys

class MainWindow(QMainWindow, calculator.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.zeroButton.clicked.connect(lambda: self.method('0'))
        self.oneButton.clicked.connect(lambda: self.method('1'))
        self.twoButton.clicked.connect(lambda: self.method('2'))
        self.threeButton.clicked.connect(lambda: self.method('3'))
        self.fourButton.clicked.connect(lambda: self.method('4'))
        self.fiveButton.clicked.connect(lambda: self.method('5'))
        self.sixButton.clicked.connect(lambda: self.method('6'))
        self.sevenButton.clicked.connect(lambda: self.method('7'))
        self.eightButton.clicked.connect(lambda: self.method('8'))
        self.nineButton.clicked.connect(lambda: self.method('9'))

        self.percentButton.clicked.connect(lambda: self.method('%'))
        self.cButton.clicked.connect(lambda: self.method('c'))
        self.arrowButton.clicked.connect(lambda: self.method('<<'))
        self.divideButton.clicked.connect(lambda: self.method('/'))
        self.multiplyButton.clicked.connect(lambda: self.method('*'))
        self.minusButton.clicked.connect(lambda: self.method('-'))
        self.plusButton.clicked.connect(lambda: self.method('+'))
        self.equalButton.clicked.connect(lambda: self.method('='))
        self.dotButton.clicked.connect(lambda: self.method('.'))
        #self.plusminusButton.clicked.connect(self.methodPlusminus)


    def method(self,val):
        text = self.label.text()
        try:
            if val=='=':
                if text=='=':
                    self.label.setText('')    
                else:      
                    answer = eval(text)
                    self.label.setText(str(answer))
            elif val=='<<':
                text = text[:-1]
                self.label.setText(text) 

            elif val=='c':
                self.label.setText('')
            elif val=='.':
                if '.' in text:
                    pass
                else:
                    self.label.setText(text+val)
            else:
                if text=='0':
                    self.label.setText('')
                else:
                    self.label.setText(text+val)
        except:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Warning MessageBox")
            msg.setText("Error")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msg.exec_()

def main():
    app = QApplication(sys.argv)
    mw = MainWindow()
    app.exec_()

if __name__=="__main__":
    main()