import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate mathematical constant e
e_val = mp.e

# Compute (e - 2) component
e_minus_2 = e_val - 2

# Calculate π/2 component
pi_over_2 = mp.pi / 2

# Multiply components to get final result
result = pi_over_2 * e_minus_2

# Print result with 10 decimal places
print(mp.nstr(result, n=10))