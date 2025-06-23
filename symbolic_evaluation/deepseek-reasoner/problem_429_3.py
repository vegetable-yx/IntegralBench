import mpmath as mp

mp.dps = 15  # Set decimal places for internal calculations

# Compute the fraction 80/23 with high precision
numerator = mp.mpf(80)
denominator = mp.mpf(23)
fraction = numerator / denominator

# Calculate natural logarithm of the fraction
result = mp.log(fraction)

# Print result with 10 decimal places
print(mp.nstr(result, n=10))