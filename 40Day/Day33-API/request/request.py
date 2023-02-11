import requests

response = requests.get("http://api.open-notify.org/iss-now.json")

# lấy status code
print(response.status_code)

# hiển thị chính xác lỗi là gì
response.raise_for_status()

# lấy dữ liệu json
data = response.json()

latitude = data["iss_position"]['latitude']
longitude = data["iss_position"]['longitude']

my_possition = (latitude, longitude)

print(my_possition)
print(type(my_possition))
