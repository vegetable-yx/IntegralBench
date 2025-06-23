import mpmath as mp

# Set the internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute arguments for erf functions
erf_arg1 = sqrt3 / 2
erf_arg2 = 1 / (2 * sqrt3)

# Calculate error function values
erf1 = mp.erf(erf_arg1)
erf2 = mp.erf(erf_arg2)

# Compute the difference between erf values
erf_diff = erf1 - erf2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * erf_diff

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))