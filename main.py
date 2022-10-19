from Class.Asm import Asm

FILENAME = 'main.jasm'


def main() -> None:
    a = Asm(FILENAME)
    a.register()


if __name__ == "__main__":
    main()
