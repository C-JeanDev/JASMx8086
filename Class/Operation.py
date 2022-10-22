import math
from .Utils.Data import *


class Operation:

    @staticmethod
    def operation_syntax(loc: list):
        if loc[0] not in KEY:
            raise Exception('Keyword non Riconosciuta')
        if loc[0] == 'mov':
            loc = loc[1].split(',')
            if loc[0] in SUB_REGISTER:
                SUB_REGISTER.update({loc[0]: int(loc[1])})
        elif loc[0] == 'add':
            loc = loc[1].split(',')
            if loc[0] in SUB_REGISTER:
                SUB_REGISTER.update(
                    {loc[0]: int(loc[1]) + SUB_REGISTER.get(loc[0])})
        elif loc[0] == 'sub':
            loc = loc[1].split(',')
            if loc[0] in SUB_REGISTER:
                SUB_REGISTER.update(
                    {loc[0]: SUB_REGISTER.get(loc[0]) - int(loc[1])})
        elif loc[0] == 'mul':
            loc = loc[1].split(',')
            if loc[0] in SUB_REGISTER:
                SUB_REGISTER.update(
                    {loc[0]: SUB_REGISTER.get(loc[0]) * int(loc[1])})
        elif loc[0] == 'div':
            loc = loc[1].split(',')
            if loc[0] in SUB_REGISTER:
                SUB_REGISTER.update(
                    {loc[0]: math.floor(SUB_REGISTER.get(loc[0]) / int(loc[1]))})
                SUB_REGISTER.update(
                    {'ah': SUB_REGISTER.get(loc[0]) % int(loc[1])})
        elif loc[0] == 'inc':
            if loc[1] in SUB_REGISTER:
                SUB_REGISTER.update({loc[1]: SUB_REGISTER.get(loc[1]) + 1})
        elif loc[0] == 'dec':
            if loc[1] in SUB_REGISTER:
                SUB_REGISTER.update({loc[1]: SUB_REGISTER.get(loc[1]) - 1})

            # da mettere il risultato in al e il resto in ah


SUB_REGISTER: dict = {'jxa': 0, 'jxb': 0, 'jxc': 0,
                      'jxd': 0, 'jya': 0, 'jyb': 0, 'jyc': 0, 'jyd': 0}
