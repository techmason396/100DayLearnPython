import art
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def start(cards):
    if input("Do you want to play a game Blackjack? Type 'y' or 'n': ") == 'y':
        # play game

        play_again = True
        while play_again:
            print(art.logo)
            user_cards = deal_cards(cards)
            com_cards = deal_cards(cards)
            print(f"Your cards: {user_cards}")
            print(f"Computer's first card: {com_cards[0]}")
            continue_choise = True
            while continue_choise:
                if input(f"Type 'y' to get another card, type 'n' to pass: ") == 'y':
                    user_cards.append(deal_card(cards))
                    print(f"Your cards: {user_cards}")
                else:
                    continue_choise = False
                    if count_score(com_cards) <= 10:
                        com_cards.append(deal_card(cards))
                    showResult(user_cards, com_cards)
            if input("Continue play? type 'y' continue, type 'n' to end: ") != 'y':
                play_again = False
                print("GoodBye!")
    else:
        print("GoodBye!")
        return


def deal_card(cards):
    return random.choice(cards)


def showResult(user_cards, com_cards):
    best_score = 21
    user_score = count_score(user_cards)
    com_score = count_score(com_cards)

    if user_score == com_score:
        print(
            f"User score: {user_score}, Computer score: {com_score} ==> DRAWN")
    elif user_score > com_score and user_score <= best_score:
        print(
            f"User score: {user_score}, Computer score: {com_score} ==> User Win")
    elif user_score < com_score and com_score <= best_score:
        print(
            f"User score: {user_score}, Computer score: {com_score} ==> Computer Win")
    elif user_score > best_score and com_score > best_score:
        print(
            f"User score: {user_score}, Computer score: {com_score} ==> Dealer Win")
    elif user_score > best_score:
        print(
            f"User score: {user_score}, Computer score: {com_score} ==> Computer Win")
    else:
        print(
            f"User score: {user_score}, Computer score: {com_score} ==> Computer Win")


def count_score(cards):
    total_score = 0
    for card in cards:
        total_score += card
    return total_score


def deal_cards(cards):
    cards_choice = []
    for i in range(0, 2):
        cards_choice.append(random.choice(cards))
    return cards_choice


start(cards)
