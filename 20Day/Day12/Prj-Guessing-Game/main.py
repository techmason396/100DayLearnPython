import random
# easy level 10 times
# hard level 5 times


def guessing_game():
    play_again = True
    print("Welcome to the Number Guessing Game!")
    while play_again:
        attempts = 10
        number_thinking = random.randint(0, 100)
        print(number_thinking)
        print("I'm thinking of a number between 1 and 100.")
        if input("Choose a difficulty. Type 'easy' or 'hard': ") == 'hard':
            attempts = 5
        while True:
            if attempts == 0:
                print("You're run out of guesses, you lose")
                break
            print(
                f"You have {attempts} attempts remaining to guess the number.")
            guess = int(input("Make a guess:"))
            if (guess == number_thinking):
                print(f"You Win!, Number thinking is {number_thinking}")
                break
            elif guess > number_thinking:
                print("Too high. \nGuess again.")
                attempts -= 1
            else:
                print("Too low. \nGuess again.")
                attempts -= 1
        if input("Play again? Type 'y' to play again, Type 'n' to exit: ") != 'y':
            play_again = False
            print("GoodByle!")


guessing_game()
