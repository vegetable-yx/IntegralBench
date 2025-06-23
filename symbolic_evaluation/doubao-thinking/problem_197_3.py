import mpmath as mp
mp.dps = 15

# Calculate the exact fraction 1/4 using high-precision arithmetic
result = mp.mpf(1)/4

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))