def generate_keys(master_key, rounds=16):

    keys = []
    for i in range(rounds):
        round_constant = (0x6ED9EBA1 * (i + 1)) & 0xFFFFFFFF
        round_key = (master_key ^ round_constant) &  0xFFFFFFFF
        keys.append(round_key)
    return keys

print('=== KEY GENERATION PROCESS ===')
master = 0x12345678
print(f'Master key: {hex(master)}')

keys = generate_keys(master, 16)

print('Round keys (first 5 shown):')

for i, k in enumerate(keys[:5]):
    print(f'    K{i:2d}: {hex(k)}')

print('...')
print('Key derivation: K_i = (master XOR (0x6EFD9EBA1 * (i_1))) & 0xFFFFFFFF')   
print('Purpose: Ensure round keys are different and unpredictable')
