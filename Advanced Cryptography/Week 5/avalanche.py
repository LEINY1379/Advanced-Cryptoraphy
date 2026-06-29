import struct
from turtle import left, right
from turtle import right

def feistel_round_function(half_block, round_key):
    half_block &= 0xFFFFFFFF  
    round_key &= 0xFFFFFFFF  

    mixed = (half_block + round_key) & 0x4519663D
    return ((mixed >> 16) ^ mixed) & 0xFFFFFFFF

def generate_keys(master_key, rounds=16):
    keys = []
    current_key = master_key
    for i in range(rounds):
        current_key = (current_key * 0x1F3D5B79+ i) & 0xFFFFFFFF
        keys.append(current_key)
    return keys

def text_to_block(text):
    text_bytes = text.encode('utf-8').ljust(8, b'\x00')[:8]
    return struct.unpack('>Q', text_bytes)[0]
    

def feistel_encrypt(block, keys):
    left = (block >> 32) & 0xFFFFFFFF
    right = block & 0xFFFFFFFF

    for key in keys:
        new_right = left ^ feistel_round_function(right, key)
        left = right
        right = new_right

    return (right << 32) | left

def bit_difference(a, b):
    xor = a ^ b
    count = 0
    while xor:
        count += xor & 1
        xor >>= 1
    return count

def demonstrate_avalanche():
    master_key = 0x12345678
    keys = generate_keys(master_key, rounds=16)

    text1 = "BIT4138A"
    block1 = text_to_block(text1)

    text2 = "BIT4138B"
    block2 = text_to_block(text2)

    print(f"=== AVALANCHE EFFECT DEMONSTRATION ===")
    print(f"Plaintext 1: {text1}, -> {hex(block1)}")
    print(f"Plaintext 2: {text2}, -> {hex(block2)}")
    print(f"Input bit difference: {bit_difference(block1, block2)}")

    ciper1 = feistel_encrypt(block1, keys)
    ciper2 = feistel_encrypt(block2, keys)

    print(f"Ciphertext 1: {hex(ciper1)}")
    print(f"Ciphertext 2: {hex(ciper2)}")

    diff = bit_difference(ciper1, ciper2)
    total_bits = 64
    percentage = (diff / total_bits) * 100

    print(f"\nOutput bit difference: {diff} out of {total_bits}")
    print(f"Avalanche percentage: {percentage:.1f}%")

    if percentage > 50:
        print("  Strong avalanche effect - good diffusion!")
    else:
        print("  Weak avalanche effect - cipher needs improvement")


if __name__ =="__main__":
    demonstrate_avalanche()
