import os
import pandas as pd

PATH_DATA_FILE = os.path.abspath(
    os.path.dirname(__file__))

data = pd.read_csv(PATH_DATA_FILE + "/weather_data.csv")  # đọc file csv
data_dict = data.to_dict()  # chuyển dữ liệu  về dạng dict (object)

# tính dữ liệu trung bình của một cột
# cách 1
temp_list = data['temp'].to_list()  # chuyễn dữ liệu về dạn list (array)
avg_temp = sum(temp_list) / len(temp_list)

# cách 2 sử dụng pandas
avg_temp2 = data.temp.mean()

# tìm giá trị lớn nhất
# cách 1
max_temp = max(temp_list)

# cách 2 sử dụng dữ liệu trưc tiếp pandas
max_temp_pd = data['temp'].max()

# lấy dữ liệu từ cột vd cột temp
temp_list = data.temp

# lấy dữ liệu từ dòng vd lấy dòng dữ liệu ngày monday
monday = data[data.day == "Monday"]

# lấy dữ liệu từ dòng có ngày nhiệt độ lớn nhất
day_max_temp = data[data.temp == data.temp.max()]
day_max_temp_F = (day_max_temp.temp * (9/5)) + 32

# lấy một giá trị của một dòng
monday_condition = monday.condition

# chuyển độ c sang độ f ct (độ c * 9/5) + 32
monday_temp_F = (monday.temp * (9/5)) + 32

# tạo khung dữ liệu
data_dict = {
    "Day max temp: ": day_max_temp.day,
    "temp": day_max_temp.temp,
    "temp_F": day_max_temp_F,
    "condition": day_max_temp.condition
}

# chuyển dữ dữ liệu dict sang data Frame
max_day_data = pd.DataFrame(data_dict)
# print(max_day_data)

# lưu dữ liệu thành file csv
max_day_data.to_csv(PATH_DATA_FILE+"/max_day_temp.csv")

# test create dataFrame

data_dict_test_2 = {
    "Tên": ["Trung", "Vui", "Quang"],
    "Tuổi": [31, 28, 1],
    "Địa chỉ": ["Tuy Phong", "Hàm Thắng", "Hàm Thắng"],
    "Vai vế": ["Cha", "Mẹ", "Con"]
}

my_family = pd.DataFrame(data_dict_test_2)
print(my_family)
my_family.to_csv(PATH_DATA_FILE+"/my_family_2023.csv")
