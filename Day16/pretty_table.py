
from prettytable import PrettyTable
x = PrettyTable()
# x.field_names = ["Tên", "Tuổi", "năm sinh", "địa chỉ"]
# x.add_row = ["Trung", 31, 1992, "Tuy Phong"]
# x.add_row = ["Vui", 28, 1996, "Hàm Thắng"]
# x.add_row = ["Nhân", 1, 2023, "Hàm Thắng"]
x.field_names = ["Name", "Age", "Birth Year", "Address"]
x.add_rows(
    [
        ["Trung", 31, 1992, "Tuy Phong"],
        ["Vui", 28, 1996, "Ham Thang"],
        ["Nhan", 1, 2023, "Ham Thang"],
    ]
)
print(x.get_string())
