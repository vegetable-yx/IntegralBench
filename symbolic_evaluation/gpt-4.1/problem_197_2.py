import mpmath as mp

# Set the internal decimal precision to 15 digits
mp.dps = 15

# The analytical expression is a constant fraction: 1/4
result = mp.mpf(1) / 4

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))