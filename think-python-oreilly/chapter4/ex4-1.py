import math
import turtle

bob = turtle.Turtle()

def circle(t , r):
    """
    creates a circle with turtle t, radius r
    """
    circumference = 2 * math.pi * r
    n = int(circumference/3) + 1

radius = 10

circle(bob, radius)

turtle.mainloop()