# Ethan Davis

def encode(password):
    """Encoding a password by incrementing each value by 3"""
    encoded_password = ""  # An empty string to be added to

    for num in password:
        encoded_num = (int(num) + 3) % 10  # Using % 10 to wrap numbers greater than 9
        encoded_password += str(encoded_num)

    return encoded_password


def decode(password):
    """Decoding a password by decrementing each value by 3"""
    decoded_password = ""  # An empty string representing what will be the decoded_password; a new string object is necessary to return a decoded password without modifying password itself.

    for num in password:
        inner_num = int(num)  # int(...) ensures num, and by extension inner_num, is numeric.
        if (inner_num - 3 < 0):  # As an "inverse" to % 10, if subtraction by the value (three in this case) yields a value below 0, add 10 so the resulting digit is within 0-9.
            inner_num += 10
        decoded_num = (inner_num - 3)  # The opposite operation of the encode (+3) is -3. This shift decodes the number...
        decoded_password += str(decoded_num)  # ...which can then be concatenated to decoded_password.

    return decoded_password

def main():

    menu_selection = 1

    while menu_selection != 3:

        # Displaying the selection menu
        print("Menu\n"
              "-------------\n"
              "1. Encode\n"
              "2. Decode\n"
              "3. Quit\n")

        menu_selection = int(input("Please enter an option: "))

        if menu_selection == 1:  # Encode a password
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!\n")

        elif menu_selection == 2:  # Decode a password
            print(f"The encoded password is {encoded_password}, and "
                  f"the original password is {decode(encoded_password)}.\n")

        elif menu_selection == 3:  # Quit the program
            break


if __name__ == "__main__":
    main()
