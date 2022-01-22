def sqroot(a):
    x = a/2
    y = (x + a/x) / 2
    while y != x:
        x = y
        y = (x + a/x) / 2
    return y

def main():
    print(sqroot(25))

if __name__ == "__main__":
    main()