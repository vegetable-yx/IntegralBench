import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# The analytical result is exactly 2
result = mp.mpf(2)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))