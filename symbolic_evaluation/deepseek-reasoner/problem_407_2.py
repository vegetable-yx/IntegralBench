import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 3 for repeated use
sqrt3 = mp.sqrt(3)

# Compute arguments for the error functions
erf_arg1 = sqrt3 / 2
erf_arg2 = 1 / (2 * sqrt3)

# Calculate both error function values
erf_term1 = mp.erf(erf_arg1)
erf_term2 = mp.erf(erf_arg2)

# Compute the difference between error function terms
erf_difference = erf_term1 - erf_term2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * erf_difference

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))