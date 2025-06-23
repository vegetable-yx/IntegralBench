import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant integer: 2011
result = mp.mpf(2011)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))