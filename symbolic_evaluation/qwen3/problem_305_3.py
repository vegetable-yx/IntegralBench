import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the exact value of 1/8 using arbitrary precision arithmetic
result = mp.mpf(1)/mp.mpf(8)

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))