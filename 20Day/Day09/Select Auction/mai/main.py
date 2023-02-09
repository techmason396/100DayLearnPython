import art
import os


def start():
    listAuction = []
    run = True
    while run:
        name = input("what is your name?: ")
        price = input("what is your bid?: $")
        listAuction.append({"name": name, "price": price})
        moreAuction = input(
            "Are there any other bidders? Type 'yes' or 'no' : ")
        if moreAuction != "yes":
            # show result
            winnerAuction = findWinner(listAuction)
            print(
                f"The winner is {winnerAuction['name']} with a bid of ${winnerAuction['price']}")
            return
        os.system('cls' if os.name == 'nt' else 'clear')


def findWinner(listAuction):
    winnerAuction = listAuction[0]
    for auction in listAuction:
        if winnerAuction["price"] < auction["price"]:
            winnerAuction = auction
    return winnerAuction


print(art.logo)
start()
