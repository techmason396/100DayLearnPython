import pandas

students_dic = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

data = pandas.DataFrame(students_dic)

# loop in padas (index là số thứ tự của dòng, row là nội dung của dòng)
for (index, row) in data.iterrows():
    print(row)

# chỉ lấy giá trị điểm của 1 dòng
for (index, row) in data.iterrows():
    print(row.score)
