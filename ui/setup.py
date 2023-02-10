import re

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from qt_material import apply_stylesheet

from GameWindow import GameWindow
from MainWindow import MainWindow
from level0 import Level0
from PyQt5 import QtCore
import sys
from save.SaveInfo import SaveInfo


class SetUp:
    Signal = pyqtSignal(int)

    def __init__(self):
        self.level = None
        self.saveinfo = SaveInfo()
        self.max_level_num = self.saveinfo.read_level_info()
        self.now_level = None
        self.desktop = QApplication.desktop()

    # jump to main window
    def show_main_window(self):
        self.now_level = -1
        self.hello = MainWindow()
        self.level0 = Level0()
        self.hello.startButton.clicked.connect(self.start)
        self.hello.restartButton.clicked.connect(self.restart)
        self.hello.exitButton.clicked.connect(self.exit)

        self.level0.nextButton.clicked.connect(self.start)

        self.hello.move(self.desktop.width() // 4, self.desktop.height() // 6)

        if self.max_level_num != -1:
            # 用户不是第一次玩
            self.hello.startButton.setText('继续')
        else:
            self.hello.startButton.setText('开始')

        self.hello.show()

    def restart(self):
        ok = QMessageBox().question(None, "Question", "是否清除所有存档?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ok == QMessageBox.Yes:
            self.max_level_num = -1
            self.saveinfo.save_level_info(self.max_level_num)
            self.hello.close()
            self.show_main_window()

    def exit(self):
        self.hello.close()

    def back_to_main_window(self):
        self.level.close()
        self.show_main_window()

    def start(self):
        if self.max_level_num == -1:
            # 第一次玩的用户，从hello进入到level0
            self.hello.close()
            self.level0.show()
            self.max_level_num = 0
            self.now_level = self.max_level_num
            return
        elif self.max_level_num == 0:
            # 玩过level0，从level0进入level1
            self.level0.bell.stop()
            self.level0.close()
            self.max_level_num = 1
            self.now_level = self.max_level_num
            self.saveinfo.save_level_info(self.now_level)
        else:
            # 玩过level1的用户，回到上一次的最后一关
            self.hello.close()
            self.now_level = self.max_level_num

        self.level = GameWindow(self, self.now_level)

        self.level.actionmain_screen.triggered.connect(self.back_to_main_window)
        self.level.actionlevel1.triggered.connect(lambda: self.switch_level(1))
        self.level.actionlevel2.triggered.connect(lambda: self.switch_level(2))
        self.level.actionlevel3.triggered.connect(lambda: self.switch_level(3))
        self.level.actionlevel4.triggered.connect(lambda: self.switch_level(4))
        self.level.actionlevel5.triggered.connect(lambda: self.switch_level(5))
        self.level.actionlevel6.triggered.connect(lambda: self.switch_level(6))
        self.level.actionlevel7.triggered.connect(lambda: self.switch_level(7))
        self.level.actionlevel8.triggered.connect(lambda: self.switch_level(8))
        self.level.actionlevel9.triggered.connect(lambda: self.switch_level(9))
        self.level.actionlevel10.triggered.connect(lambda: self.switch_level(10))
        self.level.actionlevel11.triggered.connect(lambda: self.switch_level(11))
        self.level.actionlevel12.triggered.connect(lambda: self.switch_level(12))
        self.level.actionlevel13.triggered.connect(lambda: self.switch_level(13))

        # dynamically generate the level
        self.display_level_info()
        # display current level information
        _translate = QtCore.QCoreApplication.translate
        self.level.menulevel.setTitle(_translate("MainWindow", "level " + str(self.now_level)))

        self.level.move(self.desktop.width() // 8, self.desktop.height() // 20)
        self.level.show()
        self.hello.close()

    def display_level_info(self):
        self.level.menulevel.addAction(self.level.actionlevel1)
        if self.max_level_num > 1:
            self.level.menulevel.addAction(self.level.actionlevel2)
        if self.max_level_num > 2:
            self.level.menulevel.addAction(self.level.actionlevel3)
        if self.max_level_num > 3:
            self.level.menulevel.addAction(self.level.actionlevel4)
        if self.max_level_num > 4:
            self.level.menulevel.addAction(self.level.actionlevel5)
        if self.max_level_num > 5:
            self.level.menulevel.addAction(self.level.actionlevel6)
        if self.max_level_num > 6:
            self.level.menulevel.addAction(self.level.actionlevel7)
        if self.max_level_num > 7:
            self.level.menulevel.addAction(self.level.actionlevel8)
        if self.max_level_num > 8:
            self.level.menulevel.addAction(self.level.actionlevel9)
        if self.max_level_num > 9:
            self.level.menulevel.addAction(self.level.actionlevel10)
        if self.max_level_num > 10:
            self.level.menulevel.addAction(self.level.actionlevel11)
        if self.max_level_num > 11:
            self.level.menulevel.addAction(self.level.actionlevel12)
        if self.max_level_num > 12:
            self.level.menulevel.addAction(self.level.actionlevel13)

    # switch level
    def switch_level(self, level_num):
        self.level.close()
        self.now_level = level_num

        self.level = GameWindow(self, self.now_level)
        self.level.actionmain_screen.triggered.connect(self.back_to_main_window)
        self.level.actionlevel1.triggered.connect(lambda: self.switch_level(1))
        self.level.actionlevel2.triggered.connect(lambda: self.switch_level(2))
        self.level.actionlevel3.triggered.connect(lambda: self.switch_level(3))
        self.level.actionlevel4.triggered.connect(lambda: self.switch_level(4))
        self.level.actionlevel5.triggered.connect(lambda: self.switch_level(5))
        self.level.actionlevel6.triggered.connect(lambda: self.switch_level(6))
        self.level.actionlevel7.triggered.connect(lambda: self.switch_level(7))
        self.level.actionlevel8.triggered.connect(lambda: self.switch_level(8))
        self.level.actionlevel9.triggered.connect(lambda: self.switch_level(9))
        self.level.actionlevel10.triggered.connect(lambda: self.switch_level(10))
        self.level.actionlevel11.triggered.connect(lambda: self.switch_level(11))
        self.level.actionlevel12.triggered.connect(lambda: self.switch_level(12))
        self.level.actionlevel13.triggered.connect(lambda: self.switch_level(13))

        # dynamically generate the level
        self.display_level_info()

        # display current level information
        _translate = QtCore.QCoreApplication.translate
        self.level.menulevel.setTitle(_translate("MainWindow", "level " + str(self.now_level)))

        self.level.move(self.desktop.width() // 8, self.desktop.height() // 20)
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
    apply_stylesheet(app, theme='dark_cyan.xml')
    window.show_main_window()
    sys.exit(app.exec_())
