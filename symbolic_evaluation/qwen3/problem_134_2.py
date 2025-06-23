import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Get pi constant from mpmath
pi_value = mp.pi

# Multiply components to get final result
result = sqrt2 * pi_value

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))