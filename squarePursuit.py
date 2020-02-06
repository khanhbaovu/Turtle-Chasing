#Khanh Vu - CSCI 2202 - Lab 3
#Question c)(Part I) - [Four turtles at the corner of a square]


import turtle

turtleWindow = turtle.Screen()

turtle1 = turtle.Turtle(shape="turtle")

turtle2 = turtle.Turtle(shape="turtle")

turtle3 = turtle.Turtle(shape="turtle")

turtle4 = turtle.Turtle(shape="turtle")

turtle1.penup()
turtle1.setposition(-200,200)
turtle1.pencolor("red")
turtle1.pendown()

turtle2.penup()
turtle2.setposition(200,200)
turtle2.pencolor("blue")
turtle2.pendown()

turtle3.penup()
turtle3.setposition(-200,-200)
turtle3.pencolor("green")
turtle3.pendown()

turtle4.penup()
turtle4.setposition(200,-200)
turtle4.pencolor("pink")
turtle4.pendown()

follower = turtle1
target = turtle3

i = 0
while i<300:
    targetPos = target.position()
    angle = follower.towards(targetPos[0], targetPos[1])
    follower.setheading(angle)
    target.fd(3)
    follower.fd(3)
    i += 1
    if follower == turtle1:
        follower = turtle3
        target = turtle4
    elif follower == turtle3:
        follower = turtle4
        target = turtle2
    elif follower == turtle4:
        follower = turtle2
        target = turtle1
    else:
        follower = turtle1
        target = turtle3

