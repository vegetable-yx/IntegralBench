import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# The analytical expression is the constant integer 9
result = mp.mpf(9)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))