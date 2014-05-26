from PyQt4 import QtGui, QtCore
import sys
import platform


label = False
app = QtGui.QApplication(sys.argv)

class myWindow(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('CVG2014')
        self.setFixedSize(900, 550)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.label = QtGui.QLabel('....', self)
        self.label.setFixedWidth(300)
        self.label.move(100, 8)
        self.button = QtGui.QPushButton('open file', self)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        OS_PLATFORM = platform.system()
        sender = self.sender()
        directory = '/home' if (OS_PLATFORM is 'Linux') else 'E:\PythonProjects\GEO_PROJ\GEO'
        fileName = QtGui.QFileDialog.getOpenFileName(sender, 'Open Xml file with points', directory, 'XML *.xml')
        fileName = fileName[fileName.rfind('/')+1:]
        self.label.setText(fileName)


win = myWindow()
win.show()
app.exec_()