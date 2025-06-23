import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Compute pi
pi_val = mp.pi

# Cube the value of pi
pi_cubed = pi_val ** 3

# Divide by 48 to get the result
result = pi_cubed / 48

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))