from turtle import Turtle, Screen
import random

X_POS = -380
y_pos = [100, 70, 40, 10, -20, -50]
colors = ["red", "green", "yellow", "black", "pink", "orange"]
is_race_on = False

# tạo các con rùa


def create_turtle(colors, x_pos, y_pos):
    list_turtle = []
    for index_turtle in range(0, len(colors)):
        new_turtle = Turtle()
        new_turtle.color(colors[index_turtle])
        new_turtle.shape("turtle")
        new_turtle.penup()
        new_turtle.setpos(x_pos, y_pos[index_turtle])
        list_turtle.append(new_turtle)
    return list_turtle


def create_list_speed(list_turtle):
    list_speed = []
    for turtle in list_turtle:
        speed = random.randint(3, 10)
        list_speed.append(speed)
    return list_speed


# set up screen
screen = Screen()

# cài đặt độ lơn của màn hình
screen.setup(800, 400)

list_turtle = create_turtle(colors, X_POS, y_pos)
list_speed = create_list_speed(list_turtle)
print(list_speed)
cheat_print = list_speed. index(max(list_speed))
print(cheat_print)
# hiển popup nhập input đầu vào
user_bet = screen.textinput(title="Make your bet",
                            prompt="Which turtle win the racer? Enter a color: ")


# nếu người dùng nhập vào thì mới chạy đua
if user_bet:
    is_race_on = True

while is_race_on:
    for index_turtle in range(0, len(list_turtle)):
        # kiểm tra xem con rùa nào chay qua vạch đích tai x = 350 thì hiên trị chiến thắng
        if list_turtle[index_turtle].xcor() > 350:
            winner_color = list_turtle[index_turtle].pencolor()
            is_race_on = False
            if user_bet == winner_color:
                print(f"You've wont! the {winner_color} turtle is the winner")
            else:
                print(f"You've lose! the {winner_color} turtle is the winner")
        list_turtle[index_turtle].forward(list_speed[index_turtle])

screen.exitonclick()
