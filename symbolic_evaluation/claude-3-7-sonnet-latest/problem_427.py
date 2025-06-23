import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the square root of 11
sqrt_11 = mp.sqrt(11)

# Compute the numerator: 11 * sqrt(11)
numerator = 11 * sqrt_11

# Compute the denominator
denominator = 15

# Calculate the result: numerator divided by denominator
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))