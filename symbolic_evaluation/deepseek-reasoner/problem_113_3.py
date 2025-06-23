import mpmath as mp
mp.dps = 15

# Calculate square root of 2 for later use
sqrt2 = mp.sqrt(2)

# Compute arguments for dilogarithm functions
arg1 = (2 - sqrt2) / 4
arg2 = (2 + sqrt2) / 4

# Calculate dilogarithm values for both arguments
li2_arg1 = mp.polylog(2, arg1)
li2_arg2 = mp.polylog(2, arg2)

# Compute the difference between dilogarithm values
dilog_difference = li2_arg1 - li2_arg2

# Calculate the square root term (sqrt(2π))
sqrt_2pi = mp.sqrt(2 * mp.pi)

# Combine all components for final result
result = 2 * sqrt_2pi * dilog_difference

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))