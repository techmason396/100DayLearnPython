from turtle import Turtle, Screen
import pandas as pd
import os

PATH = os.path.abspath(os.path.dirname(__file__))
IMG = PATH + "/binhThuan_map.gif"
DATA = pd.read_csv(PATH+"/10_huyen.csv")
DS_HUYEN = DATA['state'].to_list()
is_running = True


def get_mouse_click_coor(x, y):
    print(x, y)


def print_in_screen(answer, DATA):
    text = Turtle()
    text.penup()
    text.hideturtle()
    text.color("red")
    state_data = DATA[DATA.state == answer]
    text.goto(float(state_data.x), float(state_data.y))
    # chỉ hiện thị giá trị state chứ ko hiển thị các thông tin phụ
    text.write(state_data.state.item())


screen = Screen()
screen.setup(width=700, height=500)
screen.title("Đoán tên 10 Huyện tỉnh Bình Thuận")
# thêm loại shape vào trong screen
screen.addshape(IMG)

turtle = Turtle()

# thay đổi con trở thành hình img đã chọn
turtle.shape(IMG)
# hàm này trả về giá trị x, y khi click có thể tận dụng để hiển thị giá trị khi click chuột
# screen.onscreenclick(get_mouse_click_coor)
answer_states = []

while len(answer_states) < len(DS_HUYEN):
    # nhập câu trả lời
    answer = screen.textinput(title=f"{len(answer_states)}/10 huyện đúng",
                              prompt="Nhập tên một huyện:").title()
    if answer == "Exit":
        missing_state = [
            huyen for huyen in DS_HUYEN if huyen not in answer_states]
        missing_state_data = pd.DataFrame(missing_state)
        missing_state_data.to_csv(PATH+"/miss_data.csv")
        break
    # kiểm tra  câu trả lời có đúng ko
    if answer in DS_HUYEN:
        answer_states.append(answer)
        print_in_screen(answer, DATA)
    else:
        print("Trả lời sai")

# cách hiển thị mãi ko bị tắt màng hình khi click chuột
