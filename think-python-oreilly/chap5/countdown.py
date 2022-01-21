def countdown(n):
    if n <= 0:
        print("blastoff")
    else:
        print(n)
        countdown(n-1)

countdown(7)
countdown(6)
