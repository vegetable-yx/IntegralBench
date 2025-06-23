import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute π using mpmath's built-in constant
pi_val = mp.pi

# Square π to get π²
pi_squared = pi_val ** 2

# Divide π² by 4 to obtain the result
result = pi_squared / 4

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))