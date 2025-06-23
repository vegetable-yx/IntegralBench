import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate square root of 2
sqrt2 = mp.sqrt(2)

# Compute the coefficient (4*sqrt(2))/3
coefficient = (4 * sqrt2) / 3

# Multiply by pi to get the final result
result = coefficient * mp.pi

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))