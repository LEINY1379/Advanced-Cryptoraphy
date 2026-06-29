def feistel_round(left, right, round_key):

    f_output = ((right ^ round_key) * 0x5A827999) & 0xFFFFFFFFF
    new_left = right
    new_right = left ^ f_output
    return new_left, new_right

def feistel_encrypt(block, keys, rounds=16):
    left = (block >> 32) & 0xFFFFFFFFF
    right = block & 0xFFFFFFFFF

    for i in range(rounds):
        left, right = feistel_round(left, right, keys[i])

    return ((right << 32) | left) & 0xFFFFFFFFFFFFFFFF
    
def feistel_decrypt(block, keys, rounds=16):
    left = (block >>32) & 0xFFFFFFFFF
    right = block & 0xFFFFFFFFF

    for i in range (rounds -1, -1, -1):
        left, right = feistel_round(left, right, keys[i])

    return ((right << 32) | left ) & 0xFFFFFFFFFFFFFFFF
    
def generate_keys(master_key, rounds=16):
    keys = []
    for i in range (rounds):
        keys.append((master_key ^ (0x6ED9EBA1 * (i + 1))) & 0xFFFFFFFFF)
    return keys

def text_to_block(text):
    block = 0
    for i, char in enumerate(text[:8]):
        block |= (ord(char) << (8 *(7 -i)))
    return block
    
def block_to_text(block):
    text = ""
    for i in range(8):
        text += chr((block >> (8 * (7 - i))) & 0xFF)
    return text


if __name__ == "__main__":
    master_key = 0x12345678
    keys = generate_keys(master_key, rounds=16)

    plaintext = "BIT41388!"
    block = text_to_block(plaintext)
    print(f"Original Plaintext: {plaintext}")
    print(f"Plaintext Hex Block: {hex(block)}")

    encrypted = feistel_encrypt(block, keys)
    print(f"Scrambled Ciphertext: {hex(encrypted)}")

    decrypted = feistel_decrypt(encrypted, keys)
    decrypted_text = block_to_text(decrypted)

    print(f"Decrypted Hex Block: {hex(decrypted)}")
    print(f"Recoverred Text:    {decrypted_text}")
