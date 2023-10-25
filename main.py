def encode(password):
    passwordlist = list(str(password))
    newpass = ""
    for i in range(len(passwordlist)):
        passwordlist[i] = int(passwordlist[i]) + 3
        newpass += str(passwordlist[i])
    return newpass

def decode(password):
    pass

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

