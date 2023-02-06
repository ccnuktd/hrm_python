import numpy as np


def gen_data_level(level_num, inbox_data):
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
    # elif level_num == 4:
    #     gen_outbox_data_4(inbox_data)
    # elif level_num == 5:
    #     gen_outbox_data_5(inbox_data)
    # elif level_num == 6:
    #     gen_outbox_data_6(inbox_data)
    # elif level_num == 7:
    #     gen_outbox_data_7(inbox_data)
    # elif level_num == 8:
    #     gen_outbox_data_8(inbox_data)
    # elif level_num == 9:
    #     gen_outbox_data_9(inbox_data)
    # elif level_num == 10:
    #     gen_outbox_data_10(inbox_data)
    # elif level_num == 11:
    #     gen_outbox_data_10(inbox_data)
    # elif level_num == 12:
    #     gen_outbox_data_11(inbox_data)
    # elif level_num == 13:
    #     gen_outbox_data_12(inbox_data)

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
