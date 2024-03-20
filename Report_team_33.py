def encode (password):
    list = []
    # creates a list of the characters in the password
    for i, item in enumerate(password):
        list.append(password[i])
    # increments the digits by 3
    for i, item in enumerate(list):
        list[i] = int(item)
        list[i] += 3
    encoded_password = ''
    # packages the digits back into a string
    for item in list:
        encoded_password += str(item)
    return encoded_password


def decode(password):
    pass


def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")


if __name__ == '__main__':
    cnt = True
    # while cnt is true will run the option menu until quit is selected
    while True:
        menu()
        print()
        option = int(input('Please enter an option: '))
        if option == 1:
            password = input("Please enter your password to encode: ")
            password = encode(password)
            print("Your password has been encoded and stored!")
            print()
            continue
        elif option == 2:
            decoded_password = decode(password)
            print(f"The encoded password is {password}, and the original password is {decoded_password}.")
            print()
        elif option == 3:
            break





