import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Compute the fraction 128 / 153
result = mp.mpf(128) / mp.mpf(153)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))