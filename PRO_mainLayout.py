# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PRO_mainLayout.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1726, 869)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lediSearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lediSearch.setObjectName("lediSearch")
        self.verticalLayout.addWidget(self.lediSearch)
        self.SelectedProgList = QtWidgets.QListWidget(self.centralwidget)
        self.SelectedProgList.setObjectName("SelectedProgList")
        self.verticalLayout.addWidget(self.SelectedProgList)
        self.btnLoadProg = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadProg.setObjectName("btnLoadProg")
        self.verticalLayout.addWidget(self.btnLoadProg)
        self.pteDescription = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pteDescription.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pteDescription.setObjectName("pteDescription")
        self.verticalLayout.addWidget(self.pteDescription)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnStart = QtWidgets.QPushButton(self.centralwidget)
        self.btnStart.setObjectName("btnStart")
        self.horizontalLayout.addWidget(self.btnStart)
        self.btnPause = QtWidgets.QPushButton(self.centralwidget)
        self.btnPause.setObjectName("btnPause")
        self.horizontalLayout.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton(self.centralwidget)
        self.btnStop.setObjectName("btnStop")
        self.horizontalLayout.addWidget(self.btnStop)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_20.addLayout(self.verticalLayout)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_6.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout_6.addWidget(self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_6.addWidget(self.checkBox_3)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout_6.addWidget(self.checkBox_4)
        self.horizontalLayout_19.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_19.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_12.addWidget(self.label_7)
        self.spinBox = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout_12.addWidget(self.spinBox)
        self.verticalLayout_5.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_13.addWidget(self.label_8)
        self.spinBox_2 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_13.addWidget(self.spinBox_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_14.addWidget(self.label_9)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_14.addWidget(self.spinBox_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_15.addWidget(self.label_10)
        self.spinBox_4 = QtWidgets.QSpinBox(self.groupBox)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_15.addWidget(self.spinBox_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_19.addLayout(self.verticalLayout_5)
        self.verticalLayout_14.addLayout(self.horizontalLayout_19)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_11.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_11.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_11.addWidget(self.pushButton_5)
        self.verticalLayout_14.addLayout(self.horizontalLayout_11)
        self.verticalLayout_15.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_15 = QtWidgets.QLabel(self.groupBox_2)
        self.label_15.setFrameShape(QtWidgets.QFrame.Box)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_11.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.groupBox_2)
        self.label_16.setFrameShape(QtWidgets.QFrame.Box)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_11.addWidget(self.label_16)
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setFrameShape(QtWidgets.QFrame.Box)
        self.label_17.setObjectName("label_17")
        self.verticalLayout_11.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.groupBox_2)
        self.label_18.setFrameShape(QtWidgets.QFrame.Box)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_11.addWidget(self.label_18)
        self.verticalLayout_12.addLayout(self.verticalLayout_11)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_9.addWidget(self.lineEdit_6)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_8.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_8.addWidget(self.lineEdit_5)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_17.addWidget(self.pushButton_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_17.addWidget(self.pushButton_6)
        self.verticalLayout_12.addLayout(self.horizontalLayout_17)
        self.horizontalLayout_18.addLayout(self.verticalLayout_12)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setMaximumSize(QtCore.QSize(12, 16777215))
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.verticalSlider_4 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_4.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_4.setObjectName("verticalSlider_4")
        self.verticalLayout_9.addWidget(self.verticalSlider_4)
        self.horizontalLayout_16.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setMaximumSize(QtCore.QSize(12, 16777215))
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.verticalSlider_3 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_3.setObjectName("verticalSlider_3")
        self.verticalLayout_8.addWidget(self.verticalSlider_3)
        self.horizontalLayout_16.addLayout(self.verticalLayout_8)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setMaximumSize(QtCore.QSize(12, 16777215))
        self.label_11.setObjectName("label_11")
        self.verticalLayout_7.addWidget(self.label_11)
        self.verticalSlider_2 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_2.setObjectName("verticalSlider_2")
        self.verticalLayout_7.addWidget(self.verticalSlider_2)
        self.horizontalLayout_16.addLayout(self.verticalLayout_7)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setMaximumSize(QtCore.QSize(12, 16777215))
        self.label_14.setObjectName("label_14")
        self.verticalLayout_10.addWidget(self.label_14)
        self.verticalSlider_5 = QtWidgets.QSlider(self.groupBox_2)
        self.verticalSlider_5.setOrientation(QtCore.Qt.Vertical)
        self.verticalSlider_5.setObjectName("verticalSlider_5")
        self.verticalLayout_10.addWidget(self.verticalSlider_5)
        self.horizontalLayout_16.addLayout(self.verticalLayout_10)
        self.horizontalLayout_18.addLayout(self.horizontalLayout_16)
        self.verticalLayout_13.addLayout(self.horizontalLayout_18)
        self.progressBar = QtWidgets.QProgressBar(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_13.addWidget(self.progressBar)
        self.verticalLayout_15.addWidget(self.groupBox_2)
        self.horizontalLayout_20.addLayout(self.verticalLayout_15)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gbView = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gbView.sizePolicy().hasHeightForWidth())
        self.gbView.setSizePolicy(sizePolicy)
        self.gbView.setMinimumSize(QtCore.QSize(100, 0))
        self.gbView.setObjectName("gbView")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.gbView)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.myGraphicsView = QtWidgets.QGraphicsView(self.gbView)
        self.myGraphicsView.setObjectName("myGraphicsView")
        self.verticalLayout_3.addWidget(self.myGraphicsView)
        self.verticalLayout_4.addWidget(self.gbView)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbtnLedShapeS = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtnLedShapeS.setChecked(True)
        self.rbtnLedShapeS.setObjectName("rbtnLedShapeS")
        self.verticalLayout_2.addWidget(self.rbtnLedShapeS)
        self.rbtnLedShapeR = QtWidgets.QRadioButton(self.groupBox_3)
        self.rbtnLedShapeR.setObjectName("rbtnLedShapeR")
        self.verticalLayout_2.addWidget(self.rbtnLedShapeR)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label)
        self.ediDeltaX = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ediDeltaX.sizePolicy().hasHeightForWidth())
        self.ediDeltaX.setSizePolicy(sizePolicy)
        self.ediDeltaX.setMinimumSize(QtCore.QSize(20, 16))
        self.ediDeltaX.setMaximumSize(QtCore.QSize(20, 16))
        self.ediDeltaX.setObjectName("ediDeltaX")
        self.horizontalLayout_6.addWidget(self.ediDeltaX)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout_6, 0, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ediDeltaY = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ediDeltaY.sizePolicy().hasHeightForWidth())
        self.ediDeltaY.setSizePolicy(sizePolicy)
        self.ediDeltaY.setMaximumSize(QtCore.QSize(20, 16))
        self.ediDeltaY.setObjectName("ediDeltaY")
        self.horizontalLayout_3.addWidget(self.ediDeltaY)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.btnNewLedConfig = QtWidgets.QPushButton(self.groupBox_3)
        self.btnNewLedConfig.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btnNewLedConfig.setObjectName("btnNewLedConfig")
        self.horizontalLayout_3.addWidget(self.btnNewLedConfig)
        self.gridLayout.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setWordWrap(False)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.ediNumberRow = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ediNumberRow.sizePolicy().hasHeightForWidth())
        self.ediNumberRow.setSizePolicy(sizePolicy)
        self.ediNumberRow.setMinimumSize(QtCore.QSize(20, 16))
        self.ediNumberRow.setMaximumSize(QtCore.QSize(20, 16))
        self.ediNumberRow.setMaxLength(30)
        self.ediNumberRow.setObjectName("ediNumberRow")
        self.horizontalLayout_4.addWidget(self.ediNumberRow)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.ediLedInRow = QtWidgets.QLineEdit(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ediLedInRow.sizePolicy().hasHeightForWidth())
        self.ediLedInRow.setSizePolicy(sizePolicy)
        self.ediLedInRow.setMinimumSize(QtCore.QSize(20, 16))
        self.ediLedInRow.setMaximumSize(QtCore.QSize(20, 16))
        self.ediLedInRow.setMaxLength(30)
        self.ediLedInRow.setObjectName("ediLedInRow")
        self.horizontalLayout_5.addWidget(self.ediLedInRow)
        self.gridLayout.addLayout(self.horizontalLayout_5, 2, 0, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.horizontalLayout_7.addWidget(self.groupBox_3)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.btnExit = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnExit.setFont(font)
        self.btnExit.setObjectName("btnExit")
        self.horizontalLayout_7.addWidget(self.btnExit)
        self.verticalLayout_4.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_20.addLayout(self.verticalLayout_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1726, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btnLoadProg.setText(_translate("MainWindow", "Load Program"))
        self.btnStart.setText(_translate("MainWindow", "Start"))
        self.btnPause.setText(_translate("MainWindow", "Pause"))
        self.btnStop.setText(_translate("MainWindow", "Stop"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("MainWindow", "CheckBox"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_8.setText(_translate("MainWindow", "TextLabel"))
        self.label_9.setText(_translate("MainWindow", "TextLabel"))
        self.label_10.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_5.setText(_translate("MainWindow", "PushButton"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.label_15.setText(_translate("MainWindow", "TextLabel"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_17.setText(_translate("MainWindow", "TextLabel"))
        self.label_18.setText(_translate("MainWindow", "TextLabel"))
        self.label_6.setText(_translate("MainWindow", "TextLabel"))
        self.label_5.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_6.setText(_translate("MainWindow", "PushButton"))
        self.label_13.setText(_translate("MainWindow", "V1"))
        self.label_12.setText(_translate("MainWindow", "V1"))
        self.label_11.setText(_translate("MainWindow", "V1"))
        self.label_14.setText(_translate("MainWindow", "V1"))
        self.gbView.setTitle(_translate("MainWindow", "LED  Matrix"))
        self.groupBox_3.setTitle(_translate("MainWindow", "GroupBox"))
        self.rbtnLedShapeS.setText(_translate("MainWindow", "square"))
        self.rbtnLedShapeR.setText(_translate("MainWindow", "dot"))
        self.label.setText(_translate("MainWindow", "delta X:"))
        self.ediDeltaX.setText(_translate("MainWindow", "30"))
        self.label_2.setText(_translate("MainWindow", "delta Y:"))
        self.ediDeltaY.setText(_translate("MainWindow", "50"))
        self.btnNewLedConfig.setText(_translate("MainWindow", "Update"))
        self.label_4.setText(_translate("MainWindow", "Number of Row:"))
        self.ediNumberRow.setText(_translate("MainWindow", "15"))
        self.ediNumberRow.setPlaceholderText(_translate("MainWindow", "15"))
        self.label_3.setText(_translate("MainWindow", "LED in Row:"))
        self.ediLedInRow.setPlaceholderText(_translate("MainWindow", "30"))
        self.btnExit.setText(_translate("MainWindow", "Exit"))

