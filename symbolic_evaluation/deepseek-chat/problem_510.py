import mpmath as mp

# Set internal decimal precision to 15 for accurate computation
mp.dps = 15

# Calculate the numerator: 7 * pi * sqrt(3)
# pi is a mathematical constant, sqrt(3) is square root of 3
numerator = 7 * mp.pi * mp.sqrt(3)

# Denominator is 9
denominator = 9

# Compute the result: numerator divided by denominator
result = numerator / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))