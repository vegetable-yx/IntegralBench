import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 6
result = pi_value / 6

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))