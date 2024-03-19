def encoder (password):
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


def menu():
    print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")


cnt = True
# while cnt is true will run the option menu until option 0 is selected
while cnt == True:
    menu()
    print()
    option = int(input('Please enter an option: '))
    if option == 1:
        password = input("Please enter your password to encode: ")
        password = encoder(password)
        print("Your password has been encoded and stored!")
        print()
        continue
    elif option == 3:
        cnt = False





