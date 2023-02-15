import requests
import datetime as dt

USERNAME = "trungidml"
TOKEN = "trungvuiquang199319962024"

# TẠO TÀI KHOẢNG PIXELA
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# resonse = requests.post(url=pixela_endpoint, json=parameters)
# resonse.raise_for_status()
# print(resonse.text)
# connect https://pixe.la/@trungidml

# TẠO MỘT BẢNG
graph_config = {
    "id": "gidml001",
    "name": "Count Push Up",
    "unit": "time",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/"


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# connect get graph https://pixe.la/v1/users/trungidml/graphs/gidml001

# THÊM PIXEL VÀO BẢNG
now = dt.datetime.now()

# lấy định dạng ngày yyymmdd
today = now.strftime("%Y%m%d")

pixel_endpoint = graph_endpoint+graph_config['id']
pixel_config = {
    'date': today,
    'quantity': "20",
}
# res = requests.post(url=pixel_endpoint, headers=headers, json=pixel_config
# connect https://pixe.la/v1/users/trungidml/graphs/gidml001.html

# SỬ ĐỔI PIXEL
day_update = today
pixel_update_endpoint = pixel_endpoint+f"/{day_update}"
pixel_update_config = {
    'quantity': "25"
}
res = requests.put(url=pixel_update_endpoint,
                   headers=headers, json=pixel_update_config)
print(res.text)
