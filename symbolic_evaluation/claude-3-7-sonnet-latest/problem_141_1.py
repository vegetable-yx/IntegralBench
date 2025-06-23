import mpmath as mp

# Set internal decimal places for calculation
mp.dps = 15

# The analytical expression is the constant 1
result = mp.mpf(1)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))