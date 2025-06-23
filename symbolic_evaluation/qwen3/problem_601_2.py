import mpmath as mp
mp.dps = 15  # Set decimal places for internal calculations

# Calculate natural logarithm of 2
ln2 = mp.log(2)

# Multiply by pi to get final result
result = mp.pi * ln2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))