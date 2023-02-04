from turtle import Turtle, Screen
import pandas as pd
import os

PATH = os.path.abspath(os.path.dirname(__file__))
IMG = PATH + "/US_states.gif"
DATA = pd.read_csv(PATH+"/50_states.csv")


def get_mouse_click_coor(x, y):
    print(x, y)


screen = Screen()
screen.setup(width=700, height=500)
screen.title("U.S States Game")
# thêm loại shape vào trong screen
screen.addshape(IMG)

turtle = Turtle()

# thay đổi con trở thành hình img đã chọn
turtle.shape(IMG)

# hàm này trả về giá trị x, y khi click có thể tận dụng để hiển thị giá trị khi click chuột
# screen.onscreenclick(get_mouse_click_coor)

# cách hiển thị mãi ko bị tắt màng hình khi click chuột
screen.mainloop()

answer = screen.textinput(title="What's another state's")
