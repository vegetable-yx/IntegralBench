import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate the sum of pi and 2
numerator = mp.pi + 2

# Denominator for the expression
denominator = 8

# Combine components with negative sign
result = -numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))