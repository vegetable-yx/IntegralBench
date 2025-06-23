import mpmath as mp

# Set internal decimal precision to 15 to ensure 10 decimal places accuracy
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Square pi
pi_squared = pi_val ** 2

# Divide by 8 to get the final result
result = pi_squared / 8

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))