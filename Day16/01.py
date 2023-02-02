from turtle import Turtle, Screen
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("red")
timmy.fd(100)

my_screen = Screen()
print(my_screen.canvheight)

# tắt màng hình khi click
my_screen.exitonclick()
