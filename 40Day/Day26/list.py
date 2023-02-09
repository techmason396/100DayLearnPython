list = [1, 2, 3]
new_list_basic = []
for numb in list:
    new_list_basic.append(numb * 2)
print(new_list_basic)

# cách viết rút ngọn của việc tạo mảng mới
new_list = [num * 2 for num in list]

name = "trung"
letters = [letter for letter in name]

list_name = ["Alex", "Beth", "Caroline", "Dave", "Elandor", "Freeddie"]

# lấy danh sách các tên có 4 kí tự
four_letter_name = [name for name in list_name if len(name) <= 4]

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [number for number in numbers if number % 2 == 0]
