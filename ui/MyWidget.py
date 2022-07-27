import enum

from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QListWidget, \
    QListWidgetItem, QAbstractItemView, QInputDialog, QAction, QMessageBox
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont, QDragMoveEvent
from MySignal import MySignal
import hrmengine.parser


class OperationWidget(QWidget):
    """inner operation item in operation box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._operation = None

    def get_operation(self):
        """get op text"""
        return self._operation.text()

    def set_operation(self, operation: str):
        self._operation = QLabel(operation)

    def set_font(self, font=QFont("Arial", 15, QFont.Bold)):
        self._operation.setFont(font)

    def set_layout(self):
        self._operation.setAlignment(QtCore.Qt.AlignCenter)
        layout = QHBoxLayout()
        layout.addWidget(self._operation)
        self.setLayout(layout)

    def set_all(self, operation):
        """simple setup"""
        self.set_operation(operation)
        self.set_font()
        self.set_layout()


class OperationDropList(QListWidget):
    """operation box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)

        self.signal = MySignal()
        self.init_op()

    def init_op(self):
        list_op = hrmengine.parser.parse_op_list()
        for op in list_op:
            self.add_item(op)

    def _addItem(self, operation):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 60))

        op = OperationWidget()
        op.set_all(operation)

        self.addItem(item_widget)
        self.setItemWidget(item_widget, op)

    def add_item(self, operation):
        self._addItem(operation)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        self.now_row = self.currentRow()
        self.setCurrentRow(-1)
        if self.now_row != -1:
            now_item = self.itemWidget(self.item(self.now_row))
            if now_item is not None:
                op = now_item.get_operation()
            else:
                op = self.item(self.now_row).text()
            self.signal.set_item(op)
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        e.ignore()


class OpType(enum.Enum):
    OP_WITHOUT_PARAM = 0
    OP_WITH_PARAM = 1
    LABEL = 2


class CodeWidget(QWidget):
    """inner item in code box"""

    def __init__(self):
        super(CodeWidget, self).__init__()
        self._code_text = None
        self._param = None
        self._op_type = None
        self.mouseDoubleClickEvent = self.mouseDoubleClickEvent
        self.setAcceptDrops(True)

    def set_all(self, code_text, param=None):
        self._set_command(code_text, param)
        self._set_operation_type()
        self._init_layout()

    def get_code_text(self):
        if self._code_text is not None:
            return self._code_text.text()

    def get_param(self):
        if self._param is not None:
            return self._param.text()

    def get_command(self):
        param = self.get_param()
        if param is None:
            return [self.get_code_text()]
        else:
            return [self.get_code_text(), param]

    def _set_command(self, code_text, param):
        self._code_text = QLabel(code_text)
        self._code_text.setFont(QFont("Arial", 10, QFont.Bold))
        self._param = QLabel(param)
        self._param.setFont(QFont("Arial", 10, QFont.Bold))

    def _set_operation_type(self):
        if self._code_text.text() == "LABEL" or hrmengine.parser.is_label(self._code_text.text()):
            # case: label
            self._op_type = OpType.LABEL
        elif hrmengine.parser.needs_param(self._code_text.text()):
            # case: operation with param
            self._op_type = OpType.OP_WITH_PARAM
        else:
            # case: operation without param
            self._op_type = OpType.OP_WITHOUT_PARAM

    def _init_layout(self):
        """handle layout"""
        ly_main = QHBoxLayout()
        if self._op_type == OpType.OP_WITH_PARAM:
            # case: operation with param
            blank = QLabel()
            ly_main.addWidget(blank)
            ly_main.addWidget(self._code_text)
            ly_main.addWidget(self._param)
            # blank:code:param=1:3:1
            ly_main.setStretchFactor(blank, 1)
            ly_main.setStretchFactor(self._code_text, 3)
            ly_main.setStretchFactor(self._param, 1)
        elif self._op_type == OpType.LABEL:
            # case: label
            ly_main.addWidget(self._code_text)
            self._param = None
        else:
            # case: operation without param
            blank = QLabel()
            ly_main.addWidget(blank)
            ly_main.addWidget(self._code_text)
            # blank:code=1:4
            ly_main.setStretchFactor(blank, 1)
            ly_main.setStretchFactor(self._code_text, 4)
            self._param = None

        self.setLayout(ly_main)

    def mouseDoubleClickEvent(self, event):
        """set label and param or modify them"""
        if self._op_type == OpType.OP_WITH_PARAM:
            text, ok = QInputDialog().getText(QWidget(), 'set param', 'please input param:')
            if ok and text:
                self._param.setText(text)
        elif self._op_type == OpType.LABEL:
            text, ok = QInputDialog().getText(QWidget(), 'set label', 'please input label:')
            if ok:
                # add ':' in the end
                if text.endswith(':'):
                    self._code_text.setText(text)
                else:
                    self._code_text.setText(text + ':')
        else:
            event.ignore()


