import mpmath as mp

mp.dps = 15  # Set internal precision

# Calculate each term separately
pi_cubed = mp.pi ** 3
term1 = pi_cubed / 192  # First term: π³/192

ln2 = mp.log(2)
term2 = (mp.pi * ln2) / 16  # Second term: (π ln2)/16 (to be subtracted)

term3 = mp.mpf(7) / 16  # Third term: 7/16

# Combine all terms for final result
result = term1 - term2 + term3

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))