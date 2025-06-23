import mpmath as mp

# Set the internal decimal precision to 15 for accurate computations
mp.dps = 15

# Compute the constant π using mpmath's built-in constant
pi_value = mp.pi

# Divide π by 8 to get the result
result = pi_value / 8

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))