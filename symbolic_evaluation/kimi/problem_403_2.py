import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is the constant 5040
result = mp.mpf(5040)

# Print the result to exactly 10 decimal places using nstr formatting
print(mp.nstr(result, n=10))