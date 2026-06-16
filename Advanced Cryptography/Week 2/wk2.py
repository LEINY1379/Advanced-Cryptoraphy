# Caesar cipher

def caesar_encrypt(text, shift):
    encrypted = ""

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))


            key_index += 1
        else:
            encrypted += char

    return encrypted


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Vigenere Cipher

def vigenere_encrypt(text, key):
    encrypted =""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index%len(key)]) - ord('A')

            if char.isupper():
                encrypted += chr((ord(char) - ord('A') + shift) %26 +ord('A'))
            else:
                 encrypted += chr((ord(char) - ord('a') + shift) %26 +ord('a'))

            key_index += 1
        else:
            encrypted +=char

        return encrypted
                

def vigenere_decrypt(text, key):
    decrypted = ""
    key = key.upper()
    key_index = 0

    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')

            if char.isupper():
                decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))

            key_index += 1
        else:
            decrypted += char

        
    return decrypted

# main program

print("1. Caesar Cipher")
print("2. Vigenere Cipher")

choice = input("Choose cipher (1 or 2): ")

if choice == "1":
    text = input("Enter message: ")
    shift = int(input("Enter shift value: "))

    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted,shift)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

elif choice == "2":
    text =input("Enter message: ")
    key = input("Enter key: ")

    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)

    print("Encrypted:", encrypted)
    print("Decrypted:", decrypted)

else:
    print("Invalid Choice!")
