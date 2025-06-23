import mpmath as mp
mp.dps = 15  # Set decimal precision for calculations

# Define numerator and denominator
numerator = 16
denominator = 3

# Compute the result of the fraction
result = mp.mpf(numerator) / denominator

# Print the result to 10 decimal places
print(mp.nstr(result, n=10))