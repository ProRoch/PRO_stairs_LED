from PyQt5.QtGui import *
import sys
import types
        #from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class MyFrame(QGraphicsView):
    def __init__( self, parent = None ):
        super(MyFrame, self).__init__(parent)

        self.setScene(QGraphicsScene())

        # add some items
        x = 0
        y = 0
        w = 20
        h = 20
        pen = QPen(QColor(Qt.green))
        brush = QBrush(pen.color().darker(150))

        # i want a mouse over and mouse click event for this ellipse
        for xi in range(10):
            for yi in range(10):
                item = callbackRect(x+xi*30, y+yi*30, w, h)
                item.setAcceptHoverEvents(True)
                item.setPen(pen)
                item.setBrush(brush)
                self.scene().addItem(item)

        # item = self.scene().addEllipse(x, y, w, h, pen, brush)


        item.setFlag(QGraphicsItem.ItemIsMovable)

class callbackRect(QGraphicsRectItem):
    '''
    Rectangle call-back class.
    '''

    def mouseReleaseEvent(self, event):
        # recolor on click
        color = QColor(180, 174, 185)
        brush = QBrush(color)
        QGraphicsRectItem.setBrush(self, brush)

        return QGraphicsRectItem.mouseReleaseEvent(self, event)

    def hoverMoveEvent(self, event):
        # Do your stuff here.
        pass

if ( __name__ == '__main__' ):
    app = QApplication([])
    f = MyFrame()
    f.show()
    app.exec_()