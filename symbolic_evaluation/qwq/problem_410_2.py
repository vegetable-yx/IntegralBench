import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate numerator: square root of pi
numerator = mp.sqrt(mp.pi)

# Calculate denominator: 2 multiplied by Euler's number
denominator = 2 * mp.e

# Compute final result by dividing numerator by denominator
result = numerator / denominator

# Print result with 10 decimal places precision
print(mp.nstr(result, n=10))