import mpmath as mp
mp.dps = 15  # Set internal precision to 15 decimal places

# Calculate the square root of 2 with high precision
sqrt2 = mp.sqrt(2)

# Compute the numerator (5 * sqrt(2))
numerator = 5 * sqrt2

# Divide the numerator by 8 to get the coefficient
coefficient = numerator / 8

# Multiply the coefficient by pi to get the final result
result = coefficient * mp.pi

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))