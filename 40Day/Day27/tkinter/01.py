import tkinter
from tkinter import *

# FUNCTION


def button_click():
    # lấy dữ liệu từ input và thực thi
    new_text = input.get()
    my_label["text"] = new_text


window = tkinter.Tk()

# thiết lập tiêu đề cho giao diện
window.title("Hello đây là chương trình GUI python đầu tiên")

# thiết lập độ rộng của giao diện
window.minsize(width=600, height=300)

# thiết lập nhãn (label)
# vd thiết lập text, sử dụng font hack độ lớn 24px và font-weight bold
my_label = tkinter.Label(text="Đây là nhãn", font=("hack", 24, "bold"))

# thiết lập cách thức hiển thị label
# hiển thị chính giữa và canh giữa
# side  - căn chỉnh vị trí của text
# expand  - True or False : nhãn có chiều cao lớn bằng giao diện
my_label.pack()

# những cách thay đổi chữ laybel
my_label["text"] = "dòng chữ update I"
my_label.config(text="dòng chữ  update II")

# tạo input nhập dữ liêu vào
# width cài đặt chiều rộng
input = Entry(width=30)
# thêm kiểu text mặc định vào trong input,
input.insert(END, string="Xin chào")
# lấy dữ liệu nhập từ file input
content = input.get()
input.pack()

# tạo ra khu vực để nhập dữ liệu giống như texarea
text_area = Text(height=5, width=30)
# chuột mặc định insert vào text area
text_area.focus()
text_area.insert(END, "Nhập văn bản vào đây...")
# lấy  giá trị nhập vào của text
print(text_area.get("1.0", END))
# thiết lập hiển thị
text_area.pack()


# tạo nút bấm
# text = chữ hiển thị button
# command = gọi thực thi function khác vào class button
button = Button(text="click me", command=button_click)
# lưu ý các đối tượng thêm vào cần xác định cách nó hiển thị qua hàm .pack()
button.pack()


def spinbox_used():
    # lấy dữ liệu spinbox
    print(spinbox.get())


def scale_used(value):
    # lấy dữ liệu scale
    print(value)


def checkbox_used():
    # lấy dữ liệu của checkbox
    print(check_state.get())


def radio_button_used():
    # lấy dữ liệu của checkbox
    print(radio_state.get())


def lisbox_used(event):
    print(lisbox.curselection())


    # Spinbox
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

# Scale
scale = Scale(from_=0, to=10, command=scale_used)
scale.pack()

# checkbox
# tạo kiểu dữ liêu giá trị 0 hoặc 1
check_state = IntVar()
checkbox = Checkbutton(
    text="Is On?", variable=check_state, command=checkbox_used)

# radio-button
radio_state = IntVar()
radio_button_1 = Radiobutton(text="Option1", value=1,
                             variable=radio_state, command=radio_button_used)
radio_button_2 = Radiobutton(text="Option2", value=2,
                             variable=radio_state, command=radio_button_used)
radio_button_1.pack()
radio_button_2.pack()

# list-box
lisbox = Listbox(height=3)
family = ["Trung", "Vui", "Quang"]
for member in family:
    lisbox.insert(family.index(member), member)
lisbox.bind("<<Chọn thành viên gia đình>>", lisbox_used)
lisbox.pack()

window.mainloop()
