import struct

def feistel_round_function(half_block, round_key):
    half_block &= 0xFFFFFFFF  
    round_key &= 0xFFFFFFFF  

    mixed = (half_block + round_key) & 0x4519663D
    return ((mixed >> 16) ^ mixed) & 0xFFFFFFFF

def generate_keys(master_key, rounds=16):
    keys = []
    current_key = master_key
    for i in range(rounds):
        current_key = (current_key * 0x1F3D5B79 + i) & 0xFFFFFFFF
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

keys = generate_keys(0xDEADBEEF, 16)

messages = [
    'SECRET!!',
    'MESSAGE',
    'BIT4138!',
    'BLOCK!!1'
]

print("=== BLOCK ENCRYPTION DEMONSTRATION ===")
for msg in messages:
    block = text_to_block(msg)
    cipher = feistel_encrypt(block, keys)
    print(f': {msg:8} -> {hex(block)} -> {hex(cipher)}')
