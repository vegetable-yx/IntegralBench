import mpmath as mp

# Set internal precision to 15 decimal places
mp.dps = 15

# Define numerator and denominator as exact integers
numerator = -2023
denominator = 2022

# Convert to mpmath floating-point numbers for precise division
a = mp.mpf(numerator)
b = mp.mpf(denominator)

# Compute the exact fraction
result = a / b

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))