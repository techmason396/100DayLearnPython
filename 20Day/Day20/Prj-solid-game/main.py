from turtle import Turtle, Screen
import time


def create_snake_body():
    snake_p = [(0, 0), (-20, 0), (-40, 0)]
    snakes = []
    for pos in snake_p:
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(pos)

        snakes.append(snake)
    return snakes


def move_snake(speed, snakes, screen):
    while True:
        # loại bỏ quá trình hiển thị
        screen.update()
        for snake_index in range():
            pass
            # snake.forward(speed)
            # time.sleep(1)


screen = Screen()
screen.setup(width=550, height=550)
screen.bgcolor("black")
screen.title("My Snake game")
# loại bỏ quá trình hiển thị
screen.tracer(0)

snakes = create_snake_body()
move_snake(20, snakes, screen)


screen.exitonclick()
