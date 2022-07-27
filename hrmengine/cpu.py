import logging as log
from copy import deepcopy
from util import MyUtil
import sys


class State:
    """
    Representate a state for the cpu to process
    inbox: iterable array, used to process
    code: input programming language
    regs: registers in CPU, total 10
    pointer: bus data
    outbox: iterable array, used to output
    pc: program counter
    prev_state: recode the previous state
    """

    def __init__(self, inbox, code):
        self.inbox = inbox
        self.code = code
        self.regs = [None] * 10
        self.pointer = None
        self.outbox = []
        self.pc = 0
        self.prev_state = None


class ExecutionExceptin(Exception):
    """
    exception handle
    """

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def getRegIndexToRef(ref, regs):
    """
    Memory addressing:
    X: Direct Addressing
    [X]: Indirect Addressing
    return: an int address
    """
    if ref.startswith('['):
        return int(regs[int(ref[1:-1])])
    elif MyUtil.is_int(ref):
        return int(ref)
    else:
        raise ExecutionExceptin(str(ref) + " is not an address")


def setReg(state, rules):
    """
    load register group state
    """
    if rules is not None:
        for rule in rules:
            state.regs[rule[0]] = rule[1]


def exeInbox(state, params):
    """
    put the head of input box to pointer
    """
    try:
        state.pointer = next(state.inbox)
    except StopIteration:
        raise ExecutionExceptin("INBOX has no more items")


def exeOutbox(state, params):
    """
    put the pointer value to the tail of output box
    """
    if state.pointer is None:
        raise ExecutionExceptin("OUTBOX without pointer")
    state.outbox.append(state.pointer)
    state.pointer = None


def exeCopyfrom(state, params):
    """
    put pointer value to register
    """
    index = getRegIndexToRef(params[0], state.regs)
    state.pointer = state.regs[index]


def exeCopyto(state, params):
    """
    load register value to pointer
    """
    index = getRegIndexToRef(params[0], state.regs)
    if state.pointer is not None:
        state.regs[index] = state.pointer
    else:
        raise ExecutionExceptin("'None' can't copy to an register")


def exeAdd(state, params):
    """
    add Pointer value and Register value, copy it to Pointer
    only support number
    """
    if state.pointer is None:
        raise ExecutionExceptin("ADD without pointer")
    index = getRegIndexToRef(params[0], state.regs)

    if isinstance(state.pointer, str) or isinstance(state.regs[index], str):
        raise ExecutionExceptin("Not able to handle unequal types")
    state.pointer = state.pointer + state.regs[index]


def exeSub(state, params):
    """
    subtract Pointer value to Register value and copy it to Pointer
    support number sub number and alphabet sub alphabet
    """
    if state.pointer is None:
        raise ExecutionExceptin("Sub without pointer")

    index = getRegIndexToRef(params[0], state.regs)

    if isinstance(state.pointer, str) and isinstance(state.regs[index], str):
        base = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        pointer_val = base.find(state.pointer.upper())
        reg_val = base.find(state.regs[index].upper())
        state.pointer = pointer_val - reg_val

    elif isinstance(state.pointer, str) or isinstance(state.regs[index], str):
        raise ExecutionExceptin("Not able to handle unequal types")
    else:
        state.pointer = state.pointer - state.regs[index]


def exeBumpup(state, params):
    """
    let register number add one and put value to pointer
    only support number
    """
    index = getRegIndexToRef(params[0], state.regs)

    if state.regs[index] is None:
        raise ExecutionExceptin("Reg doesn't contain a value")
    elif isinstance(state.regs[index], str):
        raise ExecutionExceptin("Not able to bump str type")

    state.regs[index] += 1
    state.pointer = state.regs[index]


def exeBumpdn(state, params):
    """
    let register number subtract one and put value to pointer
    only support number
    """
    index = getRegIndexToRef(params[0], state.regs)

    if state.regs[index] is None:
        raise ExecutionExceptin("Reg doesn't contain a value")
    elif isinstance(state.regs[index], str):
        raise ExecutionExceptin("Not able to bump str type")

    state.regs[index] -= 1
    state.pointer = state.regs[index]


def exeJump(state, params):
    label = params[0] + ':'
    code_list = list(map(lambda x: x[0], state.code))

    if label not in code_list:
        raise ExecutionExceptin("Label for target not found")
    return code_list.index(label)


def exeJumpz(state, params):
    if state.pointer == 0:
        return list(map(lambda x: x[0], state.code)).index(params[0] + ':')


def exeJumpn(state, params):
    if state.pointer < 0:
        return list(map(lambda x: x[0], state.code)).index(params[0] + ':')


def isLabel(str):
    return str.endswith(':')


exes = {
    'INBOX': exeInbox,
    'OUTBOX': exeOutbox,
    'COPYFROM': exeCopyfrom,
    'COPYTO': exeCopyto,
    'ADD': exeAdd,
    'SUB': exeSub,
    'BUMPUP': exeBumpup,
    'BUMPDN': exeBumpdn,
    'JUMP': exeJump,
    'JUMPZ': exeJumpz,
    'JUMPN': exeJumpn
}
knownOps = exes.keys()


def create_state(inbox, code, rules=None):
    cpu = State(inbox, code)
    setReg(cpu, rules)
    return cpu


def tick(given_state):
    state = deepcopy(given_state)
    state.prev_state = given_state

    if state.pc >= len(state.code) or state.pc < 0:
        state.pc = -1
        return state
    else:
        log.debug('')
        log.debug("### PC:{}".format(state.pc))

        command = state.code[state.pc]
        op = command[0]

        if isLabel(op):
            log.debug("Skip {}".format(op))
            pass
        else:
            params = []
            if len(command) > 1:
                params = command[1:]

            if op not in exes:
                raise ExecutionExceptin("Unknown command " + op)

            if params == []:
                log.debug("Execute {} with no params".format(op))
            else:
                log.debug("Execute {} with params {}".format(op, params[0]))

            nextPC = None
            try:
                # only JUMP, JUMPZ and JUMPN have nextPC
                # nextPC is index of next code
                nextPC = exes[op](state, params)
            except ExecutionExceptin as e:
                raise e
            except:
                e = sys.exc_info()[1]
                log.error("Unexpected error while execution", e)
                raise e

            log.debug("pointer: {}".format(state.pointer))
            log.debug("reg state: {}".format(state.regs))
            if nextPC is not None:
                state.pc = nextPC
                return state

        state.pc += 1
        return state
