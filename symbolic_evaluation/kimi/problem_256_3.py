import mpmath as mp
mp.dps = 15

# Calculate -2 multiplied by pi
result = -2 * mp.pi

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))