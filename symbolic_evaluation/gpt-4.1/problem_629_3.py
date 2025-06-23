import mpmath as mp

# Set internal decimal places for high precision calculation
mp.dps = 15

# Define numerator and denominator
numerator = 24
denominator = 2024

# Calculate the fraction value
fraction_value = mp.mpf(numerator) / mp.mpf(denominator)

# Compute the natural logarithm of the fraction
result = mp.log(fraction_value)

# Print the result to exactly 10 decimal places
print(mp.nstr(result, n=10))