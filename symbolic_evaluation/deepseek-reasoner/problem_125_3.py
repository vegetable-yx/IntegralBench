import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Divide π by 5 to get the final result
result = pi_value / 5

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))