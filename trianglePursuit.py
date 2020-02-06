#Khanh Vu - CSCI 2202 - Lab 3
#Question b)(Part I) - [Three turtles at the corners of an equilateral triangle, of side 400 units]


import turtle

turtleWindow = turtle.Screen()

turtle1 = turtle.Turtle(shape="turtle")

turtle2 = turtle.Turtle(shape="turtle")

turtle3 = turtle.Turtle(shape="turtle")

turtle1.penup()
turtle1.setposition(0,200)
turtle1.pencolor("red")
turtle1.pendown()

turtle2.penup()
turtle2.setposition(-200,-200)
turtle2.pencolor("blue")
turtle2.pendown()

turtle3.penup()
turtle3.setposition(200,-200)
turtle3.pencolor("green")
turtle3.pendown()

follower = turtle1
target = turtle2

i = 0
while i<222:
    targetPos = target.position()
    angle = follower.towards(targetPos[0], targetPos[1])
    follower.setheading(angle)
    target.fd(2)
    follower.fd(2)
    i += 1
    if follower == turtle1:
        follower = turtle2
        target = turtle3
    elif follower == turtle2:
        follower = turtle3
        target = turtle1
    else:
        follower = turtle1
        target = turtle2

