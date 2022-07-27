from PyQt5.QtCore import QCoreApplication, QTime
import xml.etree.ElementTree


def read_file(filepath):
    # read file:
    with open(filepath) as f:
        lines = f.readlines()
    # trim
    lines = list(map(lambda x: x.strip(), lines))
    # filter empty
    file_list = list(filter(lambda x: len(x) > 0, lines))
    # get number
    ret_list = []
    for i in file_list:
        if is_number(i):
            ret_list.append(int(i))
        else:
            ret_list.append(i)
    return ret_list


def flash(display_func, clear_func, flash_time, flash_cnt=4):
    """
    animation flash
    :param display_func:
    :param clear_func:
    :param flash_time:
    :param flash_cnt:
    """
    timer = QTime()
    timer.start()
    flash_num = 1
    flag = True
    while timer.elapsed() < flash_time:
        if timer.elapsed() > flash_time * flash_num / flash_cnt:
            if flag is True:
                display_func()
                flag = False
            else:
                clear_func()
                flag = True
            flash_num += 1
        # remain event loop
        QCoreApplication.processEvents()
    clear_func()


def is_number(number):
    try:
        float(number)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(number)
        return True
    except (TypeError, ValueError):
        pass
    return False


def is_int(number):
    result = False
    try:
        n = float(number)
        if n.is_integer() and str(number).count('.') == 0:
            result = True
    except:
        pass

    return result


class ParserException(Exception):
    """
    exception handle
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def get_level_data(file_path):
    """get input information for this level"""
    level = xml.etree.ElementTree.parse(file_path).getroot()
    # get inbox data
    inbox_data = []
    for inbox in level.findall("inbox"):
        for data in inbox:
            if is_int(data.text):
                inbox_data.append(int(data.text))
            else:
                raise ParserException("inbox data could only be integer.")

    # get register group data
    register_data = []
    for register in level.findall("register"):
        for data in register:
            if data[0] is None:
                register_data = None
                break
            if is_int(data[0].text):
                id = int(data[0].text)
            else:
                raise ParserException("inbox data could only be integer.")
            if is_int(data[1].text):
                value = int(data[1].text)
            else:
                raise ParserException("inbox data could only be integer.")
            register_data.append([id, value])

    # get level description
    desc_data = ""
    for desc in level.findall("desc"):
        desc_data += desc.text
    return inbox_data, register_data, desc_data
