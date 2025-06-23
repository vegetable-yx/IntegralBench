import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate 18 * π using exact mathematical constant
coefficient = 18
result = coefficient * mp.pi  # Multiply coefficient by π

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))