import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Square pi
pi_squared = pi_val ** 2

# Divide by 16
result = pi_squared / 16

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))