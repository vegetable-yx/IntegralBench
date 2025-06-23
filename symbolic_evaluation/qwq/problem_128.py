import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Directly assign the mathematical constant π
result = mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))