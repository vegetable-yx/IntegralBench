import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2 using mpmath
sqrt2 = mp.sqrt(2)

# Get pi constant from mpmath
pi = mp.pi

# Compute the final result using exact mathematical expression
result = pi / sqrt2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))