import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate π squared
pi_squared = mp.pi ** 2

# Divide π squared by 4
pi_sq_over_4 = pi_squared / 4

# Subtract 2 from the result
result = pi_sq_over_4 - 2

# Print the final result to exactly 10 decimal places
print(mp.nstr(result, n=10))