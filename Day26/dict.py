
import random
list_name = ["Alex", "Beth", "Caroline", "Dave", "Elandor", "Freeddie"]

students_score = {name: random.randint(1, 100) for name in list_name}
print(students_score)

# cách sử dụng tùy chọn in key hoặc value
for (key, value) in students_score.items():
    pass

students_pass = {student_key: student_value for (
    student_key, student_value) in students_score.items() if student_value >= 50}
print(students_pass)
