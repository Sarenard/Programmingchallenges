import sys

#ceasar encryption
def encrypt(text,s):
    result = ""
    for i in text:
        if i.isupper():
            result += chr((ord(i) + s-65) % 26 + 65)
        else:
            result += chr((ord(i) + s-97) % 26 + 97)
    return result
def decrypt(text,s):
    result = ""
    for i in text:
        if i.isupper():
            result += chr((ord(i) - s-65) % 26 + 65)
        else:
            result += chr((ord(i) - s-97) % 26 + 97)
    return result
print("Caesar Cipher")
print("1. Encrypt")
print("2. Decrypt")
print("3. Exit")
print("Enter your choice: ", end="")
choice = int(input())
match choice:
    case 1:
        print(encrypt(input("texte >>> "),int(input("clé >>> "))))
    case 2:
        print(decrypt(input("texte >>> "),int(input("clé >>> "))))
    case 3:
        sys.exit()