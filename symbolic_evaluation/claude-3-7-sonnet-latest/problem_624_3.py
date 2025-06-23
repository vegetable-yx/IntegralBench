import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute pi squared
pi_val = mp.pi
pi_squared = mp.power(pi_val, 2)

# Divide by 6 to get the result
result = pi_squared / 6

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))