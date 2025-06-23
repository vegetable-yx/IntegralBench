import mpmath as mp

# Set internal decimal places for high precision calculations
mp.dps = 15

# The analytical expression evaluates to exactly 0
result = mp.mpf(0)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))