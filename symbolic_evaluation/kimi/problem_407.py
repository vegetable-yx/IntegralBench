import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of 3
sqrt3 = mp.sqrt(3)

# Calculate the arguments for the error functions
arg1 = sqrt3 / 2
arg2 = 1 / (2 * sqrt3)

# Compute the error function values
erf_val1 = mp.erf(arg1)
erf_val2 = mp.erf(arg2)

# Calculate the difference between the error function values
erf_diff = erf_val1 - erf_val2

# Multiply by pi/2 to get the final result
result = (mp.pi / 2) * erf_diff

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))