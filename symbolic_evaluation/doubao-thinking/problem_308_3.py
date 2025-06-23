import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π/2
result = pi_value / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))