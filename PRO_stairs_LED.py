import config as cfg
import sys
import types

from PyQt5 import QtWidgets, QtCore, QtGui

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




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.title = 'PyQt5 layout - Stairs LEDs lighting.'
        self.left = 100
        self.top = 50
        self.width = 1200
        self.height = 600
#        self.xLED_size = 3
        self.xLED_size = cfg.myLedInSingleRow
        self.yLED_size = cfg.myLedRow
#        self.yLED_size = 4
        self.ledStripLenght =  self.xLED_size * self.yLED_size
        self.deltaTime = 500

        self.initUI()

        self.progClassHolder = initClassHolder()


        #self._timer = QTimer()
        #self._timer.timeout.connect(self.update_timer)
        #self._timer.start(5000)  # 1 second timer



    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hLayout_main    = QHBoxLayout()
        vLayout_Config  = QVBoxLayout()
        vLayout_ConfigParam  = QVBoxLayout()
        vLayout_LED     = QVBoxLayout()
        hLayout_main.addLayout(vLayout_Config)
        hLayout_main.addLayout(vLayout_ConfigParam)
        hLayout_main.addLayout(vLayout_LED)

        ###==--vLayout_Config----GUI--layout1--------------------------
        qle = QLineEdit()
        listW = QListWidget()
        listW.setObjectName("SelectedProgList")
        listW.setSelectionMode(QAbstractItemView.SingleSelection)
        listW.itemSelectionChanged.connect(self.prog_list_update)

        btn_load_prog = QPushButton("Load Program")
        btn_load_prog.setObjectName("btn_load_prog")
        btn_load_prog.clicked.connect(self.btn_load_prog_clicked)


        txtb =QPlainTextEdit()
        txtb.setObjectName("txtB_Description")
        txtb.setMaximumHeight(200)
        #
        hLayout_control_btn = QHBoxLayout()

        btn = QPushButton("Start")
        btn.setObjectName("btn_Start")
        btn.clicked.connect(self.btn_start_clicked)
        hLayout_control_btn.addWidget(btn)
        btn = QPushButton("Pause")
        btn.setObjectName("btn_Pause")
        btn.clicked.connect(self.btn_pause_clicked)
        hLayout_control_btn.addWidget(btn)
        btn = QPushButton("Stop")
        btn.setObjectName("btn_Stop")
        btn.clicked.connect(self.btn_stop_clicked)
        hLayout_control_btn.addWidget(btn)


        vLayout_Config.addWidget(qle)
        vLayout_Config.addWidget(listW)
        vLayout_Config.addWidget(btn_load_prog)
        vLayout_Config.addWidget(txtb)
        vLayout_Config.addLayout(hLayout_control_btn)
        ###==--end------end----vLayout_Config----GUI--layout1--------------------------

        self.createGridLayout()
        vLayout_LED.addWidget(self.horizontalGroupBox)



        """
        #### start  from do funkcji
        #self.createConfigParam(vLayout_ConfigParam)
        self.groupBox = QtWidgets.QGroupBox("Grid for Parameter.")
        self.groupBox.setObjectName("groupBox")

        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)

        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)

        vLayout_ConfigParam.addWidget(self.groupBox)
       # self.groupBox.setLayout(self.gridLayout)

        #### end  from do funkcji

        """





        w = QWidget()
        w.setLayout(hLayout_main)
        self.setCentralWidget(w)
        self.initWidgets()
        #self.centralwidget = QtWidgets.QWidget(MainWindow) in our case we have Layout
        self.show()

        print("==================")

    def createConfigParam(self, layout):

        layout = QGroupBox("Grid for Parameter.")
        myGrid = QGridLayout()
        lbl1 = QLabel()
        qle = QLineEdit()
        myGrid.addWidget(lbl1, 0,0)
        myGrid.addWidget(qle, 0,1)
        layout.setLayout(myGrid)




    def createGridLayout(self):
        layout = QGridLayout()
        view = QGraphicsView()
        scene = QGraphicsScene()
        view.setScene(scene)
        layout.addWidget( view )
        view.setMinimumWidth(cfg.myLedInSingleRow*  cfg.myLedDeltaX +  cfg.myLedDeltaX)
        view.setMinimumHeight(cfg.myLedRow * cfg.myLedDeltaY + cfg.myLedDeltaY)

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
        self.horizontalGroupBox = QGroupBox("Grid od LED block")
        self.horizontalGroupBox.setLayout(layout)




    def update_timer(self):
        buttonReply = QMessageBox.question(self, 'PyQt5 message', "Do you want to save?", QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel, QMessageBox.Cancel)

    def prog_list_update(self):
        listW =self.findChild(QListWidget,"SelectedProgList")
        desc = program_List[listW.currentRow()]["description"]
        txtB = self.findChild(QPlainTextEdit, "txtB_Description")
        txtB.setPlaceholderText(desc)

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
