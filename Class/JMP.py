from Class.Utils.Data import LABELS
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


    @staticmethod
    def jump(line1: list, line2: list):

        if line2[0] == 'jz' or line2[0] == 'jnz':
            if line1[0] == 'jz' and SUB_REGISTER.get(line1[1]) == 0:
                return True
            if line1[0] == 'jnz' and SUB_REGISTER.get(line1[1]) != 0:
                return True
            raise Exception("Wrong Number of Parameters")

        if line2[0] == 'je' and (line1[1] == line1[2] or SUB_REGISTER.get(line1[1]) == SUB_REGISTER.get(line1[2])):
            return True
        if line2[0] == 'jne' and (line1[1] != line1[2] or SUB_REGISTER.get(line1[1]) != SUB_REGISTER.get(line1[2])):
            return True
        if line2[0] == 'jg' and (line1[1] > line1[2] or SUB_REGISTER.get(line1[1]) > SUB_REGISTER.get(line1[2])):
            return True
        if line2[0] == 'jl' and (line1[1] < line1[2] or SUB_REGISTER.get(line1[1]) < SUB_REGISTER.get(line1[2])):
            return True
        if line2[0] == 'jge' and (line1[1] >= line1[2] or SUB_REGISTER.get(line1[1]) >= SUB_REGISTER.get(line1[2])):
            return True
        if line2[0] == 'jle' and (line1[1] <= line1[2] or SUB_REGISTER.get(line1[1]) <= SUB_REGISTER.get(line1[2])):
            return True
        raise Exception("Value Error")

    @staticmethod
    def compare(line2: list):
        return LABELS.get(line2[1])
