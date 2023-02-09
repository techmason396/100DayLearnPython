import tkinter
from tkinter import *


window = Tk()
window.config(width=300, height=200)
window.title("Đổi từ Km sang Dặm")
window.config(padx=20, pady=20)

input_km = Entry(width=5)
input_km.grid(row=0, column=1)

label_input_km = Label(text="Km")
label_input_km.grid(row=0, column=2)

label_result = Label(text="gần bằng")
label_result.grid(row=1, column=0)

label_Dam = Label(text="0")
label_Dam.grid(row=1, column=1)

label_don_vi = Label(text="Dặm")
label_don_vi.grid(row=1, column=2)


def doi_km_sang_dam():
    km = float(input_km.get())
    dam = round(km * 0.62137, 1)
    label_Dam.config(text=dam)


button_cal = Button(text="Đổi kết quả", command=doi_km_sang_dam)
button_cal.grid(column=1, row=2)

window.mainloop()
