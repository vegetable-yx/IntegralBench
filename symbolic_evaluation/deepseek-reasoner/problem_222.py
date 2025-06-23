import mpmath as mp
mp.dps = 15

# Calculate 3 times pi using high-precision arithmetic
three_pi = 3 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(three_pi, n=10))