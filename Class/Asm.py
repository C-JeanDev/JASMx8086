from .Lexer import *
from .Operation import SUB_REGISTER


class Asm:

    def __init__(self, filename: str):
        file = open(filename, 'r')
        lex = Lexer(file)

    @classmethod
    def registers(cls):
        print(SUB_REGISTER)
