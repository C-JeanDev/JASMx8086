from Class.Asm import Asm

FILENAME = 'main.pyasm'


def main() -> None:
    a = Asm(FILENAME)
    a.registers()
    a.vars()


if __name__ == "__main__":
    main()
