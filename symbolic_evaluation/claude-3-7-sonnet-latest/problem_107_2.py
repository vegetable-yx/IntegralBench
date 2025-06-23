import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate π using mpmath constant
pi_val = mp.pi

# Square π to get π²
pi_squared = pi_val ** 2

# Divide π² by 6 to obtain the result
result = pi_squared / 6

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))