from random import shuffle, randint
test: list = ['!', '@', '#', '$', '%', '&', '*']
shuffle(test)
num = randint(1, 7)

print(test[num])