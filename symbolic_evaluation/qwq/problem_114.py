import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 4
quarter_pi = pi_value / 4

# Apply negative sign to get final result
result = -quarter_pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))