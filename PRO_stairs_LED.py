import config as cfg
import sys
import types

from PyQt5 import QtWidgets, QtCore, QtGui, Qt
from PRO_mainLayout import Ui_MainWindow
#

COLORS = [
    '#000000', '#82817f', '#820300', '#868417', '#007e03', '#037e7b', '#040079',
    '#81067a', '#7f7e45', '#05403c', '#0a7cf6', '#093c7e', '#7e07f9', '#7c4002',

    '#ffffff', '#c1c1c1', '#f70406', '#fffd00', '#08fb01', '#0bf8ee', '#0000fa',
    '#b92fc2', '#fffc91', '#00fd83', '#87f9f9', '#8481c4', '#dc137d', '#fb803c',
]


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

        # Setup the color selection buttons.
        self.primaryButton.pressed.connect(lambda: self.choose_color(self.set_primary_color))
        self.secondaryButton.pressed.connect(lambda: self.choose_color(self.set_secondary_color))

        # Initialize button colours.
        for n, hex in enumerate(COLORS, 1):
            btn = getattr(self, 'colorButton_%d' % n)
            btn.setStyleSheet('QPushButton { background-color: %s; }' % hex)
            btn.hex = hex  # For use in the event below

            def patch_mousePressEvent(self_, event):
                if event.type() == QtCore.QEvent.MouseButtonPress:
                    if event.button() == QtCore.Qt.LeftButton:
                        cfg.myColorPrimary = int(self_.hex.replace('#', ''), 16)
                        self.primaryButton.setStyleSheet('QPushButton { background-color: %s; }' % self_.hex)
                        # If image is left clicked, display a red bar.
                        print('one left')
                    elif event.button() == QtCore.Qt.RightButton:
                        cfg.myColorBg = int(self_.hex.replace('#', ''), 16)
                        self.secondaryButton.setStyleSheet('QPushButton { background-color: %s; }' % self_.hex)
                        print('one right')
                elif event.type() == QtCore.QEvent.MouseButtonDblClick:
                    # If image is double clicked, remove bar.
                    print('two')



            btn.mousePressEvent = types.MethodType(patch_mousePressEvent, btn)

    def choose_color(self, callback):
        dlg = QColorDialog()
        if dlg.exec():
            callback( dlg.selectedColor().name() )

    def set_primary_color(self, hex):
        #self.canvas.set_primary_color(hex)
        print(f"form primary color hex {hex}")
        self.lineEdit_6.setText( hex)
        self.label_6.setText("primary color")
        self.primaryButton.setStyleSheet('QPushButton { background-color: %s; }' % hex)
        cfg.myColorPrimary =  int(hex.replace('#',''),16 )

    def set_secondary_color(self, hex):
        self.secondaryButton.setStyleSheet('QPushButton { background-color: %s; }' % hex)
        cfg.myColorBg =  int(hex.replace('#',''),16 )

    def btn_load_prog_clicked(self):
        #self.canvas.set_secondary_color(hex)
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
        cfg.myLedPointerMain = 0    # reset pointer
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
