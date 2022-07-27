import warnings
from deprecated.sphinx import deprecated
from PyQt5.QtCore import QObject, pyqtSignal

warnings.filterwarnings("always")
SET = "SET"
DELETE = "DELETE"
OPEN = "OPEN"
CLOSE = "CLOSE"


@deprecated(version='1.0', reason="This class will be removed soon")
class MySignal(QObject):
    send_msg = pyqtSignal(str, object)

    def __init__(self):
        super(MySignal, self).__init__()
        self.state = OPEN

    def set_item(self, item):
        self.item = item

    def send(self):
        # emit
        if self.state == OPEN:
            self.send_msg.emit(SET, self.item)
            self.state = CLOSE

    def close(self):
        self.send_msg.emit(DELETE, None)
        self.state = OPEN


class MySlot(QObject):
    @deprecated(version='1.0', reason="This class will be removed soon")
    def __init__(self):
        super(MySlot, self).__init__()
        self.item = None

    def recv(self, state, item):
        if state == SET:
            self.item = item
        else:
            self.item = None

    def get_item(self):
        ret = self.item
        self.item = None
        return ret


if __name__ == "__main__":
    item = 5
    signal = MySignal()
    signal.set_item(item)
    slot = MySlot()
    signal.send_msg.connect(slot.recv)

    signal.send()
    signal.close()
    print(slot.get_item())
