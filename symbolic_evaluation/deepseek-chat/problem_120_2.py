import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Compute π squared
pi_squared = mp.pi ** 2

# Divide π squared by 8
pi_sq_over_8 = pi_squared / 8

# Subtract 1/2 from the result
result = pi_sq_over_8 - 0.5

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))