from PyQt4 import QtGui, QtCore
import sys
import platform



label = False
app = QtGui.QApplication(sys.argv)

class myWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('CVG2014')
        self.setFixedSize(350, 350)
        self.setWindowIcon(QtGui.QIcon('Icon.ico'))
        self.setStyleSheet("QMainWindow {background-image: url(static/background.png);}")


        self.labelFilename = QtGui.QLabel('Select .XML file with points', self)
        self.labelFilename.setFixedWidth(300)
        self.labelFilename.setFixedHeight(25)
        self.labelFilename.move(10, 5)
        self.labelFilename.setStyleSheet("QLabel { background-color: white; \
                                           border: 1px solid black; \
                                           color: grey;}")


        self.spinBox = QtGui.QSpinBox(self)
        self.spinBox.move(10, 35)
        self.spinBox.setFixedWidth(50)
        self.spinBox.setMaximum(9999)
        self.labelPointsWidth = QtGui.QLabel('Length of points on X axis', self)
        self.labelPointsWidth.setFixedWidth(250)
        self.labelPointsWidth.setFixedHeight(25)
        self.labelPointsWidth.move(65, 47.5)



        self.button = QtGui.QPushButton('...', self)
        self.button.setFixedWidth(30)
        self.button.setFixedHeight(27)
        self.button.move(311, 4)
        self.button.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        OS_PLATFORM = platform.system()
        sender = self.sender()
        directory = '/home' if (OS_PLATFORM is 'Linux') else 'E:\PythonProjects\GEO_PROJ\GEO'
        fileName = QtGui.QFileDialog.getOpenFileName(sender, 'Open Xml file with points', directory, 'XML *.xml')
        fileName = fileName[fileName.rfind('/')+1:]
        self.labelFilename.setText(fileName)


win = myWindow()

win.show()
app.exec_()