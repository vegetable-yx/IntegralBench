import mpmath as mp
mp.dps = 15

# Calculate the result using exact mathematical constant pi
result = -3 * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))