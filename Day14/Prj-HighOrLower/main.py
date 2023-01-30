import data_game
import random
import art
import os


def higher_lower_game():
    data = data_game.data
    play_again = True
    while play_again:
        score = 0
        while True:
            print(art.logo)
            question_a = random.choice(data)
            question_b = random.choice(data)
            if score != 0:
                print(f"You're right! Current score: {score}")
            print(
                f"Compare A:{question_a['name']}, a {question_a['description']}, from {question_a['country']}")
            print(art.vs)
            print(
                f"Compare B:{question_b['name']}, a {question_b['description']}, from {question_b['country']}")
            choice = input("Who has more follower? Type 'A' or 'B': ").lower()

            # so sánh kết quả chọn với kết quả cuối cùng
            if choice == compare(question_a['follower_count'], question_b['follower_count']):
                score += 1
                os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(f"Sorry, that's wrong. Final score: {score}")
                break
        if input("Do you want to play again? type 'y' to play again, type 'n' to exits: ") != 'y':
            play_again = False
            print("GooldBye!")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')


def compare(a, b):
    if a > b:
        return 'a'
    else:
        return 'b'


higher_lower_game()
