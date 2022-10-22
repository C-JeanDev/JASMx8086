from Class.Asm import Asm

FILENAME = 'main.jasm'


def main() -> None:
    a = Asm(FILENAME)
    a.registers()
    a.vars()


if __name__ == "__main__":
    main()
