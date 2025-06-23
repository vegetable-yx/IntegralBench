import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute π squared
pi_squared = mp.pi ** 2

# Divide by 6 to obtain the result
result = pi_squared / 6

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))