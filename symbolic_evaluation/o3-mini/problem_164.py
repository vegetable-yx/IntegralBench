import mpmath as mp

# Set internal decimal precision to 15
mp.dps = 15

# The analytical expression is a constant integer 384
result = mp.mpf(384)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))