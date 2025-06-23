import mpmath as mp
mp.dps = 15

# Calculate 506 multiplied by pi
result = 506 * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))