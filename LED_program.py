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

cfg.ledStripLine = NeoPixel(11, 450, 3, 1.0, False, "RGB")
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

class prog_30(LedProgram):
    def __init__(self, lenght, deltaTime):
        super(prog_30, self).__init__(lenght, deltaTime)
        print("se jestem prog-30")


    def execute(self):
        print("Prog_3 just started.")
        cfg.uiButtonTable[3].setStyleSheet("background-color: %s" % (hex(cfg.ledStripLine.stripTab[3]).replace('0x', '#')))
        cfg.uiButtonTable[3].update()


