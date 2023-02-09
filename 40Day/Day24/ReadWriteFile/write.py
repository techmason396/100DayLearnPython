import os

# mode="w" (write) tạo một file mới và thêm nôi dung.
# mode="a" (append) dựa vào file đã tồn tại tạo một nội dung phía sau
# encoding="utf-8" ghi được tiếng việt

with open('data1.txt', mode="w", encoding="utf-8") as file:
    file.write("Xin chào tôi tên là Nguyễn Thành Trung")
