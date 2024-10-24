# Cade's lab

def encode(password):
    encoded = ''.join(str((int(digit) + 3) % 10) for digit in password)
    return encoded

def decode(password):
    decoded = ""
    while password != "":
      decoded = decoded + str((int(password[0:1]) + 7) % 10)
      password = password[1:]

    return decoded 

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
        elif option == '2':
           original_password = decode(encoded_password)
           print("The encoded password is " + encoded_password + ", and the original password is " + original_password + ".")
        elif option == '3':
            break

if __name__ == "__main__":
    main()

