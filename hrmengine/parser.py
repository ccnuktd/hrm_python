import hrmengine.cpu as cpu
import logging as log


def _to_op(string):
    """
    parse the input code as ['operator', {'operand'}]
    it is possible for no-operands operator like
    'INBOX' or 'OUTBOX'
    specific operators are in cpu.py [knownOps]
    """
    string = string.split(' ')
    return list(filter(lambda l: l != '', string))


def is_known_op(opcode):
    """
    Checks if the given op is in knownOps or ends with ':'
    if the op ends with ':', it means it's a label

    :param opcode: Operation without arguments like 'INBOX'
    :return: True or False
    """
    return opcode in cpu.knownOps or opcode.endswith(':')


def needs_param(opcode):
    """
    Check whether a known op need parameter
    """
    return opcode not in ['INBOX', 'OUTBOX'] and not opcode.endswith(":")


def is_label(opcode):
    """
    Check whether a label
    """
    return opcode.endswith(":")


def is_valid_op(op):
    """
    Checks the given op if it is valid

    :param op: [opcode, param]
    :return: True if given op is valid
    """
    if len(op) == 0 or not is_known_op(op[0]):
        return False

    if needs_param(op[0]) and (len(op) == 2 and op[1]):
        return True
    elif not needs_param(op[0]) and len(op) == 1:
        return True
    else:
        return False


def is_jump_op(opcode):
    if opcode == 'JUMP' or opcode == 'JUMPN' or opcode == 'JUMPZ':
        return True
    return False


def _read_file(filepath):
    # read file:
    with open(filepath) as f:
        lines = f.readlines()
    # trim
    lines = list(map(lambda x: x.strip(), lines))
    # filter empty
    return list(filter(lambda x: len(x) > 0, lines))


def _read_string(clipboard_string):
    # split lines (detecting linebreaks from hrm format)
    line_break = "\n"
    if "\r\n" in clipboard_string:
        line_break = "\r\n"
    lines = clipboard_string.split(line_break)
    # trim
    lines = list(map(lambda x: x.strip(), lines))
    # filter empty
    return list(filter(lambda x: len(x) > 0, lines))


def _convert_to_ops(lines):
    # split command and parameter
    ops = list(map(_to_op, lines))
    # filter unknown ops
    return list(filter(lambda op: is_known_op(op[0]), ops))


def _get_op(lines):
    ops = list(map(_to_op, lines))
    return list(ops)


def compiling(code):
    """
    returns the compile error string, which is empty if compiling succeeded
    """
    label = {}
    line = 0
    error_msgs = ""

    # check command validity
    for command in code:
        line += 1
        if is_valid_op(command):
            if cpu.isLabel(command[0]):
                label_text = command[0][:-1]
                label[label_text] = 0
        else:
            # invalid command
            error_msg = "line " + str(line) + ": lack of param\n"
            error_msgs += error_msg

    # check label
    line = 0
    for command in code:
        line += 1
        if is_valid_op(command) and is_jump_op(command[0]):
            # jump command
            label_text = command[1]
            if label_text in label.keys():
                label[label_text] += 1
            else:
                # label isn't existed
                error_msg = "line " + str(line) + "：label " + str(label_text) + "is not existed\n"
                error_msgs += error_msg

    return error_msgs


def parse_file(filepath):
    """
    Parses a file and convert it to a list of ops like
    [['BUMPUP','[1]']]

    :return: list of operations ['opcode', {'arg'}]
    """
    lines = _read_file(filepath)
    return _convert_to_ops(lines)


def parse_op_list(level_num):
    """
    Parse "../resources/op_{num}.txt" and convert to a list of operation
    ['ADD', 'SUB']

    :return: list of operations
    """
    file_path = "resources/level/op_" + str(level_num) + ".txt"
    return _read_file(file_path)


def parse_clipboard_string(clipboard_string):
    """
    Parses the string (normally from clipboard) and convert it to a list of ops like
    [['BUMPUP','[1]']]

    :return: list of operations ['opcode', {'arg'}]
    """
    lines = _read_string(clipboard_string)
    return _convert_to_ops(lines)


def parse_address(state, address):
    if address.startswith('['):
        return int(state.regs[int(address[1:-1])])
    else:
        return int(address)


def main(filepath):
    ops = parse_file(filepath)
    inbox = iter([1, 5])
    state = cpu.create_state(inbox, ops)

    next_state = cpu.tick(state)
    while next_state.pc != -1:
        next_state = cpu.tick(next_state)

    print("OUTBOX:", next_state.outbox)


if __name__ == "__main__":
    log.basicConfig(level=log.DEBUG)
    main("../resources/demo.txt")
    # main("../resources/dummy.txt")
    # main("../resources/justPrint.txt")
