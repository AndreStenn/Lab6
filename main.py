def encode(password):
    passwordlist = list(str(password))
    newpass = ""
    for i in range(len(passwordlist)):
        passwordlist[i] = int(passwordlist[i]) + 3
        newpass += str(passwordlist[i])
    return newpass

def decode(password_to_decode):
    original_password_to_decode = password_to_decode
    password_to_encode = list(str(password_to_decode))
    decoded_password = ""

    for i in range(len(password_to_encode)):
        decoded_password += (str(int(password_to_decode[i]) + 3))

    return decoded_password

def main():
    StoredP = ""
    menuOP = 0
    while menuOP != 3:
        print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
        menuOP = input("Please enter an Option:")
        if int(menuOP) == 1:
            StoredP = input("Please enter your password to encode:")
            StoredP = encode(StoredP)
            print("Your password has been encoded and stored!")
        if int(menuOP) == 2:
            print(f"The encoded password is {StoredP}, and the original password is {decode(StoredP)}.")
            StoredP = decode(StoredP)
        if int(menuOP) == 3:
            break

