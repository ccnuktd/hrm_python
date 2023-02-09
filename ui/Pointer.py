from PyQt5 import QtCore
from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import QCoreApplication

from util.MyUtil import flash


class Pointer(QLabel):
    """pointer"""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setStyleSheet("color: white;background-color: #886C54")

    def _display_func(self):
        self.setStyleSheet("color: white;background-color: #886C54;border: 2px solid red;")

    def _clear_func(self):
        self.setStyleSheet("color: white;background-color: #886C54")

    def reset(self):
        self.setText("None")

    def set_value(self, pointer_value, flash_time):
        self.setText(str(pointer_value))
        self.display_value(flash_time)
        QCoreApplication.processEvents()

    def display_outbox(self, flash_time):
        self.setText("None")
        self.display_value(flash_time)
        QCoreApplication.processEvents()

    def display_value(self, flash_time):
        flash(self._display_func, self._clear_func, flash_time)
