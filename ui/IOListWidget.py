from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import QSize, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QLabel, QHBoxLayout
from util.MyUtil import flash, is_int


class IOBlockWidget(QWidget):
    """inner block in input box and output box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._number = None

    def get_number(self):
        """get number of type int"""
        return self._number.text()

    def set_number(self, number):
        if is_int(number):
            self._number = QLabel(str(number))
        else:
            self._number = QLabel(number)

    def set_font(self, font=QFont("Arial", 10, QFont.Black)):
        self._number.setFont(font)

    def set_layout(self):
        self._number.setAlignment(QtCore.Qt.AlignCenter)
        layout = QHBoxLayout()
        layout.addWidget(self._number)
        self.setLayout(layout)

    def set_all(self, number):
        """simple setup"""
        self.set_number(number)
        self.set_font()
        self.set_layout()


class InputListWidget(QListWidget):
    """input box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(False)
        self.setDragEnabled(False)

    def _addItem(self, number):
        item_widget = QListWidgetItem()
        # set inner item height=50
        item_widget.setSizeHint(QSize(0, 50))

        op = IOBlockWidget()
        op.set_all(number)

        self.addItem(item_widget)
        self.setItemWidget(item_widget, op)

    def add_item(self, number):
        self._addItem(number)

    def init_inbox(self, input_list):
        self.clear()
        # input is int or intString
        for input in input_list:
            self._addItem(int(input))

    def display_func(self):
        """animation display"""
        widget = self.itemWidget(self.item(0))
        widget.setStyleSheet("border: 3px solid red;")

    def clear_func(self):
        """animation clear"""
        widget = self.itemWidget(self.item(0))
        widget.setStyleSheet("")

    def inbox(self, flash_time):
        flash(self.display_func, self.clear_func, flash_time)
        # takeItem is used to delete item
        self.takeItem(0)
        # refresh event loop and prevent the GUI from freezing
        QCoreApplication.processEvents()

    # the following three functions are used to disable selection
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()


class OutputListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(False)
        self.setDragEnabled(False)

    def init_outbox(self):
        self.clear()

    def _addItem(self, number):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 50))

        op = IOBlockWidget()
        op.set_all(number)

        self.addItem(item_widget)
        self.setItemWidget(item_widget, op)

    def add_item(self, number):
        self._addItem(number)

    def display_func(self):
        # display the last item
        widget = self.itemWidget(self.item(self.count() - 1))
        widget.setStyleSheet("border: 3px solid red;")

    def clear_func(self):
        widget = self.itemWidget(self.item(self.count() - 1))
        widget.setStyleSheet("")

    def outbox(self, pointer_value, flash_time):
        self._addItem(pointer_value)
        flash(self.display_func, self.clear_func, flash_time)
        QCoreApplication.processEvents()

    # the following three functions are used to disable selection
    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        self.setCurrentRow(-1)
        e.ignore()

