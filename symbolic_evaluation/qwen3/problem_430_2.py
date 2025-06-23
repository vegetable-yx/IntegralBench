import mpmath as mp
mp.dps = 15

# Calculate numerator and denominator
numerator = 2023
denominator = 2022

# Compute the exact fraction
result = -numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))