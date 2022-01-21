def recurse(n, s):
    """
    add all numbers until n to s
    """
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)
recurse(-1, 0)