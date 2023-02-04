
# cách 1 read file - nhược điểm phải nhớ đóng file (file.close())
file = open('data.txt')
contents = file.read()
file.close()
print(contents)

# cách 2 ko cần nhớ đóng fil
with open('data.txt') as file:
    contents2 = file.read()
    print(contents2)
