import mpmath as mp
mp.dps = 15  # Set internal precision

# Calculate denominator components
sqrt2 = mp.sqrt(2)  # Compute square root of 2
denominator = 2 * sqrt2  # Calculate 2*sqrt(2)

# Compute final result using exact mathematical constants
result = mp.pi / denominator  # Divide π by (2*sqrt(2))

# Print result with 10 decimal places
print(mp.nstr(result, n=10))