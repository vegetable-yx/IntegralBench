import mpmath as mp
mp.dps = 15

# Calculate 2 times pi using high-precision arithmetic
result = 2 * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))