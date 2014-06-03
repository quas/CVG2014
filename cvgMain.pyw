from PyQt4 import QtGui
import sys
import cvgLeicaXmlReader
import cvgMath

class myWindow(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle('CVG2014')
        self.setFixedSize(350, 350)
        self.setWindowIcon(QtGui.QIcon('static/Icon.png'))
        self.setStyleSheet("QMainWindow {background-image: url(static/background.png);}")
        self.directory = ''
        self.file = ''

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

        self.SB_HeightAboveSeaLevel = QtGui.QDoubleSpinBox(self)
        self.SB_HeightAboveSeaLevel.move(10, 75)
        self.SB_HeightAboveSeaLevel.setFixedWidth(50)
        self.SB_HeightAboveSeaLevel.setRange(-9999.99, 9999.99)

        self.labelPointsSeaLevel = QtGui.QLabel('Height above sea level', self)
        self.labelPointsSeaLevel.setFixedWidth(250)
        self.labelPointsSeaLevel.setFixedHeight(25)
        self.labelPointsSeaLevel.move(65, 87)

        self.buttonOpenFile = QtGui.QPushButton('...', self)
        self.buttonOpenFile.setFixedWidth(30)
        self.buttonOpenFile.setFixedHeight(27)
        self.buttonOpenFile.move(311, 4)
        self.buttonOpenFile.clicked.connect(self.getXmlFile)

        self.buttonGetVolume = QtGui.QPushButton('RUN', self)
        self.buttonGetVolume.setFixedWidth(52)
        self.buttonGetVolume.setFixedHeight(35)
        self.buttonGetVolume.move(9, 115)
        self.buttonGetVolume.clicked.connect(self.getVolume)

        self.showVolume = QtGui.QLabel('Get Vol', self)
        self.showVolume.setFixedWidth(140)
        self.showVolume.setFixedHeight(32)
        self.showVolume.move(72, 117)
        self.showVolume.setStyleSheet("QLabel { background-color: white; \
                                           border: 1px solid grey; \
                                           color: grey;}")


    def getVolume(self):

        xml_file = self.getFileName()
        points = cvgLeicaXmlReader.getPointsFromXmlFile(xml_file)
        if(xml_file and points):

            QUANTITY_POINTS_AT_X_AXIS = self.SB_WidthOfXAxis.value()
            STATIC_HEIGHT = self.SB_HeightAboveSeaLevel.value()

            rows = cvgLeicaXmlReader.getRowsFromPoints(points, QUANTITY_POINTS_AT_X_AXIS)
            quads = cvgLeicaXmlReader.getAllQuads(rows)

            volumes = []
            if (STATIC_HEIGHT or QUANTITY_POINTS_AT_X_AXIS) != 0:
                for quadrangle in quads:
                    Quadrangle_type = cvgMath.getTypeQuadrangle(quadrangle)
                    v = cvgMath.getVolumeQuadrangle(quadrangle, Quadrangle_type, STATIC_HEIGHT)
                    volumes.append(v)
            else:
                volumes = 0

            volumes = 0 if STATIC_HEIGHT == 0 else (round(sum(volumes), 3))
            result = '-'+str(volumes) if STATIC_HEIGHT < 0 else str(volumes)
            result = '0' if result == '-0' else result
            self.showVolume.setStyleSheet("QLabel { background-color: white; \
                                           border: 1px solid grey; \
                                           color: grey;}")
            self.showVolume.setText(result)
        else:
            self.showVolume.setText('Select the correct file!')
            self.showVolume.setStyleSheet("QLabel { background-color: white; \
                                           border: 1px solid grey; \
                                           color: red; \
                                           font-weight: bold}")

    def getFileName(self):
        return self.file

    def getXmlFile(self):
        sender = self.sender()
        path = QtGui.QFileDialog.getOpenFileName(sender, 'Open Xml file with points', self.directory, 'XML *.xml')
        fileName = path[path.rfind('/')+1:]
        self.directory = path[:path.rfind('/')]
        if(len(path) > 54):
            start = len(path)-54
            pathSlice = path[start:]
            pathSlice = pathSlice[pathSlice.find('/'):]
            pathSlice = '..'+pathSlice
        else:
            pathSlice = path
        self.labelFilename.setText(pathSlice)
        self.file = path


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    win = myWindow()
    win.show()
    app.exec_()