import random
import pic

listWorld = ["cao", "to", "thanh", "minh", "phong", "trung", "vui"]

keyWorld = random.choice(listWorld)
display = []

for letter in keyWorld:
    display.append(" _ ")

end_of_game = False
live = 6

while not end_of_game:
    print("".join(display))
    print(pic.stages[live])
    letter_chose = input("Hãy chọn một chữ cái: ").lower()
    if letter_chose in keyWorld:
        for position in range(len(keyWorld)):
            if keyWorld[position] == letter_chose:
                display[position] = letter_chose
    else:
        live -= 1
    if " _ " not in display:
        print("".join(display))
        print("You Win")
        end_of_game = True
    elif live == 0:
        print("".join(display))
        print(pic.stages[live])
        print("You Lose")
        end_of_game = True
