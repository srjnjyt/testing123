def is_triangle(a, b, c):
    t = max(a, b, c)
    if t > a + b + c - t:
        print("No")
    else:
        print("Yes")

p = input("enter an integer: ")
q = input("enter an integer: ")
r = input("enter an integer: ")

is_triangle(p, q, r)