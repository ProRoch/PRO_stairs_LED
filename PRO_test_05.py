import sys
import threading
import time
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget


class QThread1(QtCore.QThread):
    timeOut = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = True


    def run(self):
        print("I am in QThread1 thread.... ")
        while self.running:
            print("in thread.... ")
            time.sleep(1)
            self.timeOut.emit()

class MyGui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.thread1 = QThread1()
        self.thread1.timeOut.connect(self.update_timer)
        self.thread1.running = True
        self.thread1.start()

    def initUi(self):
        self.setGeometry(500, 500, 300, 300)
        self.pb = QPushButton("Button", self)
        self.pb.move(50, 50)

    def update_timer(self):
        print("jestem in update_timer")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = MyGui()
    gui.show()
    sys.exit(app.exec_())