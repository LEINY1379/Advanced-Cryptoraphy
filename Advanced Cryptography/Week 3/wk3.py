# LFSR Pseudorandom Number Generator

def lfsr(seed, steps):
    state = seed
    bits = []

    for _ in range(steps):
        output = state & 1
        bits.append(output)
        
        feedback = ((state >> 2) ^ (state >> 1)) & 1
        state = ((state >> 1) | (feedback)) & 0b111
    
    return bits

# Frequency Test

def frequency_test(bits):
    zeros = bits.count(0)
    ones = bits.count(1)

    print("\nFrequency Test")
    print("Zeros:", zeros)
    print("Ones:", ones)

    if abs(zeros - ones) <= len(bits) * 0.1:
        print("PASS")
    else:
        print("FAIL")

# RC4Functions

def rc4_initialize(key):
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]

    return S

def rc4_generate_keystream(S, length):
    i = 0
    j = 0
    stream = []

    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256

        S[i], S[j] = S[j], S[i]

        K = S[(S[i] + S[j]) % 256]
        stream.append(K)

    return stream

def rc4_encrypt(text, key):
    key_bytes = [ord(c) for c in key]

    S = rc4_initialize(key_bytes)
    keystream = rc4_generate_keystream(S, len(text))

    result =[]

    for char, k in zip(text, keystream):
        result.append(chr(ord(char) ^ k))

    return ''.join(result)

# Main Program

print("=== LFSR Demo ===")

bits = lfsr(seed=0b101, steps=20)

print("Generated bits:")
print(bits)

frequency_test(bits)

print("\n=== RC4 Demo ===")

message = input("Enter message: ")
key = input("Enter key: ")

encrypted = rc4_encrypt(message, key)
print("\nEncrypted (hex):", encrypted.encode('latin1').hex())

decrypted = rc4_encrypt(encrypted, key)
print("Decrypted:", decrypted)
