from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


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
        self.width = 600
        self.height = 400
        self.xLED_size = 30
        self.yLED_size = 15
#        self.yLED_size = 15
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        hLayout_main    = QHBoxLayout()
        vLayout_Config  = QVBoxLayout()
        vLayout_LED     = QVBoxLayout()
        hLayout_main.addLayout(vLayout_Config)
        hLayout_main.addLayout(vLayout_LED)

        qle = QLineEdit()
        vLayout_Config.addWidget(qle)
        self.createGridLayout()
        vLayout_LED.addWidget(self.horizontalGroupBox)

        w = QWidget()
        w.setLayout(hLayout_main)
        self.setCentralWidget(w)

        self.show()

    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("Grid od LED block")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        for x in range(0, self.xLED_size):
            for y in range(0, self.yLED_size):
                btn = QPushButton(f"oXo")
                btn.setText(".")
                btn.setObjectName(f"{str(y)}_{str(x)}_button")
                btn.setMinimumSize(QSize(15, 15))
                btn.setMaximumSize(QSize(15, 15))
                btn.setAutoFillBackground(True)
                btn.setStyleSheet("background-color: %s" % (color_LED_on))
                btn.update()
                layout.addWidget(btn, y, x)
        self.horizontalGroupBox.setLayout(layout)




if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    app.exec_()
