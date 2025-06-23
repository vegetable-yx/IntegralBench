import mpmath as mp

# Set internal decimal precision to 15 digits
mp.dps = 15

# The analytical result is a constant integer: 626
result = mp.mpf(626)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))