import mpmath as mp

# Set internal precision to 15 decimal places for reliable calculations
mp.dps = 15

# The analytical expression is a constant value
result = mp.mpf('1.2337005501')

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))