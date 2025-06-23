import mpmath as mp

# Set internal decimal places for precision
mp.dps = 15

# Calculate the analytical expression: -56/15
# Numerator is -56, denominator is 15
numerator = -56
denominator = 15

# Compute the result as a high-precision floating-point number
result = mp.mpf(numerator) / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))