import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π/4 using exact mathematical division
result = pi_value / 4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))