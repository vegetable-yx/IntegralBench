import mpmath as mp

mp.dps = 15  # Set decimal precision for calculations

# Compute square root of 3 once for reuse
sqrt3 = mp.sqrt(3)

# Calculate arguments for error functions
arg1 = sqrt3 / 2
arg2 = 1 / (2 * sqrt3)

# Compute error function values
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Calculate the difference between error functions
erf_diff = erf_val1 - erf_val2

# Multiply by pi/2 for final result
result = (mp.pi / 2) * erf_diff

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))