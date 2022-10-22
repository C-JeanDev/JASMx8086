'''
Directive	Purpose	Storage         Space                Implemented
DB	        Define Byte	allocates   1 byte                 v
DW	        Define Word	allocates   2 bytes                v
DD	        Define Doubleword	    allocates 4 bytes      v
DQ	        Define Quadword	        allocates 8 bytes      v
DT	        Define Ten Bytes	    allocates 10 bytes     v
'''

STRING_KEY: set = {
    'const', 'let'
}

SECTION: set = {
    '.data', '.code'
}

KEY: set = {
    'add', 'sub', 'mul', 'div', 'mov', 'inc', 'dec'
}

CONDITIONAL_JMP: set = {
    'je', 'jne', 'jg', 'jl', 'jz', 'jnz'
}

VAR: dict = {}

CONST: dict = {}

LABELS: dict = {}


def format_line(loc: str) -> list:
    return list(filter(lambda element: element.strip() != '', loc.rstrip('\n').split(' ')))  


def jmp_cond(loc: str) -> bool:
    for i, condition in enumerate(CONDITIONAL_JMP):
        if condition in loc:
            return True
    return False
