def gcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)
    
def main():
    print(gcd(8,10))
    print(gcd(8,11))
    print(gcd(8,12))
    print(gcd(8,13))
    print(gcd(8,14))


if __name__ == "__main__":
    main()