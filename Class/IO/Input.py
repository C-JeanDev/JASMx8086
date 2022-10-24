from Class.Operation import SUB_REGISTER
from ..Utils.Data import format_line, VAR, CONST


class Input:

    @staticmethod
    def parse(loc: str):

        formatted_str: list = format_line(
            loc.replace('(', ' ( ').replace(')', ' ) '))
        
        var: str = formatted_str[2]
        value: any

        if len(formatted_str) > 4 and '//' not in formatted_str:
            raise Exception(f'Error {loc.strip()}')
        if var in VAR:
            value = input()            
            VAR.update({var:value})
        elif var in CONST:
            raise Exception(f'ERROR Assignment to constant variable "{var}"')
        elif var in SUB_REGISTER:
            value = int(input())            
            SUB_REGISTER.update({var:value})
        else:
            raise Exception(f'Undefined Variable {var}')
