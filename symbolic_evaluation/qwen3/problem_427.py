import mpmath as mp

# Set precision to 15 decimal places for internal calculations
mp.dps = 15

# Calculate the numerator: 11 * sqrt(11)
sqrt_11 = mp.sqrt(11)
numerator = 11 * sqrt_11

# Calculate the denominator
denominator = 18

# Compute the final result
result = numerator / denominator

# Print the result with 10 decimal places precision
print(mp.nstr(result, n=10))