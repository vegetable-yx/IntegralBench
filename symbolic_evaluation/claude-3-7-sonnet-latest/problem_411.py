import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression is a constant value of 1
result = mp.mpf(1)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))