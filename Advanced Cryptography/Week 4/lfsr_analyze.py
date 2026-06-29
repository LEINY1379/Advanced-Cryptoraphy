def analyze_sequence_vulnerability(bit_sequence, target_lfsr_class, initial_seed, original_taps):
  print("=" * 40)
  print(" LFSR CRPTOGRAPHIC VULNERABILITY REPORT ")
  print("=" *40)
  print(f"Original Seed Configuration: {bin(initial_seed)}")
  print(f"Original Feedback Taps:    {original_taps}")
  print(f"Analyzing stream sample of {len(bit_sequence)} bits.\n")

  tester_lfsr = target_lfsr_class(initial_seed, original_taps)
  period, repetition_point = tester_lfsr.detect_period(max_steps=10000)

  print("[PHASE 1] Cycle & Period Analysis")
  print(f"  -> State loop length detected:{period}")
  print(f"  -> Repetition starts at index:{repetition_point}")
  if period and period < 1000:
    print("ALERT: Short repeating cycle identified. Highly vulnerable to replay matching.")
  else:
    print("State cycle space appears adequate for short-term streaming.")

  interception_window = bit_sequence[:50]

  from berlekamp_massey import berlekamp_massey
  linear_complexity, cracked_taps, _ = berlekamp_massey(interception_window)
  print("\n[PHASE 2]Structural Cmplexity Discovery")
  print("f  -> Claculated Linear Complexity (L): {linear_complexity}")
  print(f"  -> Synthesized feedback taps:    {cracked_taps}")
  if linear_complexity <20:
    print("ALERT: Low linear complexity. The register configuratino can e easily cloned.")
  else:
    print("Polynomial configuration requires a larger observation matrix to solve. ")

  print("\n[PHASE 3] VAlidation &Future Prediction Test")

  active_taps = cracked_taps if cracked_taps else original_taps
  cloned_lfsr = target_lfsr_class(initial_seed, active_taps)

  cloned_lfsr.generation(50)

  predicted_bits = [cloned_lfsr.steps() for _ in range(10)]
  actual_bits = bit_sequence[50:60]

  print(f"  -> Cloned model forecast: {predicted_bits}")
  print(f"  -> Actual sequence data:    {actual_bits}")

  is_compromised = (predicted_bits == actual_bits)
  if is_compromised:
     print("  CRITICAL FAILURE: The cloned system successfully prediicted future stream vales!.")
  else:
    print("  SUCCESS: The cloned prediction does not match the actual data stream. ")

  return is_compromised or (period is not None and period <1000)

if __name__ == "__name__":
  from lfsr import LFSR

  seed_value = 0b10110101
  tap_layout = [0, 2]

  source_lfsr= LFSR(seed=seed_value, taps=tap_layout)
  data_pool = source_lfsr.generate(200)

  is_weak = analyze_sequence_vulnerability(
      bit_sequence=data_pool,
      target_lfsr_class=LFSR,
      initial_seed=seed_value,
      original_taps=tap_layout
  )

  print("\n" + "=" * 40)
  print(f"OVERALL SYSTEMSECURITY RATING: {'  UNACCEPTABLE / WEAK' if is_weak else '  ACCEPTABLE / MODERATE'}")
  print("=" * 40)
