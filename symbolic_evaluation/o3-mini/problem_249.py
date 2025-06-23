import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 5
sqrt5 = mp.sqrt(5)

# Compute the numerator: π * (5 - 2√5)
numerator = mp.pi * (5 - 2 * sqrt5)

# Compute the denominator: 2√5
denominator = 2 * sqrt5

# Divide the numerator by the denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))