import mpmath as mp

# Set internal decimal precision to 15 for accurate calculations
mp.dps = 15

# Calculate the numerator: 13 * π * √3
pi_value = mp.pi
sqrt3 = mp.sqrt(3)
numerator = 13 * pi_value * sqrt3

# Denominator is 9
denominator = 9

# Compute the final result: (13 * π * √3) / 9
result = numerator / denominator

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))