import smtplib
import datetime as dt
import random

my_email = "techmason396@gmail.com"
my_password = "ozpmkdjlwcvewmjl"


def send_email(text):
    # nhập smpt của nhà cung cấp e mail ở đây là cả gmail
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        # bật bảo mật cho email giúp kết nối an toàn
        connection.starttls()
        # kết nối với gmail
        connection.login(user=my_email, password=my_password)
        # gửi mail đến địa chỉ
        # thêm encode('utf-8') để gửi nội dung bằng tiếng việt
        # thêm tiêu đề thì sử dụng Subject, xuống dòng thì sử dụng \n
        # text = "Subject: Thử gửi email bằng tiếng việt \n Đây là nội dung email".encode('utf-8')
        connection.sendmail(from_addr=my_email,
                            to_addrs="idml3011932021@gmail.com", msg=text)


now = dt.datetime.now()
# lấy ngày trong tuần
weekday = now.weekday()
if weekday == 5:
    with open("./quotes.txt", "r") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    subject = "Good idea \n"
    text = f"Subject: {subject}{quote}"
    send_email(text)
