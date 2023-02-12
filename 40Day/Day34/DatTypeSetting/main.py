
# cài đặt kiểu dữ liệu mặc định
age: int
name: str
money: float

# định kiểu dữ liệu trả về str


def check_age(age: int) -> str:

    if (age >= 18):
        return 1
    else:
        return "ko Được lái"


print(check_age(18))
