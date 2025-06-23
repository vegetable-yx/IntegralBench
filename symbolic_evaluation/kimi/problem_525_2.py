import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the exact value of 1/2
result = mp.mpf(1)/2

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))