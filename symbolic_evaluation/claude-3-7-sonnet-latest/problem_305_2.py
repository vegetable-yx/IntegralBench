import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is given as 0
result = mp.mpf(0)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))