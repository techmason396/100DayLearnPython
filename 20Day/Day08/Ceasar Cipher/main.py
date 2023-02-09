import art
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def ceasar(direction, text, shift):
    text_result = ""
    default_shift = 5
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = position + shift
                if new_position not in alphabet:
                    new_position = position + default_shift
            else:
                new_position = position - shift
                if new_position not in alphabet:
                    new_position = position - default_shift
            text_result += alphabet[new_position]
        else:
            text_result += letter
    return text_result


def start():
    run = True
    while run:
        print(art.logo)
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        text_ceasa = ceasar(direction, text, shift)
        if direction == "encode":
            print(f"Here's the encode result: {text_ceasa}")
        else:
            print(f"Here's the decode result: {text_ceasa}")
        keepCeasar = input(
            "Type 'yes' if you want to again. Otherwise type 'no'.")
        if keepCeasar == "no":
            run = False
            print("Good bye!")


start()
