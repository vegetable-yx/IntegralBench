import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Assign the exact integer value 4 to result
result = mp.mpf(4)

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))