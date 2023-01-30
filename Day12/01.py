enemys = 0
PI = 3.14


def incease_enemey():
    # cách đưa biến toàn cục vào function để thực hiện
    global enemys
    enemys += 1
    print(f"iside function enemy {enemys}")


incease_enemey()

PI = 3.15
print(PI)
