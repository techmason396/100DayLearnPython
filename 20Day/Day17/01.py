class User:
    def __init__(self, id, name, age, address):
        self.id = id
        self.name = name
        self.age = age
        self.address = address
        self.followers = 0
        self.following = 0

    def increase_follow(self, user):
        user.followers += 1
        self.following += 1


trung = User("id01", "Nguyen Thanh Trung", 31, "Tuy Phong")
vui = User("id02", "Bui Thi Vui", 28, "Ham Thang")

vui.increase_follow(trung)

print(f"vui dang theo doi: {vui.following} nguoi")
print(f"trung dang co : {trung.followers} nguoi theo doi")
