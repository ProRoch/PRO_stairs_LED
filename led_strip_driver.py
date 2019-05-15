#from PRO_stairs_LED import MainWindow
import config as cfg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class NeoPixel:
    """
    A sequence of neopixels.

    :param ~microcontroller.Pin pin: The pin to output neopixel data on.
    :param int n: The number of neopixels in the chain
    :param int bpp: Bytes per pixel. 3 for RGB and 4 for RGBW pixels.
    :param float brightness: Brightness of the pixels between 0.0 and 1.0 where 1.0 is full
      brightness
    :param bool auto_write: True if the neopixels should immediately change when set. If False,
      `show` must be called explicitly.
    :param tuple pixel_order: Set the pixel color channel order. GRBW is set by default.

    Example for Circuit Playground Express:

    .. code-block:: python

        import neopixel
        from board import *

        RED = 0x100000 # (0x10, 0, 0) also works

        pixels = neopixel.NeoPixel(NEOPIXEL, 10)
        for i in range(len(pixels)):
            pixels[i] = RED

    Example for Circuit Playground Express setting every other pixel red using a slice:

    .. code-block:: python

        import neopixel
        from board import *
        import time

        RED = 0x100000 # (0x10, 0, 0) also works

        # Using ``with`` ensures pixels are cleared after we're done.
        with neopixel.NeoPixel(NEOPIXEL, 10) as pixels:
            pixels[::2] = [RED] * (len(pixels) // 2)
            time.sleep(2)
    """
    def __init__(self, pin, n, bpp=3, brightness=1.0, auto_write=True, pixel_order=None):
        self.pin = pin
        self.stripTab = []
        for i in range(n):
            self.stripTab.append(0x000000)
        self.bpp = bpp
        self.brightness = brightness
        self.auto_write = auto_write
        self.pixel_order = pixel_order
        self.xlenght = 30

    def setXLenght(self, lenght):
        self.xlenght = lenght

    def __len__(self):
        return len(self.stripTab)

    def __getitem__(self, index):
        if index < 0:
            index += len(self)
        if index >= self.n or index < 0:
            raise IndexError
        return self.stripTab[index]

    def show(self):
        """ magics happenig. Find pushButton on mainWindows and change color"""
        #print(" ===== I am in show function ----")
        if self.brightness > 0.99:
            global myItemTab
            for i in range(len(cfg.myItemTabHandler)):
                pen = QPen(QColor(self.stripTab[i]))
                brush = QBrush(pen.color())
                #brush = QBrush(pen.color().darker(100))
                cfg.myItemTabHandler[i].setPen(pen)
                cfg.myItemTabHandler[i].setBrush(brush)


        else:
            pass

    def _set_item(self, index, value):
        if index < 0:
            index += len(self)
        if index >= len(self.stripTab) or index < 0:
            raise IndexError
        if value >> 24:
            raise ValueError("only bits 0->23 valid for integer input")
        self.stripTab[index] = value
        if self.auto_write == True:
            pen = QPen(QColor(value))
            brush = QBrush(pen.color())
            # brush = QBrush(pen.color().darker(100))
            cfg.myItemTabHandler[index].setPen(pen)
            cfg.myItemTabHandler[index].setBrush(brush)

    def fill(self, color):
        """Colors all pixels the given ***color***."""
        auto_write = self.auto_write
        self.auto_write = False
        for i in range(len(self.stripTab)):
            self.stripTab[i] = color
        if auto_write:
            self.show()
        self.auto_write = auto_write


