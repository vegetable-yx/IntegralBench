import mpmath as mp

# Set the internal decimal precision to 15
mp.dps = 15

# The analytical expression is a constant value of 4
result = mp.mpf(4)

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))