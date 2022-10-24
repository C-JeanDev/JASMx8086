from .Operation import *
from .IO.String import String
from .IO.Print import  Print
from .Utils.Data import *
from .JMP import JMP
from .IO.Input import Input


class Lexer:

    def __init__(self, data):
        data = [line for line in data if line != '\n']
        self.data = data
        self.find_function(data)
        self.check_general_syntax(data)

    @classmethod
    def check_general_syntax(cls, data):
        i: int = 0
        interpreter: bool = False
        data_section: bool = True
        while i < len(data):

            # Verification of the variable section
            if '_var' in data[i]:
                data_section = True

            if data_section:
                if 'const' in data[i] or 'let' in data[i]:
                    String.format_string_var(data[i])

            # Verification of the main section
            if '_main' in data[i]:
                interpreter = True

            if interpreter:
                # Line Format
                if not ':' in data:
                    loc: list = format_line(data[i])
                if 'echo' in data[i]:
                    Print.echo(data[i].replace('(', ' ( ').replace(')', ' ) ').replace("'", " ' "))
                if 'read' in data[i]:
                    Input.parse(data[i])
                if 'cmp' in data[i] and jmp_cond(format_line(data[i + 1])):
                    if (k := JMP.parse([format_line(data[i].replace(',', ' ')),
                                        format_line(data[i + 1].replace(',', ' '))])) is not None:
                        i = k
                cls.check_syntax(loc)
                try:
                    if 'jmp' in str(loc) and loc[1] in LABELS.keys():
                        i = LABELS.get(loc[1])
                except:
                    pass
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
        try:
            if loc[0] in KEY:
                Operation.operation_syntax(loc)
        except:
            pass
        
