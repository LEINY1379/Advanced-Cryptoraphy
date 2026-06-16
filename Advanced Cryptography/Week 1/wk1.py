from cryptography.fernet import Fernet

# Generating a key
key = Fernet.generate_key
cipher = Fernet(key)

# message
message = "First encrypted message"

# encrypting the message
encrypted = cipher.encrypt(message)
print("Encrypted: {encrypted}")

# decrypting the message
decrypt = cipher.decrypt(encrypted)
print("Decrypted: {decrypted.decode()}")