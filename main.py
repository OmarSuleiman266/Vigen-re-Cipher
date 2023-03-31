# Omar Alaa El-Din Suleiman Muhammad - 19108738 - Group B

# Vigenère Cipher Encryption and Decryption

# Function to encrypt plaintext using the Vigenère cipher
def encrypt(plaintext, key):
    ciphertext = ""
    key_index = 0
    for c in plaintext:
        if c.isalpha():
            key_character = key[key_index % len(key)]
            key_index += 1
            key_shift = ord(key_character.upper()) - ord('A')
            if c.isupper():
                ciphertext += chr((ord(c) + key_shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(c) + key_shift - 97) % 26 + 97)
        else:
            ciphertext += c
    return ciphertext

# Function to decrypt ciphertext using the Vigenère cipher
def decrypt(ciphertext, key):
    plaintext = ""
    key_index = 0
    for c in ciphertext:
        if c.isalpha():
            key_character = key[key_index % len(key)]
            key_index += 1
            key_shift = ord(key_character.upper()) - ord('A')
            if c.isupper():
                plaintext += chr((ord(c) - key_shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(c) - key_shift - 97) % 26 + 97)
        else:
            plaintext += c
    return plaintext

# Main program
filename = input("Enter the name of the plaintext file: ")
with open(filename, "r") as f:
    plaintext = f.read()
key = input("Enter the encryption key: ")
ciphertext = encrypt(plaintext, key)
print("Ciphertext: ", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted text: ", decrypted_text)