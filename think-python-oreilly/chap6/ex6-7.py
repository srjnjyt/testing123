def is_power(a, b):
    if a == 1:
        return True
    if a % b == 0:
        c = a / b
        if is_power(c, b):
            return True
        else:
            return False

    else:
        return False

def main():

    print(is_power(9, 3))
    print(is_power(10, 3))

    print(is_power(16,8))

    print(is_power(81, 3))

if __name__ == "__main__":
    main()