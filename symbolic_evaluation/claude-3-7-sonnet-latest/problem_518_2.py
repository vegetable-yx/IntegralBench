import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Assign the constant value directly
result = mp.mpf(4036)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))