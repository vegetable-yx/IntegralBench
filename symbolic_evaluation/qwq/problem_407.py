import mpmath as mp

mp.dps = 15  # Set internal precision

# Compute sqrt(3) once for reuse
sqrt3 = mp.sqrt(3)

# Calculate the first argument for erf
arg1 = sqrt3 / 2

# Calculate the second argument for erf
arg2 = 1 / (2 * sqrt3)

# Compute the two error functions
erf_upper = mp.erf(arg1)
erf_lower = mp.erf(arg2)

# Compute the difference between the error functions
erf_diff = erf_upper - erf_lower

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * erf_diff

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))