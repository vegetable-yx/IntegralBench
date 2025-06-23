import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate the constant pi
pi_val = mp.pi

# Square pi
pi_squared = pi_val ** 2

# Divide by 4 to get the result
result = pi_squared / 4

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))