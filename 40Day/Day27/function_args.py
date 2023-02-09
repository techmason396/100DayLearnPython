# sử dụng *args giống như toán tử ... của JS
def add(*args):
    sum_result = 0
    for n in args:
        sum_result += n
    print(sum_result)


add(1, 2, 3)

# sử dụng **kwargs để tạo các phương thức bên trong một function
# kwargs là một dict cho nên có thể sử dụng các phương thức dict thao tcs


def calculate(n, **kwargs):
    kq_cong = kwargs["cong"] + n
    kq_nhan = kwargs["nhan"] * n
    print(kq_cong, kq_nhan)


class Car:
    # cách cài đặt để nhận nhiều tham số
    def __init__(self, **kw):
        # sử dụng get thay cho kw["attribute"] vì get ko tồn tại trong dict
        # nó chỉ tồn tai khi ta gọi còn ko có thì sẽ trả về null
        self.name = kw.get("name")
        self.model = kw.get("model")
        self.model = kw.get("color")


nissan = Car(name="Nissan", model="PH200")

print(nissan.name)
print(nissan.model)
