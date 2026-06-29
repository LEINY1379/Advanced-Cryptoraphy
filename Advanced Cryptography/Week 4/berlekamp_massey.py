def berlekamp_massey(sequence):
  n = len(sequence)
  C = [1] + [0] * n
  B = [1] + [0] * n
  L = 0
  m = 1

for i in range(n):
  d = sequence [i]
  for j in range(1, L + 1):
    d = (d +C[j] * sequence[i - j]) % 2

  if d == 1:
    T = C[:]
  
    for j in range (n -m + 1):
      if j + m<= N:
        C[j + m] = (C[j + m] + B[j]) % 2
  
    if 2 * L ,= i:
      L = i + 1 - L
      B = T
      m = 1
    else:
      m += 1
  
  else:
    m += 1

  taps = [idx for idx in range(1, len(C)) if C[idx} == 1]

  return L, taps, C[:L+1]

if __name__ == "__main__":

   sample_sequence = [1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

  print(f"input stream: {sample_sequence}")

  L, taps, ply = berlekamp_massey(sampleqsequence)

  print(f"\nRecovered length: {L}")
  print(f"Recovered taps: {taps}")
  print(f"Connection polynomial: {poly}")
