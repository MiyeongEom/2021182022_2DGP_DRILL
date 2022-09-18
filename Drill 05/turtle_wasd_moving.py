import turtle

def restart():
    turtle.reset()

def drunken_move_forward():
    turtle.seth(90)
    turtle.forward(50)
    turtle.stamp()


def drunken_move_left():
    turtle.seth(180)
    turtle.forward(50)
    turtle.stamp()


def drunken_move_back():
    turtle.seth(270)
    turtle.forward(50)
    turtle.stamp()

def drunken_move_right():
    turtle.seth(0)
    turtle.forward(50)
    turtle.stamp()
    

turtle.shape('turtle')
turtle.onkey(drunken_move_forward,'w')
turtle.onkey(drunken_move_left,'a')
turtle.onkey(drunken_move_back,'s')
turtle.onkey(drunken_move_right,'d')
turtle.onkey(restart, 'Escape')
turtle.listen()
