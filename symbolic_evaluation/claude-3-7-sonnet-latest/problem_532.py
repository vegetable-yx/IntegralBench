import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute the value of pi
pi_val = mp.pi

# Square the value of pi to get pi squared
result = pi_val**2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))