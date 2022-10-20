import enum


SECTION: set = {
    '.data', '.code'
}

KEY: set = {
    'add', 'sub', 'mul', 'div', 'mov', 'inc', 'dec'
}

CONDITIONAL_JMP: set = {
    'je', 'jne', 'jg', 'jl', 'jz', 'jnz'
}

STRING: dict = {}

LABELS: dict = {}


def format_line(loc: str) -> list:
    return list(filter(lambda element: element.strip() != '', loc.rstrip('\n').split(' ')))  


def jmp_cond(loc: str) -> bool:
    for i, condition in enumerate(CONDITIONAL_JMP):
        if condition in loc:
            return True
    return False
