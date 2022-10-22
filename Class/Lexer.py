from .Operation import *
from .String import String, Print
from .Utils.Data import *
from .JMP import JMP


class Lexer:

    def __init__(self, data):
        data = [line for line in data if line != '\n']
        self.data = data
        self.find_function(data)
        self.check_general_syntax(data)

    @classmethod
    def check_general_syntax(self, data):
        i: int = 0
        Interpreter: bool = False
        data_section: bool = True
        while i < len(data):
            # Verification of the variable section
            if '_var' in data[i]:
                data_section = True

            if data_section == True:
                if 'const' in data[i] or 'let' in data[i]:
                    String.format_string_var(data[i])

            # Verification of the main section
            if '_main' in data[i]:
                Interpreter = True

            if Interpreter == True:
                # Line Format
                if not ':' in data:
                    loc: list = format_line(data[i])
                if 'echo' in data[i]:
                    Print.echo(data[i].replace('(', ' ( ').replace(')',' ) ').replace("'"," ' "))
                if 'cmp' in data[i] and jmp_cond(format_line(data[i+1])):
                    if (k := JMP.start([format_line(data[i].replace(',', ' ')), format_line(data[i+1].replace(',', ' '))])) is not None:
                        i = k
                self.check_syntax(loc)
                if 'jmp' in str(loc) and loc[1] in LABELS.keys():
                    i = LABELS.get(loc[1])

            # Verification of the end section
            if '_end' in data[i]:
                    return
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
