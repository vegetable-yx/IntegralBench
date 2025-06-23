import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Direct assignment of the constant value
result = mp.mpf(2)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))