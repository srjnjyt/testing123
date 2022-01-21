def prin1():
    for i in range(4):
        print("+ - - - -", end=' ')
    print("+")


def prin2():
    for i in range(4):
        print("|         ", end="")
    print("|")


for j in range(4):
    prin1()
    for i in range(4):
        prin2()
prin1()
