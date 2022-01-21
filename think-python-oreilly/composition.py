import math
degrees = 30
x = math.sin(degrees / 360.0 * 2 * math.pi)
print(x)

y = math.exp(math.log(x + 1))
print(y)

def print_lyrics():
    print("im a lumberjack")
    print("and im okay")

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()



def right_justify(t):
    s = len(t)
    z = ' ' * (70 - s) + t
    print(z)
    return z


right_justify('hello')
right_justify('hellohello')