import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# Compute pi constant
pi_val = mp.pi

# Square pi
pi_squared = pi_val ** 2

# Divide by 6 to get the result
result = pi_squared / 6

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))