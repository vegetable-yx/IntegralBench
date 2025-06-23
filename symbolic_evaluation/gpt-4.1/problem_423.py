import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical result is a constant: 99
result = mp.mpf(99)

# Print the result formatted to 10 significant digits
print(mp.nstr(result, n=10))