from turtle import Turtle, Screen

pointer = Turtle()
pointer.color("green")
screen = Screen()


def move_forward():
    pointer.forward(10)


def move_backward():
    pointer.backward(10)


def turn_left():
    # pointer.left(30)
    new_heading = pointer.heading() + 10
    pointer.setheading(new_heading)


def turn_right():
    # pointer.right(30)
    new_heading = pointer.heading() - 10
    pointer.setheading(new_heading)


def clear():
    pointer.clear()  # xóa các line đã vẽ
    pointer.penup()
    pointer.home()  # quay về vị trí xuất phát
    pointer.pendown()


screen.listen()
screen.onkey(move_forward, 'w')
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(move_backward, "s")
screen.onkey(clear, "c")

screen.exitonclick()
