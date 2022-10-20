# PY_ASM version 0.0.1
Interpreter for ASM done in python just for fun
# Functions Implemented:
    MOV,
    INC,
    DEC,
    ADD,
    SUB,
    MUL,
    DIV,
    Conditional Jump:
      Instruction	    Description	Flags
      JE/JZ	          Jump Equal or Jump Zero	
      JNE/JNZ	        Jump not Equal or Jump Not Zero	
      JG/JNLE	        Jump Greater or Jump Not Less/Equal	
      JGE/JNL	        Jump Greater/Equal or Jump Not Less	
      JL/JNGE	        Jump Less or Jump Not Greater/Equal
      JLE/JNG	        Jump Less/Equal or Jump Not Greater

# Get Started
  How to Start
```python   
    from Class.Asm import Asm

    FILENAME = 'main.pyasm' # <- filename here


    def main() -> None:
        a = Asm(FILENAME)
        a.registers() # <- Print of Registers here

    if __name__ == "__main__":
        main()
``` 
Write some py_asm Code in the main.pyasm file

```assembly
mov al,4
mov bl,4

je al,bl
cmp fine

mov dh,9

fine:
    mov dl,1
```
# Next Update 0.0.2:
Available soon on [pip](https://pip.pypa.io/en/stable/)
    
    More Conditional Jump:
        JNLE,
        JGE,
        JLE,
        JNG,     
    String {db,dw}
    Exceptions
    

  
  
  
  
