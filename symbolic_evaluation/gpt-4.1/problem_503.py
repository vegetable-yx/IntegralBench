import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is 0
result = mp.mpf(0)

# Print the result with exactly 10 significant digits
print(mp.nstr(result, n=10))