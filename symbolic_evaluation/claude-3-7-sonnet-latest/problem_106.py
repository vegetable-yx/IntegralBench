import mpmath as mp

# Set the internal decimal precision to 15 to ensure accurate computation
mp.dps = 15

# Compute the value of pi
pi_val = mp.pi

# Square the value of pi
pi_squared = pi_val ** 2

# Divide the squared pi by 8 to get the result
result = pi_squared / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))