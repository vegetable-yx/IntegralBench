import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the fraction: numerator = 128, denominator = 153
numerator = mp.mpf(128)
denominator = mp.mpf(153)

# Compute the result of the division
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))