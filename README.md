# JASMx8086 version 0.1.2

JASMx8086 Documentation Language

# JASMx8086 Registers:

    +-----------+-------+
    | Registers | Value |
    +-----------+-------+
    |    jxa    |   0   |
    |    jxb    |   0   |
    |    jxc    |   0   |
    |    jxd    |   0   |
    |    jya    |   0   |
    |    jyb    |   0   |
    |    jyc    |   0   |
    |    jyd    |   0   |
    +-----------+-------+
    
    
# Get Started
  How to Start
```python   
    from Class.Asm import Asm

    FILENAME = 'main.jasm' # <- filename here


    def main() -> None:
        a = Asm(FILENAME)
        a.registers() # <- Print of Registers here

    if __name__ == "__main__":
        main()
``` 
# Write some JASMx8086 Code in the main.jasm file

Variables Section

```assembly
_var 

    let lang = 'Python'
    let lang = 'Rust'

```
    
Main Section 

```assembly
_main // <-code starts here

    mov jxa,10
    mov jxb,10

    cmp jxa,jxb
    je fine

    mov jxd,88

    fine: //<- lables
        mov jyd,9999

_end // <-code ends here

```

# Hello World!
```python
_main
    echo('Hello World!')
_end
```

# Variables
```python
 _var
     let job = 'Developer'
_main
    echo(job)
_end
```
#Input
```assembly

_var
    const job  = 'Programmer'
    let job1 = 'Developer'

_main

    echo(job1)  //<- Print job1
    read(jxd)   // <- Register Read
    read(job1)  //<- job1 Read
    echo(job1)  // <- Print job1 

_end
```
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


# Next Update 0.1.3:
Available soon on [pip](https://pip.pypa.io/en/stable/)  

```    
    Exceptions
```
  
  
  
