from turtle import Turtle, Screen


tl = Turtle()


def move_up():
    tl.forward(10)


screen = Screen()
screen.listen()
screen.onkey(move_up, "Up")

screen.exitonclick()
