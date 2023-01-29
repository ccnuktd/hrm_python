# 1. 以level_1的inbox 8位数为种子生成新的8位inbox
#   A. 取出level_1的inbox 8位数
#   B. 算法8位数生成新的8位数
# 2. 通过算法描述，通过inbox生成outbox
# 3. 将新的inbox和outbox写入xml文件
import xml.etree.ElementTree
from util.MyUtil import is_int, ParserException
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


def update_level_data(file_path):
    """update new level data [xml] from former level data"""
    tree = xml.etree.ElementTree.parse(file_path)
    level = tree.getroot()
    # get inbox data
    inbox_data = []
    for inbox in level.findall("inbox"):
        for data in inbox:
            if is_int(data.text):
                inbox_data.append(int(data.text))
            else:
                raise ParserException("inbox data could only be integer.")

    inbox_data, outbox_data = gen_data_level_1(inbox_data)

    for data in level[0].findall("data"):
        level[0].remove(data)

    for data in level[3].findall("data"):
        level[3].remove(data)

    inbox_contain = level.find("inbox")
    for data in inbox_data:
        # add inbox data
        contain = xml.etree.ElementTree.SubElement(inbox_contain, 'data')
        contain.text = str(data)

    outbox_contain = level.find("outbox")

    for data in outbox_data:
        # add outbox data
        contain = xml.etree.ElementTree.SubElement(outbox_contain, 'data')
        contain.text = str(data)

    tree.write(file_path)


if __name__ == '__main__':
    update_level_data("level_1.xml")
