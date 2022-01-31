from random import randint, shuffle, randrange
import string


# Uppercase, lowercase, and special characters lists
def listAlphabetlow():  # List Alphabet lowercase
    low = list(string.ascii_lowercase)
    shuffle(low)
    num = randint(1, 7)
    return low[num]


def listAlphabetupper():  # List Alphabet uppercase
    upper = list(string.ascii_uppercase)
    shuffle(upper)
    num = randint(1, 7)
    return upper[num]


def ctrEspecials():  # List Alphabet special characters
    ctr: list = ['!', '@', '#', '$', '%', '&', '*', '_']
    shuffle(ctr)
    num = randint(1, 7)
    return ctr[num]


#  Random generators
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
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)
        shuffle(letter_low and letter_upper and ctr_especials and num)

        list_pass.append(num[1])
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
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)

        shuffle(letter_low and letter_upper and num)
        list_pass.append(num[1])
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
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)
        shuffle(ctr_especials and letter_upper and num)
        list_pass.append(num[1])
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
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)
        shuffle(letter_low and num)
        list_pass.append(num[1])
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
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)
        shuffle(letter_low and ctr_especials and num)
        list_pass.append(num[1])
        list_pass.append(ctr_especials)
        list_pass.append(letter_low)
        shuffle(list_pass)

    for c in list_pass[0: size]:
        print(c, end='')


def generate_up_num(size: int) -> None:
    list_pass = []
    for c in range(0, size):
        letter_upper = listAlphabetupper()
        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)
        shuffle(letter_upper and num)
        list_pass.append(num[1])
        list_pass.append(letter_upper)
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

        num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        shuffle(num)
        list_pass.append(num[1])
        shuffle(list_pass)
        print(len(list_pass))
    for c in list_pass[0: size]:
        print(c, end='')


def main() -> None:
    main_()


def main_() -> None:
    print(' ')
    print(f"{'=' * 20} GENERATE PASSWORD {'=' * 20}")

    size: int = int(input("Size Password: "))
    num: int = int(input("Number [\033[31m1\033[m / \033[32m0\033[m]: "))
    upper: int = int(input("Capital letters [\033[31m1\033[m / \033[32m0\033[m]: "))
    low: int = int(input("Small letters [\033[31m1\033[m / \033[32m0\033[m]: "))
    ctr: int = int(input("Special characters [\033[31m1\033[m / \033[32m0\033[m]: "))
    if upper == 1 and low == 1 and ctr == 1 and num == 1:
        generate_up_lw_ctr_num(size)

    elif upper == 1 and low == 1 and ctr == 1:
        generate_up_lw_ctr(size)
    elif upper == 1 and low == 1:
        generate_up_low(size)
    elif upper == 1 and low == 1 and num == 1:
        generate_up_low_num(size)
    elif low == 1 and ctr == 1:
        generate_low_ctr(size)

    elif low == 1 and num == 1:
        generate_low_num(size)

    elif upper == 1 and num == 1:
        generate_up_num(size)
    elif low == 1 and ctr == 1 and num == 1:
        generate_low_ctr_num(size)
    elif ctr == 1 and upper == 1:
        generate_up_ctr(size)
    elif ctr == 1 and upper == 1 and num == 1:
        generate_up_ctr_num(size)
    elif upper == 1:
        generate_up(size)
    elif low == 1:
        generate_low(size)
    elif ctr == 1:
        generate_ctr(size)

    elif num == 1:
        generate_num(size)
    else:

        print('ERROR')


if __name__ == "__main__":
    main()
