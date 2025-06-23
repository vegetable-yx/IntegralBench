import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π/4 using exact mathematical operation
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))