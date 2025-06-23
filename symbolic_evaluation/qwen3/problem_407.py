import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root constants
sqrt3 = mp.sqrt(3)

# Compute arguments for error functions
arg1 = sqrt3 / 2
arg2 = 1 / (2 * sqrt3)

# Calculate error function values
erf1 = mp.erf(arg1)
erf2 = mp.erf(arg2)

# Compute the final result
result = (mp.pi / 2) * (erf1 - erf2)

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))