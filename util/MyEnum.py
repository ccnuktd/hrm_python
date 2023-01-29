from enum import Enum


class State(Enum):
    INIT = 0
    STOP = 1
    NEXT = 2
    GOON = 3
    EXIT = 4


class OpType(Enum):
    OP_WITHOUT_PARAM = 0
    OP_WITH_PARAM = 1
    LABEL = 2
