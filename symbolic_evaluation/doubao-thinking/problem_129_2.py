import mpmath as mp

mp.dps = 15  # Set internal precision to 15 decimal places

# Compute the square root of 2
sqrt_2 = mp.sqrt(2)

# Calculate the numerator: 4 * sqrt(2)
numerator = 4 * sqrt_2

# Get the constant e
e_constant = mp.e

# Compute the final result by dividing numerator by e
result = numerator / e_constant

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))