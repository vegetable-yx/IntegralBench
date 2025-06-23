import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is exactly 1
result = mp.mpf(1)

# Format the result to display exactly 10 decimal places
# Using min_fixed=10 ensures at least 10 digits after the decimal point
# strip_zeros=False prevents removal of trailing zeros
print(mp.nstr(result, n=10, min_fixed=10, strip_zeros=False))