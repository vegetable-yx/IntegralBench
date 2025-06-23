import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is the integer 1005
result = mp.mpf(1005)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))