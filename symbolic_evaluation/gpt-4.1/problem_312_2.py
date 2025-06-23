import mpmath as mp

# Set internal decimal precision to 15 for intermediate calculations
mp.dps = 15

# Compute the constant pi
pi_val = mp.pi

# Calculate the numerator: 17 * pi
numerator = 17 * pi_val

# Calculate the denominator
denominator = 288

# Compute the result: (17 * pi) / 288
result = numerator / denominator

# Print the result with exactly 10 decimal places
print(mp.nstr(result, n=10))