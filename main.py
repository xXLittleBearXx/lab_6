# Ethan Davis

def encode(password):
    """Encoding a password by incrementing each value by 3"""
    encoded_password = ""  # An empty string to be added to

    for num in password:
        encoded_num = (int(num) + 3) % 10  # Using % 10 to wrap numbers greater than 9
        encoded_password += str(encoded_num)

    return encoded_password


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
            print("Your password has been encoded and stored!")

        elif menu_selection == 2:  # Decode a password
            print(f"The encoded password is {encoded_password}, and "
                  f"the original password is {decoded(encoded_password)}.")

        elif menu_selection == 3:  # Quit the program
            break


if __name__ == "__main__":
    main()
