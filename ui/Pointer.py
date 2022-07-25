from PyQt5 import QtCore
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, QCoreApplication, QTime

from util.MyUtil import flash


class Pointer(QLabel):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(QtCore.Qt.AlignCenter)

    def display_func(self):
        self.setStyleSheet("border: 3px solid red;")

    def clear_func(self):
        self.setStyleSheet("")

    def set_value(self, pointer_value, flash_time):
        self.setText(str(pointer_value))
        self.display_value(flash_time)
        QCoreApplication.processEvents()

    def outbox(self, flash_time):
        self.setText("None")
        self.display_value(flash_time)
        QCoreApplication.processEvents()

    def display_value(self, flash_time):
        flash(self.display_func, self.clear_func, flash_time)
