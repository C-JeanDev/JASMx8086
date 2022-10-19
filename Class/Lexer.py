from .Operation import *
from .String import String
from .Utils.Data import *
from .JMP import JMP


class Lexer:
    # fn_address = {}

    def __init__(self, data):
        data = [line for line in data if line != '\n']

        self.data = data
        self.find_function(data)
        self.check_general_syntax(data)

    @classmethod
    def check_general_syntax(self, data):
        i: int = 0
        while i < len(data):
            if 'db' in data or 'dw' in data:
                String.format_string_var(data)
            if jmp_cond(format_line(data[i])) and 'cmp' in data[i+1]:
                if (k := JMP.start([format_line(data[i].replace(',', ' ')), format_line(data[i+1].replace(',', ' '))])) is not None:
                    i = k
            if not ':' in data:
                loc: list = format_line(data[i])
            self.check_syntax(loc)
            if 'jmp' in str(loc) and loc[1] in LABELS.keys():
                i = LABELS.get(loc[1])
            i += 1

    @classmethod
    def find_function(cls, data):
        i: int = 0
        while i < len(data):
            if ':' in str(data[i]):
                a = format_line(data[i].replace(':', ' : '))
                LABELS[a[0]] = i
            i += 1

    @classmethod
    def check_syntax(cls, loc: list):
        if loc[0] in KEY:
            Operation.operation_syntax(loc)
