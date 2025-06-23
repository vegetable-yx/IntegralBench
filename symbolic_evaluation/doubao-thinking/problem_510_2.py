import mpmath as mp

# Set the decimal places of precision for internal calculations
mp.dps = 15

# Define constants and components
pi = mp.pi
sqrt_3 = mp.sqrt(3)

# Compute the numerator: 7 * pi * sqrt(3)
numerator = 7 * pi * sqrt_3

# Compute the denominator: 9
denominator = 9

# Compute the final expression: (7 * pi * sqrt(3)) / 9
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))