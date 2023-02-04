import os
import csv  # sử dụng thư viện csv để làm việc với dữ liệu được dễ hơn

PATH_FILE = os.path.abspath(os.path.dirname(__file__))

with open(PATH_FILE+"/weather_data.csv") as file_data:
    data = csv.reader(file_data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            day = {
                "day": row[0],
                "temp": int(row[1]),
                "condition": row[2]
            }
            temperatures.append(day)
    # print(temperatures)
