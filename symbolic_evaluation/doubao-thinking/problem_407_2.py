import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the arguments for the error functions
arg1 = sqrt3 / 2
arg2 = 1 / (2 * sqrt3)

# Calculate the error function values
erf_upper = mp.erf(arg1)
erf_lower = mp.erf(arg2)

# Compute the difference between error functions
erf_diff = erf_upper - erf_lower

# Multiply by π/2 to get final result
result = (mp.pi / 2) * erf_diff

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))