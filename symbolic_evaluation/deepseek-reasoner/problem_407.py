import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate square root of 3
sqrt3 = mp.sqrt(3)

# Compute arguments for error functions
arg1 = sqrt3 / 2
arg2 = 1 / (2 * sqrt3)

# Calculate error function values
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Compute the difference between error function values
erf_diff = erf_val1 - erf_val2

# Multiply by π/2 to get final result
result = (mp.pi / 2) * erf_diff

# Print result with 10 decimal places
print(mp.nstr(result, n=10))