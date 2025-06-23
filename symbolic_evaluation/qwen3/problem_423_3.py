import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Exact solution is 99
result = mp.mpf(99)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))