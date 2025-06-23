import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's constant
pi_value = mp.pi

# Compute π divided by 16
result = pi_value / 16

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))