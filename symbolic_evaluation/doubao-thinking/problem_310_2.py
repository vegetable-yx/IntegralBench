import mpmath as mp

# Set precision to 15 decimal places for calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π/4
result = pi_value / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))