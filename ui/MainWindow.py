from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
