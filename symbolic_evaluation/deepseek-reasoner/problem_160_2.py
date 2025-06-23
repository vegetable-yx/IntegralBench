import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Assign the constant π directly from mpmath
result = mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))