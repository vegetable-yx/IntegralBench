import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is 113
result = mp.mpf(113)

# Print the result with exactly 10 significant digits, showing trailing zeros
print(mp.nstr(result, n=10, strip_zeros=False))