import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate π²/6 term
pi_sq_over_6 = mp.pi**2 / 6

# Calculate (ln 2)² term
ln2_sq = mp.log(2)**2

# Compute final result by combining terms
result = pi_sq_over_6 - ln2_sq

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))