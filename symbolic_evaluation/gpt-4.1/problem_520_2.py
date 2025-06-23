import mpmath as mp

# Set internal decimal precision to 15 for calculations
mp.dps = 15

# The analytical expression is 0
result = mp.mpf(0)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))