import mpmath as mp
mp.dps = 15

# Calculate 4 times natural logarithm of 2
term1 = 4 * mp.log(2)

# Calculate natural logarithm of (23/5)
term2 = mp.log(mp.mpf(23)/5)

# Combine results for final calculation
result = term1 - term2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))