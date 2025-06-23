import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π/4 using mpmath's pi constant
pi_over_4 = mp.pi / 4

# Calculate the constant term 1/2 with high precision
half = mp.mpf(1)/2

# Combine terms for final result
result = pi_over_4 - half

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))