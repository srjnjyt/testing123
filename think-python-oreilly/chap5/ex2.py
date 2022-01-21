#5.14 Exercise 2

def check_fermat(a, b, c, n):
    p = a ** n + b ** n
    q = c ** n
    if n > 2 and p == q:
        print("holy smokes fermat was wrong")
    else:
        print(p)
        print(q)
        print("no, that doesn't work")


a = input("enter a number a: ")
b = input("enter a number b: ")
c = input("enter a number c: ")
n = input("enter a number n: ")

check_fermat(int(a), int(b), int(c), int(n))


