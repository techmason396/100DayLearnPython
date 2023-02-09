from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("red")
my_turtle.speed(1)


def drawn_square():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.left(90)


def drawn_dashed_line(time):
    for i in range(time):
        my_turtle.forward(time/2)
        my_turtle.penup()
        my_turtle.forward(time/2)
        my_turtle.pendown()


def drawn_shape(numb_sides):
    angle = 360/numb_sides
    for i in range(numb_sides):
        my_turtle.forward(100)
        my_turtle.right(angle)


drawn_shape(3)

screen = Screen()
screen.exitonclick()
