import turtle
import math

bob = turtle.Turtle()

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.rt(90)
    
square(bob, 100)
square(bob, 200)


def polygon(t, l, n):
    """
    creates polygon with turtle t, length as l, and number of sides as n
    """
    for i in range(n):
        t.fd(length)
        t.rt(360/n)

polygon(bob, 100, 7)


def circle(t , r):
    """
    creates a circle with turtle t, radius r
    """
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 1
    polygon(t, r * 2 * math.pi/n, n)

circle(bob, 10)
circle(bob, 100)

def arc(t, r, ang):
    """
    creates an arc with turtle t, radius r, and angle ang
    """
    arc_length = 2 * math.pi * r * ang / 360
    n = int(arc_length/3) + 1
    step_length = arc_length / n
    step_angle = ang / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob, 30, 90)


turtle.mainloop()