import mpmath as mp
mp.dps = 15

# Calculate 506 * π using high-precision arithmetic
result = 506 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))