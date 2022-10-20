from Class.Asm import Asm

FILENAME = 'main.pyasm'


def main() -> None:
    a = Asm(FILENAME)
    a.registers()


if __name__ == "__main__":
    main()
