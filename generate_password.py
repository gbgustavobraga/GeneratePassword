from random import randint, shuffle
import string


def listAlphabetlow():
    low = list(string.ascii_lowercase)
    shuffle(low)
    num = randint(1, 7)
    return low[num]


def listAlphabetupper():
    upper = list(string.ascii_uppercase)
    shuffle(upper)
    num = randint(1, 7)
    return upper[num]


def ctrEspecials():
    ctr: list = ['!', '@', '#', '$', '%', '&', '*', '_']
    shuffle(ctr)
    num = randint(1, 7)
    return ctr[num]


def generate(size: int) -> None:
    list_pass = []
    for c in range(0, size):

        letter_low = listAlphabetlow()
        letter_upper = listAlphabetupper()
        ctr_especials = ctrEspecials()

        shuffle(letter_low and letter_upper and ctr_especials)

        list_pass.append(letter_upper)
        list_pass.append(letter_low)
        list_pass.append(ctr_especials)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def main() -> None:
    main_()


def main_() -> None:
    print(f"{'=' * 20} GENERATE PASSWORD {'=' * 20}")

    size: int = int(input("Size Password: "))
    upper: str = str(input("Capital letters [\033[31mY\033[m / \033[32mN\033[m]: "))
    low: str = str(input("Small letters [\033[31mY\033[m / \033[32mN\033[m]: "))
    ctr: str = str(input("Special characters [\033[31mY\033[m / \033[32mN\033[m]: "))
    generate(size)


if __name__ == "__main__":
    main()
