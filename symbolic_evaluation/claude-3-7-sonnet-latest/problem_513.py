import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical expression is a constant value: 113
result = mp.mpf(113)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))