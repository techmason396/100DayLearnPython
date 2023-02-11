import datetime as dt
import smtplib
import pandas as pd
import random

##################### Extra Hard Starting Project ######################
# 2. Check if today matches a birthday in the birthdays.csv

my_email = "techmason396@gmail.com"
my_password = "ozpmkdjlwcvewmjl"


def get_list_birthdays():
    try:
        with open("./birthdays.csv") as birthday_file:
            all_birthday = pd.read_csv(birthday_file)

            # chuyển giá trị ngày, tháng sang kiểu dữ liệu int
            all_birthday['day'] = all_birthday['day'].astype(int)
            all_birthday['month'] = all_birthday['month'].astype(int)
            all_birthday = all_birthday.to_dict()
            return all_birthday
    except FileNotFoundError:
        print("File not found!")


def check_date(date, dict):
    for (key, value) in dict.items():
        if date == value:
            return key
    return None


def read_letter(num):
    try:
        with open(f"./letter_templates/letter_{num}.txt", "r") as letter_file:
            return letter_file.readlines()
    except FileNotFoundError:
        print("File not found!")


def write_letter(index, dict_birthday):
    num_letter = random.randint(1, 3)

    name = dict_birthday['name'][index]
    letter = read_letter(num_letter)
    letter[0] = letter[0].replace('[NAME]', name)
    letter = "".join(letter)
    return letter


def send_email(index, letter, dict_birthday):
    to_email = dict_birthday['email'][index]
    letter = "Subject: Happy Birth Day!\n" + letter
    # nhập smpt của nhà cung cấp e mail ở đây là cả gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # bật bảo mật cho email giúp kết nối an toàn
        connection.starttls()
        # kết nối với gmail
        connection.login(user=my_email, password=my_password)
        # gửi mail đến địa chỉ
        # thêm tiêu đề thì sử dụng Subject, xuống dòng thì sử dụng \n
        connection.sendmail(from_addr=my_email,
                            to_addrs=to_email, msg=letter)


now = dt.datetime.now()
day = now.day
month = now.month

all_birthday = get_list_birthdays()

if check_date(day, all_birthday['day']) != None and check_date(month, all_birthday['month']) != None:
    index_person = check_date(day, all_birthday['day'])
    # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    letter = write_letter(index_person, all_birthday)
    # 4. Send the letter generated in step 3 to that person's email address.
    send_email(index_person, letter, all_birthday)
