class MySignal(object):
    """set完成后只能get一次的信号量"""
    _item = None

    def get_item(self):
        ret = MySignal._item
        MySignal._item = None
        return ret

    def set_item(self, item):
        MySignal._item = item


if __name__ == "__main__":
    a = MySignal()
    b = MySignal()
    a.set_item(1)
    print(b.get_item())
    print(b.get_item())
    b.set_item(2)
    print(a.get_item())
    print(a.get_item())

