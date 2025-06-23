import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 2*Catalan's constant
result = 2 * mp.catalan

# Print result with 10 decimal places
print(mp.nstr(result, n=10))