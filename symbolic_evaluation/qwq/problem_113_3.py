import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Compute the dilogarithm of 1/2
dilog_half = mp.polylog(2, 0.5)

# Multiply by pi
result = mp.pi * dilog_half

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))