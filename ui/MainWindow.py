import operator

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from hrmengine import parser

from hrm_ui import Ui_MainWindow
from PyQt5 import QtCore
from PyQt5.QtCore import QCoreApplication
import sys

from hrmengine import cpu
from hrmengine.cpu import ExecutionExceptin
from hrmengine.parser import parse_address
from resources.level.update_level_1 import update_level_data
from util.MyUtil import get_level_data
from util.MyEnum import State


# Form implementation generated from reading ui file 'MainWindow.py'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, level_path="../resources/level/level_1.xml"):
        super().__init__()
        self.setupUi(self)
        # load level info
        self.load_level_info(level_path)
        # Button event triggering
        self.u_start_btn.clicked['bool'].connect(self.start_event)
        self.u_next_btn.clicked['bool'].connect(self.next_event)
        self.u_pause_btn.clicked['bool'].connect(self.stop_event)
        self.u_goon_btn.clicked['bool'].connect(self.goon_evnet)
        self.u_exit_btn.clicked['bool'].connect(self.exit_event)
        # set slider bar
        self.u_speed_slider.valueChanged.connect(self.change_speed)
        self.origin_flash_time = 10000
        self.flash_time = self.origin_flash_time // self.u_speed_slider.value()

        self.pre_process()
        self.last_item = None
        self.state = None
        self.process_state = State.INIT

    def change_speed(self):
        self.flash_time = self.origin_flash_time // self.u_speed_slider.value()

    def start_event(self):
        self.process_state = State.INIT
        self.u_code_droplist.set_forbidden_drag()
        self.process()

    def next_event(self):
        self.process_state = State.NEXT

    def stop_event(self):
        self.process_state = State.STOP

    def goon_evnet(self):
        self.process_state = State.GOON

    def exit_event(self):
        self.process_state = State.EXIT

    def track_code(self, row):
        if self.last_item is not None:
            self.last_item.setBackground(QColor("white"))
        this_item = self.u_code_droplist.item(row)
        this_item.setBackground(QColor("red"))
        self.last_item = this_item

    def untrack_code(self):
        self.last_item.setBackground(QColor("white"))

    def input_flash(self, next_state):
        self.u_input_list.inbox(self.flash_time)
        self.u_pointer.set_value(next_state.pointer, self.flash_time)

    def output_flash(self, next_state):
        self.u_pointer.display_outbox(self.flash_time)
        self.u_output_list.outbox(next_state.outbox[-1], self.flash_time)

    def copyto_flash(self, state, address):
        id = parse_address(state, address)
        self.u_pointer.display_value(self.flash_time)
        self.u_register_group.display_set_value(id, state.pointer, self.flash_time)

    def copyfrom_flash(self, state, address):
        id = parse_address(state, address)
        val = self.u_register_group.display_get_value(id, self.flash_time)
        self.u_pointer.set_value(val, self.flash_time)

    def add_flash(self, state, address):
        id = parse_address(state, address)
        self.u_pointer.display_value(self.flash_time)
        val = self.u_register_group.display_get_value(id, self.flash_time)
        new_val = state.pointer + val
        self.u_pointer.set_value(new_val, self.flash_time)

    def sub_flash(self, state, address):
        id = parse_address(state, address)
        self.u_pointer.display_value(self.flash_time)
        val = self.u_register_group.display_get_value(id, self.flash_time)
        new_val = state.pointer - val
        self.u_pointer.set_value(new_val, self.flash_time)

    def bumpup_flash(self, state, address):
        id = parse_address(state, address)
        val = self.u_register_group.display_get_value(id, self.flash_time)
        new_val = val + 1
        self.u_register_group.display_set_value(id, new_val, self.flash_time)
        self.u_pointer.set_value(new_val, self.flash_time)

    def bumpdn_flash(self, state, address):
        id = parse_address(state, address)
        val = self.u_register_group.display_get_value(id, self.flash_time)
        new_val = val - 1
        self.u_register_group.display_set_value(id, new_val, self.flash_time)
        self.u_pointer.set_value(new_val, self.flash_time)

    def label_flash(self):
        pass

    def jump_flash(self):
        pass

    def pre_process(self):
        # init inbox and outbox
        self.u_input_list.init_inbox(self.inbox)
        self.u_output_list.init_outbox()
        # clear code box
        self.u_code_droplist.init_current_row()
        # init register group
        self.u_register_group.init_ui(2, 5, 60)
        if self.register_data is not None:
            for data in self.register_data:
                self.u_register_group.set_value(data)

    def load_level_info(self, file_path):
        update_level_data(file_path)
        self.inbox, self.register_data, desc, self.outbox = get_level_data(file_path)
        self.u_desc.setText(desc)

    def reset_pointer(self):
        self.u_pointer.reset()

    def check_pass(self):
        if operator.eq(self.state.outbox, self.outbox):
            QMessageBox().information(self, "congratulations", "you pass this level")
        else:
            QMessageBox().information(self, "sorry", "please try again")

    def process(self):
        while True:
            if self.process_state == State.INIT:
                self.pre_process()
                ops = self.u_code_droplist.get_code_list()
                error_msgs = parser.compiling(ops)
                if error_msgs is not '':
                    QMessageBox().warning(self, "compiling error", error_msgs)
                    # reset drag mode
                    self.u_code_droplist.reset_drag()
                    self.reset_pointer()
                    return
                self.state = cpu.create_state(iter(self.inbox), ops, self.register_data)
                self.process_state = State.GOON
            elif self.process_state == State.GOON:
                try:
                    if self.state.pc != -1:
                        # CPU state
                        self.state = cpu.tick(self.state)
                        # show UI state
                        self.ui_show(self.state.prev_state, self.state)
                    else:
                        self.check_pass()
                        break
                except ExecutionExceptin as e:
                    if e.__str__() == "'INBOX has no more items'":
                        # if inbox is empty, check if pass this level
                        self.check_pass()
                    else:
                        QMessageBox().warning(self, "runtime error", e.__str__())
                    break
            elif self.process_state == State.STOP:
                QCoreApplication.processEvents()
            elif self.process_state == State.NEXT:
                try:
                    if self.state.pc != -1:
                        # CPU state
                        self.state = cpu.tick(self.state)
                        # show UI state
                        self.ui_show(self.state.prev_state, self.state)
                        self.process_state = State.STOP
                    else:
                        break
                except ExecutionExceptin as e:
                    QMessageBox().warning(self, "runtime error", e.__str__())
                    break
            elif self.process_state == State.EXIT:
                break
        self.pre_process()
        if self.last_item is not None:
            self.untrack_code()
        self.u_code_droplist.reset_drag()
        self.reset_pointer()

    def ui_show(self, state, next_state):
        if state.pc >= len(state.code) or state.pc < 0:
            return
        command = state.code[state.pc]
        op = command[0]
        param = None
        if len(command) > 1:
            param = command[1]

        self.track_code(state.pc)

        if op == 'INBOX':
            self.input_flash(next_state)
        elif op == 'OUTBOX':
            self.output_flash(next_state)
        elif op == 'COPYTO':
            self.copyto_flash(state, param)
        elif op == 'COPYFROM':
            self.copyfrom_flash(state, param)
        elif op == 'ADD':
            self.add_flash(state, param)
        elif op == 'SUB':
            self.sub_flash(state, param)
        elif op == 'BUMPUP':
            self.bumpup_flash(state, param)
        elif op == 'BUMPDN':
            self.bumpdn_flash(state, param)
        elif parser.is_label(op):
            self.label_flash()
        elif op == 'JUMP':
            self.jump_flash()
        elif op == 'JUMPN':
            self.jump_flash()
        elif op == 'JUMPZ':
            self.jump_flash()


if __name__ == '__main__':
    # make the program support high-resolution display
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
