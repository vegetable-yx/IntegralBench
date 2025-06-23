import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate square root of 2
sqrt_2 = mp.sqrt(2)

# Multiply by pi
sqrt2_pi = sqrt_2 * mp.pi

# Divide by 2 to get final result
result = sqrt2_pi / 2

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))