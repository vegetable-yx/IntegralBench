import mpmath as mp
mp.dps = 15  # Set internal decimal precision

# Calculate numerator and denominator
numerator = 2
denominator = mp.pi

# Compute the fraction 2/π
fraction = mp.mpf(numerator) / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))