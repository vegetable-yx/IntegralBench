import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Compute π divided by 12
result = pi_value / 12

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))