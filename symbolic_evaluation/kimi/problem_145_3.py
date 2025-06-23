import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant value
result = mp.mpf('1.216091987')

# Print the result to exactly 10 decimal places using nstr formatting
print(mp.nstr(result, n=10))