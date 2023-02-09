import tkinter
from tkinter import *


def button_used():
    print(input.get())


window = Tk()
window.title("Tkinter bài 2")
window.minsize(width=500, height=300)
# thêm khoản đệm từ viền đến các nội dung bên trong
window.config(padx=20, pady=30)

label = Label(text="Đây là label", font=("hack", 18, "bold"))
label.config(text="bắt đầu bài 2")
label.grid(column=0, row=0)
# thêm viền phần từ label, các phần tử khác thì tương tự
label.config(padx=20, pady=30)


button = Button(text="Xác nhận", command=button_used)
button.grid(column=1, row=1)

new_botton = Button(text="Xác nhận 2")
new_botton.grid(column=2, row=0)

input = Entry(width=20)
input.insert(END, string="Tên: ")
input.grid(column=3, row=2)


window.mainloop()

# các loại chia bố cục hiển thị
# .pack() định vị các đối tượng theo hàng dọc (từ trên xuống, hoặc từ trái qua phải..)
# .place(x, y) định vị các đối tượng theo tọa độ x, y
# .grid(columns, row)
