import numpy as np


def gen_data_level_1(inbox_data):
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
    for data in inbox_data:
        outbox_data.append(40 * data)

    return inbox_data, outbox_data
