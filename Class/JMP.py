from .Utils.Data import LABELS,VAR,CONST
from .Operation import SUB_REGISTER

'''
Instruction	    Description	Flags tested
JE/JZ	        Jump Equal or Jump Zero	
JNE/JNZ	        Jump not Equal or Jump Not Zero	
JG/JNLE	        Jump Greater or Jump Not Less/Equal	
JGE/JNL	        Jump Greater/Equal or Jump Not Less	
JL/JNGE	        Jump Less or Jump Not Greater/Equal
JLE/JNG	        Jump Less/Equal or Jump Not Greater	
'''


class JMP:

    '''
    loc return 2 lines of code
    line1 should contain jmp
    line1 should contain cmp
    '''

    @staticmethod
    def parse(loc: list) -> int:
        line1 = loc[0]
        line2 = loc[1]

        if JMP.jump(line1, line2):
            return JMP.compare(line2)

    @classmethod
    def jump(cls, line1: list, line2: list) -> bool:

        var1:any = JMP.handle_var(line1[1])
        var2:any = JMP.handle_var(line1[2])

        if line2[0] == 'jz' or line2[0] == 'jnz':
            if line1[0] == 'jz' and var1 == 0:
                return True
            elif line1[0] == 'jnz' and var2 != 0:
                return True
            raise Exception("Wrong Number of Parameters")

        if line2[0] == 'je' and var1 == var2:
            return True
        elif line2[0] == 'jne' and var1 != var2:
            return True
        elif line2[0] == 'jg' and var1 > var2:
            return True
        elif line2[0] == 'jl' and var1 < var2:
            return True
        elif line2[0] == 'jge' and var1 >= var2:
            return True
        elif line2[0] == 'jle' and var1 <= var2:
            return True


    @staticmethod
    def handle_var(value: str) -> str:
        if value in SUB_REGISTER:
            return  SUB_REGISTER.get(value)            
        elif value in VAR:
            return VAR.get(value)
        elif value in CONST:
            return CONST.get(value)
        else:
            try:
                return int(value)
            except:
                raise Exception('Value Error')

    @staticmethod
    def compare(line2: list):
        return LABELS.get(line2[1])
