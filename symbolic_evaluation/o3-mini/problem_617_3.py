import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant value 0 to result
result = mp.mpf(0)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))