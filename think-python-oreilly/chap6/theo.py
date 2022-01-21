#return values

#import statements
import math


"""
calling the function returns a value which we usually assign 
to a variable or use as part of an expression
"""


e = math.exp(1.0)
print("value of e is", e)


e2 = math.exp(2.0)
print("value of e squared is", e2)


radius = 5
radians = 3.14
height = radius * math.sin(radians)
print("height is", height)


"""
the above functions are void, basically no return value
in this chapter we are gonna write friutful functions
"""

#fruitful function no. 1
def area(radius):
    a = math.pi * radius ** 2
    return a

#print area of circle with radius 3 and 4, and their ratio
print("area of circle with \n    radius three is", area(3), "\n    radius four is", area(4), "/n and their ratio is", area(3)/area(4))


#multiple return statements
def absolute_value(x):
    """
    returns the absolute value of a number
    """
    if x < 0:
        return -x
    else:
        return x

def compare(x, y):
    """
    compares two numbers x and y and returns value accordingly
    """
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

print("comparing 3 and 9, the output is", compare(3, 9))


#incremental development
def distance(x1, y1, x2, y2):
    dx = x1 - x2
    dy = y1 - y2
    dsquared = dx ** 2 + dy ** 2
    return math.sqrt(dsquared)

print("the distance b/w (1,2) and (4,6) is", distance(1, 2, 4, 6))

"""
scaffolding is code written to test in small chunks
but code that doesn't make it to the final version
"""

def hypotenuse(x, y):
	x2 = x **2
	y2 = y ** 2
	z2 = x2 + y2
	return math.sqrt(z2)

print(hypotenuse(5,12))

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

print(circle_area(0,0,3,4))


def is_divisible(x, y):
    """
    tells us if x is divisible by y
    """
    if x % y == 0:
        return True
    else:
        return False


#boolean functions
def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False

print(is_between(3, 4, 5))
print(is_between(4, 3, 5))