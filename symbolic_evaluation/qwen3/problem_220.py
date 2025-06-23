import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the coefficient (5*sqrt(2))/8
coefficient = (5 * sqrt2) / 8

# Multiply by pi constant to get final result
result = coefficient * mp.pi

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))