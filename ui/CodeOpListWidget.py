from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout, QListWidget, \
    QListWidgetItem, QAbstractItemView, QInputDialog, QAction, QMessageBox
from PyQt5.QtCore import QSize, Qt, QCoreApplication
from PyQt5.QtGui import QFont, QDragMoveEvent
from MySignal import MySignal
import hrmengine.parser
from util.MyEnum import OpType


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
        self._operation.setStyleSheet("color: #485424")

    def set_layout(self):
        self._operation.setAlignment(QtCore.Qt.AlignCenter)
        layout = QHBoxLayout()
        layout.addWidget(self._operation)
        self.setLayout(layout)

    def set_menu(self):
        self.setContextMenuPolicy(Qt.ActionsContextMenu)
        help = QAction("help", self)
        help.triggered.connect(self._help)
        self.addAction(help)

    def _help(self):
        help = {
            'INBOX': '取出inbox中的一个方块的内容，并将值传递到bus中',
            'OUTBOX': '将bus中的内容传递到outbox中，并将bus置为None',
            'COPYFROM': '接受一个目标X，将register中的第X个格子内容复制到bus中',
            'COPYTO': '接受一个目标X，将bus中的值复制到register中的第X个格子中',
            'ADD': '接受一个目标X，将bus中的内容和register中第X个格子的值相加，并用得到的结果覆盖bus',
            'SUB': '接受一个目标X，将bus中的内容减去register中第X个格子的值，并用得到的结果覆盖bus',
            'JUMP': '接受一个目标X，跳转到设置相同目标的LABEL操作的位置上',
            'LABEL': '设置一个目标X，用于引导JUMP操作的跳转位置',
            'JUMPN': '接受一个目标X，如果bus中内容为数字且为负数，执行此操作[该操作的执行参照JUMP]，否则跳过此操作',
            'JUMPZ': '接受一个目标X，如果bus中内容为数字且为0，执行此操作[该操作的执行参照JUMP]，否则跳过此操作',
            'BUMPUP': '接受一个目标X，该操作只能对于已存在内容的register的第X个格子使用，该操作会第X个格子的内容加1，然后将结果覆盖bus内容',
            'BUMPDN': '接受一个目标X，该操作只能对于已存在内容的register的第X个格子使用，该操作会第X个格子的内容减1，然后将结果覆盖bus内容'
        }
        msg = QMessageBox()
        msg.information(None, "help", help[self.get_operation()], QMessageBox.Ok, QMessageBox.Ok)

    def _set_color(self):
        op = self.get_operation()
        if op == 'INBOX' or op == 'OUTBOX':
            self.setStyleSheet("background-color: #A0B45C")
        elif op == 'COPYFROM' or op == 'COPYTO':
            self.setStyleSheet("background-color: #CC6C54")
        elif op == 'ADD' or op == 'SUB' or op == 'BUMPUP' or op == 'BUMPDN':
            self.setStyleSheet("background-color: #C88C64")
        else:
            self.setStyleSheet("background-color: #908CC4")

    def set_all(self, operation):
        """simple setup"""
        self.set_operation(operation)
        self.set_font()
        self.set_layout()
        self._set_color()
        # self.set_menu()


class OperationDropList(QListWidget):
    """operation box"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)

        self.signal = MySignal()
        # level default is 1
        self.level_num = 1
        # 设置颜色
        self.setStyleSheet("background-color: #886C54")

    def init_op(self):
        list_op = hrmengine.parser.parse_op_list(self.level_num)
        for op in list_op:
            self.add_item(op)

    def set_level_num(self, num):
        self.level_num = num

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
        # 记录待拖动指令所在位置now_row
        self.now_row = self.currentRow()
        self.setCurrentRow(-1)
        #  根据now_row指令的信息设置到signal中
        if self.now_row != -1:
            now_item = self.itemWidget(self.item(self.now_row))
            if now_item is not None:
                op = now_item.get_operation()
                self.signal.set_item(op)
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e: QtGui.QDropEvent) -> None:
        e.ignore()


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
        self._code_text.setStyleSheet("color: #485424")
        self._param = QLabel(param)
        self._param.setFont(QFont("Arial", 10, QFont.Bold))
        self._param.setStyleSheet("color: #485424")

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
            # code:param:blank=3:2:1
            ly_main.setStretchFactor(self._code_text, 3)
            ly_main.setStretchFactor(self._param, 2)
            ly_main.setStretchFactor(blank, 1)
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
            ly_main.setStretchFactor(self._code_text, 2)
            self._param = None
        ly_main.setSpacing(0)
        self.setLayout(ly_main)

        op = self._code_text.text()
        if op == 'INBOX' or op == 'OUTBOX':
            self.setStyleSheet("background-color: #A0B45C")
        elif op == 'COPYFROM' or op == 'COPYTO':
            self.setStyleSheet("background-color: #CC6C54")
        elif op == 'ADD' or op == 'SUB' or op == 'BUMPUP' or op == 'BUMPDN':
            self.setStyleSheet("background-color: #C88C64")
        else:
            self.setStyleSheet("background-color: #908CC4")

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

        self.setStyleSheet("background-color: #886C54")

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
        ok = QMessageBox().question(None, "Question", "remove selected?", QMessageBox.Yes | QMessageBox.No,
                                    QMessageBox.Yes)
        if ok == QMessageBox.Yes:
            self.takeItem(self.currentRow())

    def _clear_all(self):
        ok = QMessageBox().question(None, "Question", "remove all?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if ok == QMessageBox.Yes:
            for row in range(self.count() - 1, -1, -1):
                self.takeItem(row)

    def _addItem(self, *command):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 65))

        code = CodeWidget()
        code.set_all(*command)
        self.addItem(item_widget)
        self.setItemWidget(item_widget, code)

    def _insertItem(self, pos, *command):
        item_widget = QListWidgetItem()
        item_widget.setSizeHint(QSize(0, 65))

        code = CodeWidget()
        code.set_all(*command)
        self.insertItem(pos, item_widget)
        self.setItemWidget(item_widget, code)

    def dragEnterEvent(self, e: QtGui.QDragEnterEvent) -> None:
        if self.forbidden_drag_flag is False:
            # 记录当前进入code box的位置now_row
            self.now_row = self.row(self.itemAt(e.pos()))
            if self.now_row == -1:
                self.now_row = 0 if self.count() == 0 else self.count()
            # 通过signal设置的信号接收指令信息
            op = self.slot.get_item()
            if op is not None:
                # drag a operation into a code box
                self.insert_item(self.now_row, *[op, None])
                # update old_item
                self.last_row = self.now_row
                self.old_item = self.itemWidget(self.item(self.now_row))
                # update currentRow
                self.setCurrentRow(self.now_row)

            # if you drag, record last_row postion
            if self.last_row != self.currentRow() and self.currentRow() != -1:
                self.last_row = self.currentRow()
                self.old_item = self.itemWidget(self.item(self.last_row))

            e.accept()
        else:
            e.ignore()

    def dragMoveEvent(self, e: QDragMoveEvent):
        if self.forbidden_drag_flag is False:
            if self.now_row != self.last_row:
                if self.old_item == None:
                    e.ignore()
                    return
                # exchange position
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
