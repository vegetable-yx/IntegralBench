import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate denominator component
denominator = 9 - 1

# Compute square root of denominator
sqrt_denominator = mp.sqrt(denominator)

# Calculate final result as reciprocal of the square root
result = 1 / sqrt_denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))