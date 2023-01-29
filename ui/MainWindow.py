from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from MainWindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    switch_game_interface = QtCore.pyqtSignal()  # Jump to the game interface

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.goLevel)

    def goLevel(self):
        self.switch_game_interface.emit()
