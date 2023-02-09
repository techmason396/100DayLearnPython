from tkinter import *
import math
# ---------------- CONSTANS ------------------------------#
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
DELAY = 1000  # milies second
# ----------------- TIME RESET -----------------------------#


def reset_time():
    global reps
    reps = 0
    # hủy bỏ hoạt động đếm ngược thời gian
    windown.after_cancel(timer)
    label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check_marks.config(text="")


# ----------------- TIME MECHANISM ------------------------#


def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        label.config(text="Work", fg=GREEN)
        # ----------------- COUNTDOWN MECHANISM -------------------#


def display_timers(count):
    hours = math.floor(count / 60)
    seconds = count % 60
    if hours < 10:
        hours = f"0{hours}"
    if seconds < 10:
        seconds = f"0{seconds}"
    return f"{hours}:{seconds}"


def count_down(count):
    text_timer = display_timers(count)
    canvas.itemconfig(timer_text, text=text_timer)
    # sau mỗi 1s thì gọi hàm count_down (hiển thị count và trừ count đi 1)
    if count > 0:
        global timer
        timer = windown.after(DELAY, count_down, count-1)
    else:
        start_timer()
        marks = ""
        work_finish = math.floor(reps/2)
        for index in range(work_finish):
            marks += "✔"
        check_marks.config(text=marks)


# ----------------- UI SETUP -----------------------------#
windown = Tk()
windown.title("Pomodoro")
windown.config(padx=100, pady=50, bg=YELLOW)

# tạo babel
# fg chỉnh màu của label
label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, "bold"), bg=YELLOW)
label.grid(row=0, column=1)

# canvas sử dụng để thêm hình ảnh và các thành phần hiển thị xếp chồng lên nhau
# highlightthickness chỉnh độ đậm đường viền của canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

tomato_img = PhotoImage(file="tomato.png")

# thêm hình ảnh trong window
canvas.create_image(100, 112, image=tomato_img)

# thêm text trong canvas
# x, y xác đị vị trí text
# text thêm nội dung chữ
# fill thêm màu sắc cho chữ
timer_text = canvas.create_text(103, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))


canvas.grid(row=1, column=1)

btn_start = Button(text="Start", highlightthickness=0, command=start_timer)
btn_start.config(padx=10, pady=5)
btn_start.grid(row=2, column=0)

btn_reset = Button(text="Reset", command=reset_time)
btn_reset.config(padx=10, pady=5)
btn_reset.grid(row=2, column=2)

check_marks = Label(text="", font=(FONT_NAME, 15),
                    bg=YELLOW, fg=GREEN)
check_marks.grid(row=3, column=1)


windown.mainloop()
