from PyQt5 import QtGui
from PyQt5 import QtCore

import time
import os
from led_strip_driver import NeoPixel
import config as cfg
from PyQt5.QtWidgets import *

program_List = []
program = {"name":"running light", "description": "one led moving from begin to end", "progName": "prog_01"}
program_List.append(program)
program = {"name":"step by step: UP", "description": "single step lighting one by one in UP direction", "progName": "prog_02"}
program_List.append(program)
program = {"name":"step by step: DOWN", "description": "single step lighting one by one in DOWN direction", "progName": "prog_03"}
program_List.append(program)
program = {"name":"Single Led run", "description": "Prog10: single Led running from begin to end direction", "progName": "prog_10"}
program_List.append(program)
program = {"name":"single test action", "description": "single test action for temporary check", "progName": "prog_30"}
program_List.append(program)

cfg.ledStripLine = NeoPixel(11, 450, 3, 1.0, True, "RGB")
cfg.ledStripLine.fill(0x000000)

class ClassHolder(object):
    def __init__(self):
        self.classes = {}

    def add_class(self, c):
        self.classes[c.__name__] = c

    def __getitem__(self, n):
        return self.classes[n]

def initClassHolder():
    list_Classes = ClassHolder()
    list_Classes.add_class(prog_01)
    list_Classes.add_class(prog_02)
    list_Classes.add_class(prog_03)
    list_Classes.add_class(prog_10)
    list_Classes.add_class(prog_30)
    return list_Classes


class LedProgram:
    deltaTime = 60
    strip_lenght = 1

    def __init__(self, strip_lenght, deltaTime, *args, **kwargs):

        self.time = deltaTime
        self.strip_lenght = strip_lenght

class prog_01(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_01, self).__init__(lenght, deltaTime)
        print("se jestem prog-01")

    def execute(self):
        print("Prog_1 just started.")
        cfg.ledStripLine.fill(0xFF0000)
        cfg.ledStripLine.show()

class prog_02(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_02, self).__init__(lenght, deltaTime)
        print("se jestem prog-02")

    def execute(self):
        print("Prog_2 just started.")
        cfg.ledStripLine._set_item(4,0x00FF00)
        cfg.ledStripLine.show()


class prog_03(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_03, self).__init__(lenght, deltaTime)
        print("se jestem prog-03")

    def execute(self):
        print("Prog_3 just started.")
        cfg.ledStripLine._set_item(4,0x0000FF)
        cfg.ledStripLine.show()




class prog_10(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_10, self).__init__(lenght, deltaTime)
        print("se jestem prog-10")
        self.mainPointer = 0
        self.mainColorBg = QtGui.QColor.yellow
        self.mainColorChange = QtGui.QColor.red
        self.myThread = QThread1()
        self.myThread.timeOut.connect(self.updateTimer)
        self.myThread.running = True
        self.myThread.start()

    def updateTimer(self):
        #print("jestem in update_timer main")
        cfg.ledStripLine._set_item(cfg.myLedPointerMain, 0x00FF00)
        cfg.myLedPointerMain = cfg.myLedPointerMain + 1
        cfg.ledStripLine._set_item(cfg.myLedPointerMain, 0x0000FF)
        if cfg.myLedPointerMain +1 >= cfg.myLedInSingleRow * cfg.myLedRow:
            cfg.myLedPointerMain = 0
        #cfg.ledStripLine.show()




class prog_30(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_30, self).__init__(lenght, deltaTime)
        print("se jestem prog-30")


    def execute(self):
        print("Prog_30 just started.")
        #pen = QPen(QColor(0x112233))
        #brush = QBrush(pen.color().darker(100))
        #cfg.myItemTab[1].setPen(pen)
        #cfg.myItemTab[1].setBrush(brush)
        pen2 = QtGui.QPen(QtGui.QColor(QtGui.Qt.yellow))
        brush2 = QtGui.QBrush(pen2.color().darker(150))
        cfg.myItemTabHandler[1].setPen(pen2)
        cfg.myItemTabHandler[1].setBrush(brush2)
        """
        cfg.myItemTab[1].setFlag(QGraphicsItem.ItemIsSelectable)
        cfg.myItemTab[1].setFlag(QGraphicsItem.ItemIsMovable)
        cfg.myItemTab[1].setFlag(QGraphicsItem.ItemIsFocusable)

        cfg.myItemTab[2].setFlag(QGraphicsItem.ItemIsMovable)
        cfg.myItemTab[3].setFlag(QGraphicsItem.ItemIsMovable)
        cfg.myItemTab[4].setFlag(QGraphicsItem.ItemIsMovable)
        cfg.myItemTab[5].setFlag(QGraphicsItem.ItemIsMovable)
        """

class QThread1(QtCore.QThread):
    timeOut = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True



    def run(self):
        print("New thread  QThread1 started... ")
        while self.running:
            time.sleep(0.005)
            self.timeOut.emit()



