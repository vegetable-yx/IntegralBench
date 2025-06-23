import mpmath as mp

mp.dps = 15  # Set decimal precision for internal calculations

# Calculate the numerator and denominator
numerator = mp.mpf(80)
denominator = mp.mpf(23)

# Compute the fraction 80/23
fraction = numerator / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))