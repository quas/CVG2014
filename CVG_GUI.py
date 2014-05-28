from PyQt4 import QtGui, QtCore
import sys
import platform

class myWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('CVG2014')
        self.setFixedSize(350, 350)
        self.setWindowIcon(QtGui.QIcon('static/Icon.png'))
        self.setStyleSheet("QMainWindow {background-image: url(static/background.png);}")
        self.directory = ''


        self.labelFilename = QtGui.QLabel('Select .XML file with points', self)
        self.labelFilename.setFixedWidth(300)
        self.labelFilename.setFixedHeight(25)
        self.labelFilename.move(10, 5)
        self.labelFilename.setStyleSheet("QLabel { background-color: white; \
                                           border: 1px solid grey; \
                                           color: grey;}")

        self.SB_WidthOfXAxis = QtGui.QSpinBox(self)
        self.SB_WidthOfXAxis.move(10, 35)
        self.SB_WidthOfXAxis.setFixedWidth(50)
        self.SB_WidthOfXAxis.setMaximum(9999)

        self.labelPointsWidth = QtGui.QLabel('Length of points on X axis', self)
        self.labelPointsWidth.setFixedWidth(250)
        self.labelPointsWidth.setFixedHeight(25)
        self.labelPointsWidth.move(65, 47.5)

        self.SB_HeightAboveSeaLevel = QtGui.QSpinBox(self)
        self.SB_HeightAboveSeaLevel.move(10, 75)
        self.SB_HeightAboveSeaLevel.setFixedWidth(50)
        self.SB_HeightAboveSeaLevel.setRange(-9999, 9999)

        self.labelPointsSeaLevel = QtGui.QLabel('Height above sea level', self)
        self.labelPointsSeaLevel.setFixedWidth(250)
        self.labelPointsSeaLevel.setFixedHeight(25)
        self.labelPointsSeaLevel.move(65, 87)

        self.buttonOpenFile = QtGui.QPushButton('...', self)
        self.buttonOpenFile.setFixedWidth(30)
        self.buttonOpenFile.setFixedHeight(27)
        self.buttonOpenFile.move(311, 4)
        self.buttonOpenFile.clicked.connect(self.buttonClicked)

        self.buttonGetVolume = QtGui.QPushButton('RUN', self)
        self.buttonGetVolume.setFixedWidth(52)
        self.buttonGetVolume.setFixedHeight(35)
        self.buttonGetVolume.move(9, 115)

        self.labelGetVolume = QtGui.QLabel('Get Vol', self)
        self.labelGetVolume.setFixedWidth(52)
        self.labelGetVolume.setFixedHeight(32)
        self.labelGetVolume.move(72, 117)
        self.labelGetVolume.setStyleSheet("QLabel { background-color: white; \
                                           border: 1px solid grey; \
                                           color: grey;}")

    def buttonClicked(self):

        sender = self.sender()
        # directory = '/home' if (OS_PLATFORM is 'Linux') else 'E:\PythonProjects\GEO_PROJ\GEO'
        path = QtGui.QFileDialog.getOpenFileName(sender, 'Open Xml file with points', self.directory, 'XML *.xml')
        fileName = path[path.rfind('/')+1:]
        self.directory = path[:path.rfind('/')]
        self.labelFilename.setText(fileName)

app = QtGui.QApplication(sys.argv)
win = myWindow()
win.show()
app.exec_()