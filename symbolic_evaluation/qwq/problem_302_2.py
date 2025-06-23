import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate arcsin(0.25) using mpmath's asin function
arcsin_val = mp.asin(0.25)

# Calculate π/2 using mpmath's pi constant
pi_over_two = mp.pi / 2

# Multiply the two components to get final result
result = pi_over_two * arcsin_val

# Print result with exactly 10 decimal places
print(mp.nstr(result, n=10))