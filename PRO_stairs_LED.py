import config as cfg
import sys
import types

from PyQt5 import QtWidgets, QtCore, QtGui
from PRO_mainLayout import Ui_MainWindow
#from PyQt5 import QtWidgets
#from PyQt5 import QtCore
#from PyQt5.QtGui import *



from LED_program import *

import led_strip_driver as led_driver


color_LED_on = "#888800"


class Btn(QtWidgets.QPushButton):
    expandable = QtCore.pyqtSignal(int, int)
    clicked = QtCore.pyqtSignal()
    ohno = QtCore.pyqtSignal()


    def __init__(self, x, y, *args, **kwargs):
        super(Btn, self).__init__(*args, **kwargs)

        self.setFixedSize(QtCore.QSize(10, 10))

        self.x = x
        self.y = y




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.title = 'PyQt5 layout - Stairs LEDs lighting.'
        self.left = 100
        self.top = 50
        self.width = 1600
        self.height = 600
        #        self.xLED_size = 3
        self.xLED_size = cfg.myLedInSingleRow
        self.yLED_size = cfg.myLedRow
        #        self.yLED_size = 4
        self.ledStripLenght =  self.xLED_size * self.yLED_size
        self.deltaTime = 500

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.progClassHolder = initClassHolder()

        self.setupUi(self)
        self.createGridLayout()

        #listW =self.findChild(QListWidget,"SelectedProgList")
        #listW.setSelectionMode(QAbstractItemView.SingleSelection)
        self.SelectedProgList.itemSelectionChanged.connect(self.prog_list_update)

        #btnLoadProg =self.findChild(QPushButton,"btnLoadProg")
        self.btnLoadProg.clicked.connect(self.btn_load_prog_clicked)
        self.btnStart.clicked.connect(self.btn_start_clicked)
        self.btnPause.clicked.connect(self.btn_pause_clicked)
        self.btnStop.clicked.connect(self.btn_stop_clicked)
        self.btnExit.clicked.connect(self.btn_exit)
        self.btnNewLedConfig.clicked.connect(self.btn_NewLedConfig)
        self.initWidgets()
        self.show()

        print("==================")

        #self._timer = QTimer()
        #self._timer.timeout.connect(self.update_timer)
        #self._timer.start(5000)  # 1 second timer


    def createGridLayout(self):
        scene = QGraphicsScene()
        self.myGraphicsView.setScene(scene)

        self.myGraphicsView.setMinimumWidth(cfg.myLedInSingleRow*  cfg.myLedDeltaX +  cfg.myLedDeltaX)
        self.myGraphicsView.setMinimumHeight(cfg.myLedRow * cfg.myLedDeltaY + cfg.myLedDeltaY)
        self.setMinimumWidth(700+self.myGraphicsView.minimumWidth())
        pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.green))
        brush = QtGui.QBrush(pen.color().darker(150))
        global mySingleLedShape, myItemTab, myLedWith, myLedHight, myLedDeltaX, myLedDeltaY
        for yi in range(cfg.myLedRow):
            for xi in range(cfg.myLedInSingleRow):
                if cfg.mySingleLedShape == 0:
                    item = QGraphicsRectItem( (cfg.myLedInSingleRow* cfg.myLedDeltaX)- xi * cfg.myLedDeltaX,
                                              (cfg.myLedRow* cfg.myLedDeltaY)-yi * cfg.myLedDeltaY,
                                              cfg.myLedWith, cfg.myLedHight)
                    #item.setFlag(QGraphicsItem.ItemIsSelectable)
                    #item.setFlag(QGraphicsItem.ItemIsMovable)
                    #item.setFlag(QGraphicsItem.ItemIsFocusable)
                else:
                    item = QGraphicsEllipseItem(xi * cfg.myLedDeltaX, yi * cfg.myLedDeltaY, cfg.myLedWith, cfg.myLedHight)
                item.setPen(pen)
                item.setBrush(brush)
                scene.addItem(item)
                cfg.myItemTabHandler.append(item)

        cfg.myGrapicsScene = scene





    def update_timer(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

    def prog_list_update(self):
        #listW =self.findChild(QListWidget,"SelectedProgList")
        #self.SelectedProgList =self.findChild(QListWidget,"SelectedProgList")
        desc = program_List[self.SelectedProgList.currentRow()]["description"]
        #self.pteDescription = self.findChild(QPlainTextEdit, "txtB_Description")
        self.pteDescription.setPlaceholderText(desc)

    #        buttonReply = QMessageBox.question(self, 'PyQt5 message', desc, QMessageBox.Cancel)

    def initWidgets(self):
        listW =self.findChild(QListWidget,"SelectedProgList")
        for prog in program_List :
            listW.addItem(prog["name"])

    def btn_load_prog_clicked(self):
        print("btn load_prog clicked.")

    def btn_start_clicked(self):
        print("btn start clicked.")
        listW = self.findChild(QListWidget, "SelectedProgList")
        programName = program_List[listW.currentRow()]["progName"]
        cfg.myProgMain = self.progClassHolder[programName](self.ledStripLenght, self.deltaTime)



    def btn_pause_clicked(self):
        print("btn pause clicked.")



    def btn_stop_clicked(self):
        print("btn stop clicked.")
        cfg.myProgMain.myThread.running = False


    def btn_exit(self):
        sys.exit()

    def btn_NewLedConfig(self):
        if self.rbtnLedShapeS.isChecked():
            cfg.mySingleLedShape = 1
        elif self.rbtnLedShapeR.isChecked():
            cfg.mySingleLedShape = 0
        tmpDeltaX = int(self.ediDeltaX.text())
        if 0< int(tmpDeltaX)  and int(tmpDeltaX) < 100 :
            cfg.myLedDeltaX = tmpDeltaX + cfg.myLedWith

        tmpDeltaY = int(self.ediDeltaY.text())
        if 0< int(tmpDeltaY)  and int(tmpDeltaY) < 100 :
            cfg.myLedDeltaY = tmpDeltaY + cfg.myLedHight
        tmpLedInRow = int(self.ediLedInRow.text())
        if 0< int(tmpLedInRow)  and int(tmpLedInRow) < 100 :
            cfg.myLedInSingleRow = tmpLedInRow

        tmpNumberRow = int(self.ediNumberRow.text())
        if 0< int(tmpNumberRow)  and int(tmpNumberRow) < 30 :
            cfg.myLedRow = tmpNumberRow
        self.createGridLayout()


    class ClassHolder(object):
        def __init__(self):
            self.classes = {}

        def add_class(self, c):
            self.classes[c.__name__] = c

        def __getitem__(self, n):
            return self.classes[n]




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
