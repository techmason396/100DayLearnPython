import data_resources


def run_machine_coffee():
    menu = data_resources.MENU
    profit = data_resources.profit
    resources = data_resources.resources

    is_on = True
    while is_on:
        choice = input("What would you like? (espresso/latte/cappuccino):")
        if choice == "off":
            is_on = False
        elif choice == "report":
            show_report(resources, profit)
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            enought_resources = check_resources(choice, resources, menu)
            if enought_resources:
                create_coffe(choice, resources, menu)


def show_report(resources, profit):
    for resource in resources:
        print(f"{resource} : {resources[resource]}")
    print(f"Money: {profit}")


def check_resources(choice, resources, menu):
    ingredients = menu[choice]['ingredients']
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(
                f'Sorry there is not enough {ingredient} : {resources[ingredient]}')
            return False
    return True


def create_coffe(choice, resources, menu):
    print(choice, resources, menu)


run_machine_coffee()
