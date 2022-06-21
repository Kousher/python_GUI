from PyQt5 import QtGui, QtCore
import sys
from PyQt5 import QtWidgets
from PyQt5 import QtGui
app = QtGui.QGuiApplication(sys.argv)

window = QtWidgets()
window.resize(300, 400)
window.setWindowTitle('TITLE1')

window_layout = QtGui.QVBoxLayout()
window.setLayout(window_layout)

label = QtGui.QLabel()   
text = '''<font face="tahoma"><span style="color:#45688E">THIS</span><span style="opacity:0"> TEXTANOTHER_WORD</span></font>'''
label.setText(text)

window_layout.addWidget(label)

window.show()
sys.exit(app.exec_())