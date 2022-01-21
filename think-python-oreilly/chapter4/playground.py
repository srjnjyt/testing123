import turtle
bob = turtle.Turtle()
print(bob)

#triangle
bob.fd(100)
bob.lt(60)
bob.fd(100)
bob.lt(150)
bob.fd(172)


#square
bob.lt(60)
for i in range(4):
    bob.fd(100)
    bob.rt(90)

bob.rt(90)
bob.fd(200)

bob.rt(60)
bob.fd(100)
bob.rt(150)
bob.fd(202)





turtle.mainloop()