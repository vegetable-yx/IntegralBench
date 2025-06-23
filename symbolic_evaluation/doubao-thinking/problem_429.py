import mpmath as mp

# Set internal decimal places to 15 for sufficient precision
mp.dps = 15

# Define numerator and denominator as mpmath floats
numerator = mp.mpf(80)
denominator = mp.mpf(23)

# Compute the fraction 80/23
fraction = numerator / denominator

# Calculate the natural logarithm of the fraction
result = mp.log(fraction)

# Print the result formatted to exactly 10 decimal places
print(mp.nstr(result, n=10))