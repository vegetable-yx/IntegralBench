import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 8
result = pi_value / 8

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))