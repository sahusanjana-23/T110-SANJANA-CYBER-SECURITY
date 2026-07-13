# Monoalphabetic Cipher - CLI

plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"


def encrypt(message):
    result = ""

    for ch in message.upper():
        if ch in plain:
            index = plain.index(ch)
            result += cipher[index]
        else:
            result += ch

    return result


def decrypt(message):
    result = ""

    for ch in message.upper():
        if ch in cipher:
            index = cipher.index(ch)
            result += plain[index]
        else:
            result += ch

    return result


while True:
    print("\n===== Monoalphabetic Cipher =====")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        msg = input("Enter Message: ")
        print("Encrypted Message:", encrypt(msg))

    elif choice == "2":
        msg = input("Enter Cipher Text: ")
        print("Decrypted Message:", decrypt(msg))

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!")