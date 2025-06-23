import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Direct assignment of the exact integer solution
result = 4

# Print result with 10 decimal place formatting
print(mp.nstr(result, n=10))