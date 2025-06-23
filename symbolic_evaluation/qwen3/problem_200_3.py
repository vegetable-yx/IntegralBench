import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate sine of 1 (radians)
sin1 = mp.sin(1)

# Multiply components together
sqrt2_times_sin1 = sqrt2 * sin1

# Multiply by 2 to get final result
result = 2 * sqrt2_times_sin1

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))