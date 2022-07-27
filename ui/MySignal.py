class MySignal(object):
    """semaphore: get_item could only get once after set_item"""
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
