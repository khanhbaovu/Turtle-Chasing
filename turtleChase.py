#Khanh Vu - CSCI 2202 - Lab 3
#Question a)(Part I) - [A dog chases a car]


import turtle
turtleWindow = turtle.Screen()
car = turtle.Turtle(shape="turtle")
car.penup()
car.pencolor("red")
car.setposition(-400/2,0)
car.pendown()

dog = turtle.Turtle(shape="turtle")
dog.penup()
dog.pencolor("blue")
dog.setposition(0,400/2)
dog.pendown()

for i in range(0,200):
    carPos = car.position()
    
    angle = dog.towards(carPos[0],carPos[1])

    dog.setheading(angle)

    car.fd(2)
    
    dog.fd(2)
