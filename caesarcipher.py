
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
# text = input("Type the message: \n").lower()
# shift = int(input("type the shift number: \n"))


#example dave => d =3 + 4
def encrypt(original_text, shift_amount):
    encrypted = ""
    for char in original_text:
        if char in alphabet:
            new_position = alphabet.index(char) + shift_amount
            new_position %= 26
            encrypted += alphabet[new_position]
        else:
            encrypted += char

    print(f"here is the decoded result: {encrypted}")


def decrypt(original_text, shift_amount):
    decrypted = ""
    for char in original_text:
        if char in alphabet:
            new_position = alphabet.index(char) - shift_amount
            new_position %= 26
            decrypted += alphabet[new_position]
        else:
            decrypted += char

    print(f"here is the decoded result: {decrypted}")



def caesar(original_text, shift_amount, encode_or_decode):
    encrypted = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for char in original_text:

        if char in alphabet:

            new_position = alphabet.index(char) + shift_amount
            new_position %= 26
            encrypted += alphabet[new_position]
        else:
            encrypted += char
    print(f"here is the {encode_or_decode}d result: {encrypted}")





check = True

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type the message: \n").lower()
    shift = int(input("type the shift number: \n"))

    caesar(text, shift, direction)
    text_loop = input("Type 'yes' if you want to go again. Otherwise type 'no': \n").lower()

    if text_loop == "no":
        check = False
        print("GoodBye")