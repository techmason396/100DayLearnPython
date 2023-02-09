import art


def add(numb1, numb2):
    return numb1 + numb2


def subtract(numb1, numb2):
    return numb1 - numb2


def multiply(numb1, numb2):
    return numb1 * numb2


def divide(numb1, numb2):
    return numb1 / numb2


# tạo object chứa các hàm  với key các phép toán tương ứng
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def start():
    runContinue = True
    print(art.logo)
    numb1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    while runContinue:
        operation_symbol = input("Pick an operation: ")
        numb2 = float(input("what's the next number?: "))
        calculator_function = operations[operation_symbol]
        result = calculator_function(numb1, numb2)
        print(f"{numb1} {operation_symbol} {numb2} = {result}")
        if input(f"Type 'y' to continue calculating with {result}, or type 'n' to exit.: ") == 'y':
            numb1 = result
        else:
            runContinue = False


start()
