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
    '''
    @staticmethod
    def start(loc: list) -> int:
        line1 = loc[0]
        line2 = loc[1]

        if JMP.jump(line1):
            return JMP.compare(line2)
        else:
            print('Condition is False')

# da mettere tutte le instruction nel data

    @staticmethod
    def jump(line1: list):
        if len(line1) == 2:
            if line1[0] == 'jz' and SUB_REGISTER.get(line1[1]) == 0:
                return True
            if line1[0] == 'jnz' and SUB_REGISTER.get(line1[1]) != 0:
                return True
        if line1[0] == 'je' and (line1[1] == line1[2] or SUB_REGISTER.get(line1[1]) == SUB_REGISTER.get(line1[2])):
            return True
        if line1[0] == 'jne' and (line1[1] != line1[2] or SUB_REGISTER.get(line1[1]) != SUB_REGISTER.get(line1[2])):
            return True
        if line1[0] == 'jg' and (line1[1] > line1[2] or SUB_REGISTER.get(line1[1]) > SUB_REGISTER.get(line1[2])):
            return True
        if line1[0] == 'jl' and (line1[1] < line1[2] or SUB_REGISTER.get(line1[1]) < SUB_REGISTER.get(line1[2])):
            return True

    @staticmethod
    def compare(line2: list):
        print(LABELS)
        print(LABELS.get(line2[1]))
        return LABELS.get(line2[1])
