from curses.ascii import SUB
from .Lexer import *
from .Operation import SUB_REGISTER
from .Utils.Data import VAR,CONST
from prettytable import PrettyTable


class Asm:

    def __init__(self, filename: str):
        file = open(filename, 'r')
        lex = Lexer(file)

    @classmethod
    def registers(cls):
        myTable = PrettyTable(["Registers", "Value"])
        for i in SUB_REGISTER.keys():
            myTable.add_row([i, SUB_REGISTER.get(i)])
        print(myTable)

    @classmethod
    def vars(cls):
        print(VAR)
        print(CONST)
