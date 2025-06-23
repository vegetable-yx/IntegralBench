import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/4 term
pi_term = mp.pi / 4

# Calculate (ln 2)/2 term
ln2_term = mp.log(2) / 2

# Combine all terms: π/4 + (ln 2)/2 - 1
result = pi_term + ln2_term - 1

# Print final result with 10 decimal places
print(mp.nstr(result, n=10))