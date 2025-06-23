import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the exact integer value using arbitrary precision
result = mp.mpf(1005)

# Print the result with exactly 10 decimal places using nstr formatting
print(mp.nstr(result, n=10))