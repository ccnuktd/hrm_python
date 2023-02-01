import re

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication

from GameWindow import GameWindow
from MainWindow import MainWindow
from PyQt5 import QtCore
import sys
from save.SaveInfo import SaveInfo


class SetUp:
    Signal = pyqtSignal(int)

    def __init__(self):
        self.level = None
        self.saveinfo = SaveInfo()
        self.max_level_num = self.saveinfo.read_level_info()
        self.now_level = 1

    # jump to main window
    def show_main_window(self):
        self.hello = MainWindow()
        self.hello.startButton.clicked.connect(self.show_level_1)
        self.hello.show()

    def show_level_1(self):
        self.level = GameWindow(self, 1)

        self.level.actionlevel1.triggered.connect(lambda: self.switch_level(1))
        self.level.actionlevel2.triggered.connect(lambda: self.switch_level(2))
        # self.level.actionlevel3.triggered.connect(self.switch_level_3)
        # self.level.actionlevel4.triggered.connect(self.switch_level_4)
        # self.level.actionlevel5.triggered.connect(self.switch_level_5)
        # self.level.actionlevel6.triggered.connect(self.switch_level_6)
        # self.level.actionlevel7.triggered.connect(self.switch_level_7)
        # self.level.actionlevel8.triggered.connect(self.switch_level_8)
        # self.level.actionlevel9.triggered.connect(self.switch_level_9)
        # self.level.actionlevel10.triggered.connect(self.switch_level_10)
        # self.level.actionlevel11.triggered.connect(self.switch_level_11)
        # self.level.actionlevel12.triggered.connect(self.switch_level_12)
        # self.level.actionlevel13.triggered.connect(self.switch_level_13)

        # dynamically generate the level
        self.display_level_info()
        # display current level information
        _translate = QtCore.QCoreApplication.translate
        self.level.menulevel.setTitle(_translate("MainWindow", "level 1"))

        self.level.show()
        self.hello.close()

    def display_level_info(self):
        self.level.menulevel.addAction(self.level.actionlevel1)
        if self.max_level_num > 1:
            self.level.menulevel.addAction(self.level.actionlevel2)
        # if self.max_level_num > 2:
        #     self.level.menulevel.addAction(self.level.actionlevel3)
        # if self.max_level_num > 3:
        #     self.level.meulevel.addAction(self.level.actionlevel4)
        # if self.max_level_num > 4:
        #     self.level.menulevel.addAction(self.level.actionlevel5)
        # if self.max_level_num > 5:
        #     self.level.menulevel.addAction(self.level.actionlevel6)
        # if self.max_level_num > 6:
        #     self.level.menulevel.addAction(self.level.actionlevel7)
        # if self.max_level_num > 7:
        #     self.level.menulevel.addAction(self.level.actionlevel8)
        # if self.max_level_num > 8:
        #     self.level.menulevel.addAction(self.level.actionlevel9)
        # if self.max_level_num > 9:
        #     self.level.menulevel.addAction(self.level.actionlevel10)
        # if self.max_level_num > 10:
        #     self.level.menulevel.addAction(self.level.actionlevel11)
        # if self.max_level_num > 11:
        #     self.level.menulevel.addAction(self.level.actionlevel12)
        # if self.max_level_num > 12:
        #     self.level.menulevel.addAction(self.level.actionlevel13)

    # switch level
    def switch_level(self, level_num):
        self.level.close()
        self.now_level = level_num

        self.level = GameWindow(self, self.now_level)
        self.level.actionlevel1.triggered.connect(lambda: self.switch_level(1))
        self.level.actionlevel2.triggered.connect(lambda: self.switch_level(2))

        # dynamically generate the level
        self.display_level_info()

        # display current level information
        _translate = QtCore.QCoreApplication.translate
        self.level.menulevel.setTitle(_translate("MainWindow", "level " + str(self.now_level)))

        self.level.show()

    def level_up(self):
        self.now_level = self.now_level + 1
        if self.now_level > 13:
            self.now_level = 13
            self.max_level_num = max(self.now_level, self.max_level_num)
        # record level data
        self.saveinfo.save_level_info(self.now_level)
        # switch level
        self.switch_level(self.now_level)



def setup(name='hrm', version='0.1', packages=['hrmengine'], url='', license='', author='Yu Huang',
          author_email='nana414021069@163.com', description=''):
    # make the program support high-resolution display
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = SetUp()
    window.show_main_window()
    sys.exit(app.exec_())
