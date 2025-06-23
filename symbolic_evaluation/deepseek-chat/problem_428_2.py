import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# The analytical answer is the constant integer 17
result = mp.mpf(17)

# Print the result to exactly 10 decimal places (using n=10 for significant digits)
print(mp.nstr(result, n=10))