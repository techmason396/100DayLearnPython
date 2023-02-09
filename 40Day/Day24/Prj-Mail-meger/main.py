import os

PATH_INPUT = os.path.abspath(os.path.dirname(__file__))+"/Input/"
PATH_OUTPUT = os.path.abspath(os.path.dirname(__file__))+"/Output/"
PLACEHOLDER = "[name]"
print(os.path.exists(PATH_OUTPUT))

with open(PATH_INPUT + "Names/invited_names.txt") as file_names:
    # readlines đọc file và chuyển các dữ liệu vào một mảng
    names = file_names.readlines()

with open(PATH_INPUT + "/Letters/starting_letter.txt") as letter_file:
    letter = letter_file.read()  # loaị bỏ khoảng trắng hoặc dấu xuống dòng
    for name in names:
        name = name.strip()
        new_letter = letter.replace(PLACEHOLDER, name)
        with open(PATH_OUTPUT + f"/ReadyToSend/letter_for_{name}.txt", "w") as file:
            file.write(new_letter)
