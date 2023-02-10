import numpy as np


def gen_data_level(level_num, inbox_data, register_data):
    """
    generate new inbox_data and outbox from inbox_data
    """
    num = 0
    for data in inbox_data:
        num *= 10
        num += abs(data)

    # generate random integer
    bg = np.random.SFC64(num)
    rng = np.random.Generator(bg)

    for index, _ in enumerate(inbox_data):
        inbox_data[index] = rng.integers(-9, 10)

    outbox_data = []
    # generate outbox data
    if level_num == 1:
        outbox_data = gen_outbox_data_1(inbox_data)
    elif level_num == 2:
        outbox_data = gen_outbox_data_2(inbox_data)
    elif level_num == 3:
        outbox_data = gen_outbox_data_3(inbox_data)
    elif level_num == 4:
        outbox_data = gen_outbox_data_4(inbox_data)
    elif level_num == 5:
        # inbox中需要比较多的0
        for i, data in enumerate(inbox_data):
            if -4 <= data <= 4:
                inbox_data[i] = 0
        outbox_data = gen_outbox_data_5(inbox_data)
    elif level_num == 6:
        outbox_data = gen_outbox_data_6(inbox_data)
    elif level_num == 7:
        outbox_data = gen_outbox_data_7(inbox_data)
    elif level_num == 8:
        outbox_data = gen_outbox_data_8(inbox_data)
    elif level_num == 9:
        # 固定输入
        inbox_data = [-3, 0, 3]
        outbox_data = gen_outbox_data_9(inbox_data)
    elif level_num == 10:
        # 固定输入
        inbox_data = [5, 2, 4, 7, 6, 3, 9, 8]
        outbox_data = gen_outbox_data_10(inbox_data, register_data)
    elif level_num == 11:
        inbox_data = [34 + inbox_data[0] % 20]
        outbox_data = gen_outbox_data_11(inbox_data)
    elif level_num == 12:
        # 输入限制在0~5之间
        i = 0
        while i < len(inbox_data):
            inbox_data[i] = inbox_data[i] % 9 + 1
            inbox_data[i + 1] = inbox_data[i + 1] % 3 + 1
            i += 2
        outbox_data = gen_outbox_data_12(inbox_data)
    elif level_num == 13:
        # 输入限制在0~5之间
        for index, data in enumerate(inbox_data):
            inbox_data[index] = data % 6
        outbox_data = gen_outbox_data_13(inbox_data)

    return inbox_data, outbox_data


def gen_outbox_data_1(inbox_data):
    outbox_data = []
    for data in inbox_data:
        outbox_data.append(data)
    return outbox_data


def gen_outbox_data_2(inbox_data):
    outbox_data = []
    for data in inbox_data:
        outbox_data.append(data)
    return outbox_data


def gen_outbox_data_3(inbox_data):
    return ["B", "U", "G"]


def gen_outbox_data_4(inbox_data):
    i = 0
    outbox = []
    while i < len(inbox_data):
        outbox.append(inbox_data[i + 1])
        outbox.append(inbox_data[i])
        i += 2
    return outbox


def gen_outbox_data_5(inbox_data):
    outbox = []
    for data in inbox_data:
        if data == 0:
            outbox.append(data)
    return outbox


def gen_outbox_data_6(inbox_data):
    i = 0
    outbox = []
    while i < len(inbox_data):
        outbox.append(inbox_data[i] + inbox_data[i + 1])
        i += 2
    return outbox


def gen_outbox_data_7(inbox_data):
    i = 0
    outbox = []
    while i < len(inbox_data):
        if inbox_data[i] == inbox_data[i + 1]:
            outbox.append(inbox_data[i])
        i += 2
    return outbox


def gen_outbox_data_8(inbox_data):
    i = 0
    outbox = []
    while i < len(inbox_data):
        outbox.append(inbox_data[i] if inbox_data[i] > inbox_data[i + 1] else inbox_data[i + 1])
        i += 2
    return outbox


def gen_outbox_data_9(inbox_data):
    return [-3, -2, -1, 0, 0, 3, 2, 1, 0]


def gen_outbox_data_10(inbox_data, register_data):
    outbox = []
    for data in inbox_data:
        for index, value in register_data:
            if index == data:
                outbox.append(value)
    return outbox


def gen_outbox_data_11(inbox_data):
    outbox = []
    for data in inbox_data:
        a, b = 1, 2
        while a <= data:
            outbox.append(a)
            b, a = a + b, b
    return outbox


def gen_outbox_data_12(inbox_data):
    i = 0
    outbox = []
    while i < len(inbox_data):
        outbox.append(inbox_data[i + 1] // inbox_data[i])
        i += 2
    return outbox


def gen_outbox_data_13(inbox_data):
    outbox = []
    mem = [-1, -1, -1, -1, -1, -1]
    for index, data in enumerate(inbox_data):
        if mem[data] == -1:
            outbox.append(data)
            mem[data] = 0
    return outbox