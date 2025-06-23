import mpmath as mp
mp.dps = 15

# Define numerator
numerator = 1

# Define denominator
denominator = 10

# Compute the exact value
result = numerator / denominator

# Print result with 10 decimal precision
print(mp.nstr(result, n=10))