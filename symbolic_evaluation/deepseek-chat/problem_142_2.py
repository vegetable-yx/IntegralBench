import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the numerator: sinh(2)
numerator = mp.sinh(2)

# Define the denominator (constant)
denominator = 4

# Compute the final result: sinh(2) / 4
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))