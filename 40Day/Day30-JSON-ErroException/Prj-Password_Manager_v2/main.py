from tkinter import *
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():
    # num_char[0] = num_text, num_char[1] = num_number, num_char[2] = num_symbol
    n_str = random.randint(8, 10)
    n_number = random.randint(1, 4)
    n_symbol = random.randint(1, 2)

    str = [random.choice(letters) for num in range(0, n_str)]
    number = [random.choice(numbers) for num in range(0, n_number)]
    symbol = [random.choice(symbols) for num in range(0, n_symbol)]
    password = sum([str, number, symbol], [])
    random.shuffle(password)
    password = "".join(password)
    input_password.delete(0, END)
    input_password.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = input_website.get()
    username_email = input_username_email.get()
    password = input_password.get()
    data = {
        website: {
            "email": username_email,
            "password": password
        }
    }

    is_accept = messagebox.askokcancel(
        title="Do you want to save!", message=f"Website: {website}\nUsername/Email: {username_email}\nPassword: {password}")
    if is_accept:
        try:
            with open("./data.json", "r") as data_file:
                # cách updata data
                # đầu tiên đọc file data
                new_data = json.load(data_file)
        except FileNotFoundError:
            with open("./data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        else:
            # sau đó cập nhật data
            new_data.update(data)
            # ghi dự liệu mới vào file
            with open("./data.json", "w") as data_file:
                # indent = 4 thêm thụt đầu dòng
                json.dump(new_data, data_file, indent=4)
        finally:
            # xóa input
            input_website.delete(0, END)
            input_password.delete(0, END)

    else:
        return

# ---------------------------- SEARCH PASSWORD ------------------------ #


def get_data():
    try:
        with open("./data.json", "r") as file_data:
            return json.load(file_data)
    except FileNotFoundError:
        return None


def search_password():
    key_word = input_website.get()
    data = get_data()
    try:
        data_password = data[key_word]
        messagebox.showinfo(
            title=key_word, message=f"Email: {data_password['email']}\nPassword: {data_password['password']}")
    except KeyError:
        messagebox.showinfo(title=key_word, message="Not found!")


# ---------------------------- UI SETUP ------------------------------- #
windown = Tk()
windown.title("Password Manger")
windown.config(padx=20, pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(110, 100, image=logo_img)
canvas.grid(row=0, column=1)

# LABEL
label_website = Label(text="Website:")
label_website.grid(row=1, column=0)

label_email_username = Label(text="Email/Username")
label_email_username.grid(row=2, column=0)

label_password = Label(text="Password")
label_password.grid(row=3, column=0)

# INPUT
input_website = Entry(width=34)
input_website.grid(row=1, column=1)

input_username_email = Entry(width=53)
input_username_email.insert(0, string="trung@gmail.com")
input_username_email.grid(row=2, column=1, columnspan=2)

input_password = Entry(width=34)
input_password.grid(row=3, column=1)

# BUTTON
btn_generate_password = Button(
    text="Generate Password", command=generate_password)
btn_generate_password.grid(row=3, column=2)

btn_add = Button(text="Add", width=44, command=save_password)
btn_add.grid(row=4, column=1, columnspan=2)

btn_search = Button(text="Search", width=14, command=search_password)
btn_search.grid(row=1, column=2)

windown.mainloop()
