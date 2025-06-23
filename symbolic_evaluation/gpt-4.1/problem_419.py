import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Calculate π using mpmath's built-in constant
pi_value = mp.pi

# Square π to get π²
pi_squared = pi_value ** 2

# Divide π² by 6 to obtain the final result
result = pi_squared / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))