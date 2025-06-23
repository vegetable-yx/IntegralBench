import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Compute pi to the fourth power
pi_to_4 = mp.pi**4

# Divide by 1280 to get the result
result = pi_to_4 / 1280

# Print the result rounded to 10 decimal places
print(mp.nstr(result, n=10))