import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression is simply 0
result = mp.mpf(0)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))