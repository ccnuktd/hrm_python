# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hrm_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = OperationDropList(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(390, 50, 151, 441))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = CodeDropList(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(580, 50, 161, 491))
        self.listWidget_2.setObjectName("listWidget_2")
        self.widget = OpCodeWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(130, 150, 121, 101))
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
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
from MyWidget import CodeDropList, OpCodeWidget, OperationDropList
