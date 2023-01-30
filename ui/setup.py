from PyQt5.QtWidgets import QMainWindow, QApplication

from GameWindow import GameWindow
from MainWindow import MainWindow
from PyQt5 import QtCore
import sys


class SetUp:
    def __init__(self):
        pass

    # jump to main window
    def show_main_window(self):
        self.hello = MainWindow()
        self.hello.startButton.clicked.connect(self.show_game_level)
        self.hello.show()

    # jump to game window and close old window
    def show_game_level(self):
        self.level = GameWindow()
        self.level.actionlevel1.triggered.connect(self.switch_level)
        self.level.actionlevel2.triggered.connect(self.switch_level)
        self.level.actionlevel3.triggered.connect(self.switch_level)
        self.level.show()
        self.hello.close()

    # switch level
    def switch_level(self):
        # if it can swtich
        if True:
            self.level.close()
            self.level = GameWindow()
            self.level.actionlevel1.triggered.connect(self.switch_level)
            self.level.actionlevel2.triggered.connect(self.switch_level)
            self.level.actionlevel3.triggered.connect(self.switch_level)
            self.level.show()
        # if not
        else:
            pass


def setup(name='hrm', version='0.1', packages=['hrmengine'], url='', license='', author='Yu Huang', author_email='nana414021069@163.com', description=''):
    # make the program support high-resolution display
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = SetUp()
    window.show_main_window()
    sys.exit(app.exec_())
