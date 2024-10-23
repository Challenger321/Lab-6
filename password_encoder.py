# Cade's lab

def encode(password):
    encoded = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        option = input("Please enter an option: ")
       
        if option == '1':
            password = input("Please enter your password to encode: ")
            if len(password) == 8 and password.isdigit():
                encoded_password = encode(password)
                print("Your password has been encoded and stored!")
            else:
                print("Please enter an 8-digit numeric password.")
        elif option == '3':
            break

if __name__ == "__main__":
    main()

