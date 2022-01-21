def ack(m, n):
    if not isinstance(m, int) or not isinstance(n, int):
        print("enter integers for m and n")
        return None
    if m < 0:
        print("m can not be negative")
        return None
    if n < 0:
        print("n can not be negative")
        return None
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))

def main():
    print(ack(3, 4))

if __name__ == "__main__":
    main()