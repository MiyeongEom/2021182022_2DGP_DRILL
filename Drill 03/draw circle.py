import turtle

count = 4
while(count>0):
    turtle.forward(500)
    turtle.left(90)
    count = count -1


turtle.left(360)
for num in range(0, 4):
    turtle.penup()
    turtle.goto(0, num*100+100)
    turtle.pendown()
    turtle.forward(500)

turtle.left(90)
for num in range(0, 4):
    turtle.penup()
    turtle.goto(num*100+100, 0)
    turtle.pendown()
    turtle.forward(500)


