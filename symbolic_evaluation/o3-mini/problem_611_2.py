import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Calculate the square root of 3
sqrt3 = mp.sqrt(3)

# Compute the numerator: 2 + sqrt(3)
numerator = 2 + sqrt3

# The denominator is sqrt(3)
denominator = sqrt3

# Form the fraction: (2 + sqrt(3)) / sqrt(3)
fraction = numerator / denominator

# Take the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))