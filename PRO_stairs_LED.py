import config as cfg
from PyQt5.QtGui import *
import sys
import types
        #from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from LED_program import *
import led_strip_driver as led_driver


color_LED_on = "#888800"


class Btn(QPushButton):
    expandable = pyqtSignal(int, int)
    clicked = pyqtSignal()
    ohno = pyqtSignal()


    def __init__(self, x, y, *args, **kwargs):
        super(Btn, self).__init__(*args, **kwargs)

        self.setFixedSize(QSize(10, 10))

        self.x = x
        self.y = y




class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.title = 'PyQt5 layout - Stairs LEDs lighting.'
        self.left = 100
        self.top = 300
        self.width = 1000
        self.height = 400
#        self.xLED_size = 3
        self.xLED_size = 30
        self.yLED_size = 15
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
        vLayout_LED     = QVBoxLayout()
        hLayout_main.addLayout(vLayout_Config)
        hLayout_main.addLayout(vLayout_LED)

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

        self.createGridLayout()
        vLayout_LED.addWidget(self.horizontalGroupBox)

        w = QWidget()
        w.setLayout(hLayout_main)
        self.setCentralWidget(w)
        self.initWidgets()
        #self.centralwidget = QtWidgets.QWidget(MainWindow) in our case we have Layout
        self.show()

        print("==================")




    def createGridLayout(self):
        layout = QGridLayout()
        view = QGraphicsView()
        layout.addWidget( view )
        scene = QGraphicsScene()

        view.setScene(scene)
        pen = QPen(QColor(Qt.green))
        brush = QBrush(pen.color().darker(150))
        global mySingleLedShape, myItemTab, myLedWith, myLedHight, myLedDeltaX, myLedDeltaY
        for xi in range(30):
            for yi in range(15):
                if cfg.mySingleLedShape == 0:
                    item = QGraphicsRectItem(xi * cfg.myLedDeltaX, yi * cfg.myLedDeltaY, cfg.myLedWith, cfg.myLedHight)
                    #item.setFlag(QGraphicsItem.ItemIsSelectable)
                    #item.setFlag(QGraphicsItem.ItemIsMovable)
                    #item.setFlag(QGraphicsItem.ItemIsFocusable)
                else:
                    item = QGraphicsEllipseItem(xi * cfg.myLedDeltaX, yi * cfg.myLedDeltaY, cfg.myLedWith, cfg.myLedHight)
                item.setPen(pen)
                item.setBrush(brush)
                scene.addItem(item)
                cfg.myItemTab.append(item)

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

        currProg = self.progClassHolder[programName](self.ledStripLenght, self.deltaTime)
        currProg.execute()



    def btn_pause_clicked(self):
        print("btn pause clicked.")

    def btn_stop_clicked(self):
        print("btn stop clicked.")

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
