import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# The analytical answer is a constant value
result = mp.mpf(626)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))