import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Calculate pi squared
pi_squared = mp.pi ** 2

# Divide by 8 to get the result
result = pi_squared / 8

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))