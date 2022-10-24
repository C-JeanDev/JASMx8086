from ..Utils.Data import format_line, VAR, CONST
from .String import String

class Print:

    @staticmethod
    def echo(loc: str):
        if loc.count('(') == 0 or loc.count(')') == 0:
            raise Exception(f'Parenthesis Missing {loc}')
        formatted_string = format_line(loc)
        if "'" not in loc and formatted_string[2] in VAR:
            print(VAR.get(formatted_string[2]))
        elif "'" not in loc and formatted_string[2] in CONST:
            print(CONST.get(formatted_string[2]))
        elif "'" not in loc:
            raise Exception(f'Undefined variable f{loc}')
        elif loc.count("'") < 2 or loc.count("'") > 2:
            raise Exception(f' " \' " Error {loc}')
        elif "'" in loc:
            print(String.clean_string(loc))
        else:
            raise Exception('SyntaxError')