import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate natural logarithm of 3
result = mp.log(3)

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))