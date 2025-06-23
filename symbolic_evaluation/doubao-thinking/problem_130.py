import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Calculate hyperbolic sine of 1
sinh1 = mp.sinh(1)

# Combine components for final result
result = 2 * sqrt2 * sinh1

# Print result with 10 decimal places
print(mp.nstr(result, n=10))