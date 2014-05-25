

from PyQt4 import QtGui, QtCore
import sys
import platform

OS_PLATFORM = platform.system()
label = False
app = QtGui.QApplication(sys.argv)
window = QtGui.QWidget()

class myWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('CVG2014')
        self.setFixedSize(900, 550)
        self.setWindowIcon(QtGui.QIcon('donkey.ico'))

    def buttonClicked(self):
        global OS_PLATFORM
        global label
        if (not label):
            label = QtGui.QLabel('....')
            label.move(20, 0)
            vbox = QtGui.QVBoxLayout()
            vbox.addWidget(label)
            self.setLayout(vbox)

        sender = self.sender()
        directory = '/home' if (OS_PLATFORM is 'Linux') else 'E:\PythonProjects\GEO_PROJ\GEO'
        fileName =  QtGui.QFileDialog.getOpenFileName(sender, 'Open Xml file with points', directory, 'XML *.xml')
        label.setText(fileName)
        label.move(20, 0)

win = myWindow()
button = QtGui.QPushButton('open file', win)
button.clicked.connect(win.buttonClicked)
win.show()
app.exec_()