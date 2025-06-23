import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the exact value of 1/2 using high-precision arithmetic
result = mp.mpf(1)/2

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))