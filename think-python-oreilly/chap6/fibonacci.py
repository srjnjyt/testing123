from math import factorial


def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def main():
    t = int(input("enter a number: "))
    print(fibonacci(t))

if __name__ == "__main__":
    main()