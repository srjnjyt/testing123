from numpy import isin


def factorial(n):
    if not isinstance(n, int):
        print('factorial only defined for integers')
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    print(factorial(1.5))


if __name__ == "__main__":
    main()