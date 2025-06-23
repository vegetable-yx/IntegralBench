import mpmath as mp

# Set precision to 15 decimal places for intermediate calculations
mp.dps = 15

# Calculate square root of 11
sqrt_11 = mp.sqrt(11)

# Calculate numerator: 11 * sqrt(11)
numerator = 11 * sqrt_11

# Calculate denominator
denominator = 18

# Compute final result
result = numerator / denominator

# Print result with 10 decimal places
print(mp.nstr(result, n=10))