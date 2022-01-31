from random import randint, shuffle, randrange
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


#  ok
def generate_up_lw_ctr(size: int) -> None:
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


def generate_up_lw_ctr_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):

        letter_low = listAlphabetlow()
        letter_upper = listAlphabetupper()
        ctr_especials = ctrEspecials()
        num = randint(1, 10)
        print(num)
        shuffle(letter_low and letter_upper and ctr_especials and num)

        list_pass.append(num)
        list_pass.append(letter_upper)
        list_pass.append(letter_low)
        list_pass.append(ctr_especials)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


#  ok
def generate_up_low_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_low = listAlphabetlow()
        letter_upper = listAlphabetupper()
        num = randint(1, 10)
        shuffle(letter_low and letter_upper and num)
        list_pass.append(num)
        list_pass.append(letter_upper)
        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


#  ok
def generate_up_low(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_low = listAlphabetlow()
        letter_upper = listAlphabetupper()

        shuffle(letter_low and letter_upper)

        list_pass.append(letter_upper)
        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


#  ok
def generate_up_ctr(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        ctr_especials = ctrEspecials()
        letter_upper = listAlphabetupper()

        shuffle(ctr_especials and letter_upper)

        list_pass.append(letter_upper)
        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_up_ctr_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        ctr_especials = ctrEspecials()
        letter_upper = listAlphabetupper()
        num = randint(1, 10)
        shuffle(ctr_especials and letter_upper and num)
        list_pass.append(num)
        list_pass.append(letter_upper)
        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


#  ok
def generate_low_ctr(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_low = listAlphabetlow()
        ctr_especials = ctrEspecials()

        shuffle(letter_low and ctr_especials)

        list_pass.append(ctr_especials)
        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_low_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_low = listAlphabetlow()
        num = randint(1, 10)
        shuffle(letter_low and num)
        list_pass.append(num)

        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


#  ok
def generate_low_ctr_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_low = listAlphabetlow()
        ctr_especials = ctrEspecials()
        num = randint(1, 10)
        shuffle(letter_low and ctr_especials and num)
        list_pass.append(num)
        list_pass.append(ctr_especials)
        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_up(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_upper = listAlphabetupper()

        shuffle(letter_upper)

        list_pass.append(letter_upper)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_low(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_low = listAlphabetlow()

        shuffle(letter_low)

        list_pass.append(letter_low)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_ctr(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        ctr_especials = ctrEspecials()
        shuffle(ctr_especials)

        list_pass.append(ctr_especials)

        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        num = randint(1, 10)
        list_pass.append(num)
        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def main() -> None:
    main_()


def main_() -> None:
    print(f"{'=' * 20} GENERATE PASSWORD {'=' * 20}")

    size: int = int(input("Size Password: "))
    num: str = str(input("Number [\033[31mY\033[m / \033[32mN\033[m]: ")).upper()[0]
    upper: str = str(input("Capital letters [\033[31mY\033[m / \033[32mN\033[m]: ")).upper()
    low: str = str(input("Small letters [\033[31mY\033[m / \033[32mN\033[m]: ")).upper()
    ctr: int = int(input("Special characters [\033[31mY\033[m / \033[32mN\033[m]: "))
    if upper == 'Y' and low == 'Y' and ctr == 'y' and num == 'Y':
        generate_up_lw_ctr_num(size)

    elif upper == 'Y' and low == 'Y' and ctr == 1:
        generate_up_lw_ctr(size)
    elif upper == 'Y' and low == 'Y':
        generate_up_low(size)
    elif upper == 'Y' and low == 'Y' and num == 'Y':
        generate_up_low_num(size)
    elif low == 'Y' and ctr == 'Y':
        generate_low_ctr(size)

    elif low == 'Y' and num == 'Y':
        generate_low_num(size)
    elif low == 'Y' and ctr == 'Y' and num == 'Y':
        generate_low_ctr_num(size)
    elif ctr == 'Y' and upper == 'Y':
        generate_up_ctr(size)
    elif ctr == 'Y' and upper == 'Y' and num == 'Y':
        generate_up_ctr_num(size)
    elif upper == 'Y':
        generate_up(size)
    elif low == 'Y':
        generate_low(size)
    elif ctr == 'Y':
        generate_ctr(size)

    elif num == 'Y':
        generate_num(size)
    else:
        print('vasco')


if __name__ == "__main__":
    main()