class CodeDropList(QListWidget):
    """code box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._set_menu()
        self.slot = MySignal()

        # set drag enable
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)

        self.forbidden_drag_flag = False
        self.last_row = None

    def set_forbidden_drag(self):
        """enable drag"""
        self.forbidden_drag_flag = True

    def reset_drag(self):
        """disable drag"""
        self.forbidden_drag_flag = False

    def get_code_list(self):
        """get all the commands in list and return command list"""
        code_list = []
        for i in range(self.count()):
            item = self.itemWidget(self.item(i))
            command = item.get_command()
            code_list.append(command)

        return code_list

    def init_current_row(self):
        self.setCurrentRow(-1)

    def insert_item(self, position, *command):
        self._insertItem(position, *command)

    def add_item(self, *command):
        self._addItem(*command)

    def _set_menu(self):
        # enable menu
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        delete_one = QAction("remove selected", self)
        delete_one.triggered.connect(self._delete)
        delete_all = QAction("remove all", self)
        delete_all.triggered.connect(self._clear_all)
        self.addAction(delete_one)
        self.addAction(delete_all)

    def _delete(self):
        ok = QMessageBox().question(self, "Question", "remove selected?", QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes)
        if ok:
            self.takeItem(self.currentRow())

    def _clear_all(self):
        ok = QMessageBox().question(self, "Question", "remove all?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if ok:
            for row in range(self.count() - 1, -1, -1):
                self.takeItem(row)

    def _addItem(self, *command):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 40))

        code = CodeWidget()
        code.set_all(*command)
        self.addItem(item_widget)
        self.setItemWidget(item_widget, code)

    def _insertItem(self, pos, *command):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 40))

        code = CodeWidget()
        code.set_all(*command)
        self.insertItem(pos, item_widget)
        self.setItemWidget(item_widget, code)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if self.forbidden_drag_flag is False:
            self.now_row = self.row(self.itemAt(e.pos()))

            op = self.slot.get_item()
            if op is not None:
                # drag a operation into a code box
                self.now_row = self.count()
                self.add_item(*[op, None])
                # update old_item
                self.old_item = self.itemWidget(self.item(self.now_row))
                # update currentRow
                self.setCurrentRow(self.now_row)

            # if you drag, recode last_row postion
            if self.last_row != self.currentRow():
                self.last_row = self.currentRow()
                self.old_item = self.itemWidget(self.item(self.last_row))

            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QDragMoveEvent):
        if self.forbidden_drag_flag is False:
            if self.now_row != -1 and self.currentRow() != -1:
                # exchange block position
                # delete last_row item
                self.takeItem(self.last_row)

                # insert new_item
                command = self.old_item.get_command()
                self.insert_item(self.now_row, *command)

                # update last_row and old_item
                self.old_item = self.itemWidget(self.item(self.now_row))
                self.last_row = self.now_row
                if self.currentRow() != self.last_row:
                    self.setCurrentRow(self.last_row)
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        e.ignore()
