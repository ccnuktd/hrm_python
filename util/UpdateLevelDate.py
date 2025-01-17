import xml.etree.ElementTree
from util.GenerateLevelData import gen_data_level
from util.MyUtil import is_int, ParserException, get_level_path


def update_level_data(level_num, register_data):
    """update new level data [xml] from former level data"""
    """
    # 1. 以level_1的inbox 8位数为种子生成新的8位inbox
    #   A. 取出level_1的inbox 8位数
    #   B. 算法8位数生成新的8位数
    # 2. 通过算法描述，通过inbox生成outbox
    # 3. 将新的inbox和outbox写入xml文件
    """
    file_path = get_level_path(level_num)
    parser = xml.etree.ElementTree.XMLParser(encoding='utf-8')
    tree = xml.etree.ElementTree.parse(file_path, parser=parser)
    level = tree.getroot()
    # get inbox data
    inbox_data = []
    for inbox in level.findall("inbox"):
        for data in inbox:
            if is_int(data.text):
                inbox_data.append(int(data.text))
            else:
                raise ParserException("inbox data could only be integer.")

    inbox_data, outbox_data = gen_data_level(level_num, inbox_data, register_data)

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

    tree.write(file_path, encoding="utf8")

