from .Utils.Data import format_line, STRING_KEY, VAR, CONST


class String:

    @staticmethod
    def format_string_var(loc: str):
        k = format_line(loc.replace('=',' = '))
        if k[1] == '=':
            raise Exception('Variable Name Missing')
        value = String.clean_string(loc)
        var_name = k[1]
        if k[0] not in STRING_KEY:
            raise Exception(f'Error {k[0]} not a keyword')
        if k[0] == 'let':
            VAR.update({var_name: value})
        else:
            CONST.update({var_name:value})

    @staticmethod
    def clean_string(loc: str) -> str:
        c: int = 0
        var: list = []
        for i, char in enumerate(list(loc)):
            if c == 2:
                break
            if char == "'":
                c += 1
            if c == 1:
                var.append(char)
            
        return ''.join(var).replace("'",'').strip()

class Print():

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

