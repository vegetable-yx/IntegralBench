import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate pi constant
pi_val = mp.pi

# Compute square root of 3
sqrt3 = mp.sqrt(3)

# Numerator: 7 * pi
numerator = 7 * pi_val

# Denominator: 3 * sqrt(3)
denominator = 3 * sqrt3

# Final result: numerator divided by denominator
result = numerator / denominator

# Print the result formatted to 10 decimal places
print(mp.nstr(result, n=10))