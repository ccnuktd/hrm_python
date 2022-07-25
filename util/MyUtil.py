from PyQt5.QtCore import QCoreApplication, QTime


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
    设置执行的动画效果
    :param display_func:无参数的显示函数
    :param clear_func:无参数的消除显示函数
    :param flash_time:显示时间
    :param flash_cnt:闪烁次数
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
        # 保持事件循环的继续运行
        QCoreApplication.processEvents()
    clear_func()


def is_number(s):
    try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
        float(s)
        return True
    except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
        pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
    try:
        import unicodedata  # 处理ASCii码的包
        unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
        return True
    except (TypeError, ValueError):
        pass
    return False
