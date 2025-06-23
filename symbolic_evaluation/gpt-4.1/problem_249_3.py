import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the numerator: 5 * sqrt(5) - 10
numerator = 5 * sqrt5 - 10

# Divide the numerator by 10 to get the fraction
fraction = numerator / 10

# Multiply by pi to get the final result
result = mp.pi * fraction

# Print the result with 10 decimal places
print(mp.nstr(result, n=10))